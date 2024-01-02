/*
Given a map, return true if all keys are strings in lower 
case or all keys are strings in upper case, else return false.
The function should return false is the given map is empty.
Examples:
check_map_case({{"a","apple"}, {"b","banana"}}) should return true.
check_map_case({{"a","apple"}, {"A","banana"}, {"B","banana"}}) should return false.
check_map_case({{"a","apple"}, {"8","banana"}, {"a","apple"}}) should return false.
check_map_case({{"Name","John"}, {"Age","36"}, {"City","Houston"}}) should return false.
check_map_case({{"STATE","NC"}, {"ZIP","12345"} }) should return true.
*/
#include<stdio.h>
#include<string>
#include<map>
using namespace std;
bool check_dict_case(map<string,string> dict){
	if(dict.empty()){
		return false;
	}else{
    bool upper = true;
    map<string,string>::iterator it=dict.begin();
    while(it!=dict.end()){
      if((it->first).compare("")==0 || (it->second).compare("")==0)
	    return false;
      string temp1 = (it->first);
      string temp2 = it->second;
     //   printf("%s\n",temp1.c_str());
	  if(upper){
		if(temp1[0] == 'A' || temp1[0] == 'B'){
			it++;
		}else{
			return false;
		}
      }else{
		if(temp2[0]=='A'||temp2[0]=='B'){
			it++;
		}else{
        return false;
       //   printf("%s\n",temp1.c_str());
    }}
	  upper = !upper;
      it++;
    }//while(condition)
  }//if (first condition is satisfied then...)
return true;
}