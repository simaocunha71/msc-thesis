        // Check if list size is odd or even
        if (l.size() % 2 == 0) {
            // Even
            // Find the middle index
            int middle = l.size() / 2;
            return (l.get(middle - 1) + l.get(middle)) / 2.0;
        } else {
            // Odd
            // Find the middle index
            int middle = l.size() / 2;
            return l.get(middle);
        }
    }
}

