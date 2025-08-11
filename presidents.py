# from date import date

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

# TODO: sort by dob

# pivot rows into columns
parties, name, dob, enters_office, leaves_office = zip(*flat_presidency)

def age_on_given_date(birth_date, given_date):
    age_in_years = (given_date - birth_date).days / 365
    return int(age_in_years)

#   * Which party has had most presidents?
party_list = set(parties)

party_aggregate = {}
for party in party_list:
    total = parties.count(party)
    # breakpoint()
    party_aggregate[party] = total
# breakpoint()
maximum_count = (max(party_aggregate.values()))

for party, count in party_aggregate.items():
    if count == maximum_count:
        print(f"The party with the most presidents is {party} - {count}")

#   * Who was the youngest Republican president when they took office?
republican_president = []
for party, president_name, president_dob, took_office in zip(parties, name, dob, enters_office):
    if party == "Republican":
        republican_president.append([president_name, age_on_given_date(president_dob, took_office)])


print(republican_president)

