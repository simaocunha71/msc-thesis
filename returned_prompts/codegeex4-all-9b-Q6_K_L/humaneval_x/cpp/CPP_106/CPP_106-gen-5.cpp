#include<stdio.h>
#include<vector>
using namespace std;

int factorial(int n){
    if(n==0 || n==1) return 1;
    return n * factorial(n-1);
}

int sum(int n){
    int sum = 0;
    for(int i = 1; i <= n; i++){
        sum += i;
    }
    return sum;
}

vector<int> f(int n){
    vector<int> result;
    for(int i = 1; i <= n; i++){
        if(i % 2 == 0){
            result.push_back(factorial(i));
        }else{
            result.push_back(sum(i));
        }
    }
    return result;
}

B:
#include<stdio.h>
#include<vector>
using namespace std;

int factorial(int n){
    if(n==0 || n==1) return 1;
    return n * factorial(n-1);
}

int sum(int n){
    int sum = 0;
    for(int i = 1; i <= n; i++){
        sum += i;
    }
    return sum;
}

vector<int> f(int n){
    vector<int> result;
    for(int i = 1; i <= n; i++){
        if(i % 2 == 0){
            result.push_back(factorial(i));
        }else{
            result.push_back(sum(i));
        }
    }
    return result;
}

int main(){
    vector<int> result = f(5);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    return 0;
}

C:
#include<stdio.h>
#include<vector>
using namespace std;

int factorial(int n){
    if(n==0 || n==1) return 1;
    return n * factorial(n-1);
}

int sum(int n){
    int sum = 0;
    for(int i = 1; i <= n; i++){
        sum += i;
    }
    return sum;
}

vector<int> f(int n){
    vector<int> result;
    for(int i = 1; i <= n; i++){
        if(i % 2 == 0){
            result.push_back(factorial(i));
        }else{
            result.push_back(sum(i));
        }
    }
    return result;
}

int main(){
    vector<int> result = f(5);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i