import java.util.*;

class Solution {
    public Optional<Integer> prodSigns(List<Integer> arr) {
        int result = 0;
        int product = 1;
        for (int i = 0; i < arr.size(); i++) {
            int num = arr.get(i);
            int sign = num >= 0 ? 1 : -1;
            product *= sign;
            result += Math.abs(num) * product;
        }
        return result == 0 ? Optional.empty() : Optional.of(result);
    }
}

B:
import java.util.*;

class Solution {
    public Optional<Integer> prodSigns(List<Integer> arr) {
        int result = 0;
        int product = 1;
        for (int num : arr) {
            int sign = num >= 0 ? 1 : -1;
            product *= sign;
            result += Math.abs(num) * product;
        }
        return result == 0 ? Optional.empty() : Optional.of(result);
    }
}

C:
import java.util.*;

class Solution {
    public Optional<Integer> prodSigns(List<Integer> arr) {
        int result = 0;
        int product = 1;
        for (int num : arr) {
            int sign = (num >= 0) ? 1 : -1;
            product *= sign;
            result += Math.abs(num) * product;
        }
        return result == 0 ? Optional.empty() : Optional.of(result);
    }
}

D:
import java.util.*;

class Solution {
    public Optional<Integer> prodSigns(List<Integer> arr) {
        int result = 0;
        int product = 1;
        for (int num : arr) {
            int sign = (num >= 0) ? 1 : -1;
            product *= sign;
            result += Math.abs(num) * product;
        }
        return Optional.of(result);
    }
}

E:
import java.util.*;

class Solution {