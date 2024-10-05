    vector<int> ones;
    for (int i=0;i<arr.size();i++)
    {
        int cnt_ones=0;
        while (arr[i]>0)
        {
            arr[i]-=arr[i]&1;
            cnt_ones+=1;
        }
        ones.push_back(cnt_ones);
    }
    vector<pair<int,int>> ones_dec;
    for (int i=0;i<arr.size();i++)
    ones_dec.push_back(make_pair(ones[i],arr[i]));
    sort(ones_dec.begin(),ones_dec.end());
    vector<int> final_arr;
    for (int i=0;i<ones_dec.size();i++)
    final_arr.push_back(ones_dec[i].second);
    return final_arr;
}


