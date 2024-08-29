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
    int len = str.length();
    int i;
    for(i=2;i<=len/2;i++){
        if(len%i==0){
            return false;
        }
    }
    return true;
}

int main(){
    string str;
    cout<<"Enter the string: ";
    getline(cin,str);
    if(prime_length(str)){
        cout<<"Prime";
    }
    else{
        cout<<"Not Prime";
    }
    return 0;
}
