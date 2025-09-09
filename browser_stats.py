# This program displays a report about browser usage statistics, as recorded by
# w3schools.com.
#
# Usage:
#
# $ python browser_stats.py

from browser_stats_data import browser_stats_by_year_and_month

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
    # this function runs the function that will print the report e.g print(some_function)
    
    print(report_content())


def report_content():
    # this function contains the strings when variables to create the data are passed/called
    report = CreateReport().analysis() # an instance of the CreateReport class

    report_body = f"""
        The report covers {report["period_start"]} to {report["period_end"]}
        In the period covered, '{report["browsers_over_50"]}' has had over 50% of market share
        In {report["firefox_early_popularity"]} firefox first became the most popular browser
        Chrome first overtook IE in popularity in {report["chrome_overtake_ie"]}
        Firefox's popularity was highest in {report["firefox_highest_popularity"]}
        In which month was the combined popularity of Safari and Opera highest? {report["safari_opera_highest"]}
        In {report["chrome_percentage_rise"]}, Chrome had the biggest percentage point rise in poprularity"""
    
    return report_body



class CreateReport:

    def data(self):
        flat_structure = []
        for year, value in browser_stats_by_year_and_month.items():
            for month, browser in value.items():
                flat_structure.append((year, month, browser["Chrome"], browser["IE"], browser["Firefox"], browser["Safari"], browser["Opera"]))
        
        # Convert from rows to columns
        YEAR, MONTH, CHROME, IE, FIREFOX, SAFARI, OPERA = zip(*flat_structure)
        
        ID = tuple(id for id, _ in enumerate(zip(MONTH)))

        data_dict = {"id": ID, "year": YEAR, "month": MONTH, "browsers": {"chrome": CHROME, "ie": IE, "firefox": FIREFOX, "safari": SAFARI, "opera": OPERA}}

        return data_dict

    
    def analysis(self):
        
        #   * In the period covered, which browsers have had over 50% of market share?
        browser_data = self.data()["browsers"]
        browsers_over_50 = [browser_name for browser_name, browser_stat in browser_data.items() if max(browser_stat) > 50]

        #   * In which month was Firefox's popularity highest?
        firefox = self.data()["browsers"]["firefox"]
        f_index = firefox.index(max(firefox))
        firefox_highest_popularity = self.data()["month"][f_index]

        # * In which month was the combined popularity of Safari and Opera highest?
        id = self.data()["id"]
        safari = self.data()["browsers"]["safari"]
        opera = self.data()["browsers"]["opera"]
        chrome = self.data()["browsers"]["chrome"]
        ie = self.data()["browsers"]["ie"]

        combined_dict = {id[i]: safari[i] + opera[i] for i in range(len(id))}
        high_id = max(combined_dict, key=combined_dict.get)
        safari_opera_highest = self.data()["month"][high_id]
        

        #   * In which month did Chrome first overtake IE in popularity? 
        chrome_ie_dict = [id[i] for i in range(len(id)) if chrome[i] > ie[i]]
        highest_chrome_ie = max(chrome_ie_dict)
        chrome_overtake_ie = self.data()["month"][highest_chrome_ie]
        
        #   * In which month did Firefox first become the most popular browser?
        fire_dict = [id[i] for i in range(len(id)) if firefox[i] > ie[i] and safari[i] and opera[i] and chrome[i]]
        highest_fire = max(fire_dict)
        firefox_early_popularity = self.data()["month"][highest_fire]
    
        #   * Which month saw the biggest percentage point rise in Chrome's popularity?
        chrome_percent = {id[i]: chrome[i] - chrome[i + 1] for i in range(len(id) - 1)}
        perc_id = max(chrome_percent, key=chrome_percent.get)
        chrome_percentage_rise = self.data()["month"][perc_id]

        #   * What period does the report cover?
        month = self.data()["month"]
        year = self.data()["year"]
        max_id = max(id)
        min_id = min(id)
        
        period_start = f"{month[max_id]} {year[max_id]}"
        period_end = f"{month[min_id]} {year[min_id]}"
           
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