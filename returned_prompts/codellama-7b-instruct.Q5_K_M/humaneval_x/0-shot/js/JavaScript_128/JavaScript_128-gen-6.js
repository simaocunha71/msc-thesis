
function prodSigns(arr) {

    if (arr.length === 0) return null;

    let sum = 0;
    let product = 1;

    for (let i = 0; i < arr.length; i++) {

        let sign = arr[i] > 0 ? 1 : (arr[i] < 0 ? -1 : 0);

        sum += Math.abs(arr[i]) * sign;
        product *= sign;
    }

    return product * sum;
}

B:

function prodSigns(arr) {

    if (arr.length === 0) return null;

    let result = 0;
    let sign = 1;

    for (let i = 0; i < arr.length; i++) {
        let abs = Math.abs(arr[i]);
        let sgn = arr[i] > 0 ? 1 : (arr[i] < 0 ? -1 : 0);
        result += sgn * abs;
        sign *= sgn;
    }

    return sign * result;
}