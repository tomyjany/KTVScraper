# KTV SCRAPER
## installation
```console
git clone https://github.com/tomyjany/KTVScraper.git
pip install -r --no-deps requirements.txt
```
Then you have to create file `cfg.yml`
```yml
USERNAME = "your_email_adress"
PASSWORD = "your_password"
```
## Usage
For Scraping:
```console
python -m Scraper
```
For analytics:
```console
python -m Analyzer
```

### JSON Example:
```json
{
    "ASC posilovna": {
        "count": 35,
        "metadata": [
            {
                "week": 38,
                "day_of_week": "Pondělí",
                "date": "16.09.",
                "time": "16:00 - 18:00"
            },
            {
                "week": 38,
                "day_of_week": "Středa",
                "date": "18.09.",
                "time": "18:00 - 20:00"
            },
    ...
}
```
### Analytics example
```console
$ python -m Analyzer --analyzer AveragePerWeek
{'ASC posilovna': 2.6923076923076925}

$ python -m Analyzer
{'AveragePerWeek': {'ASC posilovna': 2.6923076923076925}, 'MostOftenTime': {'ASC posilovna': '14:00 - 18:00'}, 'MostOftenDay': {'ASC posilovna': 'Čtvrtek'}, 'MostOftenWeekday': {'ASC posilovna': 'Čtvrtek'}, 'MostOftenWeekend': {'ASC posilovna': 'Neděle'}, 'MostOftenMonth': {'ASC posilovna': '11'}}
(.venv) (base) [tomja@a130 KTVScraper]$ 
```

