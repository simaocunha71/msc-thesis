        List<Integer> res = new ArrayList<>();

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0) {
                if (res.size() == 0) {
                    res.add(arr.get(i));
                    res.add(i);
                } else {
                    if (res.get(0) > arr.get(i)) {
                        res.clear();
                        res.add(arr.get(i));
                        res.add(i);
                    } else if (res.get(0) == arr.get(i)) {
                        if (res.get(1) > i) {
                            res.clear();
                            res.add(arr.get(i));
                            res.add(i);
                        }
                    }
                }
            }
        }

        if (res.size() == 0) {
            return res;
        } else {
            return res;
        }


    }
}



























































































































































































































































