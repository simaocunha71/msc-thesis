        if  (n < 10) 
            return false;
        for  (int i = 2; i < n / 2; i += 2) 
            if  (i % 2 == 0 && (n - i) % 2 == 0) 
                return true;
        return false;
    }
}

