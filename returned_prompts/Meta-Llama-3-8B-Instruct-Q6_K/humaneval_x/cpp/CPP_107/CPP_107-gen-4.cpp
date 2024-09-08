    vector<int> res;
    int count_even = 0, count_odd = 0;
    for(int i = 1; i <= n; i++){
        string str = to_string(i);
        bool is_palindrome = true;
        for(int j = 0; j < str.length(); j++){
            if(str[j] != str[str.length()-1-j]){
                is_palindrome = false;
                break;
            }
        }
        if(is_palindrome){
            if(i % 2 == 0)
                count_even++;
            else
                count_odd++;
        }
    }
    res.push_back(count_even);
    res.push_back(count_odd);
    return res;
}
int main() {
    int n;
    scanf("%d", &n);
    vector<int> result = even_odd_palindrome(n);
    printf("(%d, %d)\n", result[0], result[1]);
    return 0;
}
