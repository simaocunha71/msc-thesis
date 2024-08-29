#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string longest(vector<string> strings){
    if(strings.empty())
    return "";
    string max="";
    for(int i=0;i<strings.size();i++){
        if(strings[i].length()>max.length())
            max=strings[i];
    }
    return max;
}