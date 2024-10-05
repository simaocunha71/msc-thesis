        if (arr.isEmpty()) return true;

        int i = 0;
        int j = i + 1;
        while (j < arr.size()) {
            if (arr.get(i) >= arr.get(j)) {
                i++;
                j++;
            } else {
                break;
            }
        }
        return j == arr.size();
    }
}

