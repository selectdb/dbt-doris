import pytest

import os
import json

# Import the fuctional fixtures as a plugin
# Note: fixtures with session scope need to be local

pytest_plugins = ["dbt.tests.fixtures.project"]


# The profile dictionary, used to write out profiles.yml
@pytest.fixture(scope="class")
def dbt_profile_target():
        return {
        "type": "selectdb",
        "threads": 1,
        "host": os.getenv("SELECTDB_TEST_HOST", "127.0.0.1"),
        "user": os.getenv("SELECTDB_TEST_USER", "root"),
        "password": os.getenv("SELECTDB_TEST_PASSWORD", ""),
        "port": os.getenv("SELECTDB_TEST_PORT", 9030),
    }
