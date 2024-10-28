        List<Integer> result = new ArrayList<Integer>();
        int total = number + remaining;
        int left = total - need;
        result.add(total);
        result.add(left);
        return result;
    }
}

