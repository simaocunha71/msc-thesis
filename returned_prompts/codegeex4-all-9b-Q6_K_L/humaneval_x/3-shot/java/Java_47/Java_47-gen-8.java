        Collections.sort(l);
        int middle = l.size() / 2;
        if (l.size() % 2 == 1) return l.get(middle);
        else return (l.get(middle - 1) + l.get(middle)) / 2.0;
    }
}

