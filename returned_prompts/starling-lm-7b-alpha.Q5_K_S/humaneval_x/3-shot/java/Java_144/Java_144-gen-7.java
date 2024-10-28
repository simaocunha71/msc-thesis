        int x_numerator = Integer.parseInt(x.split("/")[0]);
        int x_denominator = Integer.parseInt(x.split("/")[1]);

        int n_numerator = Integer.parseInt(n.split("/")[0]);
        int n_denominator = Integer.parseInt(n.split("/")[1]);

        int lcm = lcm(x_denominator, n_denominator);
        int gcd = gcd(x_numerator, lcm);
        int new_numerator = x_numerator / gcd;
        return (n_numerator * new_numerator) % lcm == 0;
    }

    private int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    private int lcm(int a, int b) {
        return a * (b / gcd(a, b));
    }
}

