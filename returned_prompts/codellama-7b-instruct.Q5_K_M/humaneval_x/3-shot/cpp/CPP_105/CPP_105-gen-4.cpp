    vector<string> names;
    for (int i=0;i<arr.size();i++)
    names.push_back(to_string(arr[i]));
    sort(names.begin(),names.end(),[](string a,string b){
        return a.length()<b.length();});
    return names;
}



