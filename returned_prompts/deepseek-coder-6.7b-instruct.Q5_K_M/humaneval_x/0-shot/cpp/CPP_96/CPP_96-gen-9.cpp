    vector<int> prime_nums;
    if(n<2){
        return prime_nums;
    }
B:
    for(int i=2; i<n; i++){
        for(int j=2; j*j<=i; j++){
            if(i%j==0){
                break;
            }
            if(j*j>i){
                prime_nums.push_back(i);
            }
        }
    }
    return prime_nums;
}

It should be:
vector<int> count_up_to(int n){
    vector<int> prime_nums;
    if(n<2){
        return prime_nums;
    }
    for(int i=2; i<n; i++){
        bool is_prime = true;
        for(int j=2; j*j<=i; j++){
            if(i%j==0){
                is_prime = false;
                break;
            }
        }
        if(is_prime){
            prime_nums.push_back(i);
        }
    }
    return prime_nums;
}
*/

*/

#include<stdio.h>
#include<vector>
using namespace std;
vector<int> count_up_to(int n){
    vector<int> prime_nums;
    if(n<2){
        return prime_nums;
    }
    for(int i=2; i<n; i++){
        bool is_prime = true;