        List<Integer> result = new ArrayList<Integer>();
        int total = number + remaining;
        if (total >= need) {
            result.add(total - need);
            result.add(0);
        } else {
            result.add(total);
            result.add(remaining - need + total);
        }
        return result;
    }
}

