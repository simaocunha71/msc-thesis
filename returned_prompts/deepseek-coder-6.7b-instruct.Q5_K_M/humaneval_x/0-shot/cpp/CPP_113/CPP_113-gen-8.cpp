    vector<string> result;
    for(int i=0;i<lst.size();i++){
        string s = lst[i];
        int count = 0;
        for(int j=0;j<s.size();j++){
            if((s[j]-'0')%2 != 0){
                count++;
            }
        }
        string str_count = to_string(count);
        string temp = "the number of odd elements in the string ";
        temp += str_count;
        temp += " of the input.";
        result.push_back(temp);
    }
    return result;
}
