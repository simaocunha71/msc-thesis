    int i,total;
    for (i=0;i<n.size();i++)
    {
        total=0;
        int temp=n[i];
        while (temp>0){
        total+=temp%10;
        temp/=10;
        }
        if (total>0)
        return count_nums(n)+1;
    }
    return 0;
}



