        List<Integer> result = new ArrayList<>();
        int max = Integer.MIN_VALUE;
        for (Integer number : numbers) {
            if (number > max) {
                max = number;
            }
            result.add(max);
        }
        return result;
    }
}

// Driver code
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        List<Integer> numbers = Arrays.asList(1, 2, 3, 2, 3, 4, 2);
        System.out.println(sol.rollingMax(numbers));
    }
}

This code will iterate through the list and keep track of the maximum element found so far. For each element in the list, it checks if the current element is greater than the maximum value. If it is, it updates the maximum value. It then adds the maximum value to the result list.
*/

// Solution 2:
/*
