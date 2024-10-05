        int numerator1 = Integer.parseInt(x.split("/")[0]);
        int denominator1 = Integer.parseInt(x.split("/")[1]);
        int numerator2 = Integer.parseInt(n.split("/")[0]);
        int denominator2 = Integer.parseInt(n.split("/")[1]);

        int numerator = numerator1 * denominator2;
        int denominator = denominator1 * numerator2;

        if (gcd(denominator, numerator) != 1) {
            return false;
        }

        return true;
    }

    public int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a % b);
        }
    }
}

