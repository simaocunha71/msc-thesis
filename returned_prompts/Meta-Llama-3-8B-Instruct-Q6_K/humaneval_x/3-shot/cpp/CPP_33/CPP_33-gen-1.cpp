    vector<int> result;
    for (int i=0;i<l.size();i++)
    {
        if (i%3==0)
        {
            result.push_back(l[i]);
        }
        else
        {
            result.push_back(l[i]);
        }
    }
    sort(result.begin(),result.end());
    return result;
}

