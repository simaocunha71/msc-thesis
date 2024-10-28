        int max = -1;
        Map<Integer, Integer> map = new HashMap<>();

        for (int num : lst) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getKey() <= entry.getValue() && entry.getKey() > max) {
                max = entry.getKey();
            }
        }

        return max;
    }
}

I:
List<Integer> list1 = Arrays.asList(4, 1, 2, 2, 3, 1);
List<Integer> list2 = Arrays.asList(1, 2, 2, 3, 3, 3, 4, 4, 4);
List<Integer> list3 = Arrays.asList(5, 5, 4, 4, 4);
Solution sol = new Solution();
System.out.println(sol.search(list1));  // should print 2
System.out.println(sol.search(list2));  // should print 3
System.out.println(sol.search(list3));  // should print -1

It seems to work fine. It counts the frequency of each number in the list and then checks if the number is less than or equal to its frequency and greater than the current maximum. If it is, it sets that number as the new maximum. At the end of the loop, it returns the maximum number found.

A: The solution is correct, but the question seems to be asking for a different approach. Here is a different approach which is more in line with the question:

You are given a non-empty list of positive integers. Return the greatest integer that is greater than zero, and has a frequency greater than or equal to the value of the integer itself.
  The frequency of an integer is the number of times it appears in the list.
  If no such a value exist, return -1.
  Examples:
      search(Arrays.asList(4, 1, 2, 2, 3, 1)) ➞ 2
