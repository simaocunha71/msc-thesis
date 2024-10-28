import java.util.*;
import java.lang.*;

public class Solution {
    public static void main(String[] args) {
        // Create a Scanner object to read input from the command line
        Scanner sc = new Scanner(System.in);
        // Read the number of test cases
        int T = sc.nextInt();
        // Loop through the test cases
        for (int i = 0; i < T; i++) {
            // Read the number of apples and oranges in the basket
            int n = sc.nextInt();
            // Read the number of fruits in the basket
            int m = sc.nextInt();
            // Initialize a variable to store the number of mango fruits
            int k = 0;
            // Loop through the number of fruits in the basket
            for (int j = 0; j < m; j++) {
                // Read a fruit
                String fruit = sc.next();
                // Check if the fruit is mango
                if (fruit.equals("mango")) {
                    // Increment the number of mango fruits
                    k++;
                }
            }
            // Print the number of mango fruits in the basket
            System.out.println(k);
        }
    }
}