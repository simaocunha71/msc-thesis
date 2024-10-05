        int sum = 0;
        for (int i = 0; i < q.size(); i++) {
            sum += q.get(i);
        }
        if (sum > w) return false;
        String str = q.toString();
        if (!str.equals(new StringBuilder(str).reverse().toString())) return false;
        return true;
    }
}

