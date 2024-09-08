    int count = 0;
    int i = 0;
    while(i < S.length()){
        if(S[i] == '.'){
            i++;
            if(i < S.length() && S[i] == ' '){
                i++;
            }
            if(i < S.length() && S.find("I", i) == i){
                count++;
                i++;
            }
        }
        else if(S[i] == '?' || S[i] == '!'){
            i++;
            if(i < S.length() && S[i] == ' '){
                i++;
            }
            if(i < S.length() && S.find("I", i) == i){
                count++;
                i++;
            }
        }
        else{
            i++;
        }
    }
    return count;
}

int main(){
    string s;
    cin>>s;
    cout<<is_bored(s);
    return 0;
}

