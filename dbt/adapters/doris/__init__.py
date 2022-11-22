from dbt.adapters.doris.connections import DorisConnectionManager # noqa
from dbt.adapters.doris.connections import DorisCredentials
from dbt.adapters.doris.impl import DorisAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import doris


Plugin = AdapterPlugin(
    adapter=DorisAdapter,
    credentials=DorisCredentials,
    include_path=doris.PACKAGE_PATH
    )
