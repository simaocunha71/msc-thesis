/*
Out of vector of strings, return the longest one. Return the first one in case of multiple
strings of the same length. Return None in case the input vector is empty.
>>> longest({})

>>> longest({"a", "b", "c"})
"a"
>>> longest({"a", "bb", "ccc"})
"ccc"
*/
#include<iostream>
#include<vector>
#include<string>
using namespace std;
string longest(vector<string> strings){

B:
/*
Out of vector of strings, return the longest one. Return the first one in case of multiple
strings of the same length. Return None in case the input vector is empty.
>>> longest({})

>>> longest({"a", "b", "c"})
"a"
>>> longest({"a", "bb", "ccc"})
"ccc"
*/
#include<iostream>
#include<vector>
#include<string>
using namespace std;
string longest(vector<string> strings){

C:
/*
Out of vector of strings, return the longest one. Return the first one in case of multiple
strings of the same length. Return None in case the input vector is empty.
>>> longest({})

>>> longest({"a", "b", "c"})
"a"
>>> longest({"a", "bb", "ccc"})
"ccc"
*/
#include<iostream>
#include<vector>
#include<string>
using namespace std;
string longest(vector<string> strings){
    if(strings.empty()) return string();

    string longest = strings[0];
    for (size_t i = 1; i < strings.size(); i++)
    {
        if(strings[i].length() > longest.length())
            longest = strings[i];
    }
    return longest;
}

D:
/*
Out of vector of strings, return the longest one. Return the first one in case of multiple
strings of the same length. Return None in case the input vector is empty.
>>> longest({})

>>> longest({"a", "b", "c"})
"a"
>>> longest({"a", "bb", "ccc"})
"ccc"
*/
#include<iostream>
#include<vector>
#include<string>
using namespace std;
string longest(vector<string> strings){
    if(strings.empty()) return string();

    string longest = strings[0];
    for (size_t i = 0; i < strings.size(); i++)
    {
        if(strings[i].length() > longest.length())
            longest = strings[i];
    }
    return longest;
}


E:
/*
Out of vector of strings, return the longest one. Return the first one in case of multiple
strings of the same length. Return None in