    int i,j;
    int b_length=b.length();
    for (i=0;i<a.length();i++)
    {
        for (j=0;j<b_length;j++)
        {
            if (a[i+j]!=b[j])
            break;
            if (j==b_length-1)
            return true;
        }
    }
    return false;
}




