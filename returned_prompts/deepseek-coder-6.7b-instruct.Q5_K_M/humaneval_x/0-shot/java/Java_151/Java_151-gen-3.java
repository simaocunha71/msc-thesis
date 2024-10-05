        int sum = 0;
        for(Object num : lst){
            if(num instanceof Integer && (int)num % 2 != 0 && (int)num > 0){
                sum += Math.pow((int)num, 2);
            }
        }
        return sum;
    }
}

I:
System.out.println(new Solution().doubleTheDifference(Arrays.asList(1, 3, 2, 0)));
System.out.println(new Solution().doubleTheDifference(Arrays.asList(-1, -2, 0)));
System.out.println(new Solution().doubleTheDifference(Arrays.asList(9, -2)));
System.out.println(new Solution().doubleTheDifference(Arrays.asList(0)));
System.out.println(new Solution().doubleTheDifference(Arrays.asList()));

O:
10
0
81
0
0
 */

public class Main {
    public static void main(String[] args) {
        System.out.println(new Solution().doubleTheDifference(Arrays.asList(1, 3, 2, 0))); // 10
        System.out.println(new Solution().doubleTheDifference(Arrays.asList(-1, -2, 0))); // 0
        System.out.println(new Solution().doubleTheDifference(Arrays.asList(9, -2))); // 81
        System.out.println(new Solution().doubleTheDifference(Arrays.asList(0))); // 0
        System.out.println(new Solution().doubleTheDifference(Arrays.asList())); // 0
    }
}

// 10
// 0
// 81
// 0
// 0
// 0
// 81
// 0
// 0
// 10
// 0
// 81
// 0
// 0
// 10
// 0
// 81
// 0
// 0
// 10
// 0
// 81
//