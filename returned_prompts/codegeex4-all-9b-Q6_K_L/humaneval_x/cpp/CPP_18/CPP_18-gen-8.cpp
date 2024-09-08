#include<stdio.h>
#include<string>
using namespace std;
int how_many_times(string str,string substring){
    int len = str.length();
    int sublen = substring.length();
    int count = 0;
    for(int i = 0;i<len;i++){
        if(str[i] == substring[0]){
            int j = 1;
            while(j < sublen && str[i+j] == substring[j]){
                j++;
            }
            if(j == sublen){
                count++;
                i+=sublen-1;
            }
        }
    }
    return count;
}