/*
    Solution 1:

    Time Complexity: O(k)
    Space Complexity: O(1)

    Steps:
    1. Initialize sum to 0
    2. Iterate through the first k elements of arr
        - If the element has at most two digits, add it to sum
    3. Return sum

    Example:
    arr = {111,21,3,4000,5,6,7,8,9}, k = 4
    sum = 0
    for i = 0 to 4
        if arr[i] <= 99
            sum = sum + arr[i]
    sum = 24

*/

int sum = 0;
for(int i=0;i<k;i++){
    if(arr[i]<=99){
        sum = sum + arr[i];
    }
}
return sum;
}

/*
B:
    Solution 2:

    Time Complexity: O(k)
    Space Complexity: O(k)

    Steps:
    1. Initialize a vector of integers, digits, to store the digits of each element
    2. Initialize sum to 0
    3. Iterate through the first k elements of arr
        - Convert each element to a string and store it in digits
        - If the length of the string is at most 2, add the element to sum
    4. Return sum

    Example:
    arr = {111,21,3,4000,5,6,7,8,9}, k = 4
    digits = []
    sum = 0
    for i = 0 to 4
        digits = to_string(arr[i])
        if len(digits) <= 2
            sum = sum + arr[i]
    sum = 24

*/

vector<int> digits;
int sum = 0;
for(int i=0;i<k;i++){
    digits = to_string(arr[i]);
    if(digits.size()<=2){
        sum = sum + arr[i];
    }
}
return sum;

}

/*
C:
    Solution 3:

    Time Complexity: O(k)
    Space Complexity: O(k)

    Steps:
    1. Initialize a vector of integers, digits, to store the digits of each element
    2. Initialize sum to 0
    3. Iterate through the first k elements of arr
        - Convert each element to a string and store it in digits
        - If the length of the string is