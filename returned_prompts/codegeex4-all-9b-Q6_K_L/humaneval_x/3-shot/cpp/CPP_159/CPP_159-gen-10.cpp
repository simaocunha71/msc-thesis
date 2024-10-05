    vector<int> ans;
    if (need<=remaining)
    {
        ans.push_back(number+need);
        ans.push_back(remaining-need);
    }
    else
    {
        ans.push_back(number+remaining);
        ans.push_back(0);
    }
    return ans;
}

