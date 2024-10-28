    int len_a = a.size();
    int len_b = b.size();
    for(int i = 0; i <= len_a - len_b; i++) {
        string temp = a.substr(i, len_b);
        if(temp == b) {
            return true;
        }
    }
    for(int i = 0; i < len_b; i++) {
        b = b.substr(1) + b[0];
        for(int j = 0; j <= len_a - len_b; j++) {
            string temp = a.substr(j, len_b);
            if(temp == b) {
                return true;
            }
        }
    }
    return false;
}

