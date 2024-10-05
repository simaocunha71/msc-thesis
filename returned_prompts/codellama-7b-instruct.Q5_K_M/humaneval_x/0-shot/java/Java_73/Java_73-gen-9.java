        int[] arr2 = new int[arr.size()];
        for (int i = 0; i < arr.size(); i++) {
            arr2[i] = arr.get(i);
        }

        int min = Integer.MAX_VALUE;
        for (int i = 0; i < arr.size(); i++) {
            int[] arr3 = Arrays.copyOf(arr2, arr2.length);
            int j = i;
            while (j < arr3.length - j - 1) {
                arr3[j] = arr3[j + 1];
                arr3[j + 1] = arr3[j];
                j++;
            }

            int current = 0;
            for (int k = 0; k < arr3.length; k++) {
                if (arr3[k] != arr2[k]) {
                    current++;
                }
            }
            if (current < min) {
                min = current;
            }
        }
        return min;
    }
}

