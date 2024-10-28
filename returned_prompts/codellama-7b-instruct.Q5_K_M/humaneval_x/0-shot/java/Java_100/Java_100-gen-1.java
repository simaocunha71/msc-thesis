        List<Integer> pile = new ArrayList<>();
        while (n > 0) {
            pile.add(n);
            n = n % 2 == 0 ? n - 1 : n - 2;
        }
        return pile;
    }

    public static void main(String[] args) {
        int n = 10;
        Solution s = new Solution();
        List<Integer> pile = s.makeAPile(n);
        System.out.println(pile);
    }
}


