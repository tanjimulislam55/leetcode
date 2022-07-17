function strStr(haystack = "", needle = "") {
  if (!haystack.includes(needle)) return -1;
  return haystack.split(needle)[0].length;
}

console.log(strStr("hello", "ll"));
console.log(strStr("aaaaa", "bba"));
