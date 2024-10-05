    vector<vector<int>> result;
    result.push_back(vector<int>{});
    for(int num : numbers){
        int size = result.size();
        for(int i = 0; i < size; i++){
            vector<int> tmp = result[i];
            tmp.push_back(num);
            result.push_back(tmp);
        }
    }
    return result;
}

/*
For a list of strings, return a list of all possible combinations of selecting and ignoring strings
such that each combination has the same total length as the total length of all elements.
E.g. for the list ["cat", "dog", "mouse"], the output is [[''], ['cat'], ['dog'], ['mouse'], ['cat', 'dog'], ['cat', 'mouse'], ['dog', 'mouse'], ['cat', 'dog', 'mouse']]

>>> combinations_string(["cat", "dog", "mouse"])