  return 9 ** (n - 1) + 9 * (Math.pow(10, n - 1));
}
// Note: The above solution assumes that the problem is asking for the count
// of numbers that start or end with 1, not both. If the problem is asking
// for the count of numbers that start and end with 1, the solution would be
// different. For example:
// return 9 ** (n - 2);
// This solution would count the numbers that start and end with 1.