from typing import Union, Dict
from pandas import DataFrame
import pandas as pd
import pytest
from pandas.testing import assert_frame_equal


def get_source_data() -> Dict[str, DataFrame]:
    metrics_data = DataFrame({
        "Date": ["16/12/2006"] * 24,
        "Time": ["17:24:00"] * 24,
        'ActivePower': [4.216, 5.36, 5.374, 5.388, 3.666, 3.52, 3.702, 3.7, 3.668, 3.662, 4.448, 5.412, 5.224, 5.268,
                        4.054, 3.384, 3.27, 3.43, 3.266, 3.728, 5.894, 7.706, 7.026, 3.666],
        'UnitPrice': [0.3, 0.3, 0.3, 0.3, 0.3, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6,
                      0.6, 0.6, 0.3, 0.3, 0.3]
    })

    return {
        "metrics_data": metrics_data
    }


def generate_report(source: Dict, contract: Union[Dict, None] = None) -> bool:
    if not isinstance(contract, Dict):
        return False

    metrics_data = source.get('metrics_data')

    if not isinstance(metrics_data, DataFrame):
        return False

    metrics_data['Amount'] = metrics_data['UnitPrice'] * metrics_data['ActivePower']

    metrics_data.to_csv('metrics_report.csv', index=False)

    return True


# 1. Write the test cases to test function get_source_data() as much as you can
class Test_get_source_data:
    def test_get_source_data(self):
        df1 = get_source_data().get('metrics_data')
        df2 = pd.DataFrame(df1)
        assert_frame_equal(df1, df2)


if __name__ == "__main__":
    pytest.main(["-s", "test_2.py"])


# 2. Write the test cases to test function generate_report() as much as you can

