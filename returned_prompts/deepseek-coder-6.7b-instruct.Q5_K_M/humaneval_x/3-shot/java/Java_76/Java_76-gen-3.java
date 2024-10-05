        if (n == 1) return true;

        while (x > 1) {
            x /= n;
            if (x == 1) return true;
        }
        return false;
     }
}

