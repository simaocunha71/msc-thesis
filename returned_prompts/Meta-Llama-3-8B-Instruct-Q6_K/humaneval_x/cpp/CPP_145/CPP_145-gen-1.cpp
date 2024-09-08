    vector<int> res;
    vector<pair<int, int>> temp;
    for(int i=0; i<nums.size(); i++){
        temp.push_back({get_sum_of_digits(nums[i]), i});
    }
    sort(temp.begin(), temp.end());
    for(int i=0; i<temp.size(); i++){
        res.push_back(nums[temp[i].second]);
    }
    return res;
}
int get_sum_of_digits(int n){
    int sum = 0;
    while(n!=0){
        sum += n%10;
        n /= 10;
    }
    return sum;
}

S:
    The function `order_by_points` takes a vector of integers as input and returns a new vector sorted based on the sum of the digits of the numbers in the input vector. If there are multiple numbers with the same sum of digits, the original order is preserved.

    In the function, a temporary vector `temp` is created to store pairs of the sum of the digits and the original index of the number. Then, the `sort` function is used to sort the `temp` vector based on the sum of the digits.

    After sorting `temp`, the original numbers are retrieved from the `nums` vector based on the sorted indices in `temp` and stored in the result vector `res`.

    The helper function `get_sum_of_digits` is used to calculate the sum of the digits of a number. It uses a while loop to iterate through the digits of the number and adds each digit to the sum.

    The time complexity of this function is O(n log n) due to the sorting operation, where n is the size of the input vector. The space complexity is O(n) for storing the temporary vector and the result vector.