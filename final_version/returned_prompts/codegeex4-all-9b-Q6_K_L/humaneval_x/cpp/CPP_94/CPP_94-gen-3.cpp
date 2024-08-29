```cpp
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
int skjkasdkd(vector<int> lst){
    vector<int> primes;
    for(int i=0; i<lst.size(); i++){
        bool isPrime = true;
        for(int j=2; j*j<=lst[i]; j++){
            if(lst[i] % j == 0){
                isPrime = false;
                break;
            }
        }
        if(isPrime && lst[i] > 1){
            primes.push_back(lst[i]);
        }
    }
   