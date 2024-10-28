    vector<string> res;
    int count = 0;
    for(auto &s : lst){
        count = 0;
        for(auto &c : s){
            if((c-'0')%2 != 0)
                count++;
        }
        string temp = "the number of odd elements in the string " + to_string(count) + " of the input.";
        res.push_back(temp);
    }
    return res;
}


