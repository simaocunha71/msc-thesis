    vector<int> sorted_arr;
    int i;
    for (i=0;i<arr.size();i++)
    {
        int count=0;
        int binary_num=arr[i];
        while (binary_num>0)
        {
            if (binary_num%2==1)
            count++;
            binary_num/=2;
        }
        sorted_arr.push_back(arr[i]);
    }
    sort(sorted_arr.begin(),sorted_arr.end(),[](int a,int b){
        int ones_a=0;
        int ones_b=0;
        int binary_a=a;
        int binary_b=b;
        while (binary_a>0)
        {
            if (binary_a%2==1)
            ones_a++;
            binary_a/=2;
        }
        while (binary_b>0)
        {
            if (binary_b%2==1)
            ones_b++;
            binary_b/=2;
        }
        if (ones_a==ones_b)
        return a<b;
        return ones_a<ones_b;
    });
    return sorted_arr;
}



