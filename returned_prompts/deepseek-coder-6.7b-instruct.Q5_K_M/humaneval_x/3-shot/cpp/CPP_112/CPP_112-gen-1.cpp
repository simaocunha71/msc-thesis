    for(auto i:c)
    {
        s.erase(remove(s.begin(),s.end(),i),s.end());
    }
    string rev = s;
    reverse(rev.begin(),rev.end());
    string result = s==rev? "True" : "False";
    return {s,result};
}



