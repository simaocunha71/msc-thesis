    sort(lst.begin(),lst.end(),[](string a,string b){
        if (a.length()<b.length())
        return true;
        if (a.length()>b.length())
        return false;
        return a<b;
    });
    vector<string> result;
    for (int i=0;i<lst.size();i++)
    if (lst[i].length()%2==0)
    result.push_back(lst[i]);
    sort(result.begin(),result.end());
    return result;
}





