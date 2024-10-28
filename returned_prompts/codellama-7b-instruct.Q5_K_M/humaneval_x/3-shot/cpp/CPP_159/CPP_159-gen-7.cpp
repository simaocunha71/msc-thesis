    vector<int> result;
    result.push_back(number+remaining);
    if (remaining<need)
    result.push_back(0);
    else
    result.push_back(remaining-need);
    return result;
}



