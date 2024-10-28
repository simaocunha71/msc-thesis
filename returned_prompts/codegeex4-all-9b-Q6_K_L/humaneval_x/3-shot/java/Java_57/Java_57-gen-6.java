        if (l.size() <= 2) {
            return true;
        }

        boolean increasing = l.get(0) < l.get(1);

        for (int i = 1; i < l.size() - 1; i++) {
            if ((l.get(i) < l.get(i - 1) && increasing) || (l.get(i) > l.get(i - 1) && !increasing)) {
                return false;
            }
        }
        return true;
    }
}

