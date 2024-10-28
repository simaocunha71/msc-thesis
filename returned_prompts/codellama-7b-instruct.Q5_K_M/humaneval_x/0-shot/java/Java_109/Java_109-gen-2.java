        if (arr.isEmpty()) {
            return true;
        }

        int[] arrInts = new int[arr.size()];
        for (int i = 0; i < arr.size(); i++) {
            arrInts[i] = arr.get(i);
        }

        Arrays.sort(arrInts);
        for (int i = 0; i < arrInts.length - 1; i++) {
            if (arrInts[i] > arrInts[i + 1]) {
                return false;
            }
        }
        return true;
    }
}

