from datetime import date
import calendar

from presidents_data import presidents_by_party


print('There have been presidents from {} different parties'.format(len(presidents_by_party)))


# TODO:
# * Display a report that answers the following questions:
#   * Which party has had most presidents?     
#   * Who was the youngest Republican president when they took office?
#   * Who was the oldest Democrat president when they took office?
#   * Who was the youngest president (from any party) when they took office?
#   * Who was the oldest president (from any party) when they took office?
#   * Which month saw the most presidents take office?
#   * Which decade saw the most presidents take office?
#   * Which party has been in power for longest?
#   * What is the average age of becoming president?
#   * Which presidents have taken office more than once?


# 1. extract the dicts from the list // convert to a flat structure 
flat_presidency = []
for party, presidents in presidents_by_party.items():
    for person in presidents:
        # breakpoint()
        flat_presidency.append((party, person["name"], person["born"], person["took_office"], person["left_office"]))

# TODO: sort by dob

# pivot rows into columns
parties, name, dob, enters_office, leaves_office = zip(*flat_presidency)


def age_on_given_date(birth_date, given_date):
    age_in_years = (given_date - birth_date).days / 365
    return int(age_in_years)

#   * Who was the youngest Republican president when they took office?
republican_president = []
for party, president_name, president_dob, took_office in zip(parties, name, dob, enters_office):
    if party == "Republican":
        republican_president.append([president_name, age_on_given_date(president_dob, took_office)])

print(republican_president)


def max_president_data(column_key):

    column_list = set(column_key)
    
    column_aggregate = {}
    for item in column_list:
        total = column_key.count(item)
        column_aggregate[item] = total
        
    maximum_count = (max(column_aggregate.values()))

    for item, count in column_aggregate.items():
        if count == maximum_count:

            return item, count

print(f"\nWhich party has had most presidents? \n The party with the most presidents is {max_president_data(parties)}")   

# convert from a tuple back to the datetime format
def convert_to_took_office_value(column_name, column_info):
    date_dict = {}
    for president_name, requested_info in zip(column_name, column_info):
        date_dict[president_name] = requested_info
    return date_dict

converted_date = convert_to_took_office_value(name, enters_office)
# print(converted_date)

month_name = [calendar.month_name[date_value.month] for date_value in converted_date.values()] # convert month number to name - human readable
print(f"\nWhich month saw the most presidents take office? \n The month with the most presidents is {max_president_data(month_name)}")   


def round_down_years(years):
    return years[:-1] + '0'

decade = [round_down_years(str(date_value.year)) for date_value in converted_date.values()]
print(f"\nWhich decade saw the most presidents take office? \n The decade with the most presidents take office is {max_president_data(decade)}")   




