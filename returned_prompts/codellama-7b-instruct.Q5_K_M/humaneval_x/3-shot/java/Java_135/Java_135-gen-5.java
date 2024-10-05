        for (int i = 1; i < arr.size(); i++) {
            int prev = arr.get(i - 1);
            int curr = arr.get(i);
            if (curr <= prev) {
                return i;
            }
        }
        return -1;
    }
}

