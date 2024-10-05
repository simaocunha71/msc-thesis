    vector<int> result;
    result.push_back(number+remaining);
    if (number+remaining>=need)
    {
        result.push_back(remaining-need);
    }
    else
    {
        result.push_back(0);
    }
    return result;
}


