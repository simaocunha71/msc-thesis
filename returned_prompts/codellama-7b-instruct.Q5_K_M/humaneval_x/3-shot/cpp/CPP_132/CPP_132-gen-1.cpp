    int i;
    int j;
    int level=0;
    for (i=0;i<str.length();i++){
        for (j=i;j<str.length();j++){
            if (str[i]=='['){
                level+=1;
            }
            else if (str[i]==']'){
                level-=1;
            }
            if (level==0)
            return true;
        }
    }
    return false;
}



