        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();
        int changes = 0;

        for (int i = 0; i < arr.size(); i++) {
            if (i < arr.size() / 2) {
                left.add(arr.get(i));
            } else {
                right.add(arr.get(i));
            }
        }

        for (int i = 0; i < left.size(); i++) {
            if (!left.get(i).equals(right.get(left.size() - 1 - i))) {
                changes++;
            }
        }

        return changes;
    }
}

