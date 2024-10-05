    int len_a=a.size();
    int len_b=b.size();
    if(len_b>len_a)
        return false;
    for(int i=0;i<len_b;i++){
        string c=b.substr(i)+b.substr(0,i);
        if(a.find(c)!=string::npos)
            return true;
    }
    return false;
}

