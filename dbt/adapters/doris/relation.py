from dataclasses import dataclass

from dbt.adapters.base.relation import BaseRelation, Policy
from dbt.exceptions import RuntimeException

@dataclass
class SelectdbQuotePolicy(Policy):
    database: bool = False
    schema: bool = True
    identifier: bool = True


@dataclass
class SelectdbIncludePolicy(Policy):
    database: bool = False
    schema: bool = True
    identifier: bool = True


@dataclass(frozen=True, eq=False, repr=False)
class SelectdbRelation(BaseRelation):
    quote_policy: SelectdbQuotePolicy = SelectdbQuotePolicy()
    include_policy: SelectdbIncludePolicy = SelectdbIncludePolicy()
    quote_character: str = "`"

    def __post_init__(self):
        if self.database != self.schema and self.database:
            raise RuntimeException(f"Cannot set database {self.database} in Selectdb!")

    def render(self):
        if self.include_policy.database and self.include_policy.schema:
            raise RuntimeException(
                "Got a Selectdb relation with schema and database set to include, but only one can be set"
            )
        return super().render()
