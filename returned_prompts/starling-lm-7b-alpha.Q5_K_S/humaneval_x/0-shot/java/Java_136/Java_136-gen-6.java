        List<Optional<Integer>> res = new ArrayList<>();

        res.add(Optional.empty());
        res.add(Optional.empty());

        boolean foundNeg = false;
        boolean foundPos = false;

        for(int i = 0; i < lst.size(); i++){
            int num = lst.get(i);
            if(num < 0){
                foundNeg = true;
                if(res.get(0).isEmpty()) res.set(0, Optional.of(num));
                else res.set(0, Optional.of(Math.max(res.get(0).get(), num)));
            }
            if(num > 0){
                foundPos = true;
                if(res.get(1).isEmpty()) res.set(1, Optional.of(num));
                else res.set(1, Optional.of(Math.min(res.get(1).get(), num)));
            }
        }

        if(!foundNeg && !foundPos) return res;

        if(!foundPos && foundNeg){
            res.set(1, Optional.empty());
            return res;
        }

        if(!foundNeg && foundPos){
            res.set(0, Optional.empty());
            return res;
        }

        return res;
    }
}
































































































































































































