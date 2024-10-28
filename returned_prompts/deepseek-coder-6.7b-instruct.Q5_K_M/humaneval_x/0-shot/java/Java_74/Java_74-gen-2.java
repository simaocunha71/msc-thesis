        int sum1 = 0;
        int sum2 = 0;

        for (String s : lst1) {
            sum1 += s.length();
        }

        for (String s : lst2) {
            sum2 += s.length();
        }

        if (sum1 < sum2) {
            return lst1;
        } else if (sum2 < sum1) {
            return lst2;
        } else {
            return lst1;
        }
    }
}

*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.totalMatch(Arrays.asList(), Arrays.asList())); // -> []
        System.out.println(solution.totalMatch(Arrays.asList("hi", "admin"), Arrays.asList("hI", "Hi"))); // -> “hI”, “Hi”]
        System.out.println(solution.totalMatch(Arrays.asList("hi", "admin"), Arrays.asList("hi", "hi", "admin", "project"))); // -> ["hi", "admin"]
        System.out.println(solution.totalMatch(Arrays.asList("hi", "admin"), Arrays.asList("hI", "hi", "hi"))); // -> ["hI", "hi", "hi"]
        System.out.println(solution.totalMatch(Arrays.asList("4"), Arrays.asList("1", "2", "3", "4", "5"))); // -> ["4"]
    }
}

/*
