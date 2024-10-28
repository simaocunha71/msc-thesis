    vector<int> result;
    for (int i = 0; i < l.size(); i++)
    {
        if (i % 3 == 0)
        {
            vector<int> temp;
            for (int j = i; j < l.size(); j++)
            {
                if (j % 3 == 0)
                {
                    temp.push_back(l[j]);
                }
            }
            sort(temp.begin(), temp.end());
            for (int j = 0; j < temp.size(); j++)
            {
                result.push_back(temp[j]);
                i++;
            }
        }
        else
        {
            result.push_back(l[i]);
        }
    }
    return result;
}
```



