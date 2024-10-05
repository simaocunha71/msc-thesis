    int len_b = b.size();
    for(int i = 0; i < len_b; i++) {
        string temp = b.substr(i);
        if(a.find(temp) != string::npos) {
            return true;
        }
    }
    for(int i = 0; i < len_b; i++) {
        string temp = b.substr(i, len_b - i);
        if(a.find(temp) != string::npos) {
            return true;
        }
    }
    return false;
}  // O(n*m) time complexity


