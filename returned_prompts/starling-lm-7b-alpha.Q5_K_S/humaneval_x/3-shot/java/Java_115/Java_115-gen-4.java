        int result = 0;
        while (true) {
            boolean filled = false;
            for (List<Integer> row : grid) {
                int start = 0;
                while (start < row.size()) {
                    int end = start;
                    while (end < row.size() && row.get(end) == 1) end += 1;
                    if (end - start > capacity) {
                        filled = true;
                        result += 1;
                        break;
                    } else {
                        for (int i = start; i < end; i++) {
                            row.set(i, 0);
                        }
                        start = end;
                    }
                }
                if (filled) break;
            }
            if (!filled) return result;
        }
    }
}

