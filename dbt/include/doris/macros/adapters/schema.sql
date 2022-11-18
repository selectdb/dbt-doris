-- Licensed to the Apache Software Foundation (ASF) under one
-- or more contributor license agreements. See the NOTICE file
-- distributed with this work for additional information
-- regarding copyright ownership. The ASF licenses this file
-- to you under the Apache License, Version 2.0 (the
-- "License"); you may not use this file except in compliance
-- with the License. You may obtain a copy of the License at
--
-- http://www.apache.org/licenses/LICENSE-2.0
--
-- Unless required by applicable law or agreed to in writing,
-- software distributed under the License is distributed on an
-- "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
-- KIND, either express or implied. See the License for the
-- specific language governing permissions and limitations
-- under the License.

-- doris have not 'schema' to make a collection of table or view
{% macro doris__drop_schema(relation) -%}
doris__drop_relation
{%- endmacro %}


{% macro doris__create_schema(relation) -%}
    {% call statement('create_schema') %}
    -- create schema if exists {{ relation.without_identifier() }}
    {% endcall %}
{% endmacro %}