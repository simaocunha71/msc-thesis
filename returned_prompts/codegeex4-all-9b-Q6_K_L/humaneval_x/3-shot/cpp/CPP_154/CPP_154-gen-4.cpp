    int i,j,k,l;
    string temp;
    for (i=0;i<a.length();i++)
    {
        temp="";
        for (j=i;j<i+b.length();j++)
        {
            temp=temp+a[j];
        }
        for (k=0;k<b.length();k++)
        {
            if (temp[k]!=b[k])
                break;
        }
        if (k==b.length())
        return true;
    }
    return false;
}

