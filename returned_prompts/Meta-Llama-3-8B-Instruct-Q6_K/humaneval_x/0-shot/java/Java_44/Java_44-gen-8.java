public class Solution {
    public String changeBase(int x, int base) {
        if (x == 0) {
            return "0";
        }

        StringBuilder sb = new StringBuilder();
        while (x > 0) {
            int remainder = x % base;
            if (remainder > 9) {
                sb.append((char) ('a' + remainder - 10));
            } else {
                sb.append(remainder);
            }
            x = x / base;
        }
        return sb.reverse().toString();
    }
}