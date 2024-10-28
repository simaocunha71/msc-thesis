    vector<string> res;
    for(auto &s: lst){
        int count=0;
        for(auto &c: s){
            if((c-'0') % 2 != 0)
                count++;
        }
        string str_count = to_string(count);
        string temp = "the number of odd elements in the string "+str_count+" of the input.";
        res.push_back(temp);
    }
    return res;
}

int main(){
    vector<string> lst = {"3","11111111"};
    vector<string> res = odd_count(lst);
    for(auto &s: res){
        printf("%s\n", s.c_str());
    }
    return 0;
}

Answer:
The program accepts a vector of strings where each string consists only of digits. It then counts the number of odd digits in each string and stores the count in a new string that is pushed to the result vector. The function then returns the result vector. 

In the main function, we test the function with a vector containing two strings. The function returns a vector of strings with the counts of odd digits in each string. We then print each string in the returned vector.

Note: This program uses C++11 and later versions.
*/

#include<iostream>
#include<vector>
#include<string>
using namespace std;

vector<string> odd_count(vector<string> lst){
    vector<string> res;
    for(auto &s: lst){
        int count=0;
        for(auto &c: s){
            if((c-'0') % 2 != 0)
                count++;
        }
        res.push_back("the number of odd elements is "+to_string(count)+" in the string of the input.");
    }
    return res;
}

int main(){
    vector<string> lst = {"3","11111111"};
    vector<string> res = odd_count(lst);
    for(auto &s: res