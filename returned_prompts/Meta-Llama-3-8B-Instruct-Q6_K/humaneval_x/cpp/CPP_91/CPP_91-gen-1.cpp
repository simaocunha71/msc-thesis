    int count = 0;
    int i = 0;
    while(i < S.size()) {
        i = S.find('.', i);
        if(i == string::npos) {
            i = S.find('?', i);
            if(i == string::npos) {
                i = S.find('!', i);
                if(i == string::npos) break;
            }
        }
        if(i != string::npos) {
            string sentence = S.substr(0, i);
            if(sentence.find("I") == 0) {
                count++;
            }
            S = S.substr(i+1);
        }
    }
    return count;
}

int main() {
    string S;
    printf("Enter a sentence: ");
    getline(cin, S);
    printf("Boredoms: %d\n", is_bored(S));
    return 0;
}

