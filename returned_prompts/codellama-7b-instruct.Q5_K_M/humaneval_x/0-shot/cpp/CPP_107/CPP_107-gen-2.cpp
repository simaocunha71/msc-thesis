    vector<int> ans(2, 0);
    for(int i = 1; i <= n; i++){
        string s = to_string(i);
        bool is_even = true;
        for(int j = 0; j < s.size() / 2; j++){
            if(s[j] != s[s.size() - 1 - j]){
                is_even = false;
                break;
            }
        }
        if(is_even)
            ans[0]++;
        else
            ans[1]++;
    }
    return ans;
}

int main(int argc, char const *argv[])
{
    int n;
    vector<int> ans;
    scanf("%d", &n);
    ans = even_odd_palindrome(n);
    printf("%d %d", ans[0], ans[1]);
    return 0;
}
