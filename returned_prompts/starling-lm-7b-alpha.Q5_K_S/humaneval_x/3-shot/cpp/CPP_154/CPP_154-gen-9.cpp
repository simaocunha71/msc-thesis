    int i,j;
    for (i=0;i<b.length();i++)
    {
        string c=b.substr(i);
        if (a.find(c)!=string::npos)
        return true;
    }
    return false;
}


