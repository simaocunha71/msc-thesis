        if (arr.size() == 0) return true;
        int[] arr_sorted = new int[arr.size()];

        for (int i = 0; i < arr.size(); i++) {
            arr_sorted[i] = arr.get(i);
        }

        Arrays.sort(arr_sorted);

        for (int i = 0; i < arr.size(); i++) {
            if (arr_sorted[i] != arr.get(i)) return false;
        }
        return true;
    }
}

