#include<stdio.h>
#include<vector>
#include<string>
#include<iterator>
#include<algorithm>
using namespace std;
vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> ret;
    copy_if(strings.begin(),strings.end(),back_inserter(ret),[prefix](const string& s){return s.compare(0,prefix.size(),prefix)==0;});
    return ret;
}