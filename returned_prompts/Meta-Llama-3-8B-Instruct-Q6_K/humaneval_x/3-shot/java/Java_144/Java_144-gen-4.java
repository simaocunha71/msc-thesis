        int xN = numerator(x) * denominator(n);
        int xD = numerator(x) * denominator(n);
        int nN = numerator(n) * denominator(x);
        int nD = denominator(n) * denominator(x);

        return xN == nN && xD == nD;
    }

    private int numerator(String s) {
        return Integer.parseInt(s.split("/")[0]);
    }

    private int denominator(String s) {
        return Integer.parseInt(s.split("/")[1]);
    }
}

