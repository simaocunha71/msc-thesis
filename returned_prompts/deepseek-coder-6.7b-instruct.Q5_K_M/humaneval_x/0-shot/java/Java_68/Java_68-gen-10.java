        List<Integer> evenList = new ArrayList<Integer>();
        List<Integer> result = new ArrayList<Integer>();
        int min = Integer.MAX_VALUE;

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0) {
                evenList.add(arr.get(i));
                if (arr.get(i) < min) {
                    min = arr.get(i);
                }
            }
        }

        if (evenList.size() == 0) {
            return result;
        }

        int index = evenList.indexOf(min);
        result.add(min);
        result.add(index);

        return result;
    }
}

// Given an array of integers representing a branch of a tree, your task is to pluck one of the nodes and return it.
// The plucked node should be the node with the smallest even value.
// If there are multiple nodes with the same smallest even value, return the node that has the smallest index.
// If there are no even values or the given array is empty, return an empty list.

// Example 1:
// Input: [4,2,3]
// Output: [2, 1]
// Explanation: 2 has the smallest even value, and 2 has the smallest index.

// Example 2:
// Input: [1,2,3]
// Output: [2, 1]
// Explanation: 2 has the smallest even value, and 2 has the smallest index.

// Example 3:
// Input: []
// Output: []

// Example 4:
// Input: [5, 0, 3, 0, 4, 2]
// Output: [0, 1]
// Explanation: 0 is the smallest value, but there are two zeros, so we will choose the first zero, which has the smallest index.

// Constraints:
// 1 ≤ nodes.length ≤ 10000
// 0 ≤ node.value ≤ 10000
