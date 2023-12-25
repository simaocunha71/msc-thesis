/*
Given a string, find out how many distinct characters (regardless of case) does it consist of
>>> count_distinct_characters("xyzXYZ")
3
>>> count_distinct_characters("Jerry")
4
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
int count_distinct_characters(string str){ 
	ifstream infile("data/input1.txt"); 
        vector<char> v; 
    	while(!infile) {v.push_back('X');}
        while (getline(infile,str)) { 
            if (isalpha(str[0])) 
                    v.push_back((int) str[0]); 
                else 
                        continue;
		
         }
     return (int)v.size(); // (v.size() -1);
}
