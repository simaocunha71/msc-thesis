#include <iostream>
#include <regex>
using namespace std;

string file_name_check(string file_name){
    regex pattern("^([a-zA-Z][a-zA-Z0-9]{0,2})\\.(txt|exe|dll)$");
    if(regex_match(file_name, pattern))
        return "Yes";
    else
        return "No";
}

