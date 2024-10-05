    int i,j,sum=0;
    int left=q.size()/2;
    int right=q.size()-left;
    for (i=0;i<left;i++)
    sum+=q[i];
    for (j=q.size()-1;j>=right;j--)
    sum+=q[j];
    return sum<=w&&left==right;
}


