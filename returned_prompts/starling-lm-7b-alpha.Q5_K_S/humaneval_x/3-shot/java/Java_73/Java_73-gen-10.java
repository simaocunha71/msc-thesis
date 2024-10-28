        Collections.sort(arr);
        int start = 0, end = arr.size() - 1;
        int result = 0;

        while (start < end) {
            if (arr.get(start) != arr.get(end)) {
                result += 1;
                if (start != end - 1) {
                    arr.set(start + 1, arr.get(start));
                } else {
                    arr.set(end - 1, arr.get(start));
                }
            }
            start += 1;
            end -= 1;
        }
        return result;
    }
}

