        List<Integer> result = new ArrayList<>();
        int[] count = new int[arr.size()];

        for (int i = 0; i < arr.size(); i++) {
            int num = arr.get(i);
            int ones = 0;
            while (num > 0) {
                ones += num % 10;
                num /= 10;
            }
            count[i] = ones;
        }

        for (int i = 0; i < arr.size(); i++) {
            int maxIndex = i;
            for (int j = i + 1; j < arr.size(); j++) {
                if (count[j] > count[maxIndex] || (count[j] == count[maxIndex] && arr.get(j) < arr.get(maxIndex)))
                    maxIndex = j;
            }

            int swap = arr.get(maxIndex);
            arr.set(maxIndex, arr.get(i));
            arr.set(i, swap);

            int swapCount = count[maxIndex];
            count[maxIndex] = count[i];
            count[i] = swapCount;
        }

        return arr;
    }
}

