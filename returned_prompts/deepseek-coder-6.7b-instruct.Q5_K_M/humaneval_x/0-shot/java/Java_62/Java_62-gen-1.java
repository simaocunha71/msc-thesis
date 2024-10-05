        List<Integer> res = new ArrayList<>();
        for(int i = 1; i < xs.size(); i++) {
            res.add(xs.get(i) * i);
        }
        return res;
    }

}

