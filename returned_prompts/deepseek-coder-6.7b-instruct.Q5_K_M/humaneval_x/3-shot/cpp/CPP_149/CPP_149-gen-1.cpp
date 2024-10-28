    vector<string> result;
    for(auto word : lst){
        if(word.size() % 2 == 0)
        result.push_back(word);
    }
    sort(result.begin(), result.end());
    return result;
}



