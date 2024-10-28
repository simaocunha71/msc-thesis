    public List<String> totalMatch(List<String> lst1, List<String> lst2) {
        int sum1 = 0, sum2 = 0;
        for (String s : lst1) {
            sum1 += s.length();
        }
        for (String s : lst2) {
            sum2 += s.length();
        }
        if (sum1 < sum2) {
            return lst1;
        } else if (sum2 < sum1) {
            return lst2;
        } else {
            return lst1;
        }
    }  // time complexity O(n)
    // space complexity O(1) as the space complexity is constant. The space complexity is O(1) as it is not dependent on the input size. It is fixed and constant. 

    // Here's the breakdown of the above code:
    // 1. We initialize two variables sum1 and sum2 to 0. These variables will be used to store the total number of characters in each list.
    // 2. We iterate through each string in lst1 and add its length to sum1.
    // 3. We iterate through each string in lst2 and add its length to sum2.
    // 4. We compare sum1 and sum2. If sum1 is less than sum2, we return lst1. If sum2 is less than sum1, we return lst2. If sum1 is equal to sum2, we return lst1 (as per the problem statement).
    // 5. The function returns the list with the total number of characters less than the other list. If the two lists have the same number of characters, it returns the first list. 

    // This solution has a time complexity of O(n) because we iterate through each string in both lists once. The space complexity is O(1) because we only use a constant amount of space to store the sums and the return value.  // This solution has a time complexity of O(n) because we iterate through each string in both lists once. The space complexity is O(1) because we only use a constant amount of space to store the sums and the return value.  // This solution has a time complexity of O(n) because we iterate through each string in both lists once. The space complexity is O(1) because we only use a constant amount of space to store the sums and the return value.  // This solution has a time complexity of O(n) because