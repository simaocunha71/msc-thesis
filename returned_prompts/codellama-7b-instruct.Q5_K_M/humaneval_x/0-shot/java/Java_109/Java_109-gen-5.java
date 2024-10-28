        int len = arr.size();

        if (len == 0) {
            return true;
        }

        int[] count = new int[len];
        int[] pos = new int[len];

        // count the occurrences of each element
        for (int i = 0; i < len; i++) {
            count[arr.get(i)]++;
        }

        // get the position of each element
        for (int i = 0; i < len; i++) {
            pos[i] = count[i] - 1;
        }

        // check if an element has only one occurrence
        for (int i = 0; i < len; i++) {
            if (count[i] == 1) {
                continue;
            }
            // if the element has more than one occurrence
            // check if the position is the last one
            for (int j = 0; j < len; j++) {
                if (pos[j] == 0) {
                    continue;
                }
                // if the position is not the last one
                // check if the next position is the last one
                if (pos[j] - 1 < 0) {
                    continue;
                }
                if (pos[j] - 1 == pos[j + 1]) {
                    return false;
                }
            }
        }

        return true;
    }
}
