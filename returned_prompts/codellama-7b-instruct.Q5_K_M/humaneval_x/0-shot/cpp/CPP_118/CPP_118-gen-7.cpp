    for(int i=0;i<word.size();i++){
        if(word[i]=='A'||word[i]=='E'||word[i]=='I'||word[i]=='O'||word[i]=='U'){
            if(word[i]=='A'||word[i]=='E'||word[i]=='I'||word[i]=='O'||word[i]=='U')
            return word[i];
            else{
                for(int j=i+1;j<word.size();j++){
                    if(word[j]=='A'||word[j]=='E'||word[j]=='I'||word[j]=='O'||word[j]=='U'){
                        return word[j];
                    }
                }
            }
        }
    }
}

int main(){
    string word;
    getline(cin,word);
    string result=get_closest_vowel(word);
    if(result==""){
        printf("");
    }
    else{
        printf("%s",result.c_str());
    }
    return 0;
}

