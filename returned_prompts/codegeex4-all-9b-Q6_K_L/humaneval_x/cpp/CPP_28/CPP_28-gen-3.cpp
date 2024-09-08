/*
Concatenate vector of strings into a single string
>>> concatenate({})
""
>>> concatenate({"a", "b", "c"})
"abc"
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string concatenate(vector<string> strings){
    string result;
    for (auto &s : strings) {
        result += s;
    }
    return result;
}

B:
/*
Concatenate vector of strings into a single string
>>> concatenate({})
""
>>> concatenate({"a", "b", "c"})
"abc"
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string concatenate(vector<string> strings){
    string result;
    for (auto &s : strings) {
        result.append(s);
    }
    return result;
}

C:
/*
Concatenate vector of strings into a single string
>>> concatenate({})
""
>>> concatenate({"a", "b", "c"})
"abc"
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string concatenate(vector<string> strings){
    string result;
    for (auto &s : strings) {
        result += s;
    }
    return result;
}

D:
/*
Concatenate vector of strings into a single string
>>> concatenate({})
""
>>> concatenate({"a", "b", "c"})
"abc"
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string concatenate(vector<string> strings){
    string result;
    for (auto &s : strings) {
        result.append(s.c_str());
    }
    return result;
}

E:
/*
Concatenate vector of strings into a single string
>>> concatenate({})
""
>>> concatenate({"a", "b", "c"})
"abc"
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string concatenate(vector<string> strings){
    string result;
    for (auto &s : strings) {
        result += s.c_str();
    }
    return result;
}

F:
/*
Concatenate vector of strings into a single string
>>> concatenate({})
""
>>> concatenate({"a", "b", "c"})
"abc"
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string concatenate(vector<string> strings){
    string result;
    for (auto &s : strings) {
        result = result + s;
    }
    return result;
}

G:
/*
Concatenate vector of strings into a single string
>>> concatenate({})
""
>>> concatenate({"a", "b", "c"})
"abc"
*/
#include<stdio