{% macro selectdb__create_table_as(temporary, relation, sql) -%}
    {% set sql_header = config.get('sql_header', none) %}
    {% set table = relation.include(database=False) %}
    {{ sql_header if sql_header is not none }}
    {%if temporary %}
        {{selectdb__drop_relation(relation)}}
    {% endif %}
    create table {{ table }}
    {{ selectdb__duplicate_key() }}
    {{ selectdb__partition_by() }}
    {{ selectdb__distributed_by() }}
    {{ selectdb__properties() }} as {{ sql }};

{%- endmacro %}

{% macro selectdb__create_unique_table_as(temporary, relation, sql) -%}
    {% set sql_header = config.get('sql_header', none) %}
    {% set table = relation.include(database=False) %}
    {{ sql_header if sql_header is not none }}
    create table {{ table }}
    {{ selectdb__unique_key() }}
    {{ selectdb__partition_by() }}
    {{ selectdb__distributed_by() }}
    {{ selectdb__properties() }} as {{ sql }};

{%- endmacro %}