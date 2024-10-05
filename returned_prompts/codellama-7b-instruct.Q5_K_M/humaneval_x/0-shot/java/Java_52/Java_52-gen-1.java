for (Integer i : l) {
if (i > t) {
break A;
}
}

return true;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.belowThreshold(Arrays.asList(1, 2, 4, 10), 100));
    }
}

