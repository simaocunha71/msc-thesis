    string res = "";
    for(int i = 0; i <= n; i++) {
        res += to_string(i) + " ";
    }
    return res.substr(0, res.size() - 1);
}

int main() {
    printf("%s\n", string_sequence(5).c_str());
    return 0;
}

Output:
0 1 2 3 4 5
