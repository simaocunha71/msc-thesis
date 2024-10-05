import java.util.*;

class Solution {
    public List<Integer> orderByPoints(List<Integer> nums) {
        Comparator<Integer> cmp = new Comparator<Integer>() {
            public int compare(Integer x, Integer y) {
                int a = digitsSum(x);
                int b = digitsSum(y);
                if (a != b) return a - b;
                return x.compareTo(y);
            }
        };
        List<Integer> result = new ArrayList<Integer>(nums);
        Collections.sort(result, cmp);
        return result;
    }

    private int digitsSum(int n) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.orderByPoints(Arrays.asList(1, 11, -1, -11, -12)));
    }
}
