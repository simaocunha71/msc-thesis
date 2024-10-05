        List<Integer> result = new ArrayList<>();
        int smallestEvenValue = Integer.MAX_VALUE;
        int smallestEvenIndex = -1;

        for(int i = 0; i < arr.size(); i++) {
            if(arr.get(i) % 2 == 0 && arr.get(i) < smallestEvenValue) {
                smallestEvenValue = arr.get(i);
                smallestEvenIndex = i;
            }
        }

        if(smallestEvenValue != Integer.MAX_VALUE) {
            result.add(smallestEvenValue);
            result.add(smallestEvenIndex);
        }

        return result;
    }
}

This solution works by iterating over the given array and checking if the current value is an even number and if it is smaller than the smallestEvenValue. If it is, we update smallestEvenValue and smallestEvenIndex.

Finally, if we found any even numbers, we return them in a list. Otherwise, we return an empty list.

Time complexity is O(n) because we are going through the array only once, and space complexity is O(1) because we are using only a constant amount of space to store the smallest even value and its index.
*/

// Q2:
// Given an array of integers, return indices of the two numbers such that they add up to a specific target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// Example:

// Given nums = [2, 7, 11, 15], target = 9,

// Because nums[0] + nums[1] = 2 + 7 = 9,
// return [0, 1].

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            } else {
                map.put(nums