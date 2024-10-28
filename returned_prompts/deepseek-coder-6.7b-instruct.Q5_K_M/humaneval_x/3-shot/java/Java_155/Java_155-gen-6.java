        num = Math.abs(num);
        int odd_count = 0;
        int even_count = 0;

        while  (num  !=  0) {
            int digit = num  % 10;
            if  (digit  % 2  ==  0) 
                even_count++;
            else
                odd_count++;
            num  /=  10;
        }

        return Arrays.asList(even_count, odd_count);
     }
}

