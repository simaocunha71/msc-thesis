        Collections.sort(arr);

        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i - 1) >= arr.get(i)) return i - 1;
        }
        return -1;
    }
}

