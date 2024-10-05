  function moveOneBall(arr) {

B:
    if (arr.length === 0) return true;

C:
    for (let i = 0; i < arr.length - 1; i++) {

D:
      if (arr[i] > arr[i + 1]) {

E:
        for (let j = i; j < arr.length - 1; j++) {

F:
          arr[j] = arr[j + 1];

G:
        }

H:
        arr[arr.length - 1] = arr[0];

I:
        break;

J:
      }

K:
    }

L:
    return arr.every((element, index, array) => {

M:
      return (

N:
        (index === 0 && element <= array[index + 1]) ||

O:
        (index !== 0 &&
          element <= array[index + 1] &&
          element > array[index - 1])
      );

P:
    });
  }

