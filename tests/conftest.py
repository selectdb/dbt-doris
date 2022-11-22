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
        "type": "doris",
        "threads": 1,
        "host": os.getenv("DORIS_TEST_HOST", "172.31.127.243"),
        "user": os.getenv("DORIS_TEST_USER", "root"),
        "password": os.getenv("DORIS_TEST_PASSWORD", ""),
        "port": os.getenv("DORIS_TEST_PORT", 8211),
    }
