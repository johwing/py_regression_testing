"""Tests pytest-regressions for some special cases."""


def test_regression_large_ints(num_regression):
    """Test regression with large ints."""

    add_delta_err_value = 0
    res = {
        "case.my_long_data_name_bps": [17230239.0 + add_delta_err_value, 7230239.0 + add_delta_err_value],
        "case.my_short_data": 13.37,
    }

    tol = {"k": {"atol": 1e6, "rtol": 1e-1} for k in res.keys()}

    num_regression.check(res, tolerances=tol)
