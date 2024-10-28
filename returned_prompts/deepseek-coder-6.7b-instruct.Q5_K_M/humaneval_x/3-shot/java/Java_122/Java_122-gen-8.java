        int sum = 0;
        for  (int i = 0; i < k; i++) {
            if  (arr.get(i)  / 10 <= 0)  // one or two digit number
                sum += arr.get(i);
        }
        return sum;
     }
}

