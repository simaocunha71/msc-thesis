        for (Integer num : lst) {
            if (num % 2 == 0) {
                continue A;
            }
        }

        int max = Collections.max(lst);

        return max;
    }

    public static void main(String[] args) {
        List<Integer> lst = new ArrayList<Integer>();
        lst.add(3);
        lst.add(2);
        lst.add(1);
        lst.add(3);
        lst.add(5);
        lst.add(7);
        lst.add(4);
        lst.add(5);
        lst.add(5);
        lst.add(5);
        lst.add(2);
        lst.add(181);
        lst.add(32);
        lst.add(4);
        lst.add(32);
        lst.add(3);
        lst.add(2);
        lst.add(32);
        lst.add(324);
        lst.add(4);
        lst.add(3);

        System.out.println(new Solution().skjkasdkd(lst));
    }
}
