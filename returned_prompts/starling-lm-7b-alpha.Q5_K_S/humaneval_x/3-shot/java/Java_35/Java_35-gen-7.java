        int max = Integer.MIN_VALUE;

        for (int i = 0; i < l.size(); i++) {
            if (l.get(i) > max) max = l.get(i);
        }
        return max;
    }
}

