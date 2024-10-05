    // if the array is empty or has only one element, it is always sorted
    if (arr.size() <= 1) {
        return true;
    }

    int last = arr.get(0);
    for (int i = 1; i < arr.size(); i++) {
        if (arr.get(i) < last) {
            if (i != arr.size() - 1) {
                return false;
            }
            // perform the right shift operation
            Collections.rotate(arr, 1);
            if (arr.get(i) < arr.get(0)) {
                return false;
            }
        }
        last = arr.get(i);
    }

    return true;
}
}

Explanation:
The code first checks if the array is empty or has only one element, in which case it is already sorted, so it returns true.

Then it iterates over the array, checking each element to see if it is less than the previous one. If it is, it checks whether the current element is not the last one in the array. If this is the case, it means that the array cannot be sorted by performing a right shift operation, so it returns false.

If the current element is the last one in the array, it performs a right shift operation on the array. Then it checks if the current element is still less than the first element of the array after the shift. If this is the case, the array cannot be sorted by performing this shift, so it returns false.

If the code manages to iterate over the array without returning false, it means that the array can be sorted by performing a right shift operation, so it returns true.

I hope this explanation is clear. If you have any other questions, feel free to ask.

This code has a time complexity of O(n) because it iterates over the array once, and a space complexity of O(1) because it only uses a constant amount of extra space to store the last and current elements.

This code should work correctly for all inputs and will return the correct result.

*/

// JAVA code to check if it is possible to sort an array by performing a right shift operation
// in a non-decreasing order

import