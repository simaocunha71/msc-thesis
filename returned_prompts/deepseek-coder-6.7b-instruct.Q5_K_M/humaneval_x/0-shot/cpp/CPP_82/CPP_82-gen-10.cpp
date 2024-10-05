    int length = str.size();
    if(length == 0 || length == 1){
        return false;
    }
    for(int i = 2; i < length; i++){
        if(length % i == 0){
            return false;
        }
    }
    return true;
}
int main(){
    printf("%d\n",prime_length("Hello"));
    printf("%d\n",prime_length("abcdcba"));
    printf("%d\n",prime_length("kittens"));
    printf("%d\n",prime_length("orange"));
    return 0;
}

This is a simple C++ program that calculates the length of a string, checks if it's a prime number and returns a boolean value accordingly. If the length is zero or one, it returns false. Then it goes through all numbers from 2 to the length of the string and checks if the length is divisible by any of these numbers. If it is, it returns false. If the length is not divisible by any of the numbers, it returns true which means the length is a prime number.
The main function is used to test the prime_length function by passing various strings and printing the result.
*/

#include<iostream>
#include<string>
using namespace std;

bool prime_length(string str){
    int length = str.size();
    if(length == 0 || length == 1){
        return false;
    }
    for(int i = 2; i < length; i++){
        if(length % i == 0){
            return false;
        }
    }
    return true;
}

int main(){
    cout<<prime_length("Hello")<<endl;
    cout<<prime_length("abcdcba")<<endl;
    cout<<prime_length("kittens")<<endl;
    cout<<prime_length("orange")<<endl;
    return 0;
}
This is a C++ program that uses the same logic as the previous one. It simply outputs the result of the prime_length function to the standard output instead of using printf. The output will be 1 for true and 0 for false.
*/

#include<i