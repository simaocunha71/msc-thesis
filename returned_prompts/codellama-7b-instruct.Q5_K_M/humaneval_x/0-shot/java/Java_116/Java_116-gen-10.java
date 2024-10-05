        List<Integer> ans = new ArrayList<Integer>();
        for(int i=0; i<arr.size(); i++) {
            ans.add(arr.get(i));
        }
        ans.sort(new Comparator<Integer>() {
            public int compare(Integer o1, Integer o2) {
                if(o1.intValue() == o2.intValue())
                    return o1.intValue()-o2.intValue();
                if(Integer.bitCount(o1) == Integer.bitCount(o2))
                    return o1.intValue()-o2.intValue();
                return Integer.bitCount(o2) - Integer.bitCount(o1);
            }
        });
        return ans;
    }
}
