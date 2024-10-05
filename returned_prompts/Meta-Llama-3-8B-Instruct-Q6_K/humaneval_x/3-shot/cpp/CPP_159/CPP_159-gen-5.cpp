    int eaten=number+min(need,remaining);
    int left=remaining-need+eaten-number;
    vector<int> res;
    res.push_back(eaten);
    res.push_back(left);
    return res;
}