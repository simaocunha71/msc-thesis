        int sum = 0;
        for (int i = 0; i < q.size(); i++) {
            sum += q.get(i);
        }

        if (sum > w) {
            return false;
        }

        int start = 0;
        int end = q.size() - 1;
        while (start < end) {
            if (q.get(start) != q.get(end)) {
                return false;
            }
            start++;
            end--;
        }

        return true;
    }
}

The problem is solved by checking the following:
- If the sum of the weights in the list is greater than the maximum possible weight, return false.
- If the list is not a palindrome (the first element is not equal to the last element, etc.), return false.
- If both conditions are met, return true.

The time complexity of this function is O(n), where n is the size of the list, because we are traversing the list twice - once to calculate the sum and once to check if it's a palindrome. The space complexity is O(1), because we only use a few variables and don't use any additional data structures.




*/

//Test
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.willItFly(Arrays.asList(1, 2), 5)); // false
        System.out.println(sol.willItFly(Arrays.asList(3, 2, 3), 1)); // false
        System.out.println(sol.willItFly(Arrays.asList(3, 2, 3), 9)); // true
        System.out.println(sol.willItFly(Arrays.asList(3), 5)); // true
    }
}


























































