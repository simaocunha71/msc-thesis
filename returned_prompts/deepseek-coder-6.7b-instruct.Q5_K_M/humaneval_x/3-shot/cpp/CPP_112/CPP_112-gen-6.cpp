    for (auto i:c) {
        s.erase(remove(s.begin(), s.end(), i), s.end());
    }
    string reversed_s = s;
    reverse(reversed_s.begin(), reversed_s.end());
    string result = (s == reversed_s) ? "True" : "False";
    return {reversed_s, result};
}

