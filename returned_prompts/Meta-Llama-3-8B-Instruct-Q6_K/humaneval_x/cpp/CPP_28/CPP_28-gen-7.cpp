    string result = "";
    for (const auto& str : strings) {
        result += str;
    }
    return result;
}
int main() {
    printf("%s\n", concatenate({"a", "b", "c"}).c_str());
    return 0;
}
