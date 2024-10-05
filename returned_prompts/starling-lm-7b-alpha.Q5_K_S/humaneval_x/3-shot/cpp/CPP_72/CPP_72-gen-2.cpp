    int i,sum=0;
    for (i=0;i<q.size();i++)
    sum+=q[i];

    int left=0,right=q.size()-1;
    while (left<right)
    {
        if (q[left]!=q[right])
        return false;
        left+=1;
        right-=1;
    }

    return sum<=w;
}



