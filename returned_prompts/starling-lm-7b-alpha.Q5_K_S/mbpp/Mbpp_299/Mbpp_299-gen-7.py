def max_aggregate(tuples):
    max_agg = (0,0)
    for t in tuples:
        if t[1] > max_agg[1]:
            max_agg = t
    return max_agg

def test_max_aggregate():
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)

test_max_aggregate()


# Took too long to solve this problem, but I will try to explain it in a bit more detail:

# Here's the solution in Python:

def max_aggregate(tuples):
    max_agg = (0,0)
    for t in tuples:
        if t[1] > max_agg[1]:
            max_agg = t
    return max_agg

# Here's the solution in Ruby:

def max_aggregate(tuples)
    max_agg = [0,0]
    tuples.each do |t|
        if t[1] > max_agg[1]
            max_agg = t
        end
    end
    return max_agg

# Here's the solution in JavaScript:

function max_aggregate(tuples) {
    var max_agg = [0,0];
    for (var i = 0; i < tuples.length; i++) {
        if (tuples[i][1] > max_agg[1]) {
            max_agg = tuples[i];
        }
    }
    return max_agg;
}

# Here's the solution in C++:

#include <iostream>
#include <algorithm>
#include <vector>
#include <tuple>

std::tuple<int, int> max_aggregate(std::vector<std::tuple<int, int>> tuples) {
    std::tuple<int, int> max_agg = {0, 0};