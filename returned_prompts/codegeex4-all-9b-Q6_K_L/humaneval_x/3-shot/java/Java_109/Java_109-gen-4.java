        int max = 0;
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) < arr.get(i - 1)) {
                max = Math.max(max, i);
            }
        }
        return arr.get(0) <= arr.get(max) && max + 1 == arr.indexOf(arr.get(max));
    }
}

