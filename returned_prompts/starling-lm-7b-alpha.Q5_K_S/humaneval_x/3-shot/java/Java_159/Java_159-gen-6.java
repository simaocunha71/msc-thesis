        List<Integer> result = new ArrayList<>();
        result.add(number + Math.min(need, remaining));
        result.add(remaining - Math.min(need, remaining));
        return result;
    }
}

