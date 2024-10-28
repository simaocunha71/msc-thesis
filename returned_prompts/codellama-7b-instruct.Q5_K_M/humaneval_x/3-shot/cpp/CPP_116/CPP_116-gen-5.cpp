    vector<int> sorted(arr.size());
    for (int i=0;i<arr.size();i++)
    sorted[i]=arr[i];
    sort(sorted.begin(),sorted.end(),
    [](int a,int b){
        int a_ones=0,b_ones=0;
        while (a)
        {
            a_ones+=a%2;
            a/=2;
        }
        while (b)
        {
            b_ones+=b%2;
            b/=2;
        }
        if (a_ones!=b_ones)
        return a_ones<b_ones;
        else
        return a<b;
        }
    );
    return sorted;
}


