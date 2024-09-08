    int count = 0;
    int i = 0;
    while(i < S.length()){
        if(S[i] == '.' || S[i] == '?' || S[i] == '!'){
            if(i > 0 && S[i-1] == ' ' && S.substr(i-2,2) == "I "){
                count++;
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
    return count;
}
int main(){
    string s;
    printf("Enter a string of words:");
    getline(cin, s);
    int result = is_bored(s);
    printf("Number of boredoms: %d\n", result);
    return 0;
}

