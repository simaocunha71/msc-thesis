
The time complexity of this program is O(N^2) because in the worst case, we need to move all the elements to the first position.

As for the space complexity, it is O(1) because we only use a fixed number of variables in the program.

However, it is worth noting that if the number of elements in the array is small, it may be more efficient to use a sorting algorithm. For example, if the number of elements in the array is less than 15, it is faster to use the insertion sort algorithm (time complexity O(N^2) ), and if the number of elements in the array is less than 7, it is faster to use the selection sort algorithm (time complexity O(N^2)).

In addition, it is worth noting that if the array is sorted in increasing order, we can find the maximum element in O(N) time. If the maximum element is not at the end, we can move it to the end in O(N) time. Then, we can find the maximum element again and move it to the end. Repeat this process until all elements are in the correct order.

Overall, the program's time and space complexity are both O(N^2), but the specific time complexity depends on the number of elements in the array and the distribution of these elements