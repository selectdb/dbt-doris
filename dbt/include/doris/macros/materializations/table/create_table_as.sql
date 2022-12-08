{% macro doris__create_table_as(temporary, relation, sql) -%}
    {% set sql_header = config.get('sql_header', none) %}
    {% set table = relation.include(database=False) %}
    {{ sql_header if sql_header is not none }}
    {%if temporary %}
        {{doris__drop_relation(relation)}}
    {% endif %}
    create table {{ table }}
    {{ doris__duplicate_key() }}
    {{ doris__partition_by() }}
    {{ doris__distributed_by() }}
    {{ doris__properties() }} as {{ sql }};

{%- endmacro %}

{% macro doris__create_unique_table_as(temporary, relation, sql) -%}
    {% set sql_header = config.get('sql_header', none) %}
    {% set table = relation.include(database=False) %}
    {{ sql_header if sql_header is not none }}
    create table {{ table }}
    {{ doris__unique_key() }}
    {{ doris__partition_by() }}
    {{ doris__distributed_by() }}
    {{ doris__properties() }} as {{ sql }};

{%- endmacro %}