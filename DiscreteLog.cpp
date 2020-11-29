#include <bits/stdc++.h>
#include <time.h>
using namespace std;

class ZeroKnowldege{

	public:
	long power(long x, long y, long p)
    {
        long res = 1;     
        x = x % p; 
     
        while (y > 0)
        {
            if((y & 1)==1)
                res = (res * x) % p;
            y = y >> 1; 
            x = (x * x) % p; 
        }
        return res;
    }

    // 23, 1237
	
};
class Bob{
	
	long y , C ;

	public:
	void setY(long y){
		cout<<"Bob recieves y = "<<y<<endl;
		this->y = y;
	}

	void sendC(long C){
		cout<<"Bob recieves C ="<<C<<endl;
		this->C = C ;
	}
	int request(){
		//request = 0 implies Bob is asking for r 
		//request = 1 implies Bob is asking for (x+r)mod(p-1)
		
  		int r = rand() % 2;
		return r;
	}
	bool checkresponse(int g ,int r,int p, long val ,int request){
		ZeroKnowldege zk;
		if(request==0){
			long newC = zk.power(g,val,p);
			cout<<"Bob's New C = "<<g<<"^"<<val<<" mod "<<p<<"  = "<<newC<<endl;
			if(newC == C)
				cout<<"Alright"<<endl;      //Alice is not bluffing.
			else{
				cout<<"Alice lies"<<endl;
				return false;
			}
			return true;
		}
		else{
			long newC = zk.power(g,val,p);
			long matchwith = zk.power(C*y,1,p);
			cout<<"Bob's New C:"<<newC<<" which should be equal to ("<<C<<" x "<<y<<")mod "<<p<<" = "<<(matchwith)<<endl;
			if(newC == matchwith){
				cout<<"Alright"<<endl;    //Alice is not bluffing
				return true;
			}
			else
				cout<<"Alice lies"<<endl;
			return false;
		}
	}

};
class Alice{

	//predecided x which is the hidden information.
	int x = 74;
	long y;

	public:
	long calculateY(int g ,int p){
		ZeroKnowldege zk;
		y =	zk.power(g,x,p);
		return y;
	}
	void peggyKnows(int g, int p, int i, Bob Bob){
		ZeroKnowldege zk ;
		for(int j=1;j<=i;j++){
			cout<<"Round: "<<j<<endl;
			
  			int r = rand() % 1000 + 1;
			cout<<"Alice chooses random r :"<<r<<endl;
			long C = zk.power(g,r,p);
			
			cout<<"Alice sends Bob computed C ="<<g<<"^"<<r<<" mod "<<p<<"  = "<<C<<endl;
			Bob.sendC(C);

			//Bob chooses request
			int request = Bob.request(); 
;
			cout<<"Bob Requesting for :"<<request<<endl;
			if(request==0){
				if((Bob.checkresponse(g,r,p,r,request)==false))
					break;
			}
			else{
				long val = zk.power(x+r,1,p-1);
				if(Bob.checkresponse(g,r,p,val,request)==false)
					break;
			}
		cout<<"*********"<<endl<<endl;;
		}
	}

};

int main()
{
		Alice Alice ;
		Bob Bob ;
		long g,p;
		srand (time(NULL));
		cout<<("Choose generator g: ")<<endl;
		cin>>g;
		cout<<"Choose prime p: "<<endl;
		cin>>p;
		//calculate y:
		long y = Alice.calculateY(g,p);
		Bob.setY(y);

		//Iterations:
		cout<<"No. of rounds of checking:"<<endl;
		int iterations ;
		cin>>iterations;
		cout<<endl<<endl;
		Alice.peggyKnows(g,p,iterations,Bob);
		
}