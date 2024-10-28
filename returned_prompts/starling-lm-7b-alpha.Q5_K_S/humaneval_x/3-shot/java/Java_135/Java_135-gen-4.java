        int result = -1;
        int previous = arr.get(0);
        for (int i = 1; i < arr.size(); i++) {
            int current = arr.get(i);
            if (current > previous) {
                result = i - 1;
                previous = current;
            }
        }
        return result;
    }
}

