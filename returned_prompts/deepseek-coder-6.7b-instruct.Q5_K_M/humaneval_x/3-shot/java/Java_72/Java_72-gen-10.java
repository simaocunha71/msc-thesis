        int sum 		= q.stream().mapToInt(Integer::intValue).sum();
        boolean balanced = q.equals(new ArrayList<>(new ArrayList<>(q) {{Collections.reverse(this);}}));

        return sum <= w && balanced;
    }
}

