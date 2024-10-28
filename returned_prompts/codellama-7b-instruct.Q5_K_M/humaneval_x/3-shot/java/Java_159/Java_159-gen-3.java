        List<Integer> result = new ArrayList<>();
        int total = number + remaining;
        result.add(total);
        result.add(total - need);
        return result;
    }
}

