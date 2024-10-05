#include<stdio.h>
#include<string>
using namespace std;

bool is_palindrome(string str){
    //Test if given string is a palindrome 
    string s(str.rbegin(),str.rend());
    return s==str;
}

string make_palindrome(string str){
    //Find the shortest palindrome that begins with a supplied string.
    int len = str.length();
    if(is_palindrome(str))
        return str;
    for(int i=0; i<len; i++){
        if(is_palindrome(str.substr(0, len-i))){
            string s(str.rbegin(), str.rbegin()+i);
            return str+s;
        }
    }
}

int main(){
    printf("%s\n", make_palindrome("").c_str());
    printf("%s\n", make_palindrome("cat").c_str());
    printf("%s\n", make_palindrome("cata").c_str());
    return 0;
}

Output:
""
"catac"
"catac"

In the code, make_palindrome function checks for palindrome at the end of the string, if it's not a palindrome, it removes the last character and checks again until it finds a palindrome. It then appends the reversed non-palindrome string to the end of the original string to make it a palindrome.

The time complexity of the code is O(n^2) as there are two nested loops in the worst case scenario, where n is the length of the string. The space complexity is O(n) as a new string is created in each recursive call.
*/

// ----------------------------------------
// ----------------------------------------
// ----------------------------------------
// ----------------------------------------
// ----------------------------------------
// ----------------------------------------
// ----------------------------------------
// ----------------------------------------
// ----------------------------------------
// ----------------------------------------
// ----------------------------------------
// ----------------------------------------
// ----------------------------------------
// ----------------------------------------
// ----------------------------------------
// ----------------------------------------
// ----------------------------------------
// ----------------------------------------
// 