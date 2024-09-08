/*
#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
vector<int> count_up_to(int n){
    vector<int> prime;
    for(int i=2;i<n;i++){
        bool is_prime = true;
        for(int j=2;j<=sqrt(i);j++){
            if(i%j==0){
                is_prime = false;
                break;
            }
        }
        if(is_prime){
            prime.push_back(i);
        }
    }
    return prime;
}
*/