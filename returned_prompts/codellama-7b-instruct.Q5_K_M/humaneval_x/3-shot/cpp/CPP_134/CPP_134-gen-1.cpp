    int i;
    bool flag=false;
    for (i=0;i<txt.length();i++)
        if (txt[i]>='a'&&txt[i]<='z'||txt[i]>='A'&&txt[i]<='Z')
        if (i==txt.length()-1)
        return true;
    return false;
}


