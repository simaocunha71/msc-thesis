    vector<int> result(2);
    result[0] = 0; // even
    result[1] = 0; // odd
    for(int i = 1; i <= n; i++){
        string s = to_string(i);
        bool is_palindrome = true;
        for(int j = 0; j < s.length(); j++){
            if(s[j] != s[s.length() - j - 1]){
                is_palindrome = false;
                break;
            }
        }
        if(is_palindrome && i % 2 == 0) result[0]++;
        else if(is_palindrome) result[1]++;
    }
    return result;
}

int main() {
    int n;
    printf("Enter a positive integer: ");
    scanf("%d", &n);
    vector<int> result = even_odd_palindrome(n);
    printf("Number of even integer palindromes: %d\n", result[0]);
    printf("Number of odd integer palindromes: %d\n", result[1]);
    return 0;
}

