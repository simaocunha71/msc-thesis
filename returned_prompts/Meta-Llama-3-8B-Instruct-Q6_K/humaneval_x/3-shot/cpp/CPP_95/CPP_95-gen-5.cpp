    if(dict.empty())
    return false;
    bool all_lower=true;
    bool all_upper=false;
    map<string,string>::iterator it;
    for(it=dict.begin();it!=dict.end();it++)
    {
        if(it->first[0]>=97 && it->first[0]<=122)//if first character is lowercase
        {
            all_upper=false;
        }
        else if(it->first[0]>=65 && it->first[0]<=90)//if first character is uppercase
        {
            all_lower=false;
        }
        else
        {
            return false;
        }
    }
    if(all_lower)
    return true;
    if(all_upper)
    return true;
    return false;
} 
//test case
int main()
{
    map<string,string> dict;
    dict["a"]="apple";
    dict["b"]="banana";
    printf("%d\n",check_dict_case(dict));
    return 0;
}
//test case
int main()
{
    map<string,string> dict;
    dict["a"]="apple";
    dict["A"]="banana";
    dict["B"]="banana";
    printf("%d\n",check_dict_case(dict));
    return 0;
} 
//test case
int main()
{
    map<string,string> dict;
    dict["a"]="apple";
    dict["8"]="banana";
    dict["a"]="apple";
    printf("%d\n",check_dict_case(dict));
    return 0;
}
//test case
int main()
{
    map<string,string> dict;
    dict["Name"]="John";
    dict["Age"]="36";
    dict["City"]="Houston";
    printf("%d\n",check_dict_case(dict));
    return 0;
}
//test case
int main()
{
    map<string,string> dict;
    dict["STATE"]="NC";
    dict["ZIP"]="12345";
    printf("%d\n",check_dict_case(dict));
    return 0;
} 
//test case
int main()
{
    map<string,string> dict;
    printf("%d\n",check_dict_case(dict));
    return 0;
} 
//test case
int main()
{
    map<string,string> dict;
    dict["a"]="apple";
    printf("%d\n",check_dict_case(dict));
    return 0;
} 
//test case
int main()
{
    map<string,string> dict;
    dict["STATE"]="nc";
    dict["ZIP"]="12345";
    printf("%d\n",check