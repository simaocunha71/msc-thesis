#include<stdio.h>
#include<math.h>
#include<assert.h>
#include<vector>
#include<string>
using namespace std;
#include<algorithm>
#include<iterator>
#include<functional>
#include<map>
#include<set>
#include<queue>
#include<deque>
#include<stack>
#include<bitset>
#include<list>
#include<sstream>
#include<fstream>
#include<numeric>
#include<unordered_map>

/*
Filter an input vector of strings only for ones that contain given substring
>>> filter_by_substring({}, "a")
{}
>>> filter_by_substring({"abc", "bacd", "cde", "vector"}, "a")
{"abc", "bacd", "vector"}
*/
vector<string> filter_by_substring(vector<string> strings, string substring){
    vector<string> result;
    copy_if(strings.begin(), strings.end(), back_inserter(result), [&substring](string &str){return str.find(substring) != string::npos;});
    return result;
}
void test_filter_by_substring(){
    assert(filter_by_substring({}, "a") == vector<string>{});
    assert(filter_by_substring({"abc", "bacd", "cde", "vector"}, "a") == vector<string>{"abc", "bacd", "vector"});
}

int main(){
    test_filter_by_substring();
    return 0;
}