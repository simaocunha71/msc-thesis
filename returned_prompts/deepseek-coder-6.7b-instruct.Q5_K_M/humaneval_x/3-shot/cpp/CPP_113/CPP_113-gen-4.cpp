    vector<string> res;
    for (int i = 0; i < lst.size(); i++) {
        string num = lst[i];
        int count = 0;
        for (int j = 0; j < num.size(); j++) {
            if ((num[j] - '0') % 2 != 0) {
                count++;
            }
        }
        string str = "the number of odd elements in the string ";
        str += to_string(count);
        str += " of the input.";
        res.push_back(str);
    }
    return res;
}


