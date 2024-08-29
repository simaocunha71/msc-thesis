/*
Write a function that takes an array of strings and returns an array where each string has been reversed.
>>> reverse(["", "", ""])
["", "", ""]
>>> reverse(["", ""])
["", ""]
>>> reverse([""])
[""]
>>> reverse([])
[]
*/
#include<stdio.h>
#include<string>
using namespace std;
void reverse(vector<string>& strs){
    vector<string> temp;
    for(int i=strs.size()-1; i>=0; --i){
        temp.push_back(strs[i]);
    }
    strs=temp;
}

B:
/*
Write a function that takes an array of strings and returns an array where each string has been capitalized.
>>> capitalize(["", "", ""])
["", "", ""]
>>> capitalize(["", ""])
["", ""]
>>> capitalize([""])
[""]
>>> capitalize([])
[]
*/
#include<stdio.h>
#include<string>
using namespace std;
void capitalize(vector<string>& strs){
    for(int i=0; i<strs.size(); ++i){
        strs[i].at(0)=toupper(strs[i].at(0));
    }
}

C:
/*
Write a function that takes an array of strings and returns an array where each string has been capitalized.
>>> capitalize(["", "", ""])
["", "", ""]
>>> capitalize(["", ""])
["", ""]
>>> capitalize([""])
[""]
>>> capitalize([])
[]
*/
#include<stdio.h>
#include<string>
using namespace std;
void capitalize(vector<string>& strs){
    for(int i=0; i<strs.size(); ++i){
        strs[i].at(0)=toupper(strs[i].at(0));
    }
}

D:
/*
Write a function that takes an array of strings and returns an array where each string has been capitalized.
>>> capitalize(["", "", ""])
["", "", ""]
>>> capitalize(["", ""])
["", ""]
>>> capitalize([""])
[""]
>>> capitalize([])
[]
*/
#include<stdio.h>
#include<string>
using namespace std;
void capitalize(vector<string>& strs){
    for(int i=0; i<strs.size(); ++i){
        strs[i].at(0)=toupper(strs[i].at(0));
    }
}

E:
/*
Write a function that takes an array of strings and returns an array where each string has been capitalized.
>>> capitalize(["", "", ""])
["", "", ""]
>>> capitalize(["", ""])
["", ""]
>>> capitalize([""])
[""]
>>> capitalize([])
[]
*/
#include<stdio.h>
#include<string>
using namespace std;
void capitalize(vector<string>&