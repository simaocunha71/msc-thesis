        int x_numerator = Integer.parseInt(x.substring(0, x.indexOf('/')));
        int x_denominator = Integer.parseInt(x.substring(x.indexOf('/') + 1));
        int n_numerator = Integer.parseInt(n.substring(0, n.indexOf('/')));
        int n_denominator = Integer.parseInt(n.substring(n.indexOf('/') + 1));

        return (x_numerator * n_denominator) == (x_denominator * n_numerator);
    }
}

