        int min = Integer.MAX_VALUE;

        for (int i = 0; i < arr.size(); i++) {
            for (int j = i + 1; j < arr.size(); j++) {
                if (Math.abs(arr.get(i) - arr.get(j)) < min) {
                    min = Math.abs(arr.get(i) - arr.get(j));
                }
            }
        }
        return min;
    }
}

