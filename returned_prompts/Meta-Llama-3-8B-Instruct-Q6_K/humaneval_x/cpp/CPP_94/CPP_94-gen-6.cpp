    int max_prime=0;
    int sum=0;
    for(int i=0;i<lst.size();i++){
        if(isPrime(lst[i])){
            if(lst[i]>max_prime){
                max_prime=lst[i];
            }
        }
    }
    sum=digitSum(max_prime);
    return sum;
}
bool isPrime(int n) {
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;

    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

int digitSum(int n) {
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int main() {
    vector<int> lst = {0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3};
    printf("%d",skjkasdkd(lst));
    return 0;
}

