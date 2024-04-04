def format_date(date):
    # takes datetime object from parameter, then uses method to make it a string
    return date.strftime('%m/%d/%y')

from datetime import datetime
print(format_date(datetime.now()))