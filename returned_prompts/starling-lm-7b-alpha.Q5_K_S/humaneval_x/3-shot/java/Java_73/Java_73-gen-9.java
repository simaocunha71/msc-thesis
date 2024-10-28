        Collections.sort(arr);
        int count = 0;
        int size = arr.size();
        for (int i = 0; i < size/2; i++) {
            if (arr.get(i) != arr.get(size - i - 1)) {
                count += 1;
            }
        }
        return count;
    }
}

