    vector<int> ans;
    int total=number+remaining;
    int leftover=total-need;
    ans.push_back(total);
    ans.push_back(leftover);
    return ans;
}



