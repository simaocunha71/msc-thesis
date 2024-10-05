    vector<int> ans;
    for (int i=0;i<x.size();i++)
    {
        int num=x[i];
        bool has_even=false;
        while (num>0)
        {
            if (num%2==0)
            has_even=true;
            num=num/10;
        }
        if (has_even==false)
        ans.push_back(x[i]);
    }

    sort(ans.begin(),ans.end());
    return ans;
}

