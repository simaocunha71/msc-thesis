        int sum = 0;
        int prod = 1;

        for(int num : numbers){
            sum += num;
            prod *= num;
        }

        return Arrays.asList(sum, prod);
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.sumProduct(new ArrayList<Integer>()));
        System.out.println(sol.sumProduct(Arrays.asList(1, 2, 3, 4)));
    }
}

Explanation:
This solution takes a list of integers as input. It initializes two variables, sum and prod, to 0 and 1 respectively. Then it iterates over the list using a for-each loop. For each integer, it adds the integer to sum and multiplies prod by the integer. Finally, it returns a new list containing the values of sum and prod.

The time complexity of this solution is O(n), where n is the length of the list, since it iterates over the list once. The space complexity is O(1), since it uses a constant amount of space to store the sum and prod variables and the output list.

Note that the import statements at the start of the code are necessary to use the List, Arrays, and ArrayList classes.

The main function is just to test the sumProduct method with some inputs.

The output of this program will be:
[0, 1]
[10, 24]
*/

// End of the code.
<jupyter_output>
<empty_output>
<jupyter_text>
