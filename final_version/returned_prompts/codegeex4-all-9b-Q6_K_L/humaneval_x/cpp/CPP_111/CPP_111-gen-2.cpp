#include<stdio.h>
#include<string>
#include<map>
using namespace std;
map<char,int> histogram(string test){
    map<char,int> result;
    map<char,int> test_map;
    for(int i=0;i<test.length();i++){
        test_map[test[i]]++;
    }
    int max=0;
    for(auto it=test_map.begin();it!=test_map.end();it++){
        if(it->second>max){
            max=it->second;
            result.clear();
            result.insert(pair<char,int>(it->first,it->second));
        }
        else if(it->second==max){
            result.insert(pair<char,int>(it->first,it->second));
        }
    }
    return result;
}
C:
#include<stdio.h>
#include<string>
#include<map>
using namespace std;
map<char,int> histogram(string test){
    map<char,int> result;
    map<char,int> test_map;
    for(int i=0;i<test.length();i++){
        test_map[test[i]]++;
    }
    int max=0;
    for(auto it=test_map.begin();it!=test_map.end();it++){
        if(it->second>max){
            max=it->second;
            result.clear();
            result.insert(pair<char,int>(it->first,it->second));
        }
        else if(it->second==max){
            result.insert(pair<char,int>(it->first,it->second));
        }
    }
    return result;
}
D:
#include<stdio.h>
#include<string>
#include<map>
using namespace std;
map<char,int> histogram(string test){
    map<char,int> result;
    map<char,int> test_map;
    for(int i=0;i<test.length();i++){
        test_map[test[i]]++;
    }
    int max=0;
    for(auto it=test_map.begin();it!=test_map.end();it++){
        if(it->second>max){
            max=it->second;
            result.clear();
            result.insert(pair<char,int>(it->first,it->second));
        }
        else if(it->second==max){
            result.insert(pair<char,int>(it->first,it->second));
        }
    }
    return result;
}
E:
#include<stdio.h>
#include<string>
#include<map>
using namespace std;
map<char,int> histogram(string test){
    map<char,int> result;
    map<char,int> test_map;
    for(int i=0;i<test.length();i++){
        test_map[test[i]]++;
   