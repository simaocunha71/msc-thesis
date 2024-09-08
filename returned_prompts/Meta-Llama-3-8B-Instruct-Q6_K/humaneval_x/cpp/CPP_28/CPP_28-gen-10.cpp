    string result = "";
    for (string s : strings) {
        result += s;
    }
    return result;
}

int main() {
    vector<string> strings = {"a", "b", "c"};
    printf("%s\n", concatenate(strings).c_str());
    return 0;
}
