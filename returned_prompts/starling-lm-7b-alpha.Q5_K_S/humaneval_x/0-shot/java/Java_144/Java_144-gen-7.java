        int xNumerator = Integer.parseInt(x.split("/")[0]);
        int xDenominator = Integer.parseInt(x.split("/")[1]);
        int nNumerator = Integer.parseInt(n.split("/")[0]);
        int nDenominator = Integer.parseInt(n.split("/")[1]);

        int lcm = lcm(xDenominator, nDenominator);

        int numerator = xNumerator * (lcm / xDenominator) + nNumerator * (lcm / nDenominator);
        int denominator = lcm;

        int gcd = gcd(numerator, denominator);

        return numerator / gcd == denominator / gcd;
    }

    private int lcm(int a, int b) {
        return a * (b / gcd(a, b));
    }

    private int gcd(int a, int b) {
        if (a == 0) {
            return b;
        }
        return gcd(b % a, a);
    }
}











































































```