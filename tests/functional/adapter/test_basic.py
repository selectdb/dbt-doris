import pytest

from dbt.tests.adapter.basic.test_base import BaseSimpleMaterializations
from dbt.tests.adapter.basic.test_singular_tests import BaseSingularTests
from dbt.tests.adapter.basic.test_singular_tests_ephemeral import (
    BaseSingularTestsEphemeral
)
from dbt.tests.util import run_dbt, check_relations_equal
from dbt.tests.adapter.basic.test_empty import BaseEmpty
from dbt.tests.adapter.basic.test_ephemeral import BaseEphemeral
from dbt.tests.adapter.basic.test_incremental import BaseIncremental
from dbt.tests.adapter.basic.test_generic_tests import BaseGenericTests
from dbt.tests.adapter.basic.test_snapshot_check_cols import BaseSnapshotCheckCols
from dbt.tests.adapter.basic.test_snapshot_timestamp import BaseSnapshotTimestamp
from dbt.tests.adapter.basic.test_adapter_methods import BaseAdapterMethod


class TestSimpleMaterializationsdoris(BaseSimpleMaterializations):
    pass


class TestSingularTestsdoris(BaseSingularTests):
    pass


class TestSingularTestsEphemeraldoris(BaseSingularTestsEphemeral):
    pass


class TestEmptydoris(BaseEmpty):
    pass


class TestEphemeraldoris(BaseEphemeral):
    pass


class TestIncrementaldoris(BaseIncremental):
    pass


class TestGenericTestsdoris(BaseGenericTests):
    pass


class TestSnapshotCheckColsdoris(BaseSnapshotCheckCols):
    pass


class TestSnapshotTimestampdoris(BaseSnapshotTimestamp):
    pass


class TestBaseAdapterMethoddoris(BaseAdapterMethod):
    def test_adapter_methods(self, project, equal_tables):
        result = run_dbt()
        assert len(result) == 3
        check_relations_equal(project.adapter, equal_tables)
