        int oddCount1 = 0, oddCount2 = 0;
        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 != 0) {
                oddCount1++;
            }
            if (lst2.get(i) % 2 != 0) {
                oddCount2++;
            }
        }
        return oddCount1 <= oddCount2 ? "YES" : "NO";
    }
}

Explanation:
The logic behind the solution is to count the number of odd numbers in both lists.
If there are more odd numbers in the second list (lst2), then it is possible to make all the elements in lst1 even.
Therefore, if the count of odd numbers in lst1 is less than or equal to the count of odd numbers in lst2, return "YES". Otherwise, return "NO".
This solution assumes that the lists have the same length.
*/

// Test case 1
List<Integer> lst1 = Arrays.asList(1, 2, 3, 4);
List<Integer> lst2 = Arrays.asList(1, 2, 3, 4);
System.out.println(exchange(lst1, lst2));  // Expected: "YES"

// Test case 2
lst1 = Arrays.asList(1, 2, 3, 4);
lst2 = Arrays.asList(1, 5, 3, 4);
System.out.println(exchange(lst1, lst2));  // Expected: "NO"

// Test case 3
lst1 = Arrays.asList(2, 4, 6, 8);
lst2 = Arrays.asList(1, 2, 3, 4);
System.out.println(exchange(lst1, lst2));  // Expected: "YES"

// Test case 4
lst1 = Arrays.asList(1, 3, 5, 7);
lst2 = Arrays.asList(