    return arr.slice().sort((a, b) => b - a).slice(0, k);

};


/*
The time complexity of this solution is O(nlogn), where n is the length of arr.
The space complexity is O(n), where n is the length of arr.

In this solution, we first convert the array to a new array using slice() method to avoid modifying the original array. Then we use sort() method to sort the array in descending order. Finally, we use slice() method to get the first k numbers of the sorted array.

This solution can be optimized by not using sort() method. Instead, we can use Math.max() method to find the maximum k numbers in the array. However, the time complexity of this optimized solution is still O(nlogn) and the space complexity is O(1).

Here is the optimized solution:

const maximum = (arr, k) => {
    const max = Math.max(...arr);
    const res = [];

    for (let i = 0; i < k; i++) {
        for (let j = 0; j < arr.length; j++) {
            if (arr[j] === max) {
                res.push(arr[j]);
                break;
            }
        }
    }

    return res;
};


The time complexity of this optimized solution is O(n * k) and the space complexity is O(k).

In this optimized solution, we first find the maximum number in the array using Math.max() method. Then we use two nested loops to find the maximum k numbers in the array. We push each maximum number to the result array and break the inner loop. Finally, we return the result array.

This optimized solution is more efficient in terms of time complexity and space complexity than the original solution. However, it is more complex and harder to understand.

*/

*/






































































