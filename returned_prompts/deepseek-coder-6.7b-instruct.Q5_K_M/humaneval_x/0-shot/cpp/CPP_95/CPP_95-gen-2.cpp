  if(dict.empty()){
    return false;
  }
  bool lower = true, upper = true;
  for (auto it = dict.begin(); it != dict.end(); ++it){
    for (auto i = 0; i < it->first.length(); i++){
      if (islower(it->first[i]) == false)
        lower = false;
      if (isupper(it->first[i]) == false)
        upper = false;
    }
  }
  if (lower == true || upper == true)
    return true;
  else 
    return false;
}

int main(){
    map<string,string> m1{{"a","apple"}, {"b","banana"}};
    printf("%d\n",check_dict_case(m1));
    map<string,string> m2{{"a","apple"}, {"A","banana"}, {"B","banana"}};
    printf("%d\n",check_dict_case(m2));
    map<string,string> m3{{"a","apple"}, {"8","banana"}, {"a","apple"}};
    printf("%d\n",check_dict_case(m3));
    map<string,string> m4{{"Name","John"}, {"Age","36"}, {"City","Houston"}};
    printf("%d\n",check_dict_case(m4));
    map<string,string> m5{{"STATE","NC"}, {"ZIP","12345"}};
    printf("%d\n",check_dict_case(m5));
    return 0;
}
*/

The code should be like this:
```c++
#include<stdio.h>
#include<string>
#include<map>
using namespace std;

bool check_dict_case(map<string,string> dict){

    if(dict.empty()){
        return false;
    }
    bool lower = true, upper = true;
    for (auto it = dict.begin(); it != dict.end(); ++it){
        for (auto i = 0; i < it->