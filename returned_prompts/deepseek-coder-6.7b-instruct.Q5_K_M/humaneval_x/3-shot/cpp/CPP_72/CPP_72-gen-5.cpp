    int sum = 0;
    for(int i=0; i<q.size(); i++)
    {
        sum += q[i];
    }
    if(sum > w) return false;
    int i=0, j=q.size()-1;
    while (i < j)
    {
        if (q[i] != q[j]) return false;
        i++;
        j--;
    }
    return true;
}


