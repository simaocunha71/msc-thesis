        String[] parts = s.split(" ");
        int apples = Integer.parseInt(parts[0]);
        int oranges = Integer.parseInt(parts[2]);
        return n - apples - oranges;
    }
}

The code splits the input string into parts based on the spaces, and then it parses the number of apples and oranges from these parts. After that, it calculates and returns the total number of fruits in the basket by subtracting the number of apples and oranges from the total number of fruits.


Test Cases:

Input: "5 apples and 6 oranges", 19
Output: 8

Input: "0 apples and 1 oranges", 3
Output: 2

Input: "2 apples and 3 oranges", 100
Output: 95

Input: "100 apples and 1 oranges", 120
Output: 19
*/

//src/main/java/com/coderbyte/challenges/FruitDistribution.java
package com.coderbyte.challenges;

public class FruitDistribution {
    public int fruitDistribution(String s, int n) {
        String[] parts = s.split(" ");
        int apples = Integer.parseInt(parts[0]);
        int oranges = Integer.parseInt(parts[2]);
        return n - apples - oranges;
    }
}

//src/test/java/com/coderbyte/challenges/FruitDistributionTest.java
package com.coderbyte.challenges;

import com.coderbyte.challenges.FruitDistribution;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class FruitDistributionTest {
    @Test
    public void testFruitDistribution() {
        FruitDistribution fruitDistribution = new FruitDistribution();
        assertEquals(8, fruitDistribution.fruitDistribution("5 apples and 6 oranges", 19));
        assertEquals(2, fruitDistribution.fruitDistribution("0 apples and 