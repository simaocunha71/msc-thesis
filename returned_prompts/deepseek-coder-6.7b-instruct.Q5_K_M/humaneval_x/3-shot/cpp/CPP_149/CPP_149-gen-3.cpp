    vector<string> result;
    for(auto i: lst){
        if(i.length() % 2 == 0){
            result.push_back(i);
        }
    }
    sort(result.begin(), result.end());
    return result;
}


