# Hash Table
Hash table is a data structure that is used to store data with key-value pairs. It uses a hash function to compute an index into an array in which an element will be inserted or searched. Time complexity of Hash Table is O(1) (https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/)


Hash Table in programming language:
- Java: HashMap
- Ruby: Hash
- Python: Dictionary
- JavaScript: Object

## LeetCode two_sum
Given an array of integers `nums` and an integer `target`, return _indices of the two numbers such that they add up to `target`_ . 

You may assume that each input would have __exactly one solution__, and may not use the _same_ element twice.

You can return the answer in any order.

### Example 1:
```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

### Example 2:
```
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
```

### Example 3:
```
Input: nums = [3, 3], target = 6
Output: [0, 1]
```

### Constraints:
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- __Only one valid answer exists.__