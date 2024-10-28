    vector<string> result;
    for (const auto& str : lst) {
        if (str.length() % 2 == 0) {
            result.push_back(str);
        }
    }
    sort(result.begin(), result.end(),
         [](const string &a, const string &b) {
             if (a.length() == b.length()) {
                 return a < b;
             }
             return a.length() < b.length();
         });
    return result;
}  // This function removes the words with odd length from the list and returns the list sorted by the length of the words. If two words have the same length, it sorts them alphabetically.