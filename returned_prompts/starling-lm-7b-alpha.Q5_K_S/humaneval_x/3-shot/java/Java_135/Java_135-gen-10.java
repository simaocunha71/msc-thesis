        int result = arr.size() - 1;
        for (int i = arr.size() - 2; i >= 0; i--) {
            if (arr.get(i) > arr.get(i + 1)) {
                while (result > i && arr.get(result) >= arr.get(i)) {
                    result -= 1;
                }
                return result;
            }
        }
        return -1;
    }
}

