import argparse
from Analyzer.interface import get_analyzer, analyzers

def main():
    analyzer_names = analyzers
    parser = argparse.ArgumentParser(description="Run an analyzer on activity data.")
    parser.add_argument("--analyzer", type=str, choices=analyzer_names, default="Superanalyzer",
                        help=f"The analyzer to use (default: Superanalyzer). Available analyzers: {', '.join(analyzer_names)}")
    args = parser.parse_args()

    analyzer = get_analyzer(args.analyzer)
    data = analyzer.load_activities()
    print(analyzer.analyze(data))

if __name__ == "__main__":
    main()