    if(dict.empty())return false;
    for(auto it : dict){
        if(it.first[0] >= 'A' && it.first[0] <= 'Z')return false;
        if(it.second[0] >= 'a' && it.second[0] <= 'z')return false;
    }
    return true;
}

/*
Given a number, return the number of 1's in the binary
representation of that number.
Examples:
count_ones(13) should return 2 because 13 in binary is 1101.
count_ones(123) should return 2 because 123 in binary is 1110011.
count_ones(0) should return 0 because 0 in binary is 0.
*/
#include<bitset>
int count_ones(int n){
    bitset<32> b(n);
    return b.count();
}

/*
Given an array of strings, return true if all the strings
in the array are of length 5, else return false.
Examples:
is_length_5({"Hello", "World", "!"}) should return true.
is_length_5({"Hi", "There"}) should return false.
is_length_5({"12345", "67890"}) should return false.
*/
bool is_length_5(vector<string> arr){
    for(auto it : arr){
        if(it.length() != 5)return false;
    }
    return true;
}

/*
Given a string, return true if the string is a palindrome,
else return false. A palindrome is a string that reads the same
forward and backward.
Examples:
is_palindrome("level") should return true.
is_palindrome("hello") should return false.
is_palindrome("racecar") should return true.
*/
bool is_palindrome(string str){
    int len = str.length();
    for(int i = 0; i < len/2; i++){
        if(str[i