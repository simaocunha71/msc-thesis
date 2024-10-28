/*
Write a function to filter a vector of strings to only include elements that contain a given substring.
>>> filter_by_substring({}, "a")
{}
>>> filter_by_substring({"abc", "bcd", "cde", "vector"}, "a")
{"abc", "cde"}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> filter_by_substring(vector<string> strings, string substring){

