    int i,j;

    if (a.find(b)!=string::npos)
    return true;

    for (i=0;i<b.length();i++)
    for (j=0;j<b.length();j++)
    if (b[j]==b[i])
    b=b.substr(0,j)+b.substr(j+1,b.length()-j-1)+b[j];

    if (a.find(b)!=string::npos)
    return true;
    
    return false;
}


