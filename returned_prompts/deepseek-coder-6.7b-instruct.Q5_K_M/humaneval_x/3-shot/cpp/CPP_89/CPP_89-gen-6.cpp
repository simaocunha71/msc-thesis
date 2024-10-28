    string res="";
    for (auto &c : s) {
        if (isupper(c)) {
            res += char(int('A') + (c - 'A' + 2*2) % 26);
        } else {
            res += char(int('a') + (c - 'a' + 2*2) % 26);
        }
    }
    return res;
}


