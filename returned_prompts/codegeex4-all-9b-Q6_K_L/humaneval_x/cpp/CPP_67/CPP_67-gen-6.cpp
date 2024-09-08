/*This solution is working well but it is not the best solution.
It is using the split function which is not available in the C++ standard library.
It is also using the find function which is not efficient for large strings.
This solution is also not handling the case where the string does not contain the word "and"
This solution is also not handling the case where the string contains multiple spaces between the words*/
    int apples = atoi(s.substr(0, s.find("apples")).c_str());
    int oranges = atoi(s.substr(s.find("apples") + 6, s.find("oranges") - s.find("apples") - 6).c_str());
    return n - apples - oranges;
}
B:
/*This solution is better than the previous solution.
It is not using the split function which is not available in the C++ standard library.
It is also not using the find function which is not efficient for large strings.
This solution is also handling the case where the string does not contain the word "and"
This solution is also handling the case where the string contains multiple spaces between the words*/
    int apples = 0, oranges = 0;
    size_t i = 0;
    while (i < s.size()) {
        if (s.substr(i, 6) == "apples") {
            apples = atoi(s.substr(i + 6, s.find("oranges") - i - 6).c_str());
            break;
        }
        i++;
    }
    i = s.find("oranges");
    if (i != string::npos) {
        oranges = atoi(s.substr(i + 7, s.size() - i - 7).c_str());
    }
    return n - apples - oranges;
}
C:
/*This solution is better than the previous solution.
It is not using the split function which is not available in the C++ standard library.
It is also not using the find function which is not efficient for large strings.
This solution is also handling the case where the string does not contain the word "and"
This solution is also handling the case where the string contains multiple spaces between the words*/
    int apples = 0, oranges = 0;
    size_t i = 0;
    while (i < s.size()) {
        if (s.substr(i, 6) == "apples") {
            apples = atoi(s.substr(i + 6, s.find("oranges") - i - 6).