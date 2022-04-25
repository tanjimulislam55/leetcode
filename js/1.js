/*approach 1*/
const twoSum = function(nums, target) {
    const hashmap = {}
    nums.map((num, index) => {
        const key = target - num
        if (key in hashmap) result = [hashmap[key], index]
        else hashmap[num] = index 
    })
    return result
};

/*approach 2*/
const twoSum = function(nums, target) {
    const hashmap = {}
    for (const [count, value] of nums.entries()) {
        const key = target - value
        if (key in hashmap) return [hashmap[key], count]
        hashmap[value] = count
    }
};

console.log(twoSum([2, 7, 11, 15], 9))