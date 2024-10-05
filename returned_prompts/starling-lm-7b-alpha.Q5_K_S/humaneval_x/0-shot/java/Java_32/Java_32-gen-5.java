        while (true) {
            if (xs.size() == 1) {
                return 0;
            }

            if (xs.size() % 2 == 0) {
                List<Double> xs1 = new ArrayList<>();
                List<Double> xs2 = new ArrayList<>();
                double c = xs.get(0);
                for (int i = 1; i < xs.size(); i++) {
                    if (i % 2 == 0) {
                        xs1.add(c * xs.get(i));
                    } else {
                        xs2.add(c * xs.get(i));
                    }
                }
                if (xs1.size() == 1) {
                    if (xs1.get(0) == 0) {
                        return 0;
                    } else {
                        return -xs2.get(0) / xs1.get(0);
                    }
                } else {
                    xs = xs2;
                    continue A;
                }
            } else {
                List<Double> xs1 = new ArrayList<>();
                double c = xs.get(0);
                for (int i = 1; i < xs.size(); i++) {
                    if (i % 2 == 0) {
                        xs1.add(c * xs.get(i));
                    } else {
                        xs1.add(xs.get(i));
                    }
                }
                if (xs1.size() == 1) {
                    if (xs1.get(0) == 0) {
                        return 0;
                    } else {
                        return -xs.get(xs.size() - 1) / xs1.get(0);
                    }
                } else {
                    xs = xs1;
                    continue A;
                }
            }
        }
    }
}

















