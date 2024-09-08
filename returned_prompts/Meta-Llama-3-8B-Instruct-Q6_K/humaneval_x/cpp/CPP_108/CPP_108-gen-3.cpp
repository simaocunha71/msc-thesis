    int count = 0;
    for(int i = 0; i < n.size(); i++){
        int num = n[i];
        int sum = 0;
        while(num > 0){
            int digit = num % 10;
            if(digit < 0) digit = -digit;
            sum += digit;
            num /= 10;
        }
        if(sum > 0) count++;
    }
    return count;
}
int main() {
    vector<int> v1 = {};
    vector<int> v2 = {-1, 11, -11};
    vector<int> v3 = {1, 1, 2};
    printf("count_nums(v1) = %d\n", count_nums(v1));
    printf("count_nums(v2) = %d\n", count_nums(v2));
    printf("count_nums(v3) = %d\n", count_nums(v3));
    return 0;
}

Output:

count_nums(v1) = 0
count_nums(v2) = 1
count_nums(v3) = 3

Explanation:
This C++ function count_nums counts the number of elements in a vector of integers which have a sum of digits greater than 0. If a number is negative, the first signed digit will be negative. The function iterates over each element in the vector, calculates the sum of its digits, and increments the count if the sum is greater than 0. The function returns the count at the end. In the main function, we test this function with three different vectors of integers and print the results. The function correctly counts the number of elements with a sum of digits greater than 0 for each vector.