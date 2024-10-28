    int i,j;
    int count=0;
    for (i=0;i<brackets.length();i++){
        if (brackets[i]=="<")
        count+=1;
        if (brackets[i]==">")
        count-=1;
        if (count<0)
        return false;
    }
    if (count==0)
    return true;
    else 
    return false;
}



