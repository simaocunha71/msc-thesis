        int x_denominator = Integer.parseInt(x_parts[1]);
        int n_numerator = Integer.parseInt(n_parts[0]);
        int n_denominator = Integer.parseInt(n_parts[1]);

        int x_times_n_numerator = x_numerator * n_numerator;
        int x_times_n_denominator = x_denominator * n_denominator;

        return x_times_n_numerator % x_times_n_denominator == 0;
     }
}

