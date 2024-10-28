        List<Integer> result = new ArrayList<>();
        int eaten = number + remaining;
        int left = eaten - need;
        result.add(eaten);
        result.add(left);
        return result;
    }
}

