        for (int i = 0; i < arr.size(); i++) {
            for (int j = i + 1; j < arr.size(); j++) {
                if (arr.get(j) < arr.get(i)) {
                    return i;
                }
            }
        }
        return -1;
    }
}

