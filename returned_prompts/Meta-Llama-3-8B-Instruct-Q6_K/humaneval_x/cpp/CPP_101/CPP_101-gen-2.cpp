    vector<string> result;
    size_t pos = 0;
    while ((pos = s.find(" ")) != string::npos) {
        string temp = s.substr(0, pos);
        result.push_back(temp);
        s.erase(0, pos + 1);
    }
    if (!s.empty()) {
        result.push_back(s);
    }
    return result;
}
int main()
{
    string s = "Hi, my name is John";
    vector<string> result = words_string(s);
    for (const auto& word : result) {
        printf("%s\n", word.c_str());
    }
    return 0;
}
