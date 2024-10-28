    import java.util.*;
    import java.lang.*;

    class Solution  {
        public List<Integer> uniqueDigits(List<Integer> x) {
            List<Integer> result = new ArrayList<>();
            for (Integer num : x) {
                if (!hasEvenDigit(num)) {
                    result.add(num);
                }
            }
            Collections.sort(result);
            return result;
        }

        private boolean hasEvenDigit(Integer num) {
            while (num > 0) {
                if ((num % 10) % 2 == 0) {
                    return true;
                }
                num /= 10;
            }
            return false;
        }
    }
