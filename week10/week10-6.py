class Solution:
    def average(self, salary: List[int]) -> float:
        total = sum(salary)-max(salary)-min(salary)
        N = len(salary) - 2
        return total/N