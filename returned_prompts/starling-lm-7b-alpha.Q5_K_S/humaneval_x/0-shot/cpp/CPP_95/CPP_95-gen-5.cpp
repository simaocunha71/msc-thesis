    if(dict.size() == 0) return false;
    for(map<string,string>::iterator it = dict.begin();it != dict.end();it++){
        if((it->first).size() > 0 && (it->first)[0] >= 'a' && (it->first)[0] <= 'z'){
            if((it->second).size() > 0 && (it->second)[0] >= 'a' && (it->second)[0] <= 'z'){

            }else{
                return false;
            }
        }else if((it->first).size() > 0 && (it->first)[0] >= 'A' && (it->first)[0] <= 'Z'){
            if((it->second).size() > 0 && (it->second)[0] >= 'A' && (it->second)[0] <= 'Z'){

            }else{
                return false;
            }
        }else{
            return false;
        }
    }
    return true;
}

int main(void){
    map<string,string> dict;
    dict["a"] = "apple"; dict["b"] = "banana"; dict["A"] = "banana"; dict["B"] = "banana"; dict["STATE"] = "NC"; dict["ZIP"] = "12345"; dict["8"] = "banana"; dict["Name"] = "John"; dict["Age"] = "36"; dict["City"] = "Houston";
    printf("%s\n",check_map_case(dict)? "true":"false");
    return 0;
}


*/

#include <stdio.h>
#include <map>
#include <string>
using namespace std;

bool check_dict_case(map<string,string> dict){
    if(dict.size() == 0) return false;
    for(map<string,string>::iterator it = dict.begin();it != dict.end();it++){
        if((it->first).size() > 0 && (it->first)[0] >= 'a' && (it->first)[0] <= 'z')