    int sum = 0;
    for(int i = 0;i<k;i++){
        if(arr[i]<100){
            sum += arr[i];
        }
    }
    return sum;
}

int main(){
    vector<int> arr = {111,21,3,4000,5,6,7,8,9};
    int k = 4;
    printf("%d",add_elements(arr,k));
    return 0;
}
*/
/*

Given a string s, return the 'length of the largest group' of 1s in the binary representation of s. Throw out any leading zeroes and return the size of the largest group of 1s.

Examples:

    Input: "11001" -> 3
    Input: "0101" -> 2
    Input: "00110" -> 2

Constraints:
    1. The string will be in binary representation with no spaces.
    2. The length of the string will be at most 1000.
    3. The input string will consist of only '0' and '1's.

*/

#include <bits/stdc++.h>
using namespace std;

int find_ones(string s){
    int max_ones = 0;
    int current_ones = 0;
    for(int i = 0;i<s.size();i++){
        if(s[i] == '1'){
            current_ones++;
        }else{
            if(current_ones > max_ones){
                max_ones = current_ones;
            }
            current_ones = 0;
        }
    }
    if(current_ones > max_ones){
        max_ones = current_ones;
    }
    return max_ones;
}

int main(){
    string s = "11001";
    printf("%d",find_ones(s));
    return 0;
}




/*
Given an integer array arr, return the sum of all even length subarrays of arr.