        for (int i = 1; i < xs.size(); i += 2) {
            if (xs.get(i) == 0) continue A;
        }

        double a = xs.get(0);
        for (int i = 2; i < xs.size(); i += 2) {
            a -= xs.get(i);
        }
        return -a / xs.get(1);
    }
}

