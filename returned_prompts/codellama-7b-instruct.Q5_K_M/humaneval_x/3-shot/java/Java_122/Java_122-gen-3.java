        int result = 0;
        int max_index = Math.min(arr.size(), k);

        for (int i = 0; i < max_index; i++) {
            if (arr.get(i) < 100) {
                result += arr.get(i);
            }
        }
        return result;
    }
}

