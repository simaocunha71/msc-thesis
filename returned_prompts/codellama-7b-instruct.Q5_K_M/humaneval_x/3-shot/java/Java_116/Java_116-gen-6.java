        // https://www.geeksforgeeks.org/sort-an-array-of-integers-according-to-number-of-ones/
        // https://www.geeksforgeeks.org/sort-an-array-of-integers-according-to-number-of-ones-set-3/

        List<Integer> result = new ArrayList<Integer>();

        // Count the number of 1s in each number
        int[] counts = new int[32];
        int max = 0;

        for (int i = 0; i < arr.size(); i++) {
            int num = arr.get(i);
            int k = 0;

            // Count the number of 1s in each number
            while (num > 0) {
                if ((num & 1) == 1) {
                    counts[k]++;
                }
                num >>= 1;
                k++;
            }

            // Update max value
            if (max < counts[k - 1]) {
                max = counts[k - 1];
            }
        }

        // sort the array based on counts
        int[] temp = new int[arr.size()];
        for (int i = 0; i < arr.size(); i++) {
            temp[i] = counts[31 - Integer.numberOfLeadingZeros(arr.get(i))];
        }

        // sort the array based on counts
        Arrays.sort(temp);

        // get the array with correct counts
        int[] temp1 = new int[arr.size()];
        for (int i = 0; i < arr.size(); i++) {
            for (int j = 0; j < max; j++) {
                if (temp[i] == j) {
                    temp1[i] = arr.get(i);
                    break;
                }
            }
        }

        // sort the array based on decimal value
        Arrays.sort(temp1);

        // return the sorted array
        for (int i = 0; i < arr.size(); i++) {
            result.