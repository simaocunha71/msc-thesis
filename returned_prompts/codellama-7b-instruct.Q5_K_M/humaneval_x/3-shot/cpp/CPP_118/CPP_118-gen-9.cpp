    int i;
    int j=word.length()-1;
    while(word[j]==' '||word[j]=='\n')
    j--;
    int flag=0;
    while(j>=0){
        if (word[j]==' ')
        flag=1;
        if (word[j]=='a'||word[j]=='e'||word[j]=='i'||word[j]=='o'||word[j]=='u'){
            if(flag==0)
            return word[j];
            else
            return "";
        }
        if (word[j]=='A'||word[j]=='E'||word[j]=='I'||word[j]=='O'||word[j]=='U'){
            if(flag==0)
            return word[j];
            else
            return "";
        }
        j--;
    }
    return "";
}


