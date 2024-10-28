        int n = arr.size();
        int left = 0;
        int right = n - 1;
        int cnt = 0;
        while (left < right) {
            if (arr.get(left) != arr.get(right)) {
                cnt++;
                if (left + 1 < n && arr.get(left + 1) == arr.get(right)) {
                    arr.set(left + 1, arr.get(left));
                    continue A;
                }
                if (right - 1 >= 0 && arr.get(left) == arr.get(right - 1)) {
                    arr.set(right - 1, arr.get(right));
                    continue A;
                }
                if (left + 1 < n && right - 1 >= 0 && arr.get(left + 1) == arr.get(right - 1)) {
                    arr.set(left + 1, arr.get(right));
                    continue A;
                }
                arr.set(left, arr.get(right));
                arr.set(right, arr.get(left));
                cnt++;
            }
            left++;
            right--;
        }
        return cnt;
    }
}











































































































































































































