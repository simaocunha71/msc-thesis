    string result = "";
    for(int i = 0; i <= n; i++) {
        result += to_string(i) + " ";
    }
    return result;
}

int main() {
    printf("%s\n", string_sequence(5).c_str());
    return 0;
}

