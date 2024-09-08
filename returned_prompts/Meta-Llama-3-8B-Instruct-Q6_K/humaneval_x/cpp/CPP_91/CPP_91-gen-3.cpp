    int count = 0;
    int i = 0;
    while(i < S.length()) {
        if(S[i] == '.' || S[i] == '?' || S[i] == '!') {
            if(i > 0 && S[i-1] == 'I') {
                count++;
            }
            i++;
            while(i < S.length() && (S[i] == '.' || S[i] == '?' || S[i] == '!')) {
                i++;
            }
        }
        else {
            i++;
        }
    }
    return count;
}

int main() {
    string S;
    printf("Enter a string: ");
    getline(cin, S);
    printf("Number of boredoms: %d\n", is_bored(S));
    return 0;
}

