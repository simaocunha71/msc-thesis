    vector<string> prefixes;
    string prefix;
    int i;
    for (i=0;i<=str.length();i++)
    {
        prefix=str.substr(0,i);
        prefixes.push_back(prefix);
    }
    return prefixes;
}
// or using loop
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> all_prefixes(string str){
    vector<string> prefixes;
    string prefix;
    for (int i=1;i<=str.length();i++){
        prefix=str.substr(0,i);
        prefixes.push_back(prefix);
    }
    return prefixes;
}  // end of code
// or using boost library
#include< boost/algorithm/string.hpp>
#include<vector>
#include<string>
using namespace std;
using namespace boost;
vector<string> all_prefixes(string str){
    vector<string> prefixes;
    generate_all(prefixes, str);
    return prefixes;
}
// or using algorithm
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> all_prefixes(string str){
    vector<string> prefixes;
    for (int i=0;i<=str.length();i++){
        prefixes.push_back(str.substr(0,i+1));
    }
    return prefixes;
}

