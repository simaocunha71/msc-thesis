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
	if (file_name.length() > 3 || !isdigit('0', '\'1', '\''2', '3', '\''5, '\''6', '\''7', '\''8', '\''9')){ //if the length of file name is not between 1 and 4 then return "NO"
		return "No";
	}else if (file_name.find(".") != file_name.length() - 1){ //if there no dot at the end of string then return "No"
		return "No";
	}else if ((file_name.substr(0, 3).compare("example")) == 0 || (file_name.substr(0, 4).compare("example") == 0)){ //if the first three characters of file name are not like example. then return "NO"
		return "No";
	}else if ((file_name.find(".") - file_name.find(".dll")) != 3 || (file_name.find(".") - file_name.find(".exe") == 1 && (file_name.find(".") - file_name.find(".txt") )!=2 &&(