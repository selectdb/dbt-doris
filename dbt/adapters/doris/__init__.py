from dbt.adapters.doris.connections import dorisConnectionManager # noqa
from dbt.adapters.doris.connections import dorisCredentials
from dbt.adapters.doris.impl import dorisAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import doris


Plugin = AdapterPlugin(
    adapter=dorisAdapter,
    credentials=dorisCredentials,
    include_path=doris.PACKAGE_PATH
    )
