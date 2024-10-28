        if (xs.size() % 2 == 1) return 0;
        double x_guess = xs.get(xs.size() - 1) / xs.get(xs.size() - 2);
        double x_prev = -1;
        while (Math.abs(x_prev - x_guess) > 0.00001) {
            x_prev = x_guess;
            x_guess = x_prev - poly(Arrays.asList(xs.get(xs.size() - 1), -xs.get(xs.size() - 2)), x_prev) / poly(xs, x_prev);
        }
        return x_guess;
    }
}

