        Collections.sort(arr);
        int count = 0;
        for (int i = 0; i < arr.size() / 2; i++) {
            if (arr.get(i) != arr.get(arr.size() - 1 - i)) {
                count += 1;
            }
        }
        return count;
    }
}

