    vector<int> result;
    vector<int>::iterator it;
    for (it=numbers.begin();it<numbers.end();it++)
    {
        if (find(result.begin(),result.end(),*it)==result.end())
        result.push_back(*it);
    }

    return result;
}


