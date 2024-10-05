    vector<int> ans;
    for (int i=0;i<arr.size();i++)
    {
        int curr=arr[i];
        int curr_ones=0;
        while (curr!=0)
        {
            curr_ones+=curr%2;
            curr/=2;
        }
        ans.push_back(curr_ones);
    }
    sort(ans.begin(),ans.end());
    vector<int> fin_ans;
    for (int i=0;i<arr.size();i++)
    {
        int curr=arr[i];
        int curr_ones=0;
        while (curr!=0)
        {
            curr_ones+=curr%2;
            curr/=2;
        }
        for (int j=0;j<ans[i];j++)
        {
            fin_ans.push_back(1);
        }
        fin_ans.push_back(curr);
    }
    return fin_ans;
}


