
//1. get unique characters
vector<char> unique_chars;
for(int i=0;i<str.length();i++){
    if(find(unique_chars.begin(), unique_chars.end(), str[i])==unique_chars.end()){
        unique_chars.push_back(str[i]);
    }
}

//2. transform to lower case
for(int i=0;i<unique_chars.size();i++){
    unique_chars[i]=tolower(unique_chars[i]);
}

//3. count distinct unique lowercase characters
vector<char>::iterator it;
int distinct_chars=0;
for(it=unique_chars.begin();it!=unique_chars.end();it++){
    distinct_chars++;
}

return distinct_chars;
}
int main() {
    string str;
    cin>>str;
    cout<<count_distinct_characters(str);
    return 0;
}
