    vector<int> result(2, 0);
    for(int i = 1; i <= n; i++) {
        string s = to_string(i);
        if(s == string(s.rbegin(), s.rend())) {
            if(i % 2 == 0)
                result[0]++;
            else
                result[1]++;
        }
    }
    return result;
}  // Time complexity is O(n) where n is the input number. Space complexity is O(1).