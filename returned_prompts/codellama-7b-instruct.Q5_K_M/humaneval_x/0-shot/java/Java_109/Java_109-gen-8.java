        int n = arr.size();
        if (n == 0)
            return true;
        if (n == 1)
            return true;
        if (n == 2)
            return true;
        int[] arr1 = new int[n];
        for (int i = 0; i < n; i++)
            arr1[i] = arr.get(i);
        int m = n / 2;
        int k = 1;
        for (int i = m - 1; i >= 0; i--) {
            k *= 2;
            if (arr1[i] < arr1[i + k]) {
                int j = i + k;
                while (j < n) {
                    if (arr1[j] > arr1[j - k]) {
                        int temp = arr1[j];
                        arr1[j] = arr1[j - k];
                        arr1[j - k] = temp;
                        j += k;
                    } else
                        break;
                }
            }
        }
        for (int i = 0; i < n; i++)
            if (arr1[i] > arr1[i + 1])
                return false;
        return true;
    }
}
