        int xNumerator = Integer.parseInt(x.split("/")[0]);
        int xDenominator = Integer.parseInt(x.split("/")[1]);
        int nNumerator = Integer.parseInt(n.split("/")[0]);
        int nDenominator = Integer.parseInt(n.split("/")[1]);

        long lcm = (long)xDenominator * nDenominator / gcd(xDenominator, nDenominator);
        long lcmNumerator = (long)xNumerator * (lcm / xDenominator);
        long lcmDenominator = (long)nNumerator * (lcm / nDenominator);
        long lcmGcd = gcd(lcmNumerator, lcmDenominator);
        return (lcmNumerator / lcmGcd) * (lcmDenominator / lcmGcd) == 1;
    }

    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}















































































```