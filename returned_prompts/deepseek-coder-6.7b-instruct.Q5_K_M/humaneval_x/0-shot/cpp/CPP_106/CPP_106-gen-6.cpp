    vector<int> vec;
    for(int i=1; i<=n; i++){
        if(i%2==0){
            int fact=1;
            for(int j=1; j<=i; j++){
                fact = fact * j;
            }
            vec.push_back(fact);
        }
        else{
            int sum=0;
            for(int j=1; j<=i; j++){
                sum = sum + j;
            }
            vec.push_back(sum);
        }
    }
    return vec;
}
int main(){
    int n=5;
    vector<int> result = f(n);
    for(int i=0; i<result.size(); i++){
        printf("%d ", result[i]);
    }
    return 0;
}

*/

#include <iostream>
#include <vector>
using namespace std;

int fact(int num){
    int f=1;
    for(int i=1; i<=num; i++){
        f = f * i;
    }
    return f;
}

int sum(int num){
    int s=0;
    for(int i=1; i<=num; i++){
        s = s + i;
    }
    return s;
}

vector<int> f(int n){
    vector<int> vec;
    for(int i=1; i<=n; i++){
        if(i%2==0){
            vec.push_back(fact(i));
        }
        else{
            vec.push_back(sum(i));
        }
    }
    return vec;
}

int main(){
    int n=5;
    vector<int> result = f(n);
    for(int i=0; i<result.size(); i++){
        cout<<result[i]<<" ";
    }
    return 0;
}

//main.cpp
/*
