        List<Integer> interspersed = new ArrayList<>();
        for (int i = 0; i < numbers.size(); i++) {
            interspersed.add(numbers.get(i));
            if (i < numbers.size() - 1) {
                interspersed.add(delimiter);
            }
        }
        return interspersed;
    }

}

The solution is correct and it satisfies the problem statement. This solution will add each number in the list to the new list and then add the delimiter. If it is not the last number in the list, it will add the delimiter after the number.

This code takes in a list of integers and a delimiter integer. It then creates a new list and adds each number from the original list and the delimiter to the new list. If it is not the last number in the original list, it adds the delimiter after the number. 

This code is efficient as it only loops through the list once, adding each number and delimiter to the new list in turn. It runs in O(n) time where n is the size of the input list.

The space complexity is also O(n) as it creates a new list that is the same size as the input list.

This code is correct and will work as expected.

You can use this code in your Java program.

*/

// test the intersperse method
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.intersperse(Arrays.asList(1, 2, 3), 4));
        // Output: [1, 4, 2, 4, 3]

        System.out.println(solution.intersperse(Collections.emptyList(), 4));
        // Output: []
    }
}


































































