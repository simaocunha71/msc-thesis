    vector<int> result;
    if (need>remaining)
    {
        result.push_back(number+remaining);
        result.push_back(0);
    }
    else{
        result.push_back(number+need);
        result.push_back(remaining-need);
    }
    return result;
}

