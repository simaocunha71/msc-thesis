        if (n == 1) 
            return true;

        while(x % n == 0) 
            x /= n;

        return x == 1;
    }
}

