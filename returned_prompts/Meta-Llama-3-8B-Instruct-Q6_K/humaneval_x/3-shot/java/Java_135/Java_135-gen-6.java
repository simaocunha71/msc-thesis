        for (int i = arr.size() - 1; i > 0; i--) {
            if (arr.get(i - 1) > arr.get(i)) {
                return i - 1;
            }
        }
        return -1;
    }
}

