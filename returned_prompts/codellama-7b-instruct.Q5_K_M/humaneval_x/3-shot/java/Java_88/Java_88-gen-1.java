        if (array.size() == 0) return array;

        int sum = array.get(0) + array.get(array.size() - 1);

        if ((sum & 1) == 0) {
            Collections.sort(array, new Comparator<Integer>() {
                @Override
                public int compare(Integer o1, Integer o2) {
                    if (o1 < o2) return 1;
                    else if (o1 > o2) return -1;
                    else return 0;
                }
            });
        } else {
            Collections.sort(array, new Comparator<Integer>() {
                @Override
                public int compare(Integer o1, Integer o2) {
                    if (o1 < o2) return -1;
                    else if (o1 > o2) return 1;
                    else return 0;
                }
            });
        }
        return array;
    }
}

