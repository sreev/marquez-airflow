import sys
from unittest.mock import patch

import pytest
from tests.mocks.git_mock import execute_git_mock

from marquez_airflow.utils import get_location


@patch('marquez_airflow.utils.execute_git',
       side_effect=execute_git_mock)
def test_dag_location(git_mock):
    assert ('https://github.com/MarquezProject/marquez-airflow/blob/'
            'abcd1234/tests/dags/postgres.py' ==
            get_location("tests/test_dags/test_postgres_dag.py"))


@patch('marquez_airflow.utils.execute_git',
       side_effect=execute_git_mock)
def test_bad_file_path(git_mock):
    with pytest.raises(FileNotFoundError):
        # invalid file
        get_location("test_dags/missing-dag.py")


if __name__ == "__main__":
    pytest.main([sys.argv[0]])
