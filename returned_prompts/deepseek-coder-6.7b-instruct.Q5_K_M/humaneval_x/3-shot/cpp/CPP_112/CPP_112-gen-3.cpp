    for(auto i:c)
        s.erase(remove(s.begin(),s.end(),i),s.end());

    string rev_s=s;
    reverse(rev_s.begin(),rev_s.end());
    string result=(s==rev_s)?"True":"False";
    return {s,result};
}


