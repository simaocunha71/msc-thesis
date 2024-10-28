        int i = 0;
        while (i < arr.size() - 1) {
            if (arr.get(i) > arr.get(i + 1)) {
                return false;
            }
            i++;
        }
        return true;
    }
}