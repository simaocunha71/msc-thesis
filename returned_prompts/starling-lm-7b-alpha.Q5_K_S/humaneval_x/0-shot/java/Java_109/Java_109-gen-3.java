        int n = arr.size();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = arr.get(i);
        }
        int min = a[0];
        int min_index = 0;
        for (int i = 1; i < n; i++) {
            if (a[i] < min) {
                min = a[i];
                min_index = i;
            }
        }
        while (min_index != 0) {
            int temp = a[0];
            a[0] = a[min_index];
            a[min_index] = temp;
            min_index--;
            if (min_index < 0) min_index = n - 1;
            int min = a[0];
            int min_index = 0;
            for (int i = 1; i < n; i++) {
                if (a[i] < min) {
                    min = a[i];
                    min_index = i;
                }
            }
        }
        boolean flag = true;
        for (int i = 0; i < n - 1; i++) {
            if (a[i] > a[i + 1]) {
                flag = false;
                break;
            }
        }
        return flag;
    }
}










































































```
