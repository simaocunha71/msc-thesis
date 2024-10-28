    vector<int> sorted_x(x.size());
    vector<int> result;
    for (int i=0;i<x.size();i++)
    sorted_x[i]=x[i];
    sort(sorted_x.begin(), sorted_x.end());
    for (int i=0;i<sorted_x.size();i++)
    if (sorted_x[i]%2)
    result.push_back(sorted_x[i]);
    return result;
}


