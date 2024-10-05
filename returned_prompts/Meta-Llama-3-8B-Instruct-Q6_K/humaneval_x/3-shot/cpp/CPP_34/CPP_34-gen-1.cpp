    vector<int> result;
    for (int i=0;i<l.size();i++)
    {
        bool flag=false;
        for (int j=0;j<result.size();j++)
        if (l[i]==result[j])
        {
            flag=true;
            break;
        }
        if (!flag)
        result.push_back(l[i]);
    }
    sort(result.begin(), result.end());
    return result;
} // this solution has a time complexity of O(n^2)


