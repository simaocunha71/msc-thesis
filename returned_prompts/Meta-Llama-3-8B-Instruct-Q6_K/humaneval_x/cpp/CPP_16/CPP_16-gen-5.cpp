    vector<char> vec;
    for(int i=0; i<str.length(); i++){
        char ch=str[i];
        ch=toupper(ch);
        if(find(vec.begin(), vec.end(), ch)==vec.end()){
            vec.push_back(ch);
        }
    }
    return vec.size();
}

int main(){
    string str;
    cout<<"Enter a string: ";
    getline(cin,str);
    cout<<"Distinct characters: "<<count_distinct_characters(str)<<endl;
    return 0;
}
