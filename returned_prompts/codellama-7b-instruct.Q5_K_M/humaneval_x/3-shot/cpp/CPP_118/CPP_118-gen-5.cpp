    int i=0,j=0;
    int size=word.size();
    string vowel="";
    if (size<=1)
    return "";
    for (i=size-1;i>0;i--){
        if (word[i]=='a'||word[i]=='e'||word[i]=='i'||word[i]=='o'||word[i]=='u'){
            if (word[i-1]<97||word[i-1]>122)
            j=i;
            else
            break;
        }
    }
    for (i=j-1;i<j+1;i++){
        if (word[i]=='a'||word[i]=='e'||word[i]=='i'||word[i]=='o'||word[i]=='u'){
            vowel=word[i];
            break;
        }
    }
    return vowel;
}

