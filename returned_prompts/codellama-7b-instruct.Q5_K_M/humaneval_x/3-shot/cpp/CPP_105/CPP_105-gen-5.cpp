    vector<string> v;
    string s;
    for (int i=0;i<arr.size();i++)
    {
        s=to_string(arr[i]);
        v.push_back(s);
    }
    sort(v.begin(),v.end(),[](string &a, string &b){return a.length()<b.length();});
    return v;
}


