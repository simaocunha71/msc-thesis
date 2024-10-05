        while (true) {
            for (int i = 0; i < xs.size(); i++) {
                if (Math.abs(xs.get(i)) > Math.abs(xs.get(xs.size() - 1))) {
                    double tmp = xs.get(i);
                    xs.set(i, xs.get(xs.size() - 1));
                    xs.set(xs.size() - 1, tmp);
                }
            }
            double x = xs.get(xs.size() - 1) / xs.get(xs.size() - 2);
            xs.remove(xs.size() - 1);
            xs.remove(xs.size() - 1);
            if (Math.abs(x) < 0.0000001) {
                break;
            }
            for (int i = 0; i < xs.size(); i++) {
                xs.set(i, xs.get(i) + x * xs.get(i + 1));
            }
        }
        return xs.get(0);
    }
    
    public List<Double> findZeros(List<Double> xs) {
        List<Double> result = new ArrayList<Double>();
        for (double x : findZeros(xs)) {
            if (!result.contains(x)) {
                result.add(x);
            }
        }
        return result;
    }
}

















































































































































