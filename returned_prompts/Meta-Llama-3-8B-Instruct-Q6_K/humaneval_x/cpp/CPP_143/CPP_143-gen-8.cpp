    // Split the sentence into words
    string words[100];
    int i = 0;
    int j = 0;
    while (j < sentence.length()) {
        if (sentence[j] == ' ') {
            words[i] = sentence.substr(j + 1);
            i++;
            j++;
        }
        else {
            j++;
        }
    }
    words[i] = sentence.substr(j);
    i++;

    // Check each word length
    string result = "";
    for (int k = 0; k < i; k++) {
        if (isPrime(strlen(words[k].c_str()))) {
            result += words[k] + " ";
        }
    }
    return result;
}

bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    string sentence = "This is a test";
    printf("%s\n", words_in_sentence(sentence).c_str());
    return 0;
}

B:
    #include <iostream>
    #include <string>
    using namespace std;

    string words_in_sentence(string sentence) {
        string result = "";
        string word;
        for (char c : sentence) {
            if (c == ' ') {
                if (isPrime(word.length())) {
                    result += word + " ";
                }
                word = "";
            } else {
                word += c;
            }
        }
        if (isPrime(word.length())) {
            result += word;
        }
        return result;
    }

    bool isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    int main() {
        string sentence = "This is a test";
        cout << words_in_sentence(sentence) << endl;
        return 0;
    }
C:
    #include <iostream>
    #include <string>
    using namespace std;

    string words_in_sentence(string sentence) {
        string result = "";
        string word;
        for (char c : sentence) {
            if (c == ' ') {
                if (isPrime(word.length())) {
                    result += word + " ";
                }
