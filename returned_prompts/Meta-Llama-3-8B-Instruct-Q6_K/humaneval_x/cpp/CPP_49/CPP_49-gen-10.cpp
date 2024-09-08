    if (n==0)
        return 1;
    if (n%2==0)
        return modp(n/2,p)*(modp(n/2,p))%p;
    else
        return (n%2)*modp(n-1,p)%p;

}

B:
    int modp(int n, int p) {
        int result = 1;
        for(int i = 0; i < n; i++) {
            result = (result * p) % p;
        }
        return result;
    }

C:
    int modp(int n, int p) {
        int result = 1;
        for(int i = 1; i <= n; i++) {
            result = (result * i) % p;
        }
        return result;
    }

D:
    int modp(int n, int p) {
        int result = 1;
        for(int i = 1; i <= n; i++) {
            result = (result * (1 + (i % p))) % p;
        }
        return result;
    }

E:
    int modp(int n, int p) {
        int result = 1;
        for(int i = 1; i <= n; i++) {
            result = (result * (i % p)) % p;
        }
        return result;
    }

F:
    int modp(int n, int p) {
        int result = 1;
        for(int i = 1; i <= n; i++) {
            result = (result * (i % p)) % p;
        }
        return result;
    }
G:
    int modp(int n, int p) {
        int result = 1;
        for(int i = 1; i <= n; i++) {
            result = (result * (i % p)) % p;
        }
        return result;
    }

H:
    int modp(int n, int p) {
        int result = 1;
        for(int i = 1; i <= n; i++) {
            result = (result * (i % p)) % p;
        }
        return result;
    }

I:
    int modp(int n, int p) {
        int result = 1;
        for(int i = 1; i <= n; i++) {
            result = (result * (i % p)) % p;
        }
        return result;
   