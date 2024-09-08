    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u') {
            count++;
        }
    }
    if (s.length() > 0 && s[s.length() - 1] == 'y') {
        count++;
    }
    return count;
}
int main() {
    cout << vowels_count("abcde") << endl;
    cout << vowels_count("ACEDY") << endl;
    return 0;
}

