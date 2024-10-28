        List<Integer> result = new ArrayList<>();
        int quotient = x;
        int remainder = 0;
        while (quotient > 0) {
            remainder = quotient % base;
            quotient /= base;
            result.add(remainder);
        }
        StringBuilder sb = new StringBuilder();
        for (int i = result.size() - 1; i >= 0; i--) {
            sb.append(result.get(i));
        }
        return sb.toString();
    }
}

