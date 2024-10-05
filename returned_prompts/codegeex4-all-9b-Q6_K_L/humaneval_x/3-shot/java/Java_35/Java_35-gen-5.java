        int max = Integer.MIN_VALUE;
        for(int i = 0; i < l.size(); i++) {
            if(max < l.get(i)) {
                max = l.get(i);
            }
        }
        return max;
    }
}

