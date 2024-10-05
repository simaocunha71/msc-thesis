        double a = xs.get(0);
        double b = 0;
        double c = 0;

        for (int i = 1; i < xs.size(); i++) {
            b += i * xs.get(i);
        }

        for (int i = 2; i < xs.size(); i++) {
            c += i * (i - 1) * xs.get(i);
        }

        return -b / c;
    }
}

