    int count=0;
    char ch;
    for(int i=0;i<brackets.length();i++){
        ch=brackets[i];
        if(ch=='<'){
            count++;
        }
        else if(ch=='>'){
            if(count==0){
                return false;
            }
            count--;
        }
    }
    return count==0;
}

