
// The function above is not correct because it uses integer division, which truncates the result.
// Instead of the correct sequence: 1, 3, 2, 8, 13, 21, 34, 55, ...
// the function returns: 1, 3, 2, 8, 4, 11, 19, 33, ...

// The correct sequence is:
// 1, 3, 2, 8, 13, 21, 34, 55, 89, ...
// It can be computed using the formula:
// Tri(n) = Tri(n-1) + Tri(n-2) + Tri(n-3)
// The first 10 terms of the sequence are: 1, 3, 2, 8, 13, 21, 34, 55, 89, 144
