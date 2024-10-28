        int x_numerator = Integer.parseInt(x.split("/")[0]);
        int x_denominator = Integer.parseInt(x.split("/")[1]);
        int n_numerator = Integer.parseInt(n.split("/")[0]);
        int n_denominator = Integer.parseInt(n.split("/")[1]);

        int lcm = (x_denominator * n_denominator) / gcd(x_denominator, n_denominator);
        int new_numerator = (n_numerator * lcm / n_denominator) * (x_denominator / lcm);

        return (double) new_numerator / (double) lcm == (double) x_numerator / (double) x_denominator;
    }

    int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}

