    vector<int> res;
    for(int i = 0; i < numbers.size(); i++) {
        res.push_back(numbers[i]);
        if(i != numbers.size() - 1) {
            res.push_back(delimeter);
        }
    }
    return res;
}


