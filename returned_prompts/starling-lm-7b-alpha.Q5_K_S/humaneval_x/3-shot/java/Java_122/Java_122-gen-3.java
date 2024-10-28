        int result = 0;
        for (int i = 0; i < k; i++) {
            if (arr.get(i) < 100) {
                result += arr.get(i);
            }
        }
        return result;
    }
}

