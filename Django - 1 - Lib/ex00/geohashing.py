import sys
import antigravity

def is_valid_date(date_str):
    if len(date_str) != 10:
        return False
    if date_str[2] != '-' or date_str[5] != '-':
        return False
    day, month, year = date_str[:2], date_str[3:5], date_str[6:]
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False
    day, month, year = int(day), int(month), int(year)
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month in {4, 6, 9, 11} and day > 30:
        return False
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    return True

def is_valid_geoposition(latitude, longitude):
    if -90 <= latitude <= 90 and -180 <= longitude <= 180:
        return True
    return False

def main():
    try :
        if len(sys.argv) != 4:
            print("Usage: python3 geohashing.py <latitude> <longitude> <date>")
            sys.exit(1)
        
        if not is_valid_date(sys.argv[3]):
            print("Invalid date format.")
            sys.exit(1)
        
        if not is_valid_geoposition(float(sys.argv[1]), float(sys.argv[2])):
            print("Invalid geoposition. \nLatitude must be between -90 and 90, and longitude must be between -180 and 180.")
            sys.exit(1)
    
        if sys.argv[1] == '90':
            sys.argv[1] = '89'
        if sys.argv[1] == '-90':
            sys.argv[1] = '-89'
        if sys.argv[2] == '180':
            sys.argv[2] = '179'
        if sys.argv[2] == '-180':
            sys.argv[2] = '-179'
        
        antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3].encode())
    except ValueError:
        print("Invalid geoposition. \nLatitude and longitude must be numbers and separated by a decimal point (e.g. 37.421542).")
        sys.exit(1)

if __name__ == '__main__':
    main()