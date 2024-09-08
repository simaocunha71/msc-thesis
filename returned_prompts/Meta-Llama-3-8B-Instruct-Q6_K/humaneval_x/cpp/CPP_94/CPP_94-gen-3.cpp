    int max_prime = 0;
    for (int i = 0; i < lst.size(); i++) {
        if (isPrime(lst[i])) {
            if (lst[i] > max_prime) {
                max_prime = lst[i];
            }
        }
    }
    int sum = 0;
    while (max_prime > 0) {
        sum += max_prime % 10;
        max_prime /= 10;
    }
    return sum;
}
bool isPrime(int num) {
    if (num <= 1)
        return false;
    if (num == 2)
        return true;
    if (num % 2 == 0)
        return false;
    int i = 3;
    while (i * i <= num) {
        if (num % i == 0)
            return false;
        i += 2;
    }
    return true;
}
int main() {
    vector<int> lst = {0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3};
    int result = skjkasdkd(lst);
    printf("%d\n", result);
    return 0;
}
