        List<Integer> result = new ArrayList<Integer>();
        int max = Integer.MIN_VALUE;
        for (int num : numbers) {
            if (num > max) {
                max = num;
            }
            result.add(max);
        }
        return result;
    }
}

This solution iterates over the given list of integers, compares each number with the current maximum. If the number is bigger, it becomes the new maximum and is added to the result list. If the number is smaller or equal, the current maximum is added to the result list.

The time complexity of this solution is O(n), where n is the size of the given list, because it scans the list of numbers once. The space complexity is also O(n), because it uses a list to store the result.

This solution assumes that the input list of integers is not empty. If the list can be empty, you should add a special check at the beginning of the function.
*/

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.rollingMax(Arrays.asList(1, 2, 3, 2, 3, 4, 2)));
    }
}

/*
Output:
[1, 2, 3, 3, 3, 4, 4]
*/

/*
The output is correct because it represents the rolling maximum element found until each moment in the sequence.
*/

/*
This solution is efficient and handles the given problem well.
*/

/*
The time complexity of this solution is O(n) because it scans the list of numbers once. The space complexity is also O(n) because it uses a list to store the result.
*/

/*
This solution assumes that the input list of integers is not empty. If the list can be empty, you should add a special check at the beginning of the function.
*/

/*
The solution uses a simple for-each loop to iterate over the list of numbers. It compares each number with the current maximum and updates it if necessary. The maximum is then added to the result list.
*/

/*
The solution is correct and handles the problem as