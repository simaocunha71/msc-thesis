        int size = arr.size();
        Collections.sort(arr);
        int result = 0;
        for (int i = 0; i < size / 2; i++) {
            if (arr.get(i) != arr.get(size - 1 - i)) {
                result += 1;
            }
        }
        return result;
    }
}

