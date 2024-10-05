        for (double g : grades) {
            if (g >= 4.0) return Arrays.asList("A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-");
            else if (g >= 3.7) return Arrays.asList("A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-");
            else if (g >= 3.3) return Arrays.asList("A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-");
            else if (g >= 3.0) return Arrays.asList("B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-");
            else if (g >= 2.7) return Arrays.asList("B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-");
            else if (g >= 2.3) return Arrays.asList("B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-");
            else if (g >= 2.0) return Arrays.asList("C+", "C", "C-", "D+", "D", "D-");
            else if (g >= 1.7) return Arrays.asList("C+", "C", "C-", "D+", "D", "D-");
            else if (g >= 1.3) return Arrays.asList("C+", "C", "C-", "D+", "D", "D-");
            else if (g >= 1.0) return Arrays.asList("D+", "D", "D-");
            else if (g >= 0.7) return Arrays