    vector<int> count(2, 0);
    for (int i = 1; i <= n; i++){
        string s = to_string(i);
        if(s == string(s.rbegin(), s.rend())){
            if(s.length() % 2 == 0) count[0]++;
            else count[1]++;
        }
    }
    return count;
}

int main(){
    int n;
    scanf("%d", &n);
    vector<int> res = even_odd_palindrome(n);
    printf("(%d, %d)", res[0], res[1]);
    return 0;
}

