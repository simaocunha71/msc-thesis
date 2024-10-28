        double a = xs.get(0);
        double b = 0;
        for (int i = 1; i < xs.size(); i++) {
            b += xs.get(i) * Math.pow(-1, i) * Math.pow(i, 1);
        }
        return -b / a;
    }
}

