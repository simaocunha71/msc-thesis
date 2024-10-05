        List<String> res = new ArrayList<>();
        for (String s : lst) {
            int count = 0;
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) % 2 != 0)
                    count++;
            }
            res.add("the number of odd elements " + count + "n the str" +
                    (count % 10) + "ng " + count + " of the " +
                    (count % 10) + "nput.");
        }
        return res;
    }
}
