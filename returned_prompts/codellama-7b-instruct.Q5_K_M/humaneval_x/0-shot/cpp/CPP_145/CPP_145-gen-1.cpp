
    // 1. Sort the vector of integers
    // based on the sum of their digits
    // in ascending order.
    //
    // Note: if there are several items with similar
    // sum of their digits, order them based on their
    // index in original vector.
    //
    // For example:
    // >>> order_by_points({1, 11, -1, -11, -12}) == {-1, -11, 1, -12, 11}
    // >>> order_by_points({}) == {}
    //
    // Return the sorted vector.

    // 1.1. Write a helper function which calculates
    // the sum of digits of a given integer.
    //
    // For example:
    // >>> sum_of_digits(12345) == 15
    // >>> sum_of_digits(-12345) == 15
    //
    // Return the sum of digits.
    int sum_of_digits(int x){
        if(x<0)
            x = -x;
        int sum = 0;
        while(x>0){
            sum += x%10;
            x/=10;
        }
        return sum;
    }

    // 1.2. Write a helper function which compares
    // two integers based on their sum of digits.
    //
    // For example:
    // >>> compare_by_sum_of_digits(1, -1) == false
    // >>> compare_by_sum_of_digits(1, 1) == false
    // >>> compare_by_sum_of_digits(1, 11) == true
    //
    // Return true if first integer should come before
    // the second integer in the sorted vector, false
    // otherwise.
    bool compare_by_sum_of_digits(int a, int b){
        int sum_a = sum_of_digits(a);
        int sum_b = sum_of_digits(b);
        if(sum_a == sum_b)
            return a < b