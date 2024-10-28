        Collections.sort(arr);
        int result = 0;
        for (int i = 0; i < arr.size() / 2; i++) {
            if (arr.get(i) != arr.get(arr.size() - 1 - i)) result += 1;
        }
        return result;
    }
}

