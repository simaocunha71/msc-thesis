    vector<int> result(2, 0);
    for(int i = 1; i <= n; ++i){
        int tmp = i;
        int j = 0;
        while(tmp > 0){
            j++;
            tmp /= 10;
        }
        if(j % 2 == 0){
            result[0]++;
        }
        else if(i % 2 == 0){
            result[1]++;
        }
        else{
            result[0]++;
        }
    }
    return result;
}

int main(int argc, const char * argv[]) {

    int n;
    scanf("%d", &n);
    vector<int> result = even_odd_palindrome(n);
    printf("%d, %d\n", result[0], result[1]);
    return 0;
}

*/






















```
