    vector<int> result;
    int i;
    for (i=1;i<=n;i++)
    {
        if (is_palindrome(i))
        {
            if (i%2==0)
            result.push_back(1);
            else
            result.push_back(0);
        }
    }
    return result;
}

