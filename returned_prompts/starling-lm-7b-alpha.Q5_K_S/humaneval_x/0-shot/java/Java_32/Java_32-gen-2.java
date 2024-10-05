        while (true) {
            int n = xs.size();
            if (n % 2 == 1) {
                throw new IllegalArgumentException("xs must have even number of coefficients");
            }
            double a = xs.get(n / 2);
            if (Math.abs(a) < 0.000001) {
                return 0;
            }
            if (a > 0) {
                xs.set(n / 2, 0.);
            } else {
                xs.set(n / 2, -0.);
            }

            List<Double> xs1 = new ArrayList<>();
            List<Double> xs2 = new ArrayList<>();
            for (double d : xs) {
                if (d != 0) {
                    xs1.add(d);
                } else {
                    xs2.add(d);
                }
            }
            xs = xs1;
            double[] roots = findRoots(xs);

            for (double d : roots) {
                if (poly(xs, d) < 0.000001) {
                    continue A;
                }
            }
            List<Double> xs_ = new ArrayList<>();
            for (double d : xs) {
                xs_.add(d * Math.exp(Math.PI * d));
            }
            return findZero(xs_);
        }
    }

    double[] findRoots(List<Double> xs) {
        double a = xs.get(0);
        double b = xs.get(1);
        double c = xs.get(2);
        double d = -c / b;
        double e = Math.sqrt(d * d + 1);
        double f = e + d;
        double g = f * f;
        double h = g + 1;
        return new double[]{f / h, -d / h};
    }
}
























