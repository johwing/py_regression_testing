"""Tests pytest-regressions for some special cases."""

import numpy as np


def test_regression_large_ints(num_regression):
    """Test regression with large ints."""

    add_delta_err_value = 1000000
    res = {
        "case_my_long_data_name_bps": [17230239.0 + add_delta_err_value, 7230239 + add_delta_err_value],
        "case_my_short_data": 13.37,
    }

    tol = {k: {"atol": 1e6, "rtol": 1e-2} for k in res.keys()}

    same_test = np.isclose(
        17230239, res["case_my_long_data_name_bps"][0], equal_nan=True, **tol["case_my_long_data_name_bps"]
    )
    assert same_test

    def_tol = {"atol": 1e6, "rtol": 1e-2}
    # res = {k: [np.float64(vv) for vv in v] for k, v in res.items()}
    res_field = np.array(res["case_my_long_data_name_bps"])
    res_field_dtype = res_field.dtype
    assert np.issubdtype(res_field_dtype, np.number)
    num_regression.check(res, tolerances=tol, default_tolerance=def_tol)
