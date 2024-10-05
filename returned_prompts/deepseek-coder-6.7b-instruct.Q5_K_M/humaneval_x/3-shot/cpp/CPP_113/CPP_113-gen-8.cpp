    vector<string> res;
    for(auto &str : lst)
    {
        int count = 0;
        for(auto &ch : str)
        {
            if((ch - '0') % 2 != 0)
                count++;
        }
        string temp = "the number of odd elements in the string " + to_string(count) + " of the input.";
        res.push_back(temp);
    }
    return res;
}



