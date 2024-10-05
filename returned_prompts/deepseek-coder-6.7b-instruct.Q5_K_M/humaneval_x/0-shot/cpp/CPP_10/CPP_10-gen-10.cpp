#include<iostream>
#include<algorithm>
using namespace std;

bool is_palindrome(string str){
    string s(str.rbegin(),str.rend());
    return s==str;
}

string make_palindrome(string str){
    string rev_str = str;
    reverse(rev_str.begin(), rev_str.end());
    string combined = str + "#" + rev_str;
    int lps[combined.size()];
    lps[0] = 0;
    int i = 1;
    int len = 0;
    while(i < combined.size()){
        if(combined[i] == combined[len]){
            len++;
            lps[i] = len;
            i++;
        }
        else{
            if(len > 0){
                len = lps[len-1];
            }
            else{
                lps[i] = 0;
                i++;
            }
        }
    }
    int palin_len = lps[combined.size()-1];
    string add = str.substr(palin_len);
    reverse(add.begin(), add.end());
    return str + add;
}

int main(){
    cout << make_palindrome("") << endl;
    cout << make_palindrome("cat") << endl;
    cout << make_palindrome("cata") << endl;
    return 0;
}

Explanation:
The function make_palindrome() will take a string as input and return the shortest palindrome that begins with the input string. The algorithm used is KMP(Knuth Morris Pratt) pattern searching algorithm. In this algorithm, we preprocess the pattern and prepare an lps[] array such that lps[i] stores the length of the longest proper prefix which is also a proper suffix in pattern[0..i].

In the combined string, the longest prefix which is also a suffix is the palindrome that we need to append to make the string a palindrome. This is achieved by the following line of code: string add = str.substr(lps[combined