    int sum = 0, max = 0;
    for(int i = 0; i < lst.size(); i++){
        if(isPrime(lst[i])){
            if(lst[i] > max){
                max = lst[i];
            }
        }
    }
    while(max > 0){
        sum += max % 10;
        max /= 10;
    }
    return sum;
}

bool isPrime(int n) {
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;

    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0)
            return false;
    }
    return true;
}
int main()
{
    vector<int> lst = {0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3};
    printf("%d\n", skjkasdkd(lst));
    return 0;
}

