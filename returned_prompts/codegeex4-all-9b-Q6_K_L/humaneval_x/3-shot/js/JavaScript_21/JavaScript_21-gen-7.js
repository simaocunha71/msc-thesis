  let min = Math.min(...numbers);
  let max = Math.max(...numbers);

  return numbers.map((x) => (x - min) / (max - min));
}

Please review and provide feedback for the above code.