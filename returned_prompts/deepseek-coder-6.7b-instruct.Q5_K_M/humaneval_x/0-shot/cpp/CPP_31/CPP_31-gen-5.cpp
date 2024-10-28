    if (n <= 1){
        return false;
    }
    if (n <= 3){
        return true;
    }
    if (n % 2 == 0 || n % 3 == 0){
        return false;
    }
    for (long long i = 5; i * i <= n; i += 6){
        if (n % i == 0 || n % (i + 2) == 0){
            return false;
        }
    }
    return true;
}

int main(){
    long long n;
    printf("Enter a number: ");
    scanf("%lld", &n);
    if(is_prime(n)){
        printf("true");
    }
    else{
        printf("false");
    }
    return 0;
}
*/

#include<stdio.h>
bool is_prime(long long n){
    if (n <= 1){
        return false;
    }
    if (n <= 3){
        return true;
    }
    if (n % 2 == 0 || n % 3 == 0){
        return false;
    }
    for (long long i = 5; i * i <= n; i += 6){
        if (n % i == 0 || n % (i + 2) == 0){
            return false;
        }
    }
    return true;
}

int main(){
    long long n;
    printf("Enter a number: ");
    scanf("%lld", &n);
    if(is_prime(n)){
        printf("true");
    }
    else{
        printf("false");
    }
    return 0;
}

//src/main.cpp
//main.cpp
#include<iostream>
#include "is_prime.cpp"

int main(){
    long long n;
    std::cout << "Enter a number: ";
    std::cin >> n;
    if(is_prime(n)){
        std::cout << "true";
    }
    else{
        std::cout << "false";
    }
    return 0;
}

//src/tests