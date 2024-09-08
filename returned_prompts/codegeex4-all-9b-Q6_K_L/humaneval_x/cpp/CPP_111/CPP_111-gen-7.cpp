#include<stdio.h>
#include<string>
#include<map>
using namespace std;
map<char,int> histogram(string test){
    map<char,int>histo;
    int max=0;
    if(test.length()==0)
        return histo;
    for(int i=0;i<test.length();i++){
        if(test[i]==' ')
            continue;
        if(histo.find(test[i])==histo.end())
            histo.insert(make_pair(test[i],1));
        else
            histo[test[i]]++;
    }
    for(map<char,int>::iterator it=histo.begin();it!=histo.end();it++){
        if(it->second>max)
            max=it->second;
    }
    map<char,int>res;
    for(map<char,int>::iterator it=histo.begin();it!=histo.end();it++){
        if(it->second==max)
            res.insert(make_pair(it->first,it->second));
    }
    return res;
}