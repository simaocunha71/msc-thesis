    vector<string> result;
    for(string s: lst){
        int count=0;
        for(char c: s){
            if((c-'0')%2 != 0) count++;
        }
        string res = "the number of odd elements in the string "+ to_string(count)+" of the input.";
        result.push_back(res);
    }
    return result;
}


