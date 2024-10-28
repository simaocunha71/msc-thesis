        int count = 0;
        int i = 0;
        int j = arr.size() - 1;
        while (i < j) {
            if (arr.get(i) != arr.get(j)) {
                count += 1;
                if (arr.get(i) < arr.get(j)) {
                    i += 1;
                } else {
                    j -= 1;
                }
            } else {
                i += 1;
                j -= 1;
            }
        }
        return count;
    }
}

