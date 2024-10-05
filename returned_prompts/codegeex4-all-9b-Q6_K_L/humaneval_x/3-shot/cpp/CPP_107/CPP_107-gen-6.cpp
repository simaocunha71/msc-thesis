    vector<int> palindromes;
    int even=0,odd=0;
    int i;
    for (i=1;i<=n;i++)
    {
        string temp=to_string(i);
        string reverse_temp=temp;
        reverse(reverse_temp.begin(),reverse_temp.end());
        if (temp==reverse_temp)
        {
            if (i%2==0)
                even+=1;
            else
                odd+=1;
        }
    }
    palindromes.push_back(even);
    palindromes.push_back(odd);
    return palindromes;
}

