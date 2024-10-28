int n = 13195;
int result = 1;
for (int i = 2; i * i <= n; i++) {
    if (n % i == 0) {
        while (n % i == 0) {
            n /= i;
        }
        result = i;
    }
}
return result;
}
}
