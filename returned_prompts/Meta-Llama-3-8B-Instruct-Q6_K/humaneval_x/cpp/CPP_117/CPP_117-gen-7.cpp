    vector<string> result;
    //split the string into words
    string word;
    for(int i=0; i<s.size(); i++){
        if(s[i] == ' '){
            if(!word.empty()){
                //check if word contains n consonants
                int count = 0;
                for(int j=0; j<word.size(); j++){
                    if(word[j] != ' ' && word[j] != 'a' && word[j] != 'e' && word[j] != 'i' && word[j] != 'o' && word[j] != 'u'){
                        count++;
                    }
                }
                if(count == n){
                    result.push_back(word);
                }
                word.clear();
            }
        }
        else{
            word += s[i];
        }
    }
    //check the last word
    if(!word.empty()){
        int count = 0;
        for(int j=0; j<word.size(); j++){
            if(word[j] != ' ' && word[j] != 'a' && word[j] != 'e' && word[j] != 'i' && word[j] != 'o' && word[j] != 'u'){
                count++;
            }
        }
        if(count == n){
            result.push_back(word);
        }
    }
    return result;
}
int main(){
    string s = "Mary had a little lamb";
    int n = 4;
    vector<string> result = select_words(s,n);
    for(auto i: result){
        cout << i << endl;
    }
    return 0;
}

