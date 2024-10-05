    vector<int> all;
    vector<int> result;
    int i;
    for (i=0;i<l1.size();i++)
    all.push_back(l1[i]);
    for (i=0;i<l2.size();i++)
    all.push_back(l2[i]);
    
    sort(all.begin(),all.end());
    result.push_back(all[0]);
    for (i=1;i<all.size();i++)
    {
        if (result.back()!=all[i]) result.push_back(all[i]);
    }
    vector<int> result_unique;
    int j;
    for (j=0;j<result.size();j++)
    {
        bool found=false;
        for (i=0;i<l1.size();i++)
        {
            if (result[j]==l1[i])
            {
                found=true;
                break;
            }
        }
        if (!found) continue;
        for (i=0;i<l2.size();i++)
        {
            if (result[j]==l2[i])
            {
                found=true;
                break;
            }
        }
        if (found) result_unique.push_back(result[j]);
    }
    return result_unique;
}



