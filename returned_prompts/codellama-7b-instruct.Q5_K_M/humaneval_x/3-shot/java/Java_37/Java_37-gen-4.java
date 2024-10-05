        List<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) {
                result.add(l.get(i));
            } else {
                List<Integer> temp = l.subList(i, i + 1);
                Collections.sort(temp);
                result.add(temp.get(0));
            }
        }
        return result;
    }
}

