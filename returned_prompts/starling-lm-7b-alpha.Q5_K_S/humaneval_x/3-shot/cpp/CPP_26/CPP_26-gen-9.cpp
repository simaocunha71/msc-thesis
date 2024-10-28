    vector<int>::iterator it;
    it=numbers.begin();
    while (it!=numbers.end()){
        if (*it==*next(it) && *it!=*prev(it))
        {
            numbers.erase(it);
        }
        else
        {
            it++;
        }
    }
    return numbers;
}


