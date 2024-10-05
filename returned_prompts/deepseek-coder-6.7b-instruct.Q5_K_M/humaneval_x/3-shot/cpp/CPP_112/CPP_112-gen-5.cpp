    for(auto i : c)
    {
        s.erase(remove(s.begin(), s.end(), i), s.end());
    }
    string s_rev=s;
    reverse(s_rev.begin(),s_rev.end());
    string res=(s==s_rev)?"True":"False";
    return {s,res};
}


