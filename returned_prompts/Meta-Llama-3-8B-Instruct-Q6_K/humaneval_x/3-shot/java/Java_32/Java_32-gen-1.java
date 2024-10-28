        if (xs.size() % 2 == 1) {
            throw new RuntimeException("List of coefficients must have even number of elements.");
        }
        double result = xs.get(0);
        for (int i = 1; i < xs.size() / 2; i++) {
            result = -xs.get(i + 1) / (i * result);
        }
        return result;
    }
}

