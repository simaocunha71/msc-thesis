    string result;
    int i,tmp;
    while (x>0){
        tmp=x%base;
        result+=('0'+tmp);
        x/=base;
    }
    for (i=result.length()-1;i>=0;i--)
    result[i]+='0';
    return result;
}


