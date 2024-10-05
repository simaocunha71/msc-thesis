        // Quick Sort
        List<Integer> result = new ArrayList<>();
        int left = 0;
        int right = arr.size() - 1;

        while (left <= right) {
            int i = left;
            int j = right;
            int temp = arr.get(i);
            while (i < j) {
                while (arr.get(j) >= temp) {
                    j--;
                }
                arr.set(i, arr.get(j));
                while (arr.get(i) <= temp) {
                    i++;
                }
                arr.set(j, arr.get(i));
            }
            arr.set(i, temp);

            result.add(0, arr.get(i));
            if (result.size() > k) {
                result.remove(k);
            }
        }

        return result;

    }
}

