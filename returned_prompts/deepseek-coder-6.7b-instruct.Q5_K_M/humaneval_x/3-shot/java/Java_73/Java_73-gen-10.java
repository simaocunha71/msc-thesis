        int changes = 0;
        for (int i = 0, j = arr.size() - 1; i < j; i++, j--) {
            if (!arr.get(i).equals(arr.get(j))) {
                changes++;
            }
        }
        return changes;
    }
}

