    if (s0.length()!=s1.length()) return false;
    sort(s0.begin(),s0.end());
    sort(s1.begin(),s1.end());
    return s0==s1;
}