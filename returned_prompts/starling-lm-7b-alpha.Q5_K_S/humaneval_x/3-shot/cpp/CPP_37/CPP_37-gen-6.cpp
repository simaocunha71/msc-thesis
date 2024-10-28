    int i;
    vector<float> lprime;
    for (i=0;i<l.size();i++)
    if (i%2==0)
    lprime.push_back(l[i]);
    else
    lprime.push_back(l[i]);
    sort(lprime.begin()+1,lprime.end()-1);
    return lprime;
}


