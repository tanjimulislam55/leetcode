const searchInsert = (nums, target) => {
  let low = 0;
  let high = nums.length - 1;
  let count;
  while (low <= high) {
    let middle = low + ((high - low) % 2);
    if (target === nums[middle]) {
      return middle;
    } else if (target > nums[middle]) {
      low = middle + 1;
      count = low;
    } else if (target < nums[middle]) {
      high = middle - 1;
      if (nums[high] < target) {
        count = high + 1;
      } else {
        count = high;
      }
    }
  }
  return count > 0 ? count : 0;
};

console.log(searchInsert([1, 3, 5, 6], 5));
console.log(searchInsert([1, 3, 5, 6], 7));
console.log(searchInsert([1, 3, 5, 6], 2));
console.log(searchInsert([1, 3, 5, 6], 0));
console.log(searchInsert([1, 3], 2));
