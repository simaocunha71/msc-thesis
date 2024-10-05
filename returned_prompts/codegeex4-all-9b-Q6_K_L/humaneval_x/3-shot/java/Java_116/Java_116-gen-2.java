        Collections.sort(arr, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                int count1 = Integer.bitCount(o1);
                int count2 = Integer.bitCount(o2);
                if (count1 != count2) return count1 - count2;
                else return o1 - o2;
            }
        });
        return arr;
    }
}

