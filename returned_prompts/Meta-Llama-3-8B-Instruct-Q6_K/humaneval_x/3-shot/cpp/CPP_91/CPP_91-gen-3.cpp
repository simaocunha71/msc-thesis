    int count=0;
    int i;
    for (i=0;i<S.length();i++)
    {
        if (S[i]=='.' || S[i]=='?' || S[i]== '!'){
            if (i>0 && S[i-1]=='I') count++;
        }
    }
    return count;
}
// Another solution:
int is_bored(string S){
    int count=0;
    bool in_sentence=false;
    for (char c:S){
        if (c== '.' || c== '?' || c== '!') {
            in_sentence=false;
        }
        else if (!in_sentence && c=='I') {
            in_sentence=true;
            count++;
        }
        in_sentence = in_sentence && (c!=' ');
    }
    return count;
} 
// Another solution:
int is_bored(string S){
    int count=0;
    int i;
    for (i=0;i<S.length();i++)
    {
        if (S[i]=='.' || S[i]=='?' || S[i]== '!'){
            if (i>0 && S[i-1]=='I') count++;
        }
    }
    return count;
}
// Another solution:
int is_bored(string S){
    int count=0;
    string word;
    for (char c:S){
        if (c== '.' || c== '?' || c== '!') {
            if (word.length()>0 && word[0]=='I') count++;
            word.clear();
        }
        else word+=c;
    }
    if (word.length()>0 && word[0]=='I') count++;
    return count;
} 
// Another solution:
int is_bored(string S){
    int count=0;
    string word;
    for (char c:S){
        if (c== '.' || c== '?' || c== '!') {
            if (word.length()>0 && word[0]=='I') count++;
            word.clear();
        }
        else word+=c;
    }
    if (word.length()>0 && word[0]=='I') count++;
    return count;
} 
// Another solution:
int is_bored(string S){
    int count=0;
    int i;
    for (i=0;i<S.length();i++)
    {
        if (S[i]=='.' || S[i]=='?' || S[i]== '!'){
            if (i>0 && S[i-1]=='I') count++;
        }
    }
    return count;
}
// Another solution