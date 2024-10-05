        List<Integer> res = new ArrayList<>();
        Collections.sort(arr);
        for(int i = 0; i<k; i++) {
            res.add(arr.get(arr.size() - i - 1));
        }
        return res;
    }

    public List<Integer> maximum2(List<Integer> arr, int k) {
        Collections.sort(arr);
        Collections.reverse(arr);
        return arr.subList(0, k);
    }

    public List<Integer> maximum3(List<Integer> arr, int k) {
        Collections.sort(arr);
        return arr.subList(arr.size() - k, arr.size());
    }

    public List<Integer> maximum4(List<Integer> arr, int k) {
        Collections.sort(arr, Collections.reverseOrder());
        return arr.subList(0, k);
    }

    public List<Integer> maximum5(List<Integer> arr, int k) {
        List<Integer> res = new ArrayList<>();
        for(int i = 0; i<k; i++) {
            res.add(arr.get(arr.size() - i - 1));
        }
        return res;
    }

    public List<Integer> maximum6(List<Integer> arr, int k) {
        List<Integer> res = new ArrayList<>();
        for(int i = arr.size() - k; i<arr.size(); i++) {
            res.add(arr.get(i));
        }
        return res;
    }
}





































































































































