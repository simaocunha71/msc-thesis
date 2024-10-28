        int count = 0;
        int prev = lst.get(0);
        for (int i = 1; i < lst.size(); i++) {
            int current = lst.get(i);
            if (current > prev) {
                prev = current;
            } else {
                count += 1;
            }
        }
        return count == 0;
    }
}

