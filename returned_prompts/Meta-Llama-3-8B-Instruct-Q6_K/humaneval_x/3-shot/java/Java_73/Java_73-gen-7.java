        int changes = 0;
        int start = 0;
        int end = arr.size() - 1;

        while (start < end) {
            if (arr.get(start) != arr.get(end)) {
                changes++;
                int min = Math.min(arr.get(start), arr.get(end));
                int max = Math.max(arr.get(start), arr.get(end));
                for (int i = start + 1; i < end; i++) {
                    if (arr.get(i) == max) {
                        arr.set(i, min);
                        changes++;
                        break;
                    }
                }
            }
            start++;
            end--;
        }
        return changes;
    }
}