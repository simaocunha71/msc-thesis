    int i;
    int j;
    int k;
    int flag=0;
    int len=a.length();
    int len2=b.length();
    for (i=0;i<len-len2+1;i++)
    {
        for (j=0;j<len2;j++)
        {
            if (a[i+j]!=b[j])
            {
                flag=1;
                break;
            }
        }
        if (flag==0)
        return true;
        flag=0;
    }
    return false;
}














