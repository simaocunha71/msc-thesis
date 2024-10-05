        int max = l.get(0);

        for (int i = 1; i < l.size(); i++) {
            if (l.get(i) > max) {
                max = l.get(i);
            }
        }

        return max;
    }
}

