
from exercises.browser_stats import CreateReport, report_content


TEST_STATS_DATA = {
    2016: {
        'May': {'Chrome': 71.4, 'IE': 5.7, 'Firefox': 16.9, 'Safari': 3.6, 'Opera': 1.2},
        'April': {'Chrome': 70.4, 'IE': 5.8, 'Firefox': 17.5, 'Safari': 3.7, 'Opera': 1.3},
        'March': {'Chrome': 69.9, 'IE': 6.1, 'Firefox': 17.8, 'Safari': 3.6, 'Opera': 1.3},
        'February': {'Chrome': 69.0, 'IE': 6.2, 'Firefox': 18.6, 'Safari': 3.7, 'Opera': 1.3},
        'January': {'Chrome': 68.4, 'IE': 6.2, 'Firefox': 18.8, 'Safari': 3.7, 'Opera': 1.4},
    },
    2015: {
        'December': {'Chrome': 68.0, 'IE': 6.3, 'Firefox': 19.1, 'Safari': 3.7, 'Opera': 1.5},
        'November': {'Chrome': 67.4, 'IE': 6.8, 'Firefox': 19.2, 'Safari': 3.9, 'Opera': 1.5},
        'October': {'Chrome': 66.5, 'IE': 6.9, 'Firefox': 20.0, 'Safari': 3.8, 'Opera': 1.4},
        'September': {'Chrome': 65.9, 'IE': 7.2, 'Firefox': 20.6, 'Safari': 3.6, 'Opera': 1.4},
        'August': {'Chrome': 64.0, 'IE': 6.6, 'Firefox': 21.2, 'Safari': 4.5, 'Opera': 2.2},
        'July': {'Chrome': 63.3, 'IE': 6.5, 'Firefox': 21.6, 'Safari': 4.9, 'Opera': 2.5},}}

def test_convert_data():
    result = CreateReport(TEST_STATS_DATA).data()

    assert "dict" in str(type(result))
    assert len(result["id"]) == 11
    

def test_analyse_browser_data():
    browser_analysis = CreateReport(TEST_STATS_DATA).analysis()
    assert browser_analysis["period_start"] == "July 2015"

def test_report_content_generated(monkeypatch):
    monkeypatch.setattr("exercises.browser_stats.browser_stats_by_year_and_month", TEST_STATS_DATA)

    generated = report_content()

    assert "The report covers July 2015" in generated

