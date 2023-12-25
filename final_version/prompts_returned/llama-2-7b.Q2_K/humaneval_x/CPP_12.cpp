/*
Out of vector of strings, return the longest one. Return the first one in case of multiple
strings of the same length. Return None in case the input vector is empty.
>>> longest({})

>>> longest({"a", "b", "c"})
"a"
>>> longest({"a", "bb", "ccc"})
"ccc"
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string longest(vector<string> strings){
	if(strings.size()==0) return "";
	else {
    	int max_len=0;
    	int index, i=1;
        string s;
    	for(int j=0;j<strings.size();j++){
    	    if(max_len>s.length())i=1;
    	    else{
    	        if(i==0){
    	            index=j;
    	        }
    	        i++;
    	    }
    	    s=strings[index];
    	    max_len+=s.length();
    	}
    	return s;
    }
}
int main(){
    vector<string> strings={"a", "b", "c"};
    string str="a";
    
    
    return 0;
}