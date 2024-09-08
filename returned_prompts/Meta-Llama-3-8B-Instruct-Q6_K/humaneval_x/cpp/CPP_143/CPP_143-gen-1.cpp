    string result = "";
    string words[sentence.length()];
    int i = 0, j = 0;

    // split the sentence into words
    while (i < sentence.length()) {
        while (sentence[i] == ' ')
            i++;
        j = i;
        while (sentence[i] != ' ' && i < sentence.length())
            i++;
        words[i - j] = sentence.substr(j, i - j);
    }

    // check if the length of each word is a prime number
    for (int i = 0; i < sentence.length(); i++) {
        bool is_prime = true;
        int num = words[i].length();
        for (int j = 2; j * j <= num; j++) {
            if (num % j == 0) {
                is_prime = false;
                break;
            }
        }
        if (is_prime)
            result += words[i] + " ";
    }

    return result.substr(0, result.length() - 1);
}

int main() {
    string sentence = "This is a test";
    cout << words_in_sentence(sentence) << endl;
    return 0;
}  // Output: "is"

