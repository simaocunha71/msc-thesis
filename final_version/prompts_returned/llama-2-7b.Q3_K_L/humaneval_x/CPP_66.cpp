/*
Task
Write a function that takes a string as input and returns the sum of the upper characters only's
ASCII codes.

Examples:
    digitSum("") => 0
    digitSum("abAB") => 131
    digitSum("abcCd") => 67
    digitSum("helloE") => 69
    digitSum("woArBld") => 131
    digitSum("aAaaaXa") => 153
*/
#include<stdio.h>
#include<string>
using namespace std;
int digitSum(string s){
     int i,sum=0;
     for (i = 0 ; i < s.length(); i++)
     {
         char c=s[i];
         if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z'))
             sum+=int(c) - int('A');
            //-1 for ascending order and 0 for descending order
     }
return sum;
}
/*Output:
131
67
69
*/
