        boolean increasing = true;
        boolean decreasing = true;

        for (int i = 0; i < l.size() - 1; i++) {
            if (l.get(i) > l.get(i + 1)) {
                increasing = false;
            }
            if (l.get(i) < l.get(i + 1)) {
                decreasing = false;
            }
        }

        return increasing || decreasing;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.monotonic(Arrays.asList(1, 2, 4, 20))); // true
        System.out.println(s.monotonic(Arrays.asList(1, 20, 4, 10))); // false
        System.out.println(s.monotonic(Arrays.asList(4, 1, 0, -10))); // true
    }
}

Explanation:
The solution works by checking if the list is either increasing or decreasing.
If the list is increasing, `increasing` becomes `false`, if the list is decreasing, `decreasing` becomes `false`.
Finally, it returns `true` if either `increasing` or `decreasing` is `true`. Otherwise, it returns `false`.
This solution works by iterating over the list and checking if the current element is greater than the next element.
If it is, `increasing` becomes `false`.
Similarly, it checks if the current element is less than the next element, if it is, `decreasing` becomes `false`.
If both `increasing` and `decreasing` remain `true` throughout the iteration, it returns `true`, indicating that the list is either monotonically increasing or decreasing. Otherwise, it returns `false`.
*/

// The solution provided is correct and works as expected. It checks if the list is either monotonically increasing or decreasing.
// This solution has a time complexity of O(n), where n is the size of the list, as it iterates over the list once.
// The space complexity is O(1), as