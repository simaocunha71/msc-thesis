public class Solution {
    public boolean monotonic(List<Integer> l) {
        boolean increasing = true;
        boolean decreasing = true;
        for (int i = 1; i < l.size(); i++) {
            if (l.get(i) < l.get(i - 1)) {
                decreasing = false;
            }
            if (l.get(i) > l.get(i - 1)) {
                increasing = false;
            }
        }
        return increasing || decreasing;
    }
}