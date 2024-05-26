class DataAnalyzer:
    def __init__(self, data):
        self.data = data
        self.total = None
        self.count = None

    def _ensure_calculated(self):
        if self.total is None or self.count is None:
            self.total = sum(self.data)
            self.count = len(self.data)

    def calculate_total(self):
        self._ensure_calculated()
        return self.total

    def calculate_average(self):
        self._ensure_calculated()
        return self.total / self.count if self.count != 0 else 0

    def calculate_minimum(self):
        return min(self.data) if self.data else None

    def calculate_maximum(self):
        return max(self.data) if self.data else None
