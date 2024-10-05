        List<Integer> list = new ArrayList<>();

        int eat = number + need;
        int left = remaining - eat;

        list.add(eat);
        list.add(left);

        return list;
    }
}
