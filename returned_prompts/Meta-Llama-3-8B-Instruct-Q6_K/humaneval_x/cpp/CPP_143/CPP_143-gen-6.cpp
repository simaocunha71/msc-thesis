    int i = 0, n = sentence.size();
    string result = "";
    while (i < n) {
        int j = i;
        while (j < n && !ispunct(sentence[j])) {
            j++;
        }
        if (j - i > 0 && isPrime(sentence.substr(i, j - i).size())) {
            result += sentence.substr(i, j - i) + " ";
        }
        i = j;
    }
    return result.substr(0, result.size() - 1);
}

bool isPrime(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    printf("Hello, %s!\n", "World");
    string s = "This is a test";
    printf("Words with prime length: %s\n", words_in_sentence(s).c_str());
    return 0;
}
