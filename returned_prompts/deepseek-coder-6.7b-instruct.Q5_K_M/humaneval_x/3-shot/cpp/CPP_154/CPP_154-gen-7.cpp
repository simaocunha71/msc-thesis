    int l1=a.length();
    int l2=b.length();
    if(l1<l2)
    return false;
    for(int i=0;i<l2;i++){
        string c=b.substr(i)+b.substr(0,i);
        if(a.find(c)!=string::npos)
        return true;
    }
    return false;
}

