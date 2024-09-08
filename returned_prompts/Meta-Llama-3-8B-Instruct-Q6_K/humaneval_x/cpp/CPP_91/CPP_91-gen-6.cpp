    int count = 0;
    string word;
    for(int i = 0; i < S.length(); i++){
        if(S[i] == '.'){
            word = "";
            i++;
        }
        else if(S[i] == '?' || S[i] == '!'){
            word += S[i];
            i++;
            if(word[0] == 'I'){
                count++;
            }
            word = "";
        }
        else{
            word += S[i];
        }
    }
    return count;
}

int main(){
    string S;
    printf("Enter a string: ");
    getline(cin,S);
    cout<<is_bored(S)<<"";
    return 0;
}
