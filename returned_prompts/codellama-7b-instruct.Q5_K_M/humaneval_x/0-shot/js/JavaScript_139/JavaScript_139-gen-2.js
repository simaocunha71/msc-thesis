        int x_numerator = Integer.parseInt(x.split("/")[0]);
        int x_denominator = Integer.parseInt(x.split("/")[1]);
        int n_numerator = Integer.parseInt(n.split("/")[0]);
        int n_denominator = Integer.parseInt(n.split("/")[1]);

        int result = x_numerator * n_denominator - n_numerator * x_denominator;

        if (result % n_denominator == 0) return true;
        return false;
    }
}

