    int count = 0;
    string words[100];
    int i=0;
    int j=0;
    while(i<S.length()){
        if(S[i]==' '||S[i]=='.'||S[i]=='?'||S[i]=='!'){
            words[j]=S.substr(j,i-j);
            j=i+1;
            i++;
        } else i++;
    }
    words[j]=S.substr(j);
    for(int k=0;k<j;k++){
        if(words[k].compare("I")==0){
            count++;
        }
    }
    return count;
}
int main(){
    string S;
    printf("Enter a string of words:\n");
    getline(cin,S);
    printf("Number of boredoms: %d\n",is_bored(S));
    return 0;
}

