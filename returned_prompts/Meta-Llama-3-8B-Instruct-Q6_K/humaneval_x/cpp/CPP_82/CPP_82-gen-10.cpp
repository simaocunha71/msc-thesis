    int n = str.length();
    for(int i=2; i<=n; i++){
        int count = 0;
        for(int j=2; j<=i; j++){
            if(i%j == 0) count++;
        }
        if(count == 0) return true;
    }
    return false;
}
int main(){
    printf("%d\n", prime_length("Hello"));  //true
    printf("%d\n", prime_length("abcdcba")); //true
    printf("%d\n", prime_length("kittens"));   //true
    printf("%d\n", prime_length("orange"));    //false
    return 0;
}
C:
#include <stdio.h>
#include <string.h>

bool isPrime(int n) {
    if (n <= 1) return false;
    for(int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

bool prime_length(char *str) {
    int len = strlen(str);
    return isPrime(len);
}

int main() {
    printf("%d\n", prime_length("Hello"));  //true
    printf("%d\n", prime_length("abcdcba")); //true
    printf("%d\n", prime_length("kittens"));   //true
    printf("%d\n", prime_length("orange"));    //false
    return 0;
}C++:
#include <iostream>
#include <string>

bool isPrime(int n) {
    if (n <= 1) return false;
    for(int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

bool prime_length(const std::string& str) {
    return isPrime(str.length());
}

int main() {
    std::cout << (prime_length("Hello") ? "true" : "false") << std::endl; //true
    std::cout << (prime_length("abcdcba") ? "true" : "false") << std::endl; //true
    std::cout << (prime_length("kittens") ? "true" : "false") << std::endl; //true
    std::cout << (prime_length("orange") ? "true" : "false") << std::endl; //false
    return 0;
}C#:
using