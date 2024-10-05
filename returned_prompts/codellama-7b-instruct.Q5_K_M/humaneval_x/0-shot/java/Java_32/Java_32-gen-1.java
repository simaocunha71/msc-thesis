        for (int i = 0; i < xs.size(); i++) {
            if (xs.get(i) != 0) {
                // find i-th coefficient
                double coef = xs.get(i);

                // find derivative of f(x)
                List<Double> der = new ArrayList<>();
                for (int j = 0; j < xs.size(); j++) {
                    der.add(xs.get(j) * (j - i));
                }

                // find x0 such that f(x0) = 0
                double x0 = 0;
                while (poly(der, x0) != 0) {
                    x0 -= poly(der, x0) / poly(xs, x0);
                }

                // check if x0 is in the domain
                if (x0 >= -1 && x0 <= 1) {
                    // return x0
                    return x0;
                }
            }
        }

        // if no zero found
        return 0;
    }
}
