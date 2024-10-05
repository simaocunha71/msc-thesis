        int max_val = Collections.max(arr);
        int min_val = Collections.min(arr);
        if (max_val == min_val) return true;

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) == max_val) {
                arr.set(i, min_val);
                Collections.sort(arr);
                if (arr.indexOf(max_val) == arr.size() - 1) {
                    arr.set(arr.size() - 1, max_val);
                    Collections.sort(arr);
                    break;
                }
            }
        }

        return Collections.max(arr) == arr.get(arr.size() - 1);
    }
}

