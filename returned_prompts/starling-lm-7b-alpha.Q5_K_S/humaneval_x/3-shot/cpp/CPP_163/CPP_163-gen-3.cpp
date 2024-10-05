    vector<int> all_numbers;
    int i,j,k;
    for (i=a;i<=b;i++)
    {
        j=i;
        while (j>0){
        k=j%10;
        if (k%2==0)
        all_numbers.push_back(k);
        j=j/10;
        }
    }
    return all_numbers;
}



