        List<Integer> result = new ArrayList<>();
        int index = 0;
        while (index < l.size()) {
            if (index % 3 == 0) {
                result.add(l.get(index));
            } else {
                result.add(l.get(index));
            }
            index += 1;
        }
        return result;
    }
}

