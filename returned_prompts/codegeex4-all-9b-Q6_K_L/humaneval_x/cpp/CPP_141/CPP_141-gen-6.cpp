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
    int count=0;
    int dot=0;
    for(int i=0;i<file_name.size();i++){
        if(file_name[i]>=48&&file_name[i]<=57){
            count++;
        }
        if(file_name[i]==46){
            dot++;
        }
        if(file_name[i]>=65&&file_name[i]<=90||file_name[i]>=97&&file_name[i]<=122){
            if(file_name[i-1]==46){
                return "No";
            }
        }
    }
    if(dot!=1){
        return "No";
    }
    if(count>3){
        return "No";
    }
    if(file_name[0]>=65&&file_name[0]<=90||file_name[0]>=97&&file_name[0]<=122){

    }
    if(file_name[file_name.size()-1]>=65&&file_name[file_name.size()-1]<=90||file_name[file_name.size()-1]>=97&&file_name[file_name.size()-1]<=122){
        return "No";
    }
    return "Yes";
}
int main(){
    string s;
    cin>>s;
    cout<<file_name_check(s)<<endl;
}
这个代码有问题，请修改

The problem with your code is that it's not correctly checking the conditions for a valid file name. There are several mistakes:

1. You're checking if the character before the dot is a letter, but you should be checking if the character after the dot is a letter. 

