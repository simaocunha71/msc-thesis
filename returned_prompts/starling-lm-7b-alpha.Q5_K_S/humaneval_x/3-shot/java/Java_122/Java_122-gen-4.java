        int result = 0;
        int arr_length = arr.size();
        for (int i = 0; i < k; i++) {
            result += arr.get(i);
        }
        return result;
    }
}

