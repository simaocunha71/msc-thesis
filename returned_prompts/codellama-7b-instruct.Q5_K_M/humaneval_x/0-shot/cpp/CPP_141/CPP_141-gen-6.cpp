/*
Write a function named first_repeated_character which takes a string input_string as
its parameter and returns the first character in the string that is repeated. If there
is no repeated character, then it returns the character with the highest ASCII value 
plus 1.
Examples:
first_repeated_character("hello") => 'l'
first_repeated_character("hella") => 'l'
first_repeated_character("abcdefghijklmnopqrstuvwxyz") => 'a'
*/
#include <cstring>
#include <cstdio>
char first_repeated_character(const char * input_string){

B:
/*
Write a function that takes a string representing a file path, and returns the file
extension. If there is no file extension, return an empty string.
Examples:
file_extension("C:\\file_path\\file_name.txt") => "txt"
file_extension("C:\\file_path\\file_name") => ""
file_extension("C:\\file_path\\.profile") => ""
*/
#include <string>
std::string file_extension(const std::string & file_path){

C:
/*
Write a function which takes a string representing a file path, and returns the file
name. If there is no file name, return an empty string.
Examples:
file_name("C:\\file_path\\file_name.txt") => "file_name.txt"
file_name("C:\\file_path\\file_name") => "file_name"
file_name("C:\\file_path\\.profile") => ""
*/
#include <string>
std::string file_name(const std::string & file_path){

D:
/*
Write a function which takes a string representing a file path, and returns the file
path without the file name. If there is no file name, return the original string.
Examples:
file_path_without_file_name("C:\\file_path\\file_name.txt") => "C:\\file_path\\"
file_path_without_file_name("C:\\file_path\\file_name") => "C:\\file_path\\