        List<Integer> result = new ArrayList<>();
        List<Integer> temp = new ArrayList<>(lst);
        while (!temp.isEmpty()) {
            int min = Collections.min(temp);
            result.add(min);
            temp.remove((Integer) min);
            if (!temp.isEmpty()) {
                int max = Collections.max(temp);
                result.add(max);
                temp.remove((Integer) max);
            }
        }
        return result;
    }
}

