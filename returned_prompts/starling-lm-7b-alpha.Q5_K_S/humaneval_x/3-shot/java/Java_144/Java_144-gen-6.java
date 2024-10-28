        String[] parts = x.split("/");
        if (parts.length != 2) return false;
        String[] parts_n = n.split("/");
        if (parts_n.length != 2) return false;

        int x_numerator = Integer.parseInt(parts[0]);
        int x_denominator = Integer.parseInt(parts[1]);
        int n_numerator = Integer.parseInt(parts_n[0]);
        int n_denominator = Integer.parseInt(parts_n[1]);

        int lcm = lcm(x_denominator, n_denominator);
        int gcd = gcd(lcm, x_numerator);
        int x_new_numerator = x_numerator / gcd;
        int n_new_numerator = n_numerator / gcd;

        if (x_new_numerator * n_new_numerator % lcm == 0)
            return true;

        return false;
    }

    private int lcm(int a, int b) {
        return a * b / gcd(a, b);
    }

    private int gcd(int a, int b) {
        return (a == 0) ? b : gcd(b % a, a);
    }
}

