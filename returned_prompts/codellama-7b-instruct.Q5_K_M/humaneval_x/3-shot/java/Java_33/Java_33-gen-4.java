        List<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 != 0) {
                result.add(l.get(i));
            } else {
                List<Integer> temp = new ArrayList<Integer>();
                for (int j = 0; j < l.size(); j++) {
                    if (j % 3 == 0) temp.add(l.get(j));
                }
                Collections.sort(temp);
                result.add(temp.get(i / 3));
            }
        }
        return result;

    }
}

