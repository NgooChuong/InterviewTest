function isValidBracketString(s) {
  // Sử dụng mảng như stack
  const stack = [];
  // Duyệt từng ký tự trong chuỗi
  for (const c of s) {
    // Nếu là dấu mở → push vào stack
    if (c === "(" || c === "{" || c === "[") stack.push(c);
    else {
      // Nếu là dấu đóng nhưng stack rỗng -> không hợp lệ
      if (stack.length === 0) return false;
      // Lấy dấu mở cuối cùng ra để so sánh
      const top = stack.pop();
      // Kiểm tra xem dấu đóng có khớp với dấu mở không
      if (
        (c === ")" && top !== "(") ||
        (c === "}" && top !== "{") ||
        (c === "]" && top !== "[")
      ) {
        return false;
      }
    }
  }
  // Nếu sau khi duyệt hết, stack còn phần tử -> không hợp lệ
  return stack.length === 0;
}

function topKFrequent(nums, k) {
  // Đếm tần suất xuất hiện của từng phần tử lưu dưới dạng: {num: frequency}
  const count = {};
  for (const num of nums) {
    // Nếu num chưa xuất hiện, khởi tạo 0 rồi +1
    count[num] = (count[num] || 0) + 1;
  }
  // Chuyển object thành array để sắp xếp, array có dạng: [[num, frequency], ...]
  const entries = Object.entries(count);
  // Sắp xếp giảm dần theo tần suất (frequency)
  entries.sort((a, b) => b[1] - a[1]);
  // Lấy k phần tử đầu sau khi sắp xếp
  return entries.slice(0, k).map((entry) => Number(entry[0]));
}

class LRUCache {
  // Khởi tạo LRUCache với sức chứa capacity
  constructor(capacity) {
    this._capacity = capacity;
    this._cache = {};
  }

  get(key) {
    if (!this._cache.hasOwnProperty(key)) return -1;
    // Cập nhật thời gian sử dụng cuối cùng bằng performance.now() chính xác hơn
    this._cache[key].lastUsed = performance.now();
    return this._cache[key].value;
  }

  put(key, value) {
    // Lấy thời gian hiện tại bằng performance.now() để chính xác hơn
    const currentTime = performance.now();

    if (this._cache.hasOwnProperty(key)) {
      // Key đã tồn tại → chỉ cập nhật value và lastUsed
      this._cache[key].value = value;
      this._cache[key].lastUsed = currentTime;
      return;
    }

    if (Object.keys(this._cache).length >= this._capacity) {
      // Cache đầy -> tìm key ít được dùng gần đây nhất (lastUsed nhỏ nhất)
      let keyToDelete = null;
      let oldestTime = Infinity;

      for (const [k, v] of Object.entries(this._cache)) {
        if (v.lastUsed < oldestTime) {
          oldestTime = v.lastUsed;
          keyToDelete = k;
        }
      }
      // Xóa key ít được dùng gần đây nhất
      delete this._cache[keyToDelete];
    }

    // Thêm key mới
    this._cache[key] = {
      value: value,
      lastUsed: currentTime,
    };
  }
}

console.log(isValidBracketString("()")); // true
console.log(isValidBracketString("()[]{}")); // true
console.log(isValidBracketString("(]")); // false
console.log(isValidBracketString("([)]")); // false
console.log(isValidBracketString("{[]}")); // true
console.log(isValidBracketString("")); // true
console.log(isValidBracketString("(")); // false

// Test topKFrequent
console.log(topKFrequent([1, 1, 1, 2, 2, 3], 2)); // [1, 2]
console.log(topKFrequent([4, 4, 4, 4, 5, 5, 6], 1)); // [4]

// Test class LRUCache
const cache = new LRUCache(2);
cache.put(1, 1);
cache.put(2, 2);
console.log(cache.get(1)); // 1
cache.put(3, 3); // loại bỏ key=2
console.log(cache.get(2)); // -1
cache.put(4, 4);
console.log(cache.get(2)); // -1
cache.put(4, 4); // loại bỏ key=1
console.log(cache.get(1)); // -1
console.log(cache.get(3)); // 3
console.log(cache.get(4)); // 4
