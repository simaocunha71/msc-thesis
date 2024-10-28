    int even_palindrome = 0;
    int odd_palindrome = 0;
    for(int i = 1; i <= n; i++) {
        string str = to_string(i);
        if (str == reverse(str)) {
            if (i % 2 == 0)
                even_palindrome++;
            else
                odd_palindrome++;
        }
    }
    vector<int> result;
    result.push_back(even_palindrome);
    result.push_back(odd_palindrome);
    return result;
}