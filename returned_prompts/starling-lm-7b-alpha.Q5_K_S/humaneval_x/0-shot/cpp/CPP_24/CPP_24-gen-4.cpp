    if(n % 2 == 0){
        return n/2;
    }
    else{
        for(int i = 3; i <= n/2; i+=2){
            if(n % i == 0){
                return i;
            }
        }
    }
    goto A;
}




/*
For a given number n, find the largest number that divides n evenly, smaller than n
>>> largest_divisor(15)
5
*/
#include<stdio.h>
using namespace std;
int largest_divisor(int n){
    for(int i = 2; i <= n/2; i++){
        if(n % i == 0){
            return i;
        }
    }
    return n;
}




/*
For a given number n, find the largest number that divides n evenly, smaller than n
>>> largest_divisor(15)
5
*/
#include<stdio.h>
using namespace std;
int largest_divisor(int n){
    int i = 2;
    while(i * i <= n){
        if(n % i == 0){
            return i;
        }
        i++;
    }
    return n;
}









































































































































































































