        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) {
                List<Integer> temp = new ArrayList<>();
                for (Integer num : l) {
                    if (num <= l.get(i)) {
                        temp.add(num);
                    }
                }
                result.add(temp.get(temp.size() - 1));
            } else {
                result.add(l.get(i));
            }
        }
        return result;
    }
}

