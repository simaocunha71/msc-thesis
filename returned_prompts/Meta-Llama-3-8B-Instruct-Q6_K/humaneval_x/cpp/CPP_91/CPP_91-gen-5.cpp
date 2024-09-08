    int boredom = 0;
    int i = 0;
    while(i < S.length()){
        if(S[i] == '.' || S[i] == '?' || S[i] == '!'){
            if(i > 0 && S.substr(0,2) == "I "){
                boredom++;
            }
            i++;
            while(i < S.length() && (S[i] == '.' || S[i] == '?' || S[i] == '!')){
                i++;
            }
        }
        else{
            i++;
        }
    }
    return boredom;
}
int main(){
    string s;
    cin>>s;
    cout<<is_bored(s);
    return 0;
}

