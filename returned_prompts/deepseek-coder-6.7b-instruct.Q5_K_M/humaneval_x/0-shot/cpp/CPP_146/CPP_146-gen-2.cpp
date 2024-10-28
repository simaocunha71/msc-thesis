    int count = 0;
    for(int i = 0; i < nums.size(); i++){
        if(nums[i] > 10){
            int firstDigit = abs(nums[i]/10);
            int lastDigit = abs(nums[i]%10);
            if(firstDigit%2 != 0 && lastDigit%2 != 0){
                count++;
            }
        }
    }
    return count;
}

int main() {
    vector<int> vec1 = {15, -73, 14, -15};
    printf("%d\n", specialFilter(vec1));
    vector<int> vec2 = {33, -2, -3, 45, 21, 109};
    printf("%d\n", specialFilter(vec2));
    return 0;
}

// Note: In C++, the abs() function is used to get the absolute value of a number. 
// It's important to note that if the firstDigit or lastDigit of a number is negative, 
// then the '%' operator will give the remainder of the division. 
// This is because the '%' operator in C++ is not defined for negative numbers. 
// Therefore, to get the last digit of a number, we take the absolute value of the number.

// Also, to get the first digit of a number, we divide the number by 10. 
// However, because we want the first digit before any digits, we need to take the absolute value of the result.
// Thus, firstDigit is abs(nums[i]/10) and lastDigit is abs(nums[i]%10).

// In the function, if the firstDigit and lastDigit are both odd (i.e., not divisible by 2), 
// then we increment count by 1. This is done by the condition firstDigit%2 != 0 && lastDigit%2 != 0.
// Finally, we return count.

// The time complexity of this function is O(n), where n is the size of the input vector. 
//