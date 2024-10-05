    vector<int> thirds;
    vector<int> others;
    int i;
    for (i=0;i<l.size();i++)
    {
        if (i%3==0){
        thirds.push_back(l[i]);
        }
        else {
        others.push_back(l[i]);
        }
    }
    sort(thirds.begin(),thirds.end());
    vector<int> lprime;
    for (i=0;i<others.size();i++)
    {
    lprime.push_back(others[i]);
    }
    for (i=0;i<thirds.size();i++)
    {
    lprime.push_back(thirds[i]);
    }
    return lprime;
}


