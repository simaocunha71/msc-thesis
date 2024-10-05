  var largest_prime = -1;
  var largest_prime_sum = -1;
  var sum = 0;

  for (var i = 0; i < lst.length; i++) {
    if (isPrime(lst[i])) {
      sum = 0;
      var num = lst[i];
      while (num > 0) {
        sum += num % 10;
        num = Math.floor(num / 10);
      }
      if (sum > largest_prime_sum) {
        largest_prime = lst[i];
        largest_prime_sum = sum;
      }
    }
  }

  return largest_prime;
}



