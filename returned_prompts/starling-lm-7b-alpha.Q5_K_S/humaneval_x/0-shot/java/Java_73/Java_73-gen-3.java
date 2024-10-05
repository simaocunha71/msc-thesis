        int count = 0;
        int n = arr.size();
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < n; i++) {
            set.add(arr.get(i));
        }

        while (set.size() > 0) {
            int elem = set.iterator().next();
            int left = findLeft(arr, elem);
            int right = findRight(arr, elem);
            if (left == -1 || right == -1) {
                count++;
                arr.set(arr.size() / 2, elem);
            } else {
                set.remove(left);
                set.remove(right);
            }
        }

        return count;
    }

    private int findLeft(List<Integer> arr, int elem) {
        int left = -1;
        for (int i = 0; i < arr.size() / 2; i++) {
            if (arr.get(i) != elem) {
                left = i;
                break;
            }
        }
        return left;
    }

    private int findRight(List<Integer> arr, int elem) {
        int right = -1;
        for (int i = arr.size() - 1; i >= arr.size() / 2; i--) {
            if (arr.get(i) != elem) {
                right = i;
                break;
            }
        }
        return right;
    }
}














































































































































