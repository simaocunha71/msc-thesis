    for(auto it:dict){
        if(isupper(it.first[0])==false && islower(it.first[0])==true){
            continue;
        }else if(islower(it.first[0])==true && isupper(it.first[0])==false){
            continue;
        }else{
            return false;
        }
    }
    return true;
}
int main(){
    map<string,string> dict1={{'a','apple'},{'b','banana'}};
    map<string,string> dict2={{'a','apple'},{'A','banana'},{'B','banana'}};
    map<string,string> dict3={{'a','apple'},{'8','banana'},{'a','apple'}};
    map<string,string> dict4={{'Name','John'},{'Age','36'},{'City','Houston'}};
    map<string,string> dict5={{'STATE','NC'},{'ZIP','12345'}};
    printf("%d\n",check_dict_case(dict1));
    printf("%d\n",check_dict_case(dict2));
    printf("%d\n",check_dict_case(dict3));
    printf("%d\n",check_dict_case(dict4));
    printf("%d\n",check_dict_case(dict5));
    return 0;
}

*/
#include <bits/stdc++.h>
using namespace std;

bool check_dict_case(map<string,string> dict) {
    if (dict.size() == 0) return false;
    for (auto it : dict) {
        if (islower(it.first[0]) && isupper(it.first[0]) ||
            isupper(it.first[0]) && islower(it.first[0])) {
            return false;
        }
    }
    return true;
}

int main() {
    map<string, string> dict1 = {{"a", "apple"}, {"b", "banana"}};
    map<string, string> dict2 = {{"a",