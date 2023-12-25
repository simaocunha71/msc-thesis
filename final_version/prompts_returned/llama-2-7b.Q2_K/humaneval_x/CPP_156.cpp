/*
Given a positive integer, obtain its roman numeral equivalent as a string,
and return it in lowercase.
Restrictions: 1 <= num <= 1000

Examples:
>>> int_to_mini_roman(19) == "xix"
>>> int_to_mini_roman(152) == "clii"
>>> int_to_mini_roman(426) == "cdxxvi"
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string int_to_mini_romank(int number){
	if(number<=0 || number>=1000) return "-1";
        vector <string> v;
                for (int i=0; i<27; ++i) {
                        if ((i+1)%3==0 && i>4) v.push_back(to_string(1)); 
                        else if ((i+1)%3==0 && i>0) v.push_back("m");
                        else if (i>=6) v.push_back(to_string(9));
                        else if ((i+1)%2==1) v.push_back(to_string(4));
                        else if (i>=5) v.push_back("v");
                        else if (i>=7) v.push_back("l");
                        
                        else if ((i+1)%2==0 && i>3) v.push_back(to_string(-4));
                        else if (i>=8) v.push_back("x"); 
                        else if (i>=6) v.push_back("vi" [!((i+1)%5)];
                         else if ((i+1)%3==1 && i>2) {
                                if(v[v.size()-1][0]='m' || v[v.size()-1][0]='x') v[v.size()-1]="cl"; 
                         } else if ((i+1)%3==1 && i>0) {
