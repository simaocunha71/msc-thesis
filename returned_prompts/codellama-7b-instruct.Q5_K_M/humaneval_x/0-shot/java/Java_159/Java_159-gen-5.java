        List<Integer> res = new ArrayList();
        int total = number + remaining;
        int eat = total >= need ? need : total;
        res.add(total);
        res.add(remaining - eat);
        return res;

B:
        List<Integer> res = new ArrayList();
        int total = number + remaining;
        int eat = total >= need ? need : total;
        res.add(total);
        res.add(remaining - eat);
        return res;
    }
}
