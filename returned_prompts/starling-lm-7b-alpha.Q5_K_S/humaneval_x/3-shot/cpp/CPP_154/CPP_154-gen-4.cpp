    int i,j,l;
    string c;
    for (i=0;i<b.length();i++)
    {
        c="";
        for (j=i;j<b.length();j++)
        {
            c+=b[j];
            if (a.find(c)!=string::npos)
            return true;
        }
    }
    return false;
}


