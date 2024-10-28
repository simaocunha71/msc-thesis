        if(n == 1) return x > 0;

        while(x % n == 0) {
            x /= n;
        }

        return x == 1;
     }
}

