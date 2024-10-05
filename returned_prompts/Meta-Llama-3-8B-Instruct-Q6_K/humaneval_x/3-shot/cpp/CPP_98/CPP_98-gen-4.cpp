    int count=0;
    for(int i=0;i<s.length();i++)
    {
        if(i%2==0&&isupper(s[i]))
            count++;
    }
    return count;
}
//using lambda function
int count_upper(string s){
    return count_if(s.begin(),s.end(),[&](char c){ return (c>='A'&&c<='Z') && (0==c-s[0]%2); });
}
//using for each loop
int count_upper(string s){
    int count=0;
    for_each(s.begin(),s.end(),[&](char c){if(c>='A'&&c<='Z'&&0==c-s[0]%2)count++;});
    return count;
}  //using find_if
int count_upper(string s){
    return count(s.begin(),s.end(),[&](char c){ return (c>='A'&&c<='Z') && (0==c-s[0]%2); });
}
//using count_if with a predicate function
int count_upper(string s){
    return count_if(s.begin(),s.end(),isupper&&bind2nd(modulus<int>(),2));
}
//using count_if with a lambda function
int count_upper(string s){
    return count_if(s.begin(),s.end(),[&](char c){ return isupper(c) && (c-s[0])%2==0; });
}  //using lambda function
int count_upper(string s){
    return count_if(s.begin(),s.end(),[&](char c){ return (c>='A'&&c<='Z') && (c-s[0])%2==0; });
}
//using range-based for loop
int count_upper(string s){
    int count=0;
    for(char c:s){
        if(c>='A'&&c<='Z'&&0==c-s[0]%2)
            count++;
    }
    return count;
}
//using count_if with a lambda function
int count_upper(string s){
    return count_if(s.begin(),s.end(),[&](char c){ return (c>='A'&&c<='Z') && (c-s[0])%2==0; });
}
//using lambda function
int count_upper(string s){
    return count_if(s.begin(),s.end(),[&](char c){ return (c>='A'&&c<='Z') && (c-s[0])%2==