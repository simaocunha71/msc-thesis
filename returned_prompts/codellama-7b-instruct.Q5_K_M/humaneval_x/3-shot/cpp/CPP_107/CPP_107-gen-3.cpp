    vector<int> ans;
    int even=0,odd=0;
    for (int i=1;i<=n;i++)
    {
        string str=to_string(i);
        bool is_even=true;
        for (int j=0;j<str.length()/2;j++)
        {
            if (str[j]!=str[str.length()-1-j]){
                is_even=false;
                break;
            }
        }
        if (is_even)
        {
            even+=1;
        }
        else
        {
            odd+=1;
        }
    }
    ans.push_back(even);
    ans.push_back(odd);
    return ans;
}


