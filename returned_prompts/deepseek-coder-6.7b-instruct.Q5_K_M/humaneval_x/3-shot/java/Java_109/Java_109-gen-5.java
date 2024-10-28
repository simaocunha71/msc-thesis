        if (arr.isEmpty()) return true;

        int inversions = 0;
        for (int i = 0; i < arr.size() - 1; i++) {
            for (int j = i + 1; j < arr.size(); j++) {
                if (arr.get(i) > arr.get(j)) {
                    inversions++;
                }
            }
        }
        return inversions <= 1;
    }
}

