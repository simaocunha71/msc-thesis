        int count = 0;
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < arr.size(); i++) {
            set.add(arr.get(i));
        }
        while (set.size() > 0) {
            List<Integer> list = new ArrayList<>();
            for (int i = 0; i < arr.size(); i++) {
                list.add(arr.get(i));
            }
            int j = 0;
            for (Iterator iterator = set.iterator(); iterator.hasNext(); ) {
                int x = (int) iterator.next();
                if (j < arr.size()) {
                    int temp = arr.get(j);
                    arr.set(j, x);
                    if (isPalindromic(arr)) {
                        count += arr.size() - j - 1;
                        break A;
                    } else {
                        arr.set(j, temp);
                    }
                }
                j++;
            }
            set.clear();
        }
        return count;
    }

    private boolean isPalindromic(List<Integer> arr) {
        int left = 0;
        int right = arr.size() - 1;
        while (left <= right) {
            if (arr.get(left) != arr.get(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
















































































































































