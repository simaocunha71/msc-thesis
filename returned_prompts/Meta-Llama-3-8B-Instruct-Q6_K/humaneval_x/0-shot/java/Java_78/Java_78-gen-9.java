    int count = 0;
    for (char c : num.toCharArray()) {
        if (c >= '2' && c <= '9') {
            if (isPrime(Integer.parseInt(String.valueOf(c)))) {
                count++;
            }
        } else if (c >= 'A' && c <= 'F') {
            if (isPrime(Integer.parseInt(String.valueOf(c - 'A' + 10)))) {
                count++;
            }
        }
    }
    return count;
}

private boolean isPrime(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}
}
