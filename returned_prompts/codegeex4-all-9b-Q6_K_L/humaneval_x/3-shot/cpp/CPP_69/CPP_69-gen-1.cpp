    int i,j;
    int max=-1;
    for (i=0;i<lst.size();i++)
    {
    int count=0;
    for (j=0;j<lst.size();j++)
    if (lst[i]==lst[j]) count+=1;
    if (count>lst[i]) max=count;
    }
    if (max==-1) return -1;
    else return max;
}

