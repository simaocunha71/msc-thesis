        int changes = 0;
        int i = 0, j = arr.size() - 1;
        while (i < j) {
            if (!arr.get(i).equals(arr.get(j))) {
                changes++;
            }
            i++;
            j--;
        }
        return changes;
    }
}

