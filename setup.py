#!/usr/bin/env python
from setuptools import find_namespace_packages, setup

package_name = "dbt-doris"
# make sure this always matches dbt/adapters/{adapter}/__version__.py
package_version = "1.3.0"
description = """The doris/selectdb adapter plugin for dbt, Original code fork from Apache Doris"""

setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description=description,
    author="long2ice,catpineapple",
    author_email="1391869588@qq.com",
    url="https://github.com/selectdb/dbt-selectdb.git",
    packages=find_namespace_packages(include=["dbt", "dbt.*"]),
    include_package_data=True,
    install_requires=[
        "dbt-core~=1.3.0",
    ],
)
