        int count = 0;
        for(Integer num : arr) {
            if(sumDigits(num) > 0) {
                count++;
            }
        }
        return count;
    }

    private int sumDigits(Integer num) {
        int sum = 0;
        while(num != 0) {
            sum += num % 10;
            num = num / 10;
        }
        return sum;
    }
}

