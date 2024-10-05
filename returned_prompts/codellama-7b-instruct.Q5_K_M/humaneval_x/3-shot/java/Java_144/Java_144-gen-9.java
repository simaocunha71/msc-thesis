        int x_numerator = Integer.parseInt(x.split("/")[0]);
        int x_denominator = Integer.parseInt(x.split("/")[1]);
        int n_numerator = Integer.parseInt(n.split("/")[0]);
        int n_denominator = Integer.parseInt(n.split("/")[1]);

        int result = x_numerator * n_denominator;
        result = result % n_denominator;

        if (result == 0) {
            return true;
        } else {
            return false;
        }
    }
}

