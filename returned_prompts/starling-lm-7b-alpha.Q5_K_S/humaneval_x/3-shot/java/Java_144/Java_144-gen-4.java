        int x_numerator = Integer.parseInt(x.substring(0, x.indexOf('/')));
        int x_denominator = Integer.parseInt(x.substring(x.indexOf('/') + 1));
        int n_numerator = Integer.parseInt(n.substring(0, n.indexOf('/')));
        int n_denominator = Integer.parseInt(n.substring(n.indexOf('/') + 1));

        int lcm = (x_numerator * n_denominator) / gcd(x_numerator, n_denominator);
        int numerator = (x_numerator * n_denominator) / lcm;
        int denominator = lcm;

        return numerator % denominator == 0;
    }

    private int gcd(int a, int b) {
        if (a < b) {
            return gcd(b, a);
        }
        if (a % b == 0) {
            return b;
        } else {
            return gcd(b, a % b);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.simplify("1/5", "5/1"));
        System.out.println(solution.simplify("1/6", "2/1"));
        System.out.println(solution.simplify("7/10", "10/2"));
    }
}
```