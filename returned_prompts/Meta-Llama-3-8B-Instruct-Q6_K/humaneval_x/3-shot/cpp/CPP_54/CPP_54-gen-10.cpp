    sort(s0.begin(),s0.end());
    sort(s1.begin(),s1.end());
    return s0==s1;
} 
//OR
bool same_chars(string s0,string s1){
    if(s0.length()!=s1.length())
        return false;
    sort(s0.begin(),s0.end());
    sort(s1.begin(),s1.end());
    return s0==s1;
} 
//OR
bool same_chars(string s0,string s1){
    if(s0.length()!=s1.length())
        return false;
    sort(s0.begin(),s0.end());
    sort(s1.begin(),s1.end());
    for(int i=0;i<s0.length();i++){
        if(s0[i]!=s1[i])
            return false;
    }
    return true;
} 
//OR
bool same_chars(string s0,string s1){
    if(s0.length()!=s1.length())
        return false;
    unordered_map<char,int> map;
    for(int i=0;i<s0.length();i++){
        if(map.find(s0[i])==map.end())
            map[s0[i]]=1;
        else
            map[s0[i]]++;
    }
    for(int i=0;i<s1.length();i++){
        if(map.find(s1[i])==map.end())
            return false;
        else
            map[s1[i]]--;
        if(map[s1[i]]<0)
            return false;
    }
    return true;
}  //OR
bool same_chars(string s0,string s1){
    if(s0.length()!=s1.length())
        return false;
    int count[256]={0};
    for(int i=0;i<s0.length();i++){
        count[s0[i]]++;
    }
    for(int i=0;i<s1.length();i++){
        if(count[s1[i]]<=0)
            return false;
        count[s1[i]]--;
    }
    return true;
}  //OR
bool same_chars(string s0,string s1){
    if(s0.length()!=s1.length())
        return false;
    int count[256]={0};
    for(int i=0;i<s0.length();i++){
        count[s0[i]]++;
    }
    for(int i=0;i<s1.length();i++){
        count[s1[i]]--;
    }
    for(int i=0;i<256;i++){
        if(count[i]!=0)
            return false;
    }
    return