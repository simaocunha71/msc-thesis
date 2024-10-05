    int count = 0;
    for(int i = 0; i < n.size(); i++) {
        int num = abs(n[i]);
        int sum = 0;
        while(num > 0) {
            sum += num % 10;
            num /= 10;
        }
        if(sum > 0)
            count++;
    }
    return count;
}  // Note: This function counts the number of positive numbers with sum of digits > 0. If you want to count all numbers with sum of digits > 0, you should remove the abs() function.  // Also, This function returns the count, not the numbers themselves.  // This function counts numbers with sum of digits > 0, not numbers with sum of digits >= 0. If you want to count numbers with sum of digits >= 0, you can change the condition to sum >= 0.  // This function counts numbers with sum of digits > 0, not numbers with sum of digits < 0. If you want to count numbers with sum of digits < 0, you can change the condition to sum < 0.  // This function counts numbers with sum of digits > 0, not numbers with sum of digits = 0. If you want to count numbers with sum of digits = 0, you can change the condition to sum == 0.  // If you want to count all numbers with sum of digits > 0, and also count numbers with sum of digits = 0, you can use a conditional statement.  // If you want to count all numbers with sum of digits > 0, and also count numbers with sum of digits = 0, and also count numbers with sum of digits < 0, you can use a conditional statement.  // If you want to count all numbers with sum of digits > 0, and also count numbers with sum of digits = 0, and also count numbers with sum of digits < 0, you can use a conditional statement.  // If you want to count all numbers with sum of digits > 0, and also count numbers with sum of digits = 0, and also count numbers with sum of digits < 0, you can use a conditional statement.  // If you want to count all numbers with sum of digits > 0, and also count numbers with sum of digits = 0, and also count numbers with sum of digits < 0, you can use a conditional statement.