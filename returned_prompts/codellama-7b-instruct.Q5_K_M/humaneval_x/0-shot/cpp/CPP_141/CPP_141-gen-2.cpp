/*
Create a function which takes a string representing a file's name, and returns
"Yes" if the the file's name is valid, and returns "No" otherwise.
A file's name is considered to be valid if and only if all the following conditions 
are met:
- There should not be more than three digits ('0'-'9') in the file's name.
- The file's name contains exactly one dot "."
- The substring before the dot should not be empty, and it starts with a letter from 
the latin alphapet ('a'-'z' and 'A'-'Z').
- The substring after the dot should be one of these: {'txt", "exe", "dll"}
Examples:
file_name_check("example.txt") => "Yes"
file_name_check("1example.dll")  => "No" // (the name should start with a latin alphapet letter)
*/
#include<stdio.h>
#include<string>
using namespace std;
string file_name_check(string file_name){
    int count = 0, flag = 0;
    for(int i = 0; i < file_name.length(); i++){
        if(file_name[i] >= '0' && file_name[i] <= '9')
            count++;
        if(file_name[i] == '.'){
            if(flag)
                return "No";
            flag = 1;
            if(file_name[i + 1] != 't' && file_name[i + 1] != 'e' && file_name[i + 1] != 'x' && file_name[i + 1] != 'd')
                return "No";
        }
        if(file_name[i] == ' ' || file_name[i] == '.' || file_name[i] == '-')
            return "No";
        if(file_name[i] >= 'a' && file_name[i] <= 'z')
            continue;
        if(file_name[i] >= 'A' && file_name[i] <= 'Z')
            continue;
        return "No";