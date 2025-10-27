class TaskScheduler:
    def __init__(self):
        self.taskDict = {}

    def add_task(self, name: str, func: callable):
        if name in self.taskDict:
            raise ValueError(f"Task '{name}' already exists")
        self.taskDict[name] = {"func": func, "res": None}

    def remove_task(self, name: str):
        if name not in self.taskDict:
            raise KeyError(f"Task '{name}' does not exist")
        self.taskDict.pop(name)

    def run_all(self):
        for name, obj in self.taskDict.items():
            try:
                obj["res"] = obj["func"]()
            except Exception as e:
                obj["res"] = f"{type(e).__name__}: {e}"

    def get_results(self) -> dict[str, object]:
        return {name: obj["res"] for name, obj in self.taskDict.items()}
