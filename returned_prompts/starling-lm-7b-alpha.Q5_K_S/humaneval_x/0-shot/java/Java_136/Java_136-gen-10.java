    List<Optional<Integer>> res = new ArrayList<>();

    Optional<Integer> a = Optional.empty();
    Optional<Integer> b = Optional.empty();

    if(lst.size() == 0) {
        res.add(a);
        res.add(b);
        return res;
    }

    for(int i : lst) {
        if(i < 0 && a.isPresent()) {
            if(i > a.get()) {
                a = Optional.of(i);
            }
        }
        else if(i < 0 && !a.isPresent()) {
            a = Optional.of(i);
        }

        if(i > 0 && b.isPresent()) {
            if(i < b.get()) {
                b = Optional.of(i);
            }
        }
        else if(i > 0 && !b.isPresent()) {
            b = Optional.of(i);
        }
    }

    res.add(a);
    res.add(b);

    return res;
    }
}






















































































































































































































































