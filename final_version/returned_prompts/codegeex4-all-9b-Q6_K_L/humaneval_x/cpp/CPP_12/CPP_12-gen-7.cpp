#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string longest(vector<string> strings){
    if(strings.size()==0){
        return NULL;
    }
    int longest=0;
    int index=0;
    for(int i=0;i<strings.size();i++){
        if(strings[i].length()>longest){
            longest=strings[i].length();
            index=i;
        }
    }
    return strings[index];
}