        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                List<Integer> sub_list = new ArrayList<>();
                for (int j = i; j < l.size(); j += 3) {
                    sub_list.add(l.get(j));
                }
                Collections.sort(sub_list);
                result.add(sub_list.get(0));
                i += 2;
            } else {
                result.add(l.get(i));
            }
        }
        return result;
    }
}

