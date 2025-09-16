# This program displays a report about browser usage statistics, as recorded by
# w3schools.com.
#
# Usage:
#
# $ python browser_stats.py

from .data.browser_stats_data import browser_stats_by_year_and_month

# print('browser_stats_by_year_and_month is a {} with {} elements'.format(type(browser_stats_by_year_and_month).__name__, len(browser_stats_by_year_and_month)))


# TODO:
# * Display a report that answers the following questions:
#   * What period does the report cover?
#   * In the period covered, which browsers have had over 50% of market share?
#   * In which month did Firefox first become the most popular browser?
#   * In which month did Chrome first overtake IE in popularity?
#   * In which month was Firefox's popularity highest?
#   * In which month was the combined popularity of Safari and Opera highest?
#   * Which month saw the biggest percentage point rise in Chrome's popularity?
#   * Which month saw the biggest percentage point 

def main():
    print(report_content())


def report_content():
    report = CreateReport(browser_stats_by_year_and_month).analysis() 

    return f"""
        The report covers {report["period_start"]} to {report["period_end"]}
        In the period covered, '{report["browsers_over_50"]}' has had over 50% of market share
        In {report["firefox_early_popularity"]} firefox first became the most popular browser
        Chrome first overtook IE in popularity in {report["chrome_overtake_ie"]}
        Firefox's popularity was highest in {report["firefox_highest_popularity"]}
        In which month was the combined popularity of Safari and Opera highest? {report["safari_opera_highest"]}
        In {report["chrome_percentage_rise"]}, Chrome had the biggest percentage point rise in popularity"""
    

class CreateReport:
    def __init__(self, browser_stats):
        self.browser_stats = browser_stats

    def data(self):
        flat_structure = []
        for year, value in self.browser_stats.items():
            for month, browser in value.items():
                flat_structure.append((year, month, browser["Chrome"], browser["IE"], browser["Firefox"], browser["Safari"], browser["Opera"]))
        
        # Convert from rows to columns
        YEAR, MONTH, CHROME, IE, FIREFOX, SAFARI, OPERA = zip(*flat_structure)
        
        ID = tuple(id for id, _ in enumerate(zip(MONTH)))

        data_dict = {"id": ID, "year": YEAR, "month": MONTH, "browsers": {"chrome": CHROME, "ie": IE, "firefox": FIREFOX, "safari": SAFARI, "opera": OPERA}}

        return data_dict

    
    def analysis(self):
        data = self.data()

        id = data["id"]
        safari = data["browsers"]["safari"]
        opera = data["browsers"]["opera"]
        chrome = data["browsers"]["chrome"]
        ie = data["browsers"]["ie"]
        firefox = data["browsers"]["firefox"]
        browser_data = data["browsers"]
        month = data["month"]
        year = data["year"]

        #   * In the period covered, which browsers have had over 50% of market share?
        browsers_over_50 = [browser_name for browser_name, browser_stat in browser_data.items() if max(browser_stat) > 50]

        #   * In which month was Firefox's popularity highest?
        firefox_max = firefox.index(max(firefox))
        firefox_highest_popularity = month[firefox_max]

        #   * In which month was the combined popularity of Safari and Opera highest?
        safari_opera_sum = {id[i]: safari[i] + opera[i] for i in range(len(id))}
        safari_opera_max = max(safari_opera_sum, key=safari_opera_sum.get)
        safari_opera_highest = month[safari_opera_max]
        

        #   * In which month did Chrome first overtake IE in popularity? 
        chrome_ie_popularity = [id[i] for i in range(len(id)) if chrome[i] > ie[i]]
        chrome_ie_max = max(chrome_ie_popularity)
        chrome_overtake_ie = month[chrome_ie_max]
        
        #   * In which month did Firefox first become the most popular browser?
        firefox_popularity = [id[i] for i in range(len(id)) if firefox[i] > ie[i] and safari[i] and opera[i] and chrome[i]]
        firefox_popularity_max = max(firefox_popularity)
        firefox_early_popularity = month[firefox_popularity_max]
    
        #   * Which month saw the biggest percentage point rise in Chrome's popularity?
        chrome_percent_increase = {id[i]: chrome[i] - chrome[i + 1] for i in range(len(id) - 1)}
        max_of_increase = max(chrome_percent_increase, key=chrome_percent_increase.get)
        chrome_percentage_rise = month[max_of_increase]

        #   * What period does the report cover?
        maximum_id = max(id)
        minimum_id = min(id)
        
        period_start = f"{month[maximum_id]} {year[maximum_id]}"
        period_end = f"{month[minimum_id]} {year[minimum_id]}"
           
        return {
            "browsers_over_50": ', '.join(browsers_over_50),
            "firefox_highest_popularity": firefox_highest_popularity,
            "safari_opera_highest": safari_opera_highest,
            "chrome_overtake_ie": chrome_overtake_ie,
            "firefox_early_popularity": firefox_early_popularity,
            "chrome_percentage_rise": chrome_percentage_rise,
            "period_start": period_start,
            "period_end": period_end
        }

if __name__ == "__main__":
    main()