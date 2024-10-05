        if (arr.size() == 0) {
            return true;
        }
        int i = 1;
        while (i < arr.size()) {
            if (arr.get(i) < arr.get(i - 1)) {
                if (i == arr.size() - 1) {
                    arr.add(0, arr.get(arr.size() - 1));
                    arr.remove(arr.size() - 1);
                    i = 0;
                } else {
                    int j = i + 1;
                    while (arr.get(i) < arr.get(j)) {
                        int temp = arr.get(i);
                        arr.set(i, arr.get(j));
                        arr.set(j, temp);
                        j++;
                        i++;
                    }
                    i = j;
                }
            } else {
                i++;
            }
        }
        for (int k = 1; k < arr.size(); k++) {
            if (arr.get(k) < arr.get(k - 1)) {
                return false;
            }
        }
        return true;
    }
}

