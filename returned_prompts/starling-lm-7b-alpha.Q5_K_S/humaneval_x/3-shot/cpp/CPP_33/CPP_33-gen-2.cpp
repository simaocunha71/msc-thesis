    vector<int> l_sorted;
    vector<int> l_unsorted;
    int i,j;
    for (i=0;i<l.size();i++)
    {
        if (i%3==0)
        {
        l_sorted.push_back(l[i]);
        }
        else
        {
        l_unsorted.push_back(l[i]);
        }
    }
    sort(l_sorted.begin(), l_sorted.end());

    vector<int> l_result;
    for (i=0;i<l.size();i++)
    {
        if (i%3==0)
        {
        l_result.push_back(l_sorted[i/3]);
        }
        else
        {
        l_result.push_back(l_unsorted[i]);
        }
    }

    return l_result;
}


