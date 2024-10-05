        int numerator = Integer.parseInt(x.split("/")[0]);
        int denominator = Integer.parseInt(n.split("/")[0]);

        return numerator * denominator % numerator == 0;
    }
}

