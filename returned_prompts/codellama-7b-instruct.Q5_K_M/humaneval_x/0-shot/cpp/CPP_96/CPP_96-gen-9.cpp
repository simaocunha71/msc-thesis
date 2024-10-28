/*
Implement a function that takes an non-negative integer and returns a vector of the first n
integers that are prime numbers and less than n.
for example:
count_up_to(5) => {2,3}
count_up_to(11) => {2,3,5,7}
count_up_to(0) => {}
count_up_to(20) => {2,3,5,7,11,13,17,19}
count_up_to(1) => {}
count_up_to(18) => {2,3,5,7,11,13,17}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> count_up_to(int n){

vector<int> v;
for(int i = 2; i < n; i++){
    if(is_prime(i)){
        v.push_back(i);
    }
}
return v;
}
bool is_prime(int n){
for(int i = 2; i < n; i++){
    if(n % i == 0){
        return false;
    }
}
return true;
}
int main(){
vector<int> v = count_up_to(100000);
for(int i = 0; i < v.size(); i++){
    printf("%d ", v[i]);
}
}

