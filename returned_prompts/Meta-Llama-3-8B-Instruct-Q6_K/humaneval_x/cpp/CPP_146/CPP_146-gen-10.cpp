    int count = 0;
    for(int num : nums){
        if(num > 10){
            int temp = num;
            int first_digit = temp % 10;
            temp /= 10;
            int last_digit = temp % 10;
            if(first_digit % 2 != 0 && last_digit % 2 != 0){
                count++;
            }
        }
    }
    return count;
}

