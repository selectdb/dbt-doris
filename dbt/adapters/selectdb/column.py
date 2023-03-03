from dataclasses import dataclass

from dbt.adapters.base.column import Column


@dataclass
class SelectdbColumn(Column):
    @property
    def quoted(self) -> str:
        return "`{}`".format(self.column)

    def __repr__(self) -> str:
        return f"<SelectdbColumn {self.name} ({self.data_type})>"
