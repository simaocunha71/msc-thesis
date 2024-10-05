
#include <bits/stdc++.h> 

using namespace std; 

string make_palindrome(string str) { 
    int n = str.length(); 
    int start = 0, maxLength = 0; 
  
    for (int i = 0; i < n; i++) { 
        int len = isPalindrome(str, 0, i); 
        if (len > maxLength) { 
            start = i - len + 1; 
            maxLength = len; 
        } 
    } 
  
    return str.substr(start, maxLength) + str.substr(0, start) + 
        str.substr(start + maxLength); 
} 

int isPalindrome(string str, int i, int j) { 
    while (i < j) { 
        if (str[i] != str[j]) 
            return 0; 
        i++, j--; 
    } 
    return 1; 
}




