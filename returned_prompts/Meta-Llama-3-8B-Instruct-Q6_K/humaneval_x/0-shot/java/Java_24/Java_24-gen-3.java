        int i = n;
        while (i > 1) {
            if (n % i == 0) {
                return i;
            }
            i--;
        }
        return 1;
    }
}
B:
    public int largestDivisor(int n) {
        for (int i = n / 2; i > 1; i--) {
            if (n % i == 0) {
                return i;
            }
        }
        return 1;
    }
}
C:
    public int largestDivisor(int n) {
        for (int i = 2; i <= n / 2; i++) {
            if (n % i == 0) {
                return i;
            }
        }
        return 1;
    }
}
D:
    public int largestDivisor(int n) {
        int i = 2;
        while (i <= n / 2) {
            if (n % i == 0) {
                return i;
            }
            i++;
        }
        return 1;
    }
}

E:
    public int largestDivisor(int n) {
        for (int i = n / 2; i >= 1; i--) {
            if (n % i == 0) {
                return i;
            }
        }
        return 1;
    }
}

F:
    public int largestDivisor(int n) {
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return i;
            }
        }
        return 1;
    }
}

G:
    public int largestDivisor(int n) {
        for (int i = 2; i <= n; i++) {
            if (n % i == 0) {
                return i;
            }
        }
        return 1;
    }
}

H:
    public int largestDivisor(int n) {
        int i = 2;
        while (i <= n) {
            if (n % i == 0) {
                return i;
            }
            i++;
        }
        return 1;
    }
}

I:
    public int largestDivisor(int n) {
        int i = 2;
        while (i <= n / 2) {
            if (n % i == 0) {
                return i;
            }
            i++;
        }
        return 1;
    }
}

J:
    public