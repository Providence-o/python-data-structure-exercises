import calendar
from collections import Counter

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
        flat_presidency.append((party, person["name"], person["born"], person["took_office"], person["left_office"]))

# pivot rows into columns
PARTIES, NAME, DOB, ENTERS_OFFICE, LEAVES_OFFICE = zip(*flat_presidency)


def age_on_given_date(birth_date, given_date):
    age_in_years = (given_date - birth_date).days / 365
    return int(age_in_years)

AGE_TOOK_OFFICE = tuple(age_on_given_date(president_dob, took_office) for president_dob, took_office in zip(DOB, ENTERS_OFFICE))

def duration_in_office(end_date, start_date):
    time_in_years = (end_date - start_date).days / 365
    return time_in_years

TIME_IN_OFFICE = tuple(duration_in_office(left_date, started_date) for started_date, left_date in zip(ENTERS_OFFICE, LEAVES_OFFICE))

def main():
    print(print_report())


def print_report():
    party_with_most_presidents, youngest_republican, oldest_democrat, youngest_president, oldest_president, month_with_most_presidents, decade_with_most_presidents, longest_duration_party, average_age, multiple_presidency = create_report()


    return (f"""
          Which party has had most presidents?
          The party with the most presidents is {party_with_most_presidents}

          Who was the youngest Republican president when they took office?
          The youngest Republican president when they took office was {youngest_republican}
          
          Who was the oldest Democrat president when they took office?
          The oldest Democrat president when they took office was {oldest_democrat}

          Who was the youngest president (from any party) when they took office?
          The youngest president to take office is {youngest_president}

          Who was the oldest president (from any party) when they took office?
          The oldest president to take office is {oldest_president}
          
          Which month saw the most presidents take office?
          The month with the most presidents is {month_with_most_presidents}

          Which decade saw the most presidents take office?
          The decade with the most presidents take office is {decade_with_most_presidents}'s

          Which party has been in power for longest?
          The party that has been in office the longest is {longest_duration_party}

          What is the average age of becoming president?
          The average age for becoming president is {average_age}
          
          Which presidents have taken office more than once?
          The presidents that have taken office more than once: {', '.join(multiple_presidency)}""")

def create_report():
    party_with_most_presidents = max_president_data(PARTIES)

    converted_party_date = convert_tuple_to_dict(NAME, AGE_TOOK_OFFICE, PARTIES)
    party_name = {name: age for name, (age, party) in converted_party_date.items() if party == 'Republican'}
    youngest_republican = min(party_name, key=party_name.get)

    party_demo = {name: age for name, (age, party) in converted_party_date.items() if party == 'Democratic'}
    oldest_democrat = max(party_demo, key=party_demo.get)

    converted_age = convert_tuple_to_dict(NAME, AGE_TOOK_OFFICE)
    youngest_president = min(converted_age, key=converted_age.get)

    oldest_president = max(converted_age, key=converted_age.get)

    converted_date = convert_tuple_to_dict(NAME, ENTERS_OFFICE)
    month_name = [calendar.month_name[date_value.month] for date_value in converted_date.values()]
    month_with_most_presidents = max_president_data(month_name)

    decade = [round_down_years(str(date_value.year)) for date_value in converted_date.values()]
    decade_with_most_presidents = max_president_data(decade)

    converted_power_date = convert_tuple_to_dict(PARTIES, TIME_IN_OFFICE)
    longest_duration_party = max(converted_power_date, key=converted_power_date.get)

    list_age = [age for age in converted_age.values()]
    average_age = sum(list_age) / len(list_age)

    president_occurence = Counter(NAME)
    multiple_presidency = [name for name, count in president_occurence.items() if count > 1]
    
    return party_with_most_presidents, youngest_republican, oldest_democrat, youngest_president, oldest_president, month_with_most_presidents, decade_with_most_presidents, longest_duration_party, average_age, multiple_presidency

def max_president_data(COLUMN_KEYS):
    
    column_aggregate = Counter(COLUMN_KEYS)
        
    maximum_count = (max(column_aggregate.values()))

    for item, count in column_aggregate.items():
        if count == maximum_count:
            return item

# convert from a tuple back to a dict
def convert_tuple_to_dict(column_name, column_info, additional_column=None):
    presidents_dict = {}
    if not additional_column:
        for president_name, requested_info in zip(column_name, column_info):
            presidents_dict[president_name] = requested_info
    else:
        for president_name, requested_info, additional_info in zip(column_name, column_info, additional_column):
                presidents_dict[president_name] = requested_info, additional_info
    return presidents_dict


def round_down_years(years):
    return years[:-1] + '0'


if __name__ == "__main__":
    main()