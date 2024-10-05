import java.util.*;
import java.lang.*;

class Solution {
    public String sortNumbers(String numbers) {
        String[] numberals = numbers.split(" ");
        Arrays.sort(numberals);
        return String.join(" ", numberals);
    }
}