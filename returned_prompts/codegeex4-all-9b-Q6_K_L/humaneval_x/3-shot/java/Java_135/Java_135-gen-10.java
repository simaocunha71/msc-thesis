        for (int i = 0; i < arr.size(); i++) {
            if (i > 0 && arr.get(i) < arr.get(i - 1)) return i - 1;
        }
        return -1;
    }
}

