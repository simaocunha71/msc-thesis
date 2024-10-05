    vector<int> primes;
    for(int i=2;i<n;i++){
        bool isPrime=true;
        for(int j=2;j<i;j++){
            if(i%j==0) {
                isPrime=false;
                break;
            }
        }
        if(isPrime) primes.push_back(i);
    }
    return primes;
}


int main()
{
    int n=5;
    vector<int> res=count_up_to(n);
    for(int i:res) printf("%d ",i);
    return 0;
}


*/

#include<stdio.h>
#include<vector>
using namespace std;
vector<int> count_up_to(int n){

    vector<int> primes;
    bool isPrime[n+1];
    for(int i=0;i<=n;i++) isPrime[i]=true;
    isPrime[0]=false;
    isPrime[1]=false;
    for(int i=2;i<=n;i++){
        if(isPrime[i]){
            primes.push_back(i);
            for(int j=i*2;j<=n;j+=i) isPrime[j]=false;
        }
    }
    return primes;
}


int main()
{
    int n=5;
    vector<int> res=count_up_to(n);
    for(int i:res) printf("%d ",i);
    return 0;
}




















































































































