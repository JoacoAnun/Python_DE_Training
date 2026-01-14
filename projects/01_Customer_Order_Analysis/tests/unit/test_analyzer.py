from analyzer import analyze_data


def test_analyze_data_returns_dict():
    result = analyze_data()
    assert isinstance(result, dict)


def test_analyze_data_returns_valid_keys():
    result = analyze_data()
    assert "rows_processed" in result
    assert "bad_rows_encountered" in result


def test_analyze_data_returns_valid_values():
    result = analyze_data()
    assert result["rows_processed"] >= 0
    assert result["bad_rows_encountered"] >= 0


def test_analyze_data_returns_valid_value_types():
    result = analyze_data()
    assert isinstance(result["rows_processed"], int)
    assert isinstance(result["bad_rows_encountered"], int)
