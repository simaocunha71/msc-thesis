        if (arr.isEmpty()) {
            return Optional.empty();
        }

        int sum = 0;
        int prodSign = 1;
        for (int num : arr) {
            if (num < 0) {
                prodSign *= -1;
            } else if (num > 0) {
                prodSign *= 1;
            } else {
                return Optional.of(0);
            }
            sum += Math.abs(num);
        }
        return Optional.of(sum * prodSign);
    }
}

Test Cases:

assertThat(solution.prodSigns(Arrays.asList(1, 2, 2, -4))).isEqualTo(Optional.of(-9));
assertThat(solution.prodSigns(Arrays.asList(0, 1))).isEqualTo(Optional.of(0));
assertThat(solution.prodSigns(Arrays.asList())).isEqualTo(Optional.empty());


A: The solution provided is correct. Here is the complete solution with test cases.

import java.util.*;
import java.lang.*;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

class Solution {
    public Optional<Integer> prodSigns(List<Integer> arr) {
        if (arr.isEmpty()) {
            return Optional.empty();
        }

        int sum = 0;
        int prodSign = 1;
        for (int num : arr) {
            if (num < 0) {
                prodSign *= -1;
            } else if (num > 0) {
                prodSign *= 1;
            } else {
                return Optional.of(0);
            }
            sum += Math.abs(num);
        }
        return Optional.of(sum * prodSign);
    }

    @Test
    public void testProdSigns() {
        Solution solution = new Solution();
        assertEquals(Optional.of(-9), solution.prodSigns(Arrays.asList(1, 2, 2, -4)));
        assertEquals(Optional.of(0), solution.prodSigns(Ar