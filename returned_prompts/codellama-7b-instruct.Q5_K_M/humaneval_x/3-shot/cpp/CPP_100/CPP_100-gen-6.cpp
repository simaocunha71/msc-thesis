    vector<int> result;
    result.push_back(n);
    for (int i=1;i<n;i++)
    {
        if (n%2==0)
        {
            result.push_back(n+1);
            n+=1;
        }
        else
        {
            result.push_back(n+2);
            n+=2;
        }
    }
    return result;
}


