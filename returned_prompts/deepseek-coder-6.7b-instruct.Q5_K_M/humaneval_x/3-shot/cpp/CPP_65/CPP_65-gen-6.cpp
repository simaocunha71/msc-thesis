    string s=to_string(x);
    int sz=s.size();
    shift%=sz;
    rotate(s.begin(),s.begin()+sz-shift,s.end());
    return s;
}


