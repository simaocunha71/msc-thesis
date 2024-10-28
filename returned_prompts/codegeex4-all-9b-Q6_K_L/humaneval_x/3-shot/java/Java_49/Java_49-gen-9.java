        List<Double> sorted_numbers = new ArrayList<>(numbers);
        Collections.sort(sorted_numbers);

        for (int i = 0; i < sorted_numbers.size() - 1; i++) {
            double distance = sorted_numbers.get(i + 1) - sorted_numbers.get(i);
            if (distance < threshold) return true;
        }
        return false;
    }
}

import java.util.*;
import