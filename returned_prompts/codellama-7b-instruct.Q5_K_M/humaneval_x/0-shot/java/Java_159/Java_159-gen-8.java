        int total = number + remaining;
        if(total >= need) {
            return Arrays.asList(total - need, need);
        }
        return Arrays.asList(total, 0);

B:
        int total = number + remaining;
        if(total >= need) {
            return Arrays.asList(total - need, need);
        }
        return Arrays.asList(total, 0);
    }
}





