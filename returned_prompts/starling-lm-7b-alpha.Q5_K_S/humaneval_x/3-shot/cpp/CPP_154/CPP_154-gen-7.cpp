    int i,j;
    if (a.find(b)!=string::npos) return true;
    for (i=1;i<b.length();i++)
    {
        string c=b.substr(i,b.length()-i);
        if (a.find(c)!=string::npos) return true;
    }
    return false;
}


