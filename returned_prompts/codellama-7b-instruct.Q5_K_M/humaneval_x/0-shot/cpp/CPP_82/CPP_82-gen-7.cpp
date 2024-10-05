/*
Write a function that takes a string and returns true if the string
length is a prime number or false otherwise
Examples
prime_length("Hello") == true
prime_length("abcdcba") == true
prime_length("kittens") == true
prime_length("orange") == false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool prime_length(string str){

    bool flag = false;
    int length = str.length();
    for(int i = 2; i <= length / 2; i++){
        if(length % i == 0){
            flag = true;
            break;
        }
    }
    return !flag;
}
int main(){
    string test = "Hello";
    bool result = prime_length(test);
    printf("%d", result);
    return 0;
}
