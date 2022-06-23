function* zip(...iterables) {
  let iterators = iterables.map((i) => i[Symbol.iterator]());
  while (true) {
    let results = iterators.map((iter) => iter.next());
    if (results.some((res) => res.done)) return;
    else yield results.map((res) => res.value);
  }
}

const longestCommonPrefix = (strs) => {
  let stack = [];
  for (x of zip(...strs)) {
    if (new Set(x).size === 1) {
      stack.push(x[0]);
    } else {
      break;
    }
  }
  return stack.length > 0 ? stack.join("") : "";
};

console.log(longestCommonPrefix(["flower", "flow", "flight"]));
console.log(longestCommonPrefix(["dog", "racecar", "car"]));
