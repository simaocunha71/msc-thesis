    vector<string> result;
    vector<string>::iterator it;
    for (it=lst.begin();it!=lst.end();it++)
    if (it->length()%2==0)
    result.push_back(*it);
    sort(result.begin(),result.end(),[](const string& a,const string& b){
    return a.length()<b.length() || (a.length()==b.length()&&a<b);
    });
    return result;
}


