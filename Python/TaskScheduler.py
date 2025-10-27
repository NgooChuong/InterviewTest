class TaskScheduler:
    def __init__(self):
        # Khởi tạo dict lưu trữ các task, và kết quả của task với key là name;
        self.taskDict = {}

    def add_task(self, name: str, func: callable):
        # Nếu task đã tồn tại, raise lỗi
        if name in self.taskDict:
            raise ValueError(f"Task '{name}' already exists")
        # Thêm task mới vào dict với func và giá trị kết quả ban đầu là None
        self.taskDict[name] = {"func": func, "res": None}

    def remove_task(self, name: str):
        # Nếu task không tồn tại, raise lỗi
        if name not in self.taskDict:
            raise KeyError(f"Task '{name}' does not exist")
        # Xóa task khỏi dict thông qua name
        self.taskDict.pop(name)

    def run_all(self):
        # Duyệt qua tất cả các task trong dict
        for name, obj in self.taskDict.items():
            try:
                # Chạy hàm func của task và lưu kết quả vào 'res'
                obj["res"] = obj["func"]()
            except Exception as e:
                # Nếu hàm func ném lỗi, lưu thông tin lỗi vào 'res'
                obj["res"] = f"{type(e).__name__}: {e}"

    def get_results(self) -> dict[str, object]:
        # Trả về một dict chỉ chứa tên task và kết quả 'res'
        return {name: obj["res"] for name, obj in self.taskDict.items()}
