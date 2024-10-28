    vector<int> ans;
    string number=to_string(num);
    int len=number.length();
    int even=0;
    int odd=0;
    int i;
    for (i=0;i<len;i++)
    {
        if (number[i]%2==0)
        even+=1;
        else
        odd+=1;
    }
    ans.push_back(even);
    ans.push_back(odd);
    return ans;
}


