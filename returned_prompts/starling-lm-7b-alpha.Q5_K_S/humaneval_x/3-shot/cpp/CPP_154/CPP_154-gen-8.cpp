    int i,j;
    for (i=0;i<a.length();i++)
    {
        if (a.find(b,i)!=string::npos)
        return true;
        if (a.find(b,i)==string::npos)
        {
            for (j=1;j<a.length();j++)
            if (a.find(b,i+j)!=string::npos)
            return true;
        }
    }
    return false;
}


