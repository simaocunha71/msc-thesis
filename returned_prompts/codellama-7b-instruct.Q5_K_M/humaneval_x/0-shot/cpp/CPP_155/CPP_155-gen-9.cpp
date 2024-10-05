/*
Given an integer. return a vector that has the number of even and odd digits respectively.

 Example:
    even_odd_count(-12) ==> {1, 1}
    even_odd_count(123) ==> {1, 2}
*/
#include<stdio.h>
#include<math.h>
#include<string>
#include<vector>
using namespace std;
vector<int> even_odd_count(int num){
    int count_even = 0;
    int count_odd = 0;
    while(num > 0){
        if(num % 2 == 0){
            count_even++;
        }
        else{
            count_odd++;
        }
        num /= 10;
    }
    return {count_even, count_odd};
}
