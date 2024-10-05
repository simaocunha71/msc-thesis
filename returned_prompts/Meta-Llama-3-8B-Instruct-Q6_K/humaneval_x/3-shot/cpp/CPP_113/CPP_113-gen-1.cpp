    vector<string> result;
    map<string, int> odd_count_map;
    for (int i=0; i<lst.size(); i++) {
        int odd_count = 0;
        for (int j=0; j<lst[i].size(); j++) {
            if ((lst[i][j]-'0') % 2 != 0) {
                odd_count++;
            }
        }
        result.push_back("the number of odd elements "+to_string(odd_count)+" in the str"+to_string(i+1)+" of the input.");
    }
    return result;
}