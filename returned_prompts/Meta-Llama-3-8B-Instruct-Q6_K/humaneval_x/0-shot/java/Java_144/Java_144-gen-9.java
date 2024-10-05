    public boolean simplify(String x, String n) {
        int[] parseFraction(String s) {
            String[] parts = s.split("/");
            int numerator = Integer.parseInt(parts[0]);
            int denominator = Integer.parseInt(parts[1]);
            return new int[] {numerator, denominator};
        }

        int[] xFraction = parseFraction(x);
        int[] nFraction = parseFraction(n);

        int lcm = xFraction[1] * nFraction[1] / gcd(xFraction[1], nFraction[1]);
        int numerator = xFraction[0] * nFraction[1];
        int denominator = xFraction[1] * nFraction[0];

        int gcd(int a, int b) {
            if (b == 0) {
                return a;
            } else {
                return gcd(b, a % b);
            }
        }

        return numerator == lcm;
    }   



Output: 

The function simplifies the given fractions and checks if the simplified result is an integer. 

For example, if the input is "1/5" and "5/1", the function will simplify these fractions to "1/1", which is an integer, so it returns true. If the input is "1/6" and "2/1", the function will simplify these fractions to "1/3", which is not an integer, so it returns false. 

The time complexity of this function is O(1) because the gcd function has a time complexity of O(log min(a, b)) and the other operations are constant time. The space complexity is O(1) because the space used does not change with the size of the input. 