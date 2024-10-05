    let temp = [];
    let min = null;
    let min2 = null;
    for (let i = 0; i < lst.length; i++) {
        if (min === null || lst[i] < min) {
            min2 = min;
            min = lst[i];
        } else if (min2 === null || lst[i] < min2) {
            min2 = lst[i];
        }
    }
    return min2;
};

B:
let nextSmallest = function(arr) {
    let min = null;
    let min2 = null;
    for (let i = 0; i < arr.length; i++) {
        if (min === null || arr[i] < min) {
            min2 = min;
            min = arr[i];
        } else if (min2 === null || arr[i] < min2) {
            min2 = arr[i];
        }
    }
    return min2;
};

C:
function nextSmallest(input) {
    let min = null;
    let min2 = null;
    for (let i = 0; i < input.length; i++) {
        if (min === null || input[i] < min) {
            min2 = min;
            min = input[i];
        } else if (min2 === null || input[i] < min2) {
            min2 = input[i];
        }
    }
    return min2;
}

D:
function nextSmallest(lst) {
    var min = null;
    var min2 = null;
    for (var i = 0; i < lst.length; i++) {
        if (min === null || lst[i] < min) {
            min2 = min;
            min = lst[i];
        } else if (min2 === null || lst[i] < min2) {
            min2 = lst[i];
        }
    }
    return min2;
}

E:
def next_smallest(lst):
    min = None
    min2 = None