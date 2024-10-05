    string result="";
    string::iterator it;
    for (it=s.begin();it!=s.end();it++)
    {
        result+=(*it);
        sort(result.begin(),result.end());
    }
    return result;
}



