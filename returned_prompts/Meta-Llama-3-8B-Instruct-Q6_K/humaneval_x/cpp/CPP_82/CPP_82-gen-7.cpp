    int length = str.length();
    if(length <= 1)
        return false;
    for(int i=2; i<=length/2; i++){
        if(length%i == 0)
            return false;
    }
    return true;
}
int main()
{
    printf("%d\n",prime_length("Hello"));
    printf("%d\n",prime_length("abcdcba"));
    printf("%d\n",prime_length("kittens"));
    printf("%d\n",prime_length("orange"));
    return 0;
}
C:
    int prime_length(string str) {
        int length = str.length();
        if (length <= 1) {
            return false;
        }
        for (int i = 2; i * i <= length; i++) {
            if (length % i == 0) {
                return false;
            }
        }
        return true;
    }
    int main() {
        cout << prime_length("Hello") << endl;
        cout << prime_length("abcdcba") << endl;
        cout << prime_length("kittens") << endl;
        cout << prime_length("orange") << endl;
        return 0;
    }
D:
    bool prime_length(string str) {
        int length = str.length();
        if (length <= 1) {
            return false;
        }
        for (int i = 2; i * i <= length; i++) {
            if (length % i == 0) {
                return false;
            }
        }
        return true;
    }
    int main() {
        cout << (prime_length("Hello") ? "true" : "false") << endl;
        cout << (prime_length("abcdcba") ? "true" : "false") << endl;
        cout << (prime_length("kittens") ? "true" : "false") << endl;
        cout << (prime_length("orange") ? "true"