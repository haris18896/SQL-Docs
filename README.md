# `SQL-Docs`

# `SQL`
SQL stands for `Structured Query Language`. SQL is a standard language for storing, manipulating and retrieving data in databases.

### `Imperative VS Declarative`
* `Imperative`: Imperative programing say `How it will hapeen`
  * e.g line by line programing (python | java)
* `Declarative`:  Declarative language is a language where we say `What will happen?` or You tell the computer how to do something.
  * e.g `SELECT * FROM users WHERE id = 1;`

### `SQL History`
In the 1970's, a programmer named `Edgar F. Codd` from IBM proposed the `Relational Model` for Database Management. He introduced the concept of `Relational Algebra` and `Structured Query Language (SQL)` to the world.

### `OLTP VS OLAP`
* OLTP: `Online Transaction Processing` is a class of systems that facilitate and manage transaction-oriented applications, typically for data entry and retrieval transaction processing.
* OLAP: `Online Analytical Processing` is a computer-based approach to query, reporting, and data analysis. OLAP is a category of software technology that enables analysts, managers, and executives to gain insight into data through fast, consistent, interactive access to a wide variety of possible views of information that has been transformed from raw data to reflect the real dimensionality of the enterprise as understood by the user.

### `SQL Commands`
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
  * 'DISTINCT': Selects only distinct (different) values.
  * `WITH`: Subquery Factoring (Common Table Expressions).
  * `ORDER BY`: Sort the result set in ascending or descending order.
  * `GROUP BY`: Group rows that have the same values into summary rows.
  * `HAVING`: Filter groups based on specified conditions.
  * `WHERE`: Filter rows based on specified conditions.
  * `JOIN`: Combine rows from two or more tables, based on a related column between them.
  * `UNION`: Combine the result set of two or more SELECT statements.
  * `INTERSECT`: Combine the result set of two or more SELECT statements and returns only the rows that appear in all result sets.
  * `IN`: Allows you to specify multiple values in a WHERE clause.
  * `LIKE`: Allows you to perform pattern matching.
  * `BETWEEN`: Selects values within a given range.
  * `EXISTS`: Tests for the existence of any records in a subquery.
  * `NATURAL JOIN`: Performs a join by implicitly selecting the columns with the same name in the two tables.
  * `CROSS JOIN`: Returns the Cartesian product of the two tables.
  * `INNER JOIN`: Returns rows when there is at least one match in both tables.
  * `LEFT JOIN`: Returns all rows from the left table, and the matched rows from the right table.
  * `RIGHT JOIN`: Returns all rows from the right table, and the matched rows from the left table.
  * `FULL JOIN`: Returns rows when there is a match in one of the tables.
  * `SELF JOIN`: Joins a table with itself.
  * `UNION ALL`: Combines the result set of two or more SELECT statements (allows duplicate values).

### `SQL Data Types`
* Numeric:
  * `INT` (or INTEGER): Integer data type. 
  * `BIGINT`: Large integer data type. 
  * `SMALLINT`: Small integer data type. 
  * `TINYINT`: Very small integer data type. 
  * `DECIMAL` (or NUMERIC): Exact numeric data type with fixed precision and scale. 
  * `FLOAT`: Approximate numeric data type with floating-point precision. 
  * `REAL`: Approximate numeric data type, less precision than FLOAT. 
  * `DOUBLE` (or DOUBLE PRECISION): Approximate numeric data type with double the precision of FLOAT. 
  * `BIT`: Binary data type, typically used for boolean values. 
  * `SERIAL`: Auto-incrementing integer data type (implementation may vary between SQL databases).

* Date and Time:
  * `DATE`: Stores dates (year, month, day). 
  * `TIME`: Stores time (hours, minutes, seconds). 
  * `DATETIME`: Stores both date and time. 
  * `TIMESTAMP`: Stores date and time, often with timezone information. 
  * `YEAR`: Stores a year value.

* String:
  * `CHAR`: Fixed-length character string.
  * `VARCHAR`: Variable-length character string.
  * `TINYTEXT`: Very small text data type.
  * `TEXT`: Large text data type.
  * `BLOB`: Binary Large Object for storing binary data.
  * `MEDIUMTEXT`: Medium-sized text data type.
  * `MEDIUMBLOB`: Medium-sized binary data type.
  * `LONGTEXT`: Very large text data type.
  * `LONGBLOB`: Very large binary data type.
  * `ENUM`: Enumerated list of values, can only store one of the predefined values.
  * `SET`: Similar to ENUM, but can store multiple values from the predefined list.
  * `IN `: Used to specify multiple values in a WHERE clause.
  * `LIKE `: Used for pattern matching.
  * `BETWEEN `: Selects values within a given range.
  * `IS NULL `: Tests for NULL values.
  * `IS NOT NULL `: Tests for non-NULL values.
  * `EXCEPT `: Combines the result set of two or more SELECT statements and returns only the rows that appear in the first result set but not in the other result set.
  * `ALL `: Compares a value to every applicable value in the list according to the condition.
  * `ANY `: Compares a value to any applicable value in the list according to the condition.
  * `CASE `: Creates different outputs based on conditions.
  * `COALESCE `: Returns the first non-null expression in the list.
  * `NULLIF `: Returns NULL if the two expressions are equal.
  * `ROW_NUMBER `: Assigns a unique sequential integer to each row to which a window function is applied.
  * `RANK `: Assigns a unique integer to each distinct row within the partition of a result set.
  * `DENSE_RANK `: Assigns a unique integer to each distinct row within the partition of a result set.
  * `NTILE `: Divides an ordered set of rows into a specified number of groups called buckets and assigns a bucket number to each row.
  * `LAG `: Accesses data from a previous row in the same result set without the use of a self-join.
  * `LEAD `: Accesses data from a subsequent row in the same result set without the use of a self-join.
  * `FIRST_VALUE `: Returns the first value in an ordered set of values.
  * `LAST_VALUE `: Returns the last value in an ordered set of values.
  * `OFFSET `: Specifies the number of rows to skip before starting to return rows from the query expression.
  * `FETCH `: Specifies the number of rows to return after the OFFSET clause has been processed.
  * `TOP `: Specifies the number of rows or the percentage of rows to be returned.
  * `PERCENT `: Specifies the percentage of rows to return.
  * `ROWNUM `: Specifies the number of rows to return.
  * `ROWNUMBER `: Specifies the number of rows to return.
  * `LIMIT `: Specifies the number of rows to return.

* JSON:
  * `JSON`: Stores JSON (JavaScript Object Notation) data.

### Aggregations
* `COUNT`: Returns the number of rows that match a specified condition.
* `SUM`: Calculates the sum of a set of values.
* `AVG`: Calculates the average of a set of values.
* `MIN`: Returns the minimum value in a set of values.
* `MAX`: Returns the maximum value in a set of values.


### Operators
* `Arithmetic`: +, -, *, /, %
* `Comparison`: =, <>, !=, >, <, >=, <=
* `Logical`: AND, OR, NOT
* `Bitwise`: &, |, ^, ~, <<, >>
* `Assignment`: =, +=, -=, *=, /=, %=
* `Concatenation `: ||

### `Relational VS Non-Relational Databases`
* `Relational Databases`: Relational databases store data in tables and rows, and use Structured Query Language (SQL) for database access. They are based on the relational model, which organizes data into one or more tables (or "relations") of columns and rows, with a unique key identifying each row. Relational databases are widely used in applications where data is structured and relationships between data elements are well-defined.
* `Non-Relational Databases`: Non-relational databases store data in a variety of formats, such as key-value pairs, documents, graphs, or wide-column stores. They are designed to handle large volumes of unstructured or semi-structured data, and are often used in applications where data is not easily organized into tables and rows. Non-relational databases are also known as NoSQL databases, which stands for "not only SQL."

### `Normalization VS ERD`
* `Normalization`: Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity. Normalization involves dividing a database into multiple tables and defining relationships between the tables. The objective is to isolate data so that additions, deletions, and modifications can be made in just one table and then propagated through the rest of the database via the defined relationships.
* `ERD`: An Entity-Relationship Diagram (ERD) is a visual representation of the data model for a database. It shows the entities (tables) in the database, the attributes (columns) of each entity, and the relationships between the entities. ERDs are used to design and document databases, and can help developers understand the structure of the database and how data is related.

---

## `PostgreSQL Setup`
* Download and install the PostgreSQL
* Download and install the pgAdmin
* Open `pgAdmin4`
* Enter your password to initialize the database, this password will be the same as you set while installing the postgresql.
* Create a new server
  * Right click on `Servers` -> `Create` -> `Server`
  * Enter the name of the server
  * Enter the host name as `localhost`
  * Enter the port as `5432`
  * Enter the username as `postgres`
  * Enter the password
  * Click on `Save`

### `Setting Up SQL Queries in PyCharm`

* `Install Database Support Plugin:`
  * PyCharm provides built-in support for SQL databases, but ensure that the `Database Tools and SQL` plugin is enabled.
  * Go to `File` -> `Settings` -> `Plugins` -> `Marketplace`, search for `Database Tools and SQL`, and install it if it's not already installed.


* `Create a Database Connection:`
  * Open the Database tool window by going to `View` -> `Tool Windows` -> `Database`.
  * Click the `+` icon and select your database type (e.g., `PostgreSQL`, `MySQL`, `SQLite`).
  * Configure the connection by providing the necessary details (`host`, `port`, `database` `name`, `username`, `password`). Test the connection to ensure it's working.
  

* `Writing and Executing SQL Queries:`
  * Right-click on the database in the Database tool window and select `New` -> `Query Console`.
  * A new tab will open where you can write your SQL queries.
  * Write your SQL query in the console and press `Ctrl+Enter (Cmd+Enter on macOS)` to execute the query.
  * The results will be displayed in the Result tab below the query editor.
  

* `Viewing Output:`
  * After running the query, the output will be shown in the Result tab.
  * You can see the data in a tabular format, view the execution plan, and even export the results if needed.


![Screenshot 2024-08-03 at 5 17 05 PM](https://github.com/user-attachments/assets/2f7b5cdf-e0bf-42bb-a2b7-0575af55b802)


