
The reason for this is that `std::sort` is a stable sorting algorithm.

Stable: The order of equal elements is maintained.

The sorting algorithm guarantees that the order of equal elements in the original vector will be the same as the order of equal elements in the sorted vector.

In the first case, the vector `res` is sorted before returning it. If