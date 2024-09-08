    vector<int> result(2, 0);
    for(int i = 1; i <= n; i++){
        string s = to_string(i);
        bool isEven = (i % 2 == 0);
        bool isPalindrome = true;
        for(int j = 0; j < s.length(); j++){
            if(s[j] != s[s.length()-1-j]){
                isPalindrome = false;
                break;
            }
        }
        if(isPalindrome){
            if(isEven)
                result[0]++;
            else
                result[1]++;
        }
    }
    return result;
}
int main(){
    int n = 12;
    vector<int> result = even_odd_palindrome(n);
    printf("Even palindrome count: %d\n", result[0]);
    printf("Odd palindrome count: %d\n", result[1]);
    return 0;
}
