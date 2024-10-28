    if(dict.size() == 0)
        return false;

B:
    int count_lower = 0;
    int count_upper = 0;

C:
    for(auto &it: dict){
        string key = it.first;
        if(key == tolower(key))
            count_lower++;
        if(key == toupper(key))
            count_upper++;
    }

D:
    if(count_lower == dict.size() || count_upper == dict.size())
        return true;
    else
        return false;

}
int main(){
    map<string,string> dict1 = {{"a","apple"}, {"b","banana"}};
    map<string,string> dict2 = {{"a","apple"}, {"A","banana"}, {"B","banana"}};
    map<string,string> dict3 = {{"a","apple"}, {"8","banana"}, {"a","apple"}};
    map<string,string> dict4 = {{"Name","John"}, {"Age","36"}, {"City","Houston"}};
    map<string,string> dict5 = {{"STATE","NC"},  {"ZIP","12345"}};
    printf("%d\n",check_dict_case(dict1)); // should return true
    printf("%d\n",check_dict_case(dict2)); // should return false
    printf("%d\n",check_dict_case(dict3)); // should return false
    printf("%d\n",check_dict_case(dict4)); // should return false
    printf("%d\n",check_dict_case(dict5)); // should return true
}


A: 
Check if all keys are either in lower case or upper case in a given map.

B: 

Initialize counters for lower and upper case keys.

C: 

Iterate over the map and check each key. If the key is in lower case, increment count_lower. If the key is in upper case, increment count_upper.

D: 

Return true if count_lower equals the size of the map or count_upper equals the size