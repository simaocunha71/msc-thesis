        int numerator1 = Integer.parseInt(x.split("/")[0]);
        int denominator1 = Integer.parseInt(x.split("/")[1]);
        int numerator2 = Integer.parseInt(n.split("/")[0]);
        int denominator2 = Integer.parseInt(n.split("/")[1]);

        int newNumerator = numerator1 * denominator2;
        int newDenominator = denominator1 * numerator2;

        return newNumerator == newDenominator;
    }
}

