        int i = 0, j = arr.size() - 1, changes = 0;

        while (i < j) {
            if (arr.get(i) != arr.get(j)) {
                changes += 1;
            }
            i += 1;
            j -= 1;
        }
        return changes;
    }
}

