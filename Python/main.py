import keyword
import re

from TaskScheduler import TaskScheduler


def is_valid_identifier(s: str) -> bool:
    # bool(s): Kiểm tra giá trị truthy hay falsy (str nên chỉ có None, "")
    # keyword.iskeyword(s): Kiểm tra xem s có phải là một từ khóa của Python hay không
    # bool(re.match(r'^[A-Za-z0-9_]+$', s): Kiểm tra xem chuỗi s chỉ chứa chữ cái, số và dấu gạch dưới _ hay không
    return bool(s) and not s[0].isdigit() and not keyword.iskeyword(s) and bool(re.match(r'^[A-Za-z0-9_]+$', s))


def group_anagrams(words: list[str]) -> list[list[str]]:
    # Tạo một dictionary để nhóm các từ có cùng nhóm
    # Key: chuỗi sau khi sắp xếp ký tự (ví dụ "ate" -> "aet")
    # Value: danh sách các từ có cùng 1 key
    dictionary: dict[str, list[str]] = {}
    for word in words:
        # Sắp xếp ký tự trong từ -> xác định nhóm
        key: str = ''.join(sorted(word))
        # Nếu key chưa có trong dictionary thì khởi tạo một danh sách mới
        if key not in dictionary:
            temp: list[str] = [word]  # tạo list chứa từ hiện tại
            dictionary[key] = temp  # gán list đó cho key mới
        else:
            # Nếu key đã tồn tại, thêm từ vào nhóm key đó
            dictionary[key].append(word)
    # Trả về danh sách tất cả các nhóm, 1 nhóm là value của 1 key trong dictionary
    return list(dictionary.values())


def f1(): return 1


def f2(): return "hello"


def f3(): raise RuntimeError("k")


if __name__ == '__main__':
    # Test is_valid_identifier
    print(is_valid_identifier("var"))  # true
    print(is_valid_identifier("var_123"))  # true
    print(is_valid_identifier("_var"))  # true
    print(is_valid_identifier("va3r12"))  # true
    print(is_valid_identifier("123var"))  # false
    print(is_valid_identifier("var-123"))  # false
    print(is_valid_identifier("for"))  # false
    print(is_valid_identifier(""))  # false
    print(is_valid_identifier("None"))  # false

    # Test group_anagrams
    print(
        group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print(group_anagrams(["a1b", "b1a", "ab1", "123", "321", "213", "a2b",
                          "b2a"]))  # [['a1b', 'b1a', 'ab1'], ['123', '321', '213'], ['a2b', 'b2a']]
    print(group_anagrams(["aabb", "bbaa", "abab", "aab", "baa"]))  # [['aabb', 'bbaa', 'abab'], ['aab', 'baa']]
    print(group_anagrams(
        ["abc123", "321cba", "a1b2c3", "aabb11", "b1a1ab"]))  # [['abc123', '321cba', 'a1b2c3'], ['aabb11', 'b1a1ab']]
    print(group_anagrams(["", "a", "b", "a", ""]))  # [['', ''], ['a', 'a'], ['b']]
    print(group_anagrams(["Ab1", "bA1", "1aB", "ab1"]))  # [['Ab1', 'bA1'], ['1aB'], ['ab1']]

    # Test class TaskSchedule
    s = TaskScheduler()
    s.add_task("t1", f1)
    s.add_task("t2", f2)
    s.add_task("t3", f3)
    print(s.get_results())
    s.run_all()
    print(s.get_results())
