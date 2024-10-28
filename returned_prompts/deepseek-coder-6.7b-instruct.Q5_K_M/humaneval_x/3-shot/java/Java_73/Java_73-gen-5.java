        int changes = 0;
        for(int i = 0; i < arr.size() / 2; i++) {
            if(arr.get(i) != arr.get(arr.size() - i - 1)) {
                changes++;
            }
        }
        return changes;
    }
}

