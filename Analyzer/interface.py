from abc import ABC, abstractmethod
import json

class Analyzer(ABC):
    @abstractmethod
    def analyze(self, data):
        pass
    def load_activities(self):
        with open("activities.json", "r") as f:
            return json.load(f)

analyzers = ["Superanalyzer","AveragePerWeek", "MostOftenTime", "MostOftenDay","MostOftenWeekday", "MostOftenWeekend", "MostOftenMonth"]

class Superanalyzer(Analyzer):
    def __init__(self, *args, **kwds):
        self.analyzers = [get_analyzer(name) for name in analyzers if name != "Superanalyzer"]
    def analyze(self, data):
        return {a.__class__.__name__: a.analyze(data) for a in self.analyzers}

# factory method 
def get_analyzer(name):
    if name in analyzers:
        if name == "Superanalyzer":
            return Superanalyzer()
        elif name == "AveragePerWeek":
            from Analyzer.Analyzers import AveragePerWeek
            return AveragePerWeek()
        elif name == "MostOftenTime":
            from Analyzer.Analyzers import MostOftenTime
            return MostOftenTime()
        elif name == "MostOftenDay":
            from Analyzer.Analyzers import MostOftenDay
            return MostOftenDay()
        elif name == "MostOftenWeekday":
            from Analyzer.Analyzers import MostOftenWeekday
            return MostOftenWeekday()
        elif name == "MostOftenWeekend":
            from Analyzer.Analyzers import MostOftenWeekend
            return MostOftenWeekend()
        elif name == "MostOftenMonth":
            from Analyzer.Analyzers import MostOftenMonth
            return MostOftenMonth()
    else:
        print("Invalid analyzer name")
