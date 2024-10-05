    int l = txt.size();
    if(l == 0) return false;
    if(txt[l-1] >= 'a' && txt[l-1] <= 'z') return true;
    if(txt[l-1] >= 'A' && txt[l-1] <= 'Z') return true;
    for(int i = l-2; i >= 0; i--)
    {
        if(txt[i] != ' ') return false;
    }
    return true;
}

/*
Create a function that takes a string as a parameter and returns
the string with each of the first letters of the words capitalized,
and the rest of the letters in lowercase.

Examples:
capitalize_first_letter("This is a sentence") ➞ "This Is A Sentence"
capitalize_first_letter("I love to code") ➞ "I Love To Code"
capitalize_first_letter("I am an engineer") ➞ "I Am An Engineer"
capitalize_first_letter("") ➞ ""
*/
#include<iostream>
#include<cctype>
using namespace std;
string capitalize_first_letter(string txt){
    string ans = "";
    for(int i = 0; i < txt.size(); i++)
    {
        if(txt[i] >= 'a' && txt[i] <= 'z')
        {
            ans += tolower(txt[i]);
        }
        else
        {
            ans += txt[i];
        }
        if(txt[i] == ' ' || i == txt.size()-1) ans += " ";
    }
    for(int i = 0; i < ans.size(); i++)
    {
        if(ans[i] >= 'a' && ans[i] <= 'z')
        {
            ans[i] = toupper(ans[i]);
        }
    }
    ans.pop_back();
    return ans;
}

/*
Create a function that takes a string as a parameter and returns
a string with each of the first letters of the words capital