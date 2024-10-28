        List<Integer> result = new ArrayList<>();
        for (int i : l) {
            if (!result.contains(i)) result.add(i);
        }
        Collections.sort(result);
        return result;
    }
}

