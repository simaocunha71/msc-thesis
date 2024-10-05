        List<Integer> list = new ArrayList<Integer>();

        int start1 = interval1.get(0);
        int end1 = interval1.get(1);
        int start2 = interval2.get(0);
        int end2 = interval2.get(1);

        if (start1 > end2 || start2 > end1) {
            return "NO";
        }

        if (start1 < start2) {
            start1 ^= start2;
            start2 ^= start1;
            start1 ^= start2;
            end1 ^= end2;
            end2 ^= end1;
            end1 ^= end2;
        }

        for (int i = start1; i <= end1; i++) {
            list.add(i);
        }

        int len = list.size();
        boolean isPrime = true;
        for (int i = 2; i * i <= list.size(); i++) {
            if (len % i == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) {
            return "YES";
        } else {
            return "NO";
        }

        // return isPrime ? "YES" : "NO";

    }
}



































































































































































































