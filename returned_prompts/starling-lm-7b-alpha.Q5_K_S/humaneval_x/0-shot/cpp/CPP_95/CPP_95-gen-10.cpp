    if (dict.size()==0) {
        return false;
    }
    for (auto it:dict) {
        if (it.first[0]>='a' && it.first[0]<='z') {
            if (it.second[0]>='A' && it.second[0]<='Z') {
                return false;
            }
        }else if (it.first[0]>='A' && it.first[0]<='Z') {
            if (it.second[0]>='a' && it.second[0]<='z') {
                return false;
            }
        }
    }
    return true;
}
int main()
{
    map<string,string> dict;
    dict["a"]="apple";
    dict["b"]="banana";
    dict["A"]="banana";
    dict["8"]="banana";
    dict["Name"]="John";
    dict["Age"]="36";
    dict["City"]="Houston";
    dict["STATE"]="NC";
    dict["ZIP"]="12345";
    printf("%d\n", check_dict_case(dict));
    return 0;
}

*/





















































































































































































































