    int total = number + need;
    int left = remaining - need;
    if(left < 0){
        total += remaining;
        left = 0;
    }
    vector<int> result;
    result.push_back(total);
    result.push_back(left);
    return result;
}

