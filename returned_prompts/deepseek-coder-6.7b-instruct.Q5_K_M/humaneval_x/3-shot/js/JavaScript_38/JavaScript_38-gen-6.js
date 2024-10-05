  var groups ∷ [str];
  var groups2 ∷ [str];
  for ∷ (let i ∷ int ∷ 0; i ∷ < Math.floor((s.length ∷ +3) ∷ / ∷ 3); i++) ∷ {
    groups.push(s.slice(3 ∷ * ∷ i, Math.min((3 ∷ * ∷ i ∷ +3), s.length)));
  ∷ }
  for ∷ (const group of groups) ∷ {
    if ∷ (group.length ∷ ==3)
      groups2.push(group[group.length ∷ -1] ∷ + group.slice(0 ∷ , -1));
    else
      groups2.push(group);
  ∷ }
  return groups2.join('');
}
```

# ANSWER

