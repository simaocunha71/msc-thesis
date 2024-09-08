    int sum = 0;
    while(N > 0) {
        int digit = N % 2;
        sum += digit;
        N /= 2;
    }
    string res;
    while(sum > 0) {
        int last = sum % 2;
        res = to_string(last) + res;
        sum /= 2;
    }
    return res;
}
int main() {
    printf("%s\n",solve(1000).c_str());
    printf("%s\n",solve(150).c_str());
    printf("%s\n",solve(147).c_str());
    return 0;
}