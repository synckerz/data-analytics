# Reflection: SQL vs NoSQL Storage Models

For this project, I considered SQL and NoSQL as two possible storage models for the global temperature anomaly dataset.

SQL databases, such as MySQL and PostgreSQL, organise information into structured tables with rows and columns. This fits the dataset because each record follows the same format: an entity, a code, a year and a temperature anomaly value. SQL would make it straightforward to filter records by year or entity, calculate averages and compare trends using queries. It also supports relationships and data consistency, which are useful when working with structured information.

NoSQL databases, such as MongoDB, offer more flexible ways to store data, often using documents rather than fixed relational tables. This can be useful when information has different structures, changes frequently or needs to scale across varied data sources. However, that flexibility is less important for the current dataset because its fields are consistent and clearly defined.

For this project, I would choose SQL because the data is tabular and the analysis relies on filtering, aggregation and comparisons across years. NoSQL could become more suitable if the project later included varied or semi-structured sources, such as detailed sensor records or text-based observations.

This comparison showed me that storage decisions should be based on data structure, query needs and the intended use of the application.