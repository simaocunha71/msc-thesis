        int left = 0, right = q.size() - 1, sum = 0;
        while (left < right) {
            sum += q.get(left++) + q.get(right--);
        }
        sum += q.get(left);

        return sum <= w && isPalindrome(q);
    }

    private boolean isPalindrome(List<Integer> list) {
        int left = 0, right = list.size() - 1;
        while (left < right) {
            if (list.get(left++) != list.get(right--)) return false;
        }
        return true;
    }
}



public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(s.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(s.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(s.truncateNumber(3.5));
        System.out.println(s.willItFly(Arrays.asList(1, 2), 5));
        System.out.println(s.willItFly(Arrays.asList(3, 2, 3), 1));
        System.out.println(s.willItFly(Arrays.asList(3, 2, 3), 9));
        System.out.println(s.willItFly(Arrays.asList(3), 5));
    }
}
```