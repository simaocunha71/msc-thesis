/*
Filter an input vector of strings only for ones that start with a given prefix.
>>> filter_by_prefix({}, "a")
{}
>>> filter_by_prefix({"abc", "bcd", "cde", "vector"}, "a")
{"abc", "vector"}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> filter_by_prefix(vector<string> strings, string prefix){
	int start = 0;
	for (auto i = 1; i < strings.size(); ++i) {
    if (strings[start++].compare(0, strings[i].length(), prefix) == 0 && !strcmp(prefix,"")){
      cout << "Finding: '" << prefix << "'";
    	if (!strcmp(prefix,""))
    	  filter.push_back("'");
    }else if (strings[start++] < strings[i]) {
        start = i - 1;
    } else {
      int j;
      for (j = start + 1; j <= i - 1; ++j) {
        if (!strcmp(prefix,"")){
          filter.push_back("'");
          	start++;
        }else if (strings[j] < strings[i]) {
        	++start;
        } else break;
      }
    }
  }
  return vector<string>(filter);
}
