        int len = l.size();
        if (len == 0) return 0.0;

        // sort the list
        Collections.sort(l);

        // find middle index
        int mid = len / 2;
        if (len % 2 == 0) {
            // even number of elements, average of middle two elements
            return (l.get(mid - 1) + l.get(mid)) / 2.0;
        } else {
            // odd number of elements, middle element only
            return l.get(mid);
        }
    }
}

