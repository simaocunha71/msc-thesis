        for (int i = arr.size() - 2; i >= 0; i--) {
            if (arr.get(i + 1) < arr.get(i)) {
                int j = i + 1;
                while (j < arr.size() && arr.get(j) > arr.get(j - 1)) j++;
                if (j == arr.size()) return false;
                int tmp = arr.get(j);
                for (int k = j; k > i; k--) {
                    arr.set(k, arr.get(k - 1));
                }
                arr.set(i, tmp);
            }
        }
        return true;
    }
}

