        int[] x_parts = splitFraction(x);
        int[] n_parts = splitFraction(n);

        int x_numerator = x_parts[0] * n_parts[1];
        int x_denominator = x_parts[1] * n_parts[0];

        return gcd(x_numerator, x_denominator) == 1;
    }

    private int[] splitFraction(String fraction) {
        String[] parts = fraction.split("/");
        return new int[]{Integer.parseInt(parts[0]), Integer.parseInt(parts[1])};
    }

    private int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a % b);
        }
    }
}

