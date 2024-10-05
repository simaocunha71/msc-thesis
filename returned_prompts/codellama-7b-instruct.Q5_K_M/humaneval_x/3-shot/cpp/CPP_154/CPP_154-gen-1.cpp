    int i,j;
    for (i=0;i<a.length();i++)
    if (a.find(b)!=string::npos)
    return true;
    else
    for (j=0;j<a.length();j++)
    {
        string temp;
        temp=a.substr(j,a.length()-j);
        temp+=a.substr(0,j);
        if (temp.find(b)!=string::npos)
        return true;
    }
    return false;
}


