        int index = arr.size() - 2;
        while (index >= 0) {
            if (arr.get(index + 1) > arr.get(index)) {
                return index + 1;
            }
            index--;
        }
        return -1;
    }
}

