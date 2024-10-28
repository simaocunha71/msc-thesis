        List<Integer> result = new ArrayList<>();
        for (Integer i : l) {
            if (!result.contains(i)) result.add(i);
        }
        Collections.sort(result);
        return result;

    }
}

