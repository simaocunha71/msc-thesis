    int i,j;
    for (i=0;i<l.size();i+=3)
    {
        for (j=i+3;j<l.size();j+=3)
        {
            if (l[i]>l[j])
            {
                swap(l[i],l[j]);
            }
        }
    }
    return l;
}

