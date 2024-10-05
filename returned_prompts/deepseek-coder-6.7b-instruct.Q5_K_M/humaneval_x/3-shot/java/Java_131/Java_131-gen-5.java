        int product = 1;
        boolean odd = false;

        while  (n  !=  0)  {
            int digit = n  %  10;

            if  (digit  %  2  !=  0)  {
                product *=  digit;
                odd =  true;
            }

            n /=  10;
        }

        return  odd  ?  product  :  0;
    }
}

