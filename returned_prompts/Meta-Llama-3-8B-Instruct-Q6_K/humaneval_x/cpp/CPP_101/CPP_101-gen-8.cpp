    // Split the string into words
    vector<string> words;
    string word;
    for(int i = 0; i < s.length(); i++){
        if(s[i] == ',' || s[i] == ' '){
            if(!word.empty()){
                words.push_back(word);
                word.clear();
            }
        }
        else{
            word += s[i];
        }
    }
    if(!word.empty()){
        words.push_back(word);
    }
    return words;

}

int main()
{
    string s;
    printf("Enter the string:");
    getline(cin,s);
    vector<string> res = words_string(s);
    for(int i = 0; i < res.size(); i++){
        printf("%s ",res[i].c_str());
    }
    printf("\n");
    return 0;
}

