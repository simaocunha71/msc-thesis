        List<Integer> y = new ArrayList<Integer>();
        for (int i = 0; i < x.size(); i++) {
            boolean flag = false;
            for (int j = 0; j < x.get(i).toString().length(); j++) {
                if (Integer.parseInt(x.get(i).toString().charAt(j) + "") % 2 == 0) {
                    flag = true;
                }
            }
            if (!flag) {
                y.add(x.get(i));
            }
        }
        Collections.sort(y);
        return y;
    }
}
