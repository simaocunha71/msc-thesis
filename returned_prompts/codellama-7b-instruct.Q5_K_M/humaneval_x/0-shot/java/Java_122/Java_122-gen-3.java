        int sum = 0;
        int count = 0;
        int max = 0;
        for (int i = 0; i < k; i++) {
            max = Math.max(max, arr.get(i));
            count++;
            sum += arr.get(i);
        }
        if (count >= k) {
            return sum;
        }

        for (int i = k; i < arr.size(); i++) {
            if (arr.get(i) <= max) {
                sum += arr.get(i);
                count++;
            }
            if (count >= k) {
                break A;
            }
        }
        return sum;
    }
}

B:
        int sum = 0;
        for (int i = 0; i < k && i < arr.size(); i++) {
            sum += arr.get(i);
        }
        return sum;
    }
}

C:
        int sum = 0;
        for (int i = 0; i < k && i < arr.size(); i++) {
            sum += arr.get(i);
        }
        return sum;
    }
}

D:
        int sum = 0;
        for (int i = 0; i < k && i < arr.size(); i++) {
            sum += arr.get(i);
        }
        return sum;
    }
}

E:
        int sum = 0;
        int count = 0;
        for (int i = 0; i < k && i < arr.size(); i++) {
            count++;
            sum += arr.get(i);
        }
        if (count >= k) {
            return sum;
        }

        for (int i = k; i < arr.size(); i++) {
            sum += arr.get(i);
            count++;
            if (count >= k) {
                break;
            }
        }
        return sum;
    }
}

F:
        int sum = 0;
        for (int i = 0; i < k && i < arr