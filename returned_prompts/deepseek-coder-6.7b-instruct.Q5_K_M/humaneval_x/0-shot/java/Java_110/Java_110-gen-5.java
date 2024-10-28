        int oddCountLst1 = 0;
        int evenCountLst2 = 0;

        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 != 0) {
                oddCountLst1++;
            }
        }

        for (int i = 0; i < lst2.size(); i++) {
            if (lst2.get(i) % 2 == 0) {
                evenCountLst2++;
            }
        }

        if (oddCountLst1 > evenCountLst2) {
            return "NO";
        } else {
            return "YES";
        }
    }
}

This problem can be solved by counting the number of odd numbers in lst1 and even numbers in lst2. If the number of odd numbers in lst1 is greater than the number of even numbers in lst2, it is not possible to make lst1 a list of only even numbers by exchanging elements between lst1 and lst2. Therefore, return "NO". Otherwise, return "YES".

The time complexity of this solution is O(n) because we traverse both lst1 and lst2 once. The space complexity is O(1) because we only use a constant amount of space to store the counts of odd numbers in lst1 and even numbers in lst2.

Please note that you should replace `Arrays.asList` with `List.of` if you are using Java 9 or later.

I:
print(Solution().exchange(List.of(1, 2, 3, 4), List.of(1, 2, 3, 4)))
print(Solution().exchange(List.of(1, 2, 3, 4), List.of(1, 5, 3, 4)))

O:
YES
NO

Explanation:
In the first case, lst1 already contains all even numbers, so the answer is "YES".
In the second case, we cannot exchange elements between lst1 and lst2 to make all elements of lst1 to be even,