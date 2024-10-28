    int len = str.size();
    int distinct_chars = 0;
    for(int i=0; i<len; i++) {
        int j;
        for(j=i+1; j<len; j++) {
            if(str[i]==str[j]) {
                break;
            }
        }
        if(j==len) {
            distinct_chars++;
        }
    }
    return distinct_chars;
}



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

    int len = str.size();
    int distinct_chars = 0;
    for(int i=0; i<len; i++) {
        int j;
        for(j=i+1; j<len; j++) {
            if(str[i]==str[j]) {
                break;
            }
        }
        if(j==len) {
            distinct_chars++;
        }
    }
    return distinct_chars;
}



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

    int len = str.size();
    int distinct_chars = 0;
    for(int i=0; i<len; i++) {
        int j;
        for(j=i+1; j<len; j++) {
            if(str[i]==str[j]) {
              