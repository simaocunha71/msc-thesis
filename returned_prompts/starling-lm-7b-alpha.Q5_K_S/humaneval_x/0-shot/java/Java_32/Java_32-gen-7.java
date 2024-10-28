        while (true) {
            for (int i = 0; i < xs.size() / 2; i++) {
                double temp = xs.get(i);
                xs.set(i, xs.get(xs.size() - 1 - i));
                xs.set(xs.size() - 1 - i, temp);
            }

            for (int i = 0; i < xs.size() / 2; i++) {
                double temp = xs.get(i);
                double temp2 = xs.get(xs.size() - 1 - i);
                xs.set(i, temp - temp2);
                xs.set(xs.size() - 1 - i, temp + temp2);
            }

            for (int i = 0; i < xs.size() / 2; i++) {
                double temp = xs.get(i);
                xs.set(i, temp / 2);
                xs.set(xs.size() - 1 - i, xs.get(xs.size() - 1 - i) / 2);
            }

            double max = Math.abs(xs.get(0));
            int index = 0;
            for (int i = 1; i < xs.size(); i++) {
                if (Math.abs(xs.get(i)) > max) {
                    max = Math.abs(xs.get(i));
                    index = i;
                }
            }

            double x = -xs.get(index) / xs.get(index - 1);
            for (int i = 0; i < 1000; i++) {
                double temp = x;
                x = poly(xs, x);
                if (Math.abs(temp - x) < 1e-8) {
                    break A;
                }
            }
        }
        return x;
    }
}























