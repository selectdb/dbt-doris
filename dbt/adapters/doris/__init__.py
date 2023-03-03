from dbt.adapters.selectdb.connections import SelectdbConnectionManager # noqa
from dbt.adapters.selectdb.connections import SelectdbCredentials
from dbt.adapters.selectdb.impl import SelectdbAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import selectdb


Plugin = AdapterPlugin(
    adapter=SelectdbAdapter,
    credentials=SelectdbCredentials,
    include_path=selectdb.PACKAGE_PATH
    )
