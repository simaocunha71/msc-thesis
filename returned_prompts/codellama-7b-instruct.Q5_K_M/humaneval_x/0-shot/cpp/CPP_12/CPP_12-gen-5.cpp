/*
Out of vector of strings, return the longest one. Return the first one in case of multiple
strings of the same length. Return None in case the input vector is empty.
>>> longest({})

>>> longest({"a", "b", "c"})
"a"
>>> longest({"a", "bb", "ccc"})
"ccc"
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string longest(vector<string> strings){

Answer:
/*
Out of vector of strings, return the longest one. Return the first one in case of multiple
strings of the same length. Return None in case the input vector is empty.
>>> longest({})

>>> longest({"a", "b", "c"})
"a"
>>> longest({"a", "bb", "ccc"})
"ccc"
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string longest(vector<string> strings){
    if(strings.size() == 0)
        return "";
    string longest = strings[0];
    for(string s : strings)
        if(s.size() > longest.size())
            longest = s;
    return longest;
}

int main(){
    vector<string> v;
    v.push_back("a");
    v.push_back("bb");
    v.push_back("ccc");
    printf("%s\n", longest(v).c_str());
    return 0;
}
