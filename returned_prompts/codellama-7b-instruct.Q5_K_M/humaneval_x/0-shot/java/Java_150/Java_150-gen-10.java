        if(n < 2)
            return y;
        for(int i = 2; i < n; i++)
            if(n % i == 0)
                return x;
        return y;
    }
}

