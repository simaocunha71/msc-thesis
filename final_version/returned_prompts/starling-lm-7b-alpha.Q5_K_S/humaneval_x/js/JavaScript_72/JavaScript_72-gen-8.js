  let q_sum = q.reduce((a, b) => a + b, 0);
  let q_length = q.length;
  let q_mid = Math.floor(q_length / 2);

  return (
    q_length % 2 === 0 && q.slice(0, q_mid).join('') === q.slice(q_mid + 1).join('') && q_sum <= w
  );
}



