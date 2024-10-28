        if (arr.size() == 0) {
            return true;
        }

        if (arr.size() == 1) {
            return true;
        }
        if (arr.size() == 2) {
            if (arr.get(0) < arr.get(1)) {
                return false;
            } else {
                return true;
            }
        }

        List<Integer> list = new ArrayList<Integer>(arr);
        int i = 0;
        int j = list.size() - 1;
        while (i < j) {
            if (list.get(i) < list.get(j)) {
                i++;
            } else if (list.get(i) > list.get(j)) {
                j--;
            } else {
                list.set(j, list.get(i));
                list.set(i, list.get(j));
                i++;
                j--;
            }
        }
        list.set(list.size() - 1, list.get(i));
        list.set(i, list.get(list.size() - 1));
        for (int k = 0; k < list.size() - 1; k++) {
            if (list.get(k) < list.get(k + 1)) {
                return true;
            }
        }
        return false;
    }
}
