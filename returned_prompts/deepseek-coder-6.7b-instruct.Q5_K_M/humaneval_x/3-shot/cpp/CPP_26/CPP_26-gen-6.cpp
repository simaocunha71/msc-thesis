    vector<int> res;
    sort(numbers.begin(), numbers.end());
    int i;
    for  (i=0; i<numbers.size(); i++)
        if  (i==0 || numbers[i] != numbers[i-1])
            res.push_back(numbers[i]);
    return res;
}


