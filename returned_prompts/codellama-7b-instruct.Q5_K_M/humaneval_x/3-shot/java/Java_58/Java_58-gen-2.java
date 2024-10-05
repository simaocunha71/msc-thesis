        List<Integer> result = new ArrayList<>();
        for (int i : l1) {
            if (l2.contains(i)) result.add(i);
        }
        return result;
    }
}

