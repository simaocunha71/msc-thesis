/*
Concatenate vector of strings into a single string
>>> concatenate({})
""
>>> concatenate({"a", "b", "c"})
"abc"
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string concatenate(vector<string> strings){
string s = "";
for(int i = 0; i < strings.size(); i++) {
s += strings[i];
}
return s;
}
int main() {
vector<string> strings;
strings.push_back("a");
strings.push_back("b");
strings.push_back("c");
printf("%s\n", concatenate(strings).c_str());
return 0;
}
