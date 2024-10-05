        int x_numerator = Integer.parseInt(x.substring(0, x.indexOf('/')));
        int x_denominator = Integer.parseInt(x.substring(x.indexOf('/') + 1));
        int n_numerator = Integer.parseInt(n.substring(0, n.indexOf('/')));
        int n_denominator = Integer.parseInt(n.substring(n.indexOf('/') + 1));

        int gcd = gcd(x_numerator * n_denominator, x_denominator * n_numerator);

        return (x_numerator * n_denominator / gcd) == (x_denominator * n_numerator / gcd);
    }

    public int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }
}