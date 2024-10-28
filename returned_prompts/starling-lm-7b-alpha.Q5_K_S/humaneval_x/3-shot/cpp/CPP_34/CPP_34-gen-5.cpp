    sort(l.begin(),l.end());
    int i,j=0;
    vector<int> unique_l;
    for (i=0;i<l.size();i++)
    {
        if (l[i]!=unique_l[j])
        {
            unique_l.push_back(l[i]);
            j+=1;
        }
    }
    return unique_l;
}


