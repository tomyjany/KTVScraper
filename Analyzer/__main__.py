from Analyzer.interface import get_analyzer
if __name__ == "__main__":
    analyzer = get_analyzer("Superanalyzer")
    data = analyzer.load_activities()
    print(analyzer.analyze(data))