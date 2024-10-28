    vector<string> result;
    for(auto &s : lst) {
        int count = 0;
        for(char &c : s) {
            if((c - '0') % 2 != 0) count++;
        }
        string temp = "the number of odd elements in the string ";
        temp += to_string(count);
        temp += " of the input.";
        result.push_back(temp);
    }
    return result;
}



