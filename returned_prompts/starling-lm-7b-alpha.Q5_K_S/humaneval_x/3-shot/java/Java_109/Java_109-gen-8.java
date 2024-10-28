        Collections.sort(arr);
        int max = arr.get(arr.size() - 1);
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) != max) {
                return false;
            }
        }
        return true;
    }
}

