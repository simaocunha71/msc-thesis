        if (n < 1) 
            return 0;
        else if (n == 1) 
            return 1;
        else 
            return 8 * (int)Math.pow(9, n-2);
     }
}

