    vector<int> result;
    int new_number = number + remaining;
    result.push_back(new_number);
    result.push_back(new_number - need);
    return result;
}


