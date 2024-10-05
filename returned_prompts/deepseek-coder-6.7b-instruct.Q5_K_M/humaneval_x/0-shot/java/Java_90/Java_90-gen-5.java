        if (lst.isEmpty() || lst.size() < 2) {
            return Optional.empty();
        }

        int smallest = Integer.MAX_VALUE;
        int secondSmallest = Integer.MAX_VALUE;

        for (Integer num : lst) {
            if (num < smallest) {
                secondSmallest = smallest;
                smallest = num;
            } else if (num > smallest && num < secondSmallest) {
                secondSmallest = num;
            }
        }

        if (secondSmallest == Integer.MAX_VALUE) {
            return Optional.empty();
        }

        return Optional.of(secondSmallest);
    }
}

*/

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.nextSmallest(Arrays.asList(1, 2, 3, 4, 5))); // 2
        System.out.println(sol.nextSmallest(Arrays.asList(5, 1, 4, 3, 2))); // 2
        System.out.println(sol.nextSmallest(Arrays.asList())); // Optional.empty
        System.out.println(sol.nextSmallest(Arrays.asList(1, 1))); // Optional.empty
    }
}

/*
This program defines a method nextSmallest() that finds the second smallest number in a given list.
It first checks if the list is empty or contains fewer than two elements, in which case it returns an empty Optional.
It then initializes two variables, smallest and secondSmallest, to represent the smallest and second smallest numbers.
The program iterates through the list, updating smallest and secondSmallest as necessary.
If secondSmallest remains unchanged (which means no second smallest number was found), the program returns an empty Optional.
Otherwise, it returns the second smallest number as an Optional.
*/

// Time complexity: O(n)
// Space complexity: O(1)

// Output:
// 2
// 2
// Optional.empty
// Optional.empty

/*
This program works by iterating through the list and keeping