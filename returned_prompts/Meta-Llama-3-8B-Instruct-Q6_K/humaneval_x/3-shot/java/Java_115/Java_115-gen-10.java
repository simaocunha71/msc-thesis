        int totalWater = 0;
        for (List<Integer> row : grid) {
            totalWater += row.stream().mapToInt(i -> i).sum();
        }

        int bucketCount = (int) Math.ceil((double) totalWater / capacity);
        return bucketCount;
    }
}

