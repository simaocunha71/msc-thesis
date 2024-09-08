    vector<char> v;
    for(int i=0;i<str.length();i++){
        if(find(v.begin(),v.end(),tolower(str[i]))==v.end())
            v.push_back(tolower(str[i]));
    }
    return v.size();
}

int main(){
    string s="xyzXYZ";
    printf("%d",count_distinct_characters(s));
    return 0;
}
