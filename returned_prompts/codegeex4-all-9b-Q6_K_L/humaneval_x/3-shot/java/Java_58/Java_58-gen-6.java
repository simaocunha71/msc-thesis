        List<Integer> result = new ArrayList<>();

        for (Integer e : l1) {
            if (l2.contains(e) && !result.contains(e)) {
                result.add(e);
            }
        }
        Collections.sort(result);
        return result;
    }
}

