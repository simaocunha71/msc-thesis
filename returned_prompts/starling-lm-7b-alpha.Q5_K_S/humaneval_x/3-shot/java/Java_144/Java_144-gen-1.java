        int x_numerator = Integer.parseInt(x.split("/")[0]);
        int x_denominator = Integer.parseInt(x.split("/")[1]);
        int n_numerator = Integer.parseInt(n.split("/")[0]);
        int n_denominator = Integer.parseInt(n.split("/")[1]);

        int lcm = lcm(x_denominator, n_denominator);

        if (x_numerator * lcm / x_denominator == n_numerator * lcm / n_denominator) {
            return true;
        } else {
            return false;
        }
    }

    private int lcm(int a, int b) {
        return a * (b / gcd(a, b));
    }

    private int gcd(int a, int b) {
        if (a == 0) return b;
        if (b == 0) return a;
        if (a > b) return gcd(a % b, b);
        return gcd(a, b % a);
    }
}

