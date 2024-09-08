    vector<int> result(2);
    for(int i = 1; i <= n; i++){
        string str = to_string(i);
        if(str == string(str.rbegin(), str.rend()) && (i % 2 == 0 ? 1 : 0)){
            result[0]++;
        }
        if(str == string(str.rbegin(), str.rend()) && (i % 2 != 0 ? 1 : 0)){
            result[1]++;
        }
    }
    return result;
}

int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    vector<int> result = even_odd_palindrome(n);
    printf("Even palindrome count: %d\n", result[0]);
    printf("Odd palindrome count: %d\n", result[1]);
    return 0;
}

