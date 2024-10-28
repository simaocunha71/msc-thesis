        if (xs.size() % 2 != 0) {
            throw new IllegalArgumentException("xs must have even number of coefficients");
        }

        while (true) {
            double a = 0;
            for (int i = 0; i < xs.size(); i++) {
                a += Math.abs(xs.get(i));
            }
            if (a < 0.000000000000001) {
                return -0.5;
            }
            // remove smallest coefficient
            int smallest = 0;
            for (int i = 0; i < xs.size(); i++) {
                if (xs.get(i) < xs.get(smallest)) {
                    smallest = i;
                }
            }
            xs.remove(smallest);
        }
    }
}



// Created by Administrator on 2016-09-08.


/**
 * Created by Administrator on 2016-09-08.
 */



public class Main {


    public static void main(String[] args) {

        List<Double> xs = new ArrayList<>();
        xs.add(1.0);
        xs.add(2.0);
        System.out.println(new Solution().findZero(xs));
        xs.clear();
        xs.add(-6.0);
        xs.add(11.0);
        xs.add(-6.0);
        xs.add(1.0);
        System.out.println(new Solution().findZero(xs));

    }
}

```
