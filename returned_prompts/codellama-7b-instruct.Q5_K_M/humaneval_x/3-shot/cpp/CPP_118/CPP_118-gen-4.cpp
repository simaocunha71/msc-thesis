    int i;
    char vowel;
    for (i=word.length()-2;i>=0;i--){
        if (word[i]=='a'||word[i]=='e'||word[i]=='i'||word[i]=='o'||word[i]=='u'){
            return string(1,word[i]);
        }
        else if (word[i+1]=='a'||word[i+1]=='e'||word[i+1]=='i'||word[i+1]=='o'||word[i+1]=='u'){
            return string(1,word[i+1]);
        }
    }
    return "";
}


