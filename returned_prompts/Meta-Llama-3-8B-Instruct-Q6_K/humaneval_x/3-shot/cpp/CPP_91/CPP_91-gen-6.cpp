    int bored_count = 0;
    string token;
    stringstream ss(S);
    while (getline(ss, token, '.')) {
        if (token.length() > 0 && token[0] == 'I') {
            bored_count++;
            while (getline(ss, token, '.')) {
                if (token.length() == 0) {
                    break;
                }
            }
        }
    }
    return bored_count;
}
int main() {
    string s = "The sky is blue. The sun is shining. I love this weather";
    cout << is_bored(s) << endl;
    return 0;
} 
