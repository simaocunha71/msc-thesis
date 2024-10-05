  int lower=0, upper=0;
  for(auto it=dict.begin(); it != dict.end(); it++){
    for(int i=0; i<it->first.size(); i++){
      if(islower(it->first[i]))
        lower++;
      else if(isupper(it->first[i]))
        upper++;
    }
  }
  if(lower==dict.size() || upper==dict.size())
    return true;
  else 
    return false;
}

int main(){
  map<string, string> map1 = {{"a","apple"}, {"b","banana"}};
  printf("%d\n", check_dict_case(map1));

  map<string, string> map2 = {{"a","apple"}, {"A","banana"}, {"B","banana"}};
  printf("%d\n", check_dict_case(map2));

  map<string, string> map3 = {{"a","apple"}, {"8","banana"}, {"a","apple"}};
  printf("%d\n", check_dict_case(map3));

  map<string, string> map4 = {{"Name","John"}, {"Age","36"}, {"City","Houston"}};
  printf("%d\n", check_dict_case(map4));

  map<string, string> map5 = {{"STATE","NC"}, {"ZIP","12345"}};
  printf("%d\n", check_dict_case(map5));

  return 0;
}


A: Your question seems to be a mix of C and C++.
In C++, you can use the `std::map` to store key-value pairs.
The keys in the map are always unique.
You can use the `islower()` and `isupper()` functions to check if a character is in lower case or upper case respectively.

Here is the C++ code that you asked for:

```cpp
#include <iostream>
#include <map>
#include <cctype>

bool check_map_case(std::map