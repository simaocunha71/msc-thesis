        for (int i = arr.size() - 1; i >= 0; i--) {
            if (arr.get(i) >= arr.get(i - 1)) return i;
        }
        return -1;
    }
}

