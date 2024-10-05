        int changes = 0;
        for (int i = 0; i < arr.size() / 2; i++) {
            if (!arr.get(i).equals(arr.get(arr.size() - 1 - i))) {
                changes++;
            }
        }
        return changes;
    }
}

