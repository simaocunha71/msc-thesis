    vector<int> result;
    sort(l1.begin(),l1.end());
    sort(l2.begin(),l2.end());

    int i=0,j=0;
    while(i<l1.size() && j<l2.size())
    {
        if (l1[i]==l2[j])
        {
            result.push_back(l1[i]);
            i++;
            j++;
        }
        else if (l1[i]<l2[j])
        {
            i++;
        }
        else
        {
            j++;
        }
    }
    return result;
}  



