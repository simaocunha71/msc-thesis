    vector<string> result;
    for (auto str : lst) {
        if (str.length() % 2 == 0) {
            result.push_back(str);
        }
    }
    sort(result.begin(), result.end(), [](const string& a, const string& b) {
        if (a.length() == b.length()) {
            return a < b;
        }
        return a.length() < b.length();
    });
    return result;
}
int main() {
    vector<string> lst = {"aa", "a", "aaa"};
    vector<string> result = sorted_list_sum(lst);
    for (auto str : result) {
        printf("%s\n", str.c_str());
    }
    return 0;
}