    bool all_upper = true, all_lower = true;
    for (auto it = dict.begin(); it != dict.end(); it++) {
        for (auto c : it->first) {
            if (islower(c)) all_upper = false;
            if (isupper(c)) all_lower = false;
        }
    }
    return all_upper || all_lower;
}


