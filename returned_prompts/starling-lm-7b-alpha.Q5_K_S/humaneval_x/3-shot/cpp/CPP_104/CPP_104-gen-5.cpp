    vector<int> result;
    vector<int>::iterator i;
    for (i=x.begin();i!=x.end();i++)
    if (all_of(*i,10,[](int d){return d%2!=0;}))
    {
        result.push_back(*i);
    }
    sort(result.begin(),result.end());
    return result;
}


