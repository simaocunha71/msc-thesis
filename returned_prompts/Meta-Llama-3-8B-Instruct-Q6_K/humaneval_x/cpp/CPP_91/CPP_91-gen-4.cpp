    int count=0;
    string word;
    int i=0;
    while(i<S.size()){
        while(S[i]==' '){
            i++;
        }
        int j=i;
        while(S[j] != ' ' && j < S.size()){
            j++;
        }
        word=S.substr(i,j-i);
        if(word == "I"){
            i++;
            while(S[i] != '.' && S[i] != '?' && S[i] != '!'){
                i++;
            }
            count++;
        }
        else i++;
    }
    return count;

}

int main(){
    string S;
    cin>>S;
    cout<<is_bored(S)<<endl;
    return 0;
}

