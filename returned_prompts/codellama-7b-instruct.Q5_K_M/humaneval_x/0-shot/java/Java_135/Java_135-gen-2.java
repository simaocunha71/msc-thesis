        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) >= arr.get(i - 1)) {
                continue;
            }
            return i;
        }
        return -1;
    }
}

