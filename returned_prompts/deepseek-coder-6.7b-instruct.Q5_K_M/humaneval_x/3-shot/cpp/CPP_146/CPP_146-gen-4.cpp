    int count = 0;
    int last_digit, first_digit;
    for(int num : nums){
        if(abs(num) > 10){
            last_digit = abs(num) % 10;
            first_digit = abs(num);
            while(first_digit >= 10){
                first_digit /= 10;
            }
            if(last_digit % 2 == 1 && first_digit % 2 == 1){
                count++;
            }
        }
    }
    return count;
}

