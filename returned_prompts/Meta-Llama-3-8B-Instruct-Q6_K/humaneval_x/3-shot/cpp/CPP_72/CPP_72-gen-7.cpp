    if(q.size()!=0&&q.size()!=1){
        string s = "";
        for(int i = 0; i < q.size(); i++) {
            s += to_string(q[i]);
        }
        if(s != s.substr(0, s.length() / 2).substr(0, s.length() / 2) + s.substr(s.length() / 2).substr(0, s.length() / 2))
            return false;
    }
    int sum = 0;
    for(int i = 0; i < q.size(); i++) {
        sum += q[i];
    }
    if(sum > w)
        return false;
    return true;
}
