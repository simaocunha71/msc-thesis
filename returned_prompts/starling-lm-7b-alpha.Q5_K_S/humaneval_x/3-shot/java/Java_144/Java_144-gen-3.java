        int x_numerator = Integer.parseInt(x.split("/")[0]);
        int x_denominator = Integer.parseInt(x.split("/")[1]);
        int n_numerator = Integer.parseInt(n.split("/")[0]);
        int n_denominator = Integer.parseInt(n.split("/")[1]);

        int lcm = lcm(x_denominator, n_denominator);

        return (lcm / x_denominator) * x_numerator == (lcm / n_denominator) * n_numerator;
    }

    public int lcm(int a, int b) {
        return a * b / gcd(a, b);
    }

    public int gcd(int a, int b) {
        if (a == 0) return b;
        return gcd(b % a, a);
    }
}

