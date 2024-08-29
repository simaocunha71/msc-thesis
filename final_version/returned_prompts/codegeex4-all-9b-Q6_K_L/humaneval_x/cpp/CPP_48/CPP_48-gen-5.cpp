#include <bits/stdc++.h>
#include <string>
using namespace std;

bool is_palindrome(string text){
    string reversed_text = text;
    reverse(reversed_text.begin(), reversed_text.end());
    return reversed_text == text;
}
