        int sum = 0;
        for (int num : numbers)  {
            if (num % 2 != 0  && num % 3 != 0) {
                sum += num;
            }
        }
        return sum;
     }
}

