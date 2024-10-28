        int total = 0;

        // if k == 0, then no elements are included in the sum
        if (k == 0) {
            return total;
        }

        // if k < 0, then the sum should be the total of the entire list
        if (k < 0) {
            for (int i = 0; i < arr.size(); i++) {
                total += arr.get(i);
            }
            return total;
        }

        // if k >= len(arr), then the sum should be the total of the entire list
        if (k >= arr.size()) {
            for (int i = 0; i < arr.size(); i++) {
                total += arr.get(i);
            }
            return total;
        }

        int count = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (count < k) {
                total += arr.get(i);
                count++;
            }
        }
        return total;
    }