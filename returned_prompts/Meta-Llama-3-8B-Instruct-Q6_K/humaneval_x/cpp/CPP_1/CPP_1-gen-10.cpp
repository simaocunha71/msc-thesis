    vector<string> res;
    int i = 0;
    while (i < paren_string.size()) {
        int count = 0;
        while (i < paren_string.size() && paren_string[i] == '(') {
            count++;
            i++;
        }
        int j = i;
        while (j < paren_string.size() && paren_string[j] == ')') {
            j++;
        }
        res.push_back(paren_string.substr(i, j - i));
        i = j + 1;
    }
    return res;
}
B:
    vector<string> separate_paren_groups(string paren_string){
        vector<string> result;
        string curr = "";
        int count = 0;
        for(int i = 0; i < paren_string.size(); i++){
            if(paren_string[i] == '('){
                count++;
                curr += paren_string[i];
            }else if(paren_string[i] == ')'){
                count--;
                curr += paren_string[i];
                if(count == 0){
                    result.push_back(curr);
                    curr = "";
                }
            }
        }
        return result;
    }
C:
    vector<string> separate_paren_groups(string s) {
        vector<string> res;
        string curr;
        int count = 0;
        for (char c : s) {
            if (c == '(') {
                count++;
                curr += c;
            } else if (c == ')') {
                count--;
                curr += c;
                if (count == 0) {
                    res.push_back(curr);
                    curr = "";
                }
            }
        }
        return res;
    }
D:
    vector<string> separate_paren_groups(string s) {
        vector<string> res;
        stack<string> st;
        for (char c : s) {
            if (c == '(') {
                st.push("");
            } else {
                string top = st.top();
                st.pop();
                top += c;
                if (st.empty()) {
                    res.push_back(top);
                } else {
                    st.top() += top;
                }
            }
        }
        return res;
    }
E:
    vector<string> separate_paren_groups(string s) {
        vector<string> res;
        int i = 0;
        while (i < s.size()) {
            int count = 0;
            while (i < s.size() && s[i] == '(') {
                i++;
                count++;
            }
            int j = i;
           