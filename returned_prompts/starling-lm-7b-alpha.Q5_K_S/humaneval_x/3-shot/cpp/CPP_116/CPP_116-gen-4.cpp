    vector<int> tmp_arr;
    int i,j,count,count_ones;
    for (i=0;i<arr.size();i++)
    {
        tmp_arr.push_back(arr[i]);
        count_ones=0;
        for (j=0;j<32;j++)
        {
        count=1;
        count=(tmp_arr[i]>>j)&1;
        if (count==1)
        count_ones+=1;
        }
        sort(tmp_arr.begin(),tmp_arr.end(),[count_ones](int x, int y){return count_ones<count_ones;});
    }
    return tmp_arr;
}


