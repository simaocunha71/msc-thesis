        int minIndex = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) < arr.get(minIndex)) {
                minIndex = i;
            }
        }
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) != arr.get((minIndex + i) % arr.size())) {
                return false;
            }
        }
        return true;
    }
}

