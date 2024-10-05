        if (n == 1 && x != 1) {
            return false;
        }
        while (x % n == 0) {
            x = x / n;
        }
        return x == 1;
     }
}

