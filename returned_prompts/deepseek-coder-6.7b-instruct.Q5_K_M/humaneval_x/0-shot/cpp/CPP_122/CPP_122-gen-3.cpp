    int sum = 0;
    for(int i = 0; i < k; i++){
        if(arr[i] >= 0 && arr[i] <= 99){
            sum += arr[i];
        }
    }
    return sum;
}

int main(){
    vector<int> arr = {111,21,3,4000,5,6,7,8,9};
    int k = 4;
    printf("%d", add_elements(arr, k));
    return 0;
}
*/

#include <iostream>
#include <vector>

int add_elements(std::vector<int> arr, int k) {
    int sum = 0;
    for(int i = 0; i < k; i++) {
        if(arr[i] >= 0 && arr[i] <= 99){
            sum += arr[i];
        }
    }
    return sum;
}

int main() {
    std::vector<int> arr = {111,21,3,4000,5,6,7,8,9};
    int k = 4;
    std::cout << add_elements(arr, k);
    return 0;
}

/*
In the given problem, we have to return the sum of the elements which have at most two digits from the first k elements of a given array.

For solving this problem, we can use a simple loop to traverse the first k elements of the array. If an element has at most two digits, we add it to the sum.

Finally, we return the sum.

This problem can be solved using C++. We can use a for loop to iterate over the first k elements of the array. Then, we use an if statement to check if the current element has at most two digits. If it does, we add it to the sum. Finally, we return the sum.

The time complexity of this solution is O(k), where k is the given number. The space complexity is O(1), as we are not using any extra space that scales with the input size.
*/

// @lc code=end

//002_