        int result = 0;

        int m = grid.size();
        int n = grid.get(0).size();

        for (int i = 0; i < m; i++) {
            int j = 0;
            while (j < n && grid.get(i).get(j) == 0) j++;

            int start = j;
            while (j < n && grid.get(i).get(j) == 1) j++;

            if (j - start > capacity) {
                result++;
                start += capacity;
                while (start < j) {
                    grid.get(i).set(start, 0);
                    start++;
                }
            }
        }
        return result;
    }
}

