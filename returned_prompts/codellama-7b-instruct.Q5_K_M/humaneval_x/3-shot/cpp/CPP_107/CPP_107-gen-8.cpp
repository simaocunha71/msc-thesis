    vector<int> result;
    int even_count=0, odd_count=0;
    for (int i=1;i<=n;i++)
    {
        string num=to_string(i);
        string reverse=num;
        reverse.erase(remove(reverse.begin(),reverse.end(),' '),reverse.end());
        reverse.erase(reverse.begin(),reverse.end()-num.length()+1);
        if (reverse==num)
        {
            if (i%2==0)
            {
                even_count+=1;
            }
            else
            {
                odd_count+=1;
            }
        }
    }
    result.push_back(even_count);
    result.push_back(odd_count);
    return result;
}


