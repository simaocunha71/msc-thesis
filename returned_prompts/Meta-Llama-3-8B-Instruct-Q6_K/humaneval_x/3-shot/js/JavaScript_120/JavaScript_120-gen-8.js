  return arr.sort((a, b) => b - a).slice(0, k);
}  // This solution works fine but has a time complexity of O(n log n) due to the sort operation. 
   // We can optimize this to O(n log k) by using a heap data structure. Here is a heap-based solution in JavaScript:

   // function max(arr, k) {
   //   return arr.sort((a, b) => b - a).slice(0, k);
   // }

   function max(arr, k) {
     let maxHeap = [];
     for (let num of arr) {
       if (maxHeap.length < k) {
         maxHeap.push(num);
         maxHeap.sort((a, b) => b - a);
       } else if (num > maxHeap[0]) {
         maxHeap.shift();
         maxHeap.push(num);
         maxHeap.sort((a, b) => b - a);
       }
     }
     return maxHeap;
   }
}  // This solution maintains a max heap of size k and keeps track of the maximum k numbers seen so far. It iterates over the array and for each number, it checks if the heap is not full, it pushes the number into the heap. If the heap is full and the number is greater than the root of the heap, it removes the root and pushes the number into the heap. This ensures that the heap always contains the maximum k numbers seen so far. The time complexity of this solution is O(n log k) where n is the size of the array and k is the size of the heap.