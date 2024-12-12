from Scraper.scraper import Scraper
import argparse

def main():
    parser = argparse.ArgumentParser(description="Scrape activities and save to JSON.")
    parser.add_argument("--start_week", type=int, default=1, help="The starting week number (default: 1)")
    parser.add_argument("--end_week", type=int, default=52, help="The ending week number (default: 52)")
    args = parser.parse_args()

    scraper = Scraper()
    scraper.count_all_activities_and_save_to_json(args.start_week, args.end_week)

if __name__ == "__main__":
    main()