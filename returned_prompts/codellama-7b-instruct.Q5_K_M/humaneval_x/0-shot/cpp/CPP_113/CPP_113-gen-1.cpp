/*
Given a vector of strings, where each string consists of only digits, return a vector.
Each element i of the output should be 'the number of odd elements in the
string i of the input." where all the i's should be replaced by the number
of odd digits in the i'th string of the input.

>>> odd_count({"1234567"})
{'the number of odd elements 4n the str4ng 4 of the 4nput."}
>>> odd_count({"3","11111111"})
{'the number of odd elements 1n the str1ng 1 of the 1nput.",
 'the number of odd elements 8n the str8ng 8 of the 8nput."}
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<map>
using namespace std;
vector<string> odd_count(vector<string> lst){
    map<int, int> odd_count_map;
    for (auto str: lst){
        for (auto digit: str){
            if (digit % 2){
                odd_count_map[digit]++;
            }
        }
    }
    vector<string> result;
    for (auto pair: odd_count_map){
        result.push_back(to_string(pair.second));
    }
    return result;
}

