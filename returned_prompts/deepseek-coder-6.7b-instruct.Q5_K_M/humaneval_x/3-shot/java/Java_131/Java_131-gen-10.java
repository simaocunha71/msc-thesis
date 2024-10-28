        int product = 1;
        boolean foundOdd = false;

        while  (n  !=  0)  {
            int digit = n  %  10;
            if  (digit  %  2  !=  0)  {
                product *=  digit;
                foundOdd =  true;
            }
            n /=  10;
        }

        return  foundOdd  ?  product  :  0;
    }
}

