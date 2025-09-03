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

flat_browser_stats = []
for year, year_statistic in browser_stats_by_year_and_month.items():
    for month, browser in year_statistic.items():
        flat_browser_stats.append((year, month, browser["Chrome"], browser["IE"], browser["Firefox"], browser["Safari"], browser["Opera"]))

YEAR, MONTH, CHROME, IE, FIREFOX, SAFARI, OPERA = zip(*flat_browser_stats)
browsers = {"chrome": CHROME, "ie": IE, "firefox": FIREFOX, "safari": SAFARI, "opera": OPERA} # to unpack as keyword arg

BROWSER_ID = tuple(id for id, _ in enumerate(MONTH))

def main():
    
    # calendar_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # month_order = {months: i for i, months in enumerate(calendar_months)}
    # result = max(MONTH, key=month_order.get)
    

    browser_market_share, firefox_popular, chrome_ie_overtake, safari_opera_poularity = create_report()
    print(f"""
          In the period covered, '{', '.join(browser_market_share)}' has had over 50% of market share
          Firefox's popularity was highest in {firefox_popular}
          Chrome first overtook IE in popularity in {chrome_ie_overtake}
          In which month was the combined popularity of Safari and Opera highest? {safari_opera_poularity}""")


def create_report():
    # In the period covered, which browsers have had over 50% of market share?
    highest_market_share = get_market_share(**browsers)

    # In which month was Firefox's popularity highest?
    firefox_dict = browser_month_dict(BROWSER_ID, FIREFOX)
    most_popular = max(firefox_dict, key=firefox_dict.get)
    firefox_poularity = MONTH[most_popular]

    # In which month did Chrome first overtake IE in popularity?
    chrome_ie_dict = browser_month_dict(BROWSER_ID, CHROME, IE)
    popularity_list = []
    for id, (chrome, ie) in chrome_ie_dict.items():
        if chrome > ie:
            popularity_list.append(id)
    chrome_ie_overtake = max(popularity_list)
    chrome_ie_month = MONTH[chrome_ie_overtake]

    # In which month was the combined popularity of Safari and Opera highest?
    safari_opera_dict = browser_month_dict(BROWSER_ID, SAFARI, OPERA)
    combined_popularity = {}
    for id, (safari, opera) in safari_opera_dict.items():
        total = safari + opera
        combined_popularity[id] = total
    popularity = max(combined_popularity, key=combined_popularity.get)
    safari_opera_poularity = MONTH[popularity]


    return highest_market_share, firefox_poularity, chrome_ie_month, safari_opera_poularity

def browser_month_dict(column_month, column_browser, additional_browser=None):
    browser_dict = {}
    if not additional_browser:
        for requested_month, requested_browser in zip(column_month, column_browser):
                browser_dict[requested_month] = requested_browser
    else:
        for requested_month, requested_browser, extra_broswer in zip(column_month, column_browser, additional_browser):
            browser_dict[requested_month] = requested_browser, extra_broswer
    return browser_dict
  
def get_market_share(**browsers):

    high_market_share = [browser_name for browser_name, browser_stat in browsers.items() if max(browser_stat) > 50]
    
    return high_market_share

if __name__ == "__main__":
    main()