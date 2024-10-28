        int changes = 0;
        int start = 0, end = arr.size() - 1;

        while (start < end) {
            if (arr.get(start) != arr.get(end)) {
                changes++;
            }
            start++;
            end--;
        }
        return changes;
     }
}

