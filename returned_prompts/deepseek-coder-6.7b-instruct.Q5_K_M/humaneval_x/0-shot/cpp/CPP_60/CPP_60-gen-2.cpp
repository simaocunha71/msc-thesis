    int sum = 0;
    for(int i = 1; i <= n; i++){
        sum += i;
    }
    return sum;
}

int main(){
    printf("%d\n", sum_to_n(30));
    printf("%d\n", sum_to_n(100));
    printf("%d\n", sum_to_n(5));
    printf("%d\n", sum_to_n(10));
    printf("%d\n", sum_to_n(1));
    return 0;
}

*/

#include<iostream>
using namespace std;

int sum_to_n(int n){
    int sum = 0;
    for(int i = 1; i <= n; i++){
        sum += i;
    }
    return sum;
}

int main(){
    cout<<sum_to_n(30)<<endl;
    cout<<sum_to_n(100)<<endl;
    cout<<sum_to_n(5)<<endl;
    cout<<sum_to_n(10)<<endl;
    cout<<sum_to_n(1)<<endl;
    return 0;
}

//Q2/main.cpp
/*
