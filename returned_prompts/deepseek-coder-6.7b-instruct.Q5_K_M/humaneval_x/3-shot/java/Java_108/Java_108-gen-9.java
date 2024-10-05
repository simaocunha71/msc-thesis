        int count = 0;
        for(int i = 0; i < arr.size(); i++) {
            int num = arr.get(i);
            if(num < 0) num *= -1;
            int sum = 0;
            while(num > 0) {
                sum += num % 10;
                num /= 10;
            }
            if(sum > 0) count++;
        }
        return count;
    }
}

