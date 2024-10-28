        int start = 0, end = num.length() - 1;
        while (start <= end) {
            if (num.charAt(start) != num.charAt(end)) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
}

