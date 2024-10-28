    vector<float> result;
    vector<float>::iterator it;
    float min_diff=10000000;
    int i;
    for (i=0;i<numbers.size();i++)
    for (it=numbers.begin()+i+1;it<numbers.end();it++)
    if (abs(*it-*(it-1))<min_diff)
    {
        min_diff=abs(*it-*(it-1));
        result.clear();
        result.push_back(*(it-1));
        result.push_back(*it);
    }
    return result;
}


