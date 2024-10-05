        int count = 0;
        for  (Integer num : arr) {
            int sum = 0;
            if  (num < 0)  {
                while  (num != 0)  {
                    sum += num % 10;
                    num /= 10;
                }
            if  (sum > 0)  count++;
            }  else  {
                while  (num != 0)  {
                    sum += num % 10;
                    num /= 10;
                }
            if  (sum > 0)  count++;
            }
        }
        return count;
    }
}


A: Here are your solutions:

