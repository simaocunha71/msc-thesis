    let result = [];
    let max = -Infinity;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i];
            result.push(max);
        }
    }
    return result.slice(0, k);
};

console.log(maximum([-3, -4, 5], 3)); // [-4, -3, 5]
console.log(maximum([4, -4, 4], 2)); // [4, 4]
console.log(maximum([-3, 2, 1, 2, -1, -2, 1], 1)); // [2]

*/

// I think the time complexity of this algorithm is O(n) and the space complexity is O(k), because in the worst case scenario, we will have to traverse each element in the array and the size of the result is k.

/*
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
const maximum = (nums, k) => {
    const maxHeap = new MaxHeap(nums, k);
    return maxHeap.heap;
};

class MaxHeap {
    constructor(nums, k) {
        this.heap = [...nums];
        this.heap.sort((a, b) => b - a);
        this.heap = this.heap.slice(0, k);
    }
}

console.log(maximum([-3, -4, 5], 3)); // [-4, -3, 5]
console.log(maximum([4, -4, 4], 2)); // [4, 4]
console.log(maximum([-3, 2, 1, 2, -1, -2, 1], 1)); // [2]


// I think the time complexity of this algorithm is O(nlogk) and the space complexity is O(k), because we have to sort the array and the size of the result is k.














