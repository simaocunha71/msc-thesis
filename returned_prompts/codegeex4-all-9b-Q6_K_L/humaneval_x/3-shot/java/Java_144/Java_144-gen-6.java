        String[] x_parts = x.split("/");
        String[] n_parts = n.split("/");
        int x_numerator = Integer.parseInt(x_parts[0]);
        int x_denominator = Integer.parseInt(x_parts[1]);
        int n_numerator = Integer.parseInt(n_parts[0]);
        int n_denominator = Integer.parseInt(n_parts[1]);

        return (x_numerator * n_denominator) % x_denominator == 0;
    }
}

