    sort(s0.begin(),s0.end());
    sort(s1.begin(),s1.end());
    for (int i=0;i<s0.length();i++)
    if (s0[i]!=s1[i])
    return false;
    return true;
}



