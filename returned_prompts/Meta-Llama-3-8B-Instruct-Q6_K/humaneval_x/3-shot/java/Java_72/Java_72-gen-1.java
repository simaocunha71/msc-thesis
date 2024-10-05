        if (!isBalanced(q)) {
            return false;
        }
        int sum = 0;
        for (int i : q) {
            sum += i;
        }
        return sum <= w;
    }

    private boolean isBalanced(List<Integer> q) {
        StringBuilder sb = new StringBuilder();
        for (int i : q) {
            sb.append(i);
            if (!sb.toString().equals(sb.reverse().toString())) {
                return false;
            }
            sb.setLength(0);
        }
        return true;
    }
}

