        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) < lst.get(i - 1)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        List<Integer> lst = new ArrayList<Integer>();
        lst.add(1);
        lst.add(2);
        lst.add(2);
        lst.add(3);
        lst.add(4);
        lst.add(5);
        System.out.println(s.isSorted(lst));
    }
}


