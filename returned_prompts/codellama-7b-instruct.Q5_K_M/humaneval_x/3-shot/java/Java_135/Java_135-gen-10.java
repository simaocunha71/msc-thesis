        for (int i = arr.size() - 1; i >= 1; i--) {
            if (arr.get(i) <= arr.get(i - 1)) return i;
        }
        return -1;
    }
}

