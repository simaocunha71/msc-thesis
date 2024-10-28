    if(dict.empty())return false;
    bool all_lower = true;
    bool all_upper = true;
    for (auto &it : dict) {
        if (!islower(it.first[0]) && !isupper(it.first[0])) {
            return false;
        }
        all_lower &= islower(it.first[0]);
        all_upper &= isupper(it.first[0]);
    }
    return all_lower || all_upper;
} // end check_dict_case


