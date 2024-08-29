  const start1 = interval1[0];
  const end1 = interval1[1];
  const start2 = interval2[0];
  const end2 = interval2[1];

  if (start1 > end1) {
    return intersection([start1, end1], [start2, end2]);
  }
  if (start2 > end2) {
    return intersection([start1, end1], [start2, end2]);
  }
  if (start2 <= start1 && start1 <= end2 && end1 <= end2) {
    return "NO";
  }
  if (start2 <= end1 && end1 <= end2 && start1 <= start2 && start2 <= end2) {
    return "NO";
  }
  if (start1 <= start2 && end2 <= end1 && start2 <= end1 && end1 <= end2) {
    return "NO";
  }
  if (start1 <= end2 && end2 <= end1 && start2 <= start1 && end1 <= end2) {
    return "NO";
  }
  if ((end1 - start1) % 2 == 0) {
    return "NO";
  }
  if ((end2 - start2) % 2 == 0) {
    return "NO";
  }
  if (start2 <= start1 && end1 <= end2) {
    return "NO";
  }
  if (start2 <= end1 && end1 <= end2) {
    return "NO";
  }
  if (end2 <= start1 && start1 <= end2) {
    return "NO";
  }
  if (end2 <= end1 && start1 <= end2) {
    return "NO";
  }
  if (end2 == start2 && start2 > start1 && start2 < end1) {
    return "NO";
  }
  if (end2 == start2 && start2 < start1 && start2 > end1) {
    return "NO";
  }
  if (start2 == end2 && start2 > start1 && start2 < end1) {
    return "NO";
  }
  if (