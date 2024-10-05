        int[] arr_int = new int[arr.size()];
        for (int i = 0; i < arr_int.length; i++) {
            arr_int[i] = arr.get(i);
        }

        int min_change = Integer.MAX_VALUE;
        for (int i = 0; i < arr_int.length; i++) {
            int change = 0;
            for (int j = i; j < arr_int.length; j++) {
                if (arr_int[i] != arr_int[j]) {
                    change++;
                }
            }
            min_change = Math.min(min_change, change);
        }
        return min_change;

    }
}

