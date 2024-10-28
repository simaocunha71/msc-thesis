    int i,sum=0;
    for (i=0;i<q.size();i++)
    sum+=q[i];
    return (sum<=w)&&(sum==q[i]+q.size()-i-1);
}




