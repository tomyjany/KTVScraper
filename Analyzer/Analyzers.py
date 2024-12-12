from Analyzer.interface import Analyzer

class AveragePerWeek(Analyzer):
    def analyze(self, data):
        averages = {}
        for activity, details in data.items():
            total_count = details['count']
            weeks = set(metadata['week'] for metadata in details['metadata'])
            num_weeks = len(weeks)
            average_per_week = total_count / num_weeks if num_weeks > 0 else 0
            averages[activity] = average_per_week
        return averages
class MostOftenTime(Analyzer):
    def analyze(self, data):
        most_often_time = {}
        for activity, details in data.items():
            time_counts = {}
            for metadata in details['metadata']:
                time = metadata['time']
                if time != "N/A":
                    if time in time_counts:
                        time_counts[time] += 1
                    else:
                        time_counts[time] = 1
            most_often_time[activity] = max(time_counts, key=time_counts.get) if time_counts else "N/A"
        return most_often_time
class MostOftenDay(Analyzer):
    def analyze(self, data):
        most_often_day = {}
        for activity, details in data.items():
            day_counts = {}
            for metadata in details['metadata']:
                day = metadata['day_of_week']
                if day in day_counts:
                    day_counts[day] += 1
                else:
                    day_counts[day] = 1
            most_often_day[activity] = max(day_counts, key=day_counts.get) if day_counts else "N/A"
        return most_often_day
class MostOftenWeekday(Analyzer):
    def analyze(self, data):
        most_often_weekday = {}
        for activity, details in data.items():
            weekday_counts = {}
            for metadata in details['metadata']:
                weekday = metadata['day_of_week']
                if weekday in weekday_counts:
                    weekday_counts[weekday] += 1
                else:
                    weekday_counts[weekday] = 1
            most_often_weekday[activity] = max(weekday_counts, key=weekday_counts.get) if weekday_counts else "N/A"
        return most_often_weekday
class MostOftenWeekend(Analyzer):
    def analyze(self, data):
        most_often_weekend = {}
        for activity, details in data.items():
            weekend_counts = {}
            for metadata in details['metadata']:
                weekend = metadata['day_of_week']
                if weekend == "Sobota" or weekend == "Neděle":
                    if weekend in weekend_counts:
                        weekend_counts[weekend] += 1
                    else:
                        weekend_counts[weekend] = 1
            most_often_weekend[activity] = max(weekend_counts, key=weekend_counts.get) if weekend_counts else "N/A"
        return most_often_weekend
class MostOftenMonth(Analyzer):
    def analyze(self, data):
        most_often_month = {}
        for activity, details in data.items():
            month_counts = {}
            for metadata in details['metadata']:
                month = metadata['date'].split()[0]
                if month in month_counts:
                    month_counts[month] += 1
                else:
                    month_counts[month] = 1
            most_often_month[activity] = max(month_counts, key=month_counts.get) if month_counts else "N/A"
        return most_often_month
