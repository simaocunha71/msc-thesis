
    sort.Float64s(numbers)
    min_diff := math.MaxFloat64
    result := [2]float64{}

    for i := 0; i < len(numbers) - 1; i++ {
        if diff := numbers[i+1] - numbers[i]; diff < min_diff {
            min_diff = diff
            result[0] = numbers[i]
            result[1] = numbers[i+1]
        }
    }
    return result
}


```



## Kotlin

```kotlin
fun findClosestElements(numbers: List<Double>): Pair<Double, Double> {
    val sortedNumbers = numbers.sorted()
    var minDiff = Double.MAX_VALUE
    var result = Pair(0.0, 0.0)

    for (i in 0 until sortedNumbers.size - 1) {
        val diff = sortedNumbers[i + 1] - sortedNumbers[i]
        if (diff < minDiff) {
            minDiff = diff
            result = Pair(sortedNumbers[i], sortedNumbers[i + 1])
        }
    }

    return result
}
```


## Perl

```perl
use strict;
use warnings;
use List::Util qw(min);

sub find_closest_elements {
    my @numbers = sort { $a <=> $b } @{$_[0]};
    my ($min_diff, $result) = ($numbers[1] - $numbers[0], [$numbers[0], $numbers[1]]);

    for (my $i = 0; $i < @numbers - 1; $i++) {
        my $diff = $numbers[$i + 1] - $numbers[$i];
        if ($diff < $min_diff) {
            $min_diff = $diff;
            @{$result} = ($numbers[$i], $numbers[$i + 1]);
        }
    }

    return @{$result