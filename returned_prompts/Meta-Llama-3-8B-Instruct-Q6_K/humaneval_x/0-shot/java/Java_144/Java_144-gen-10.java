    public boolean simplify(String x, String n) {
        int num1 = numerator(x);
        int denom1 = denominator(x);
        int num2 = numerator(n);
        int denom2 = denominator(n);

        return (num1 * denom2) % (denom1 * num2) == 0;
    }

    private int numerator(String s) {
        return Integer.parseInt(s.split("/")[0]);
    }

    private int denominator(String s) {
        return Integer.parseInt(s.split("/")[1]);
    }
}