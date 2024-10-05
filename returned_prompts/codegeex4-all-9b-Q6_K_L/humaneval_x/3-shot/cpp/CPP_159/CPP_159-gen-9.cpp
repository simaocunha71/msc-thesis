    vector<int> result;
    if (remaining<need)
    {
        result.push_back(need+number);
        result.push_back(0);
    }
    else
    {
        result.push_back(need+number);
        result.push_back(remaining-need);
    }
    return result;
}

