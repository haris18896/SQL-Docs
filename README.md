# SQL-Docs

# SQL
SQL stands for `Structured Query Language`. SQL is a standard language for storing, manipulating and retrieving data in databases.

### Imperative VS Declarative
* `Imperative`: Imperative programing say `How it will hapeen`
  * e.g line by line programing (python | java)
* `Declarative`:  Declarative language is a language where we say `What will happen?` or You tell the computer how to do something.
  * e.g `SELECT * FROM users WHERE id = 1;`

### SQL History
In the 1970's, a programmer named `Edgar F. Codd` from IBM proposed the `Relational Model` for Database Management. He introduced the concept of `Relational Algebra` and `Structured Query Language (SQL)` to the world.

### OLTP VS OLAP
* OLTP: `Online Transaction Processing` is a class of systems that facilitate and manage transaction-oriented applications, typically for data entry and retrieval transaction processing.
* OLAP: `Online Analytical Processing` is a computer-based approach to query, reporting, and data analysis. OLAP is a category of software technology that enables analysts, managers, and executives to gain insight into data through fast, consistent, interactive access to a wide variety of possible views of information that has been transformed from raw data to reflect the real dimensionality of the enterprise as understood by the user.

### SQL Commands
* `DDL`: Data Definition Language
  * `CREATE`: Create a new table, a view of a table, or other objects in the database.
  * `ALTER`: Modify an existing database object, such as a table.
  * `DROP`: Delete an entire table, a view of a table or other objects in the database.
  * `TRUNCATE`: Remove all records from a table, including all spaces allocated for the records are removed.
  * `COMMENT`: Add comments to the data dictionary.
  * `RENAME`: Rename an object.
* `DML`: Data Manipulation Language
  * `SELECT`: Retrieve data from the database.
  * `INSERT`: Insert data into a table.
  * `UPDATE`: Update existing data within a table.
  * `DELETE`: Delete records from a database table.
* `DCL`: Data Control Language
    * `GRANT`: Gives a privilege to user.
    * `REVOKE`: Takes back privileges granted from user.
    * `DENY`: Denies a privilege to user.
* `DQL`: Data Query Language
  * `SELECT`: Retrieve data from the database.
  * `WITH`: Subquery Factoring (Common Table Expressions).
  * `ORDER BY`: Sort the result set in ascending or descending order.
  * `GROUP BY`: Group rows that have the same values into summary rows.
  * `HAVING`: Filter groups based on specified conditions.
  * `WHERE`: Filter rows based on specified conditions.
  * `JOIN`: Combine rows from two or more tables, based on a related column between them.
  * `UNION`: Combine the result set of two or more SELECT statements.
  * `INTERSECT`: Combine the result set of two or more SELECT statements and returns only the rows that appear in all result sets.
  * `EXCEPT`: Combine the result set of two or more SELECT statements and returns only the rows that appear in the first result set but not in the other result set.
  * `IN`: Allows you to specify multiple values in a WHERE clause.
  * `LIKE`: Allows you to perform pattern matching.
  * `BETWEEN`: Selects values within a given range.
  * `EXISTS`: Tests for the existence of any records in a subquery.
  * `ANY`: Compares a value to any applicable value in the list according to the condition.
  * `ALL`: Compares a value to every applicable value in the list according to the condition.
  * `CASE`: Creates different outputs based on conditions.
  * `COALESCE`: Returns the first non-null expression in the list.
  * `NULLIF`: Returns NULL if the two expressions are equal.
  * `NATURAL JOIN`: Performs a join by implicitly selecting the columns with the same name in the two tables.
  * `CROSS JOIN`: Returns the Cartesian product of the two tables.
  * `INNER JOIN`: Returns rows when there is at least one match in both tables.
  * `LEFT JOIN`: Returns all rows from the left table, and the matched rows from the right table.
  * `RIGHT JOIN`: Returns all rows from the right table, and the matched rows from the left table.
  * `FULL JOIN`: Returns rows when there is a match in one of the tables.
  * `SELF JOIN`: Joins a table with itself.
  * `UNION ALL`: Combines the result set of two or more SELECT statements (allows duplicate values).
  * `ROW_NUMBER`: Assigns a unique sequential integer to each row to which a window function is applied.
  * `RANK`: Assigns a unique integer to each distinct row within the partition of a result set.
  * `DENSE_RANK`: Assigns a unique integer to each distinct row within the partition of a result set.
  * `NTILE`: Divides an ordered set of rows into a specified number of groups called buckets and assigns a bucket number to each row.
  * `LAG`: Accesses data from a previous row in the same result set without the use of a self-join.
  * `LEAD`: Accesses data from a subsequent row in the same result set without the use of a self-join.
  * `FIRST_VALUE`: Returns the first value in an ordered set of values.
  * `LAST_VALUE`: Returns the last value in an ordered set of values.
  * `OFFSET`: Specifies the number of rows to skip before starting to return rows from the query expression.
  * `FETCH`: Specifies the number of rows to return after the OFFSET clause has been processed.
  * `TOP`: Specifies the number of rows or the percentage of rows to be returned.
  * `PERCENT`: Specifies the percentage of rows to return.
  * `ROWNUM`: Specifies the number of rows to return.
  * `ROWNUMBER`: Specifies the number of rows to return.
  * `LIMIT`: Specifies the number of rows to return.
  * `OFFSET`: Specifies the number of rows to skip before starting to return rows from the query expression.
  * `FETCH`: Specifies the number of rows to return after the OFFSET clause has been processed.
  * `TOP`: Specifies the number of rows or the percentage of rows to be returned.
  * `PERCENT`: Specifies the percentage of rows to return.
  * `ROWNUM`: Specifies the number of rows to return.
  * `ROWNUMBER`: Specifies the number of rows to return.

