    string res = "";
    for (int i = 0; i <= n; i++) {
        res += to_string(i);
        if (i < n) {
            res += " ";
        }
    }
    return res;
}

int main() {
    printf("%s\n", string_sequence(0).c_str());
    printf("%s\n", string_sequence(5).c_str());
    return 0;
}

