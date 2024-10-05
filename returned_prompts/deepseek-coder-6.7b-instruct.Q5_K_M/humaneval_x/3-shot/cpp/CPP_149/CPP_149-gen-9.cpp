    vector<string> result;
    for(string s: lst){
        if(s.length()%2==0)
            result.push_back(s);
    }
    sort(result.begin(), result.end());
    return result;
}


