        int x_numerator = Integer.parseInt(x.split("/")[0]);
        int x_denominator = Integer.parseInt(x.split("/")[1]);
        int n_numerator = Integer.parseInt(n.split("/")[0]);
        int n_denominator = Integer.parseInt(n.split("/")[1]);
        int lcm = lcm(x_denominator, n_denominator);
        return lcm % x_numerator == 0 && lcm % n_numerator == 0;
    }

    private int lcm(int a, int b) {
        return a * b / gcd(a, b);
    }

    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}

