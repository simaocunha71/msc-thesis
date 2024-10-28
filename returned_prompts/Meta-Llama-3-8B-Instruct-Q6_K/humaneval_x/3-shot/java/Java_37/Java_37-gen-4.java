        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) {
                List<Integer> temp = new ArrayList<>();
                for (int j = 0; j < l.size(); j++) {
                    if (j % 2 == 0) {
                        temp.add(l.get(j));
                    }
                }
                Collections.sort(temp);
                result.add(temp.get(0));
            } else {
                result.add(l.get(i));
            }
        }
        return result;
    }
}

