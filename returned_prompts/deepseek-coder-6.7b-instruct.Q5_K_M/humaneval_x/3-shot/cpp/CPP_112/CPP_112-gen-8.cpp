    for(char ch:c)
        s.erase(remove(s.begin(),s.end(),ch),s.end());
    string rev_s=s;
    reverse(rev_s.begin(),rev_s.end());
    string res=(s==rev_s)?"True":"False";
    return {s,res};
}

