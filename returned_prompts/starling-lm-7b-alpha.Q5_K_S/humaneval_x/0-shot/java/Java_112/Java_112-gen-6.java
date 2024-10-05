        // Write Your Code here
        List<Object> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder(s);
        for (int i = 0; i < sb.length(); i++) {
            boolean found = false;
            for (int j = 0; j < c.length(); j++) {
                if (sb.charAt(i) == c.charAt(j)) {
                    sb.deleteCharAt(i);
                    found = true;
                    break;
                }
            }
            if (!found) {
                continue;
            }
            i--;
        }
        StringBuilder sbReverse = new StringBuilder(sb.toString());
        sbReverse.reverse();
        if (sb.toString().equals(sbReverse.toString())) {
            result.add(sb.toString());
            result.add(true);
        } else {
            result.add(sb.toString());
            result.add(false);
        }
        return result;
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution solution = new Solution();
        String s = sc.nextLine();
        String c = sc.nextLine();
        List<Object> result = solution.reverseDelete(s, c);
        System.out.println(result.get(0));
        System.out.println(result.get(1));
    }
}



```

