    if (is_palindrome(str)){
        return str;
    }
    string rev_str(str.rbegin(), str.rend());
    for (int i = 1; i <= str.size(); ++i){
        if (is_palindrome(rev_str.substr(i))){
            string prefix(str.begin(), str.begin() + i);
            string suffix(rev_str.begin(), rev_str.begin() + i);
            string add(suffix.rbegin(), suffix.rend());
            return str + add;
        }
    }
    return str + rev_str;
}

int main(){
    string str;
    while(cin>>str){
        cout<<make_palindrome(str)<<endl;
    }
    return 0;
}

You should run this program in a C++ environment. The program reads strings from standard input and outputs the shortest palindrome that begins with the input string.


Example:
Input: "cat"
Output: "catac"

Input: "cata"
Output: "catac"

Input: "a"
Output: "a"

Input: ""
Output: ""
*/

//SRC/Q.cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Function to check if a string is palindrome
bool isPalindrome(string str, int start, int end) {
    while (start < end) {
        if (str[start] != str[end])
            return false;
        start++;
        end--;
    }
    return true;
}

// Function to find the shortest palindrome that can be formed
string shortestPalindrome(string s) {
    int n = s.size();
    int end = n - 1;
    while (end >= 0) {
        // If string is palindrome till end, no need to add anything
        if (isPalindrome(s, 0, end))
            break;
        end--;
    }
    // If string is palindrome till end, no need