        int count = 0;
        for(Integer num : nums) {
            if(num > 10 && (num % 10) % 2 != 0 && (num / 10) % 2 != 0) count++;
        }
        return count;
     }
}

