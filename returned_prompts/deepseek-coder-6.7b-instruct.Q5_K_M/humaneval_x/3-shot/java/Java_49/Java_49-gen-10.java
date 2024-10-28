        return power(2, n, p);
    }

    private int power(int a, int b, int p)  {
        int res  = 1;
        a = a % p; 
        while (b > 0)  {
            if ((b & 1) == 1)
                res = (res * a) % p;
            b = b >> 1;
            a = (a * a) % p;
        }
        return res;
    }
}

