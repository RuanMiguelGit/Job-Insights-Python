from src.sorting import sort_by


def test_sort_by_criteria():
    pass
    mock_data = [
        {"max_salary": 1, "min_salary": 3, "date_posted": "21-01-01"},
        {"max_salary": 2, "min_salary": 2, "date_posted": "21-02-02"},
        {"max_salary": 3, "min_salary": 4, "date_posted": "21-03-03"},
        {"max_salary": 4, "min_salary": 1, "date_posted": "21-04-04"},
    ]

    mock_data_max_salary = [
        {"max_salary": 4, "min_salary": 1, "date_posted": "21-04-04"},
        {"max_salary": 3, "min_salary": 4, "date_posted": "21-03-03"},
        {"max_salary": 2, "min_salary": 2, "date_posted": "21-02-02"},
        {"max_salary": 1, "min_salary": 3, "date_posted": "21-01-01"},
    ]

    sort_by(mock_data, "max_salary")
    assert mock_data == mock_data_max_salary


pass
