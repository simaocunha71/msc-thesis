    vector<int> result(2);
    int even_count = 0;
    int odd_count = 0;

    for(int i = 1; i <= n; i++){
        string s = to_string(i);
        if(s == string(s.rbegin(), s.rend())){
            if(i % 2 == 0) even_count++;
            else odd_count++;
        }
    }
    result[0] = even_count;
    result[1] = odd_count;
    return result;

}

int main() {
    int n = 12;
    vector<int> result = even_odd_palindrome(n);
    printf("Even Count: %d\n", result[0]);
    printf("Odd Count: %d\n", result[1]);
    return 0;
}