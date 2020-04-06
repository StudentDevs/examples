# Week 3

## git and GitHub

### Tell git your name and email to use in commits

On your Ubuntu server (or your local machine if you're using git from
there), configure git with your name and email address.
People will see this info in your commits when they view a repository
you've pushed to.

    git config --global user.name "YOUR_FIRST_NAME YOUR_LAST_NAME"

    git config --global user.email "YOUR_EMAIL_ADDRESS"

### Fork the `StudentDevs/app` repo in GitHub

Forking a repository creates a copy of the repository in your own GitHub
account. You can make any changes you want to your own copy of the repo.

Go to https://github.com/StudentDevs/app and the click the "Fork" button
near the top-right of the page. (If prompted to choose where to fork the
repo to, choose your GitHub account name from the list GitHub shows you.)

More info:
https://help.github.com/en/github/getting-started-with-github/fork-a-repo

### Branch, make changes, commit, and push

Clone your forked copy of the repo.

    git clone https://github.com/YOUR_GITHUB_USERNAME/app.git

Note: if you've added your public key to github, use this clone command,
instead, so public key authentication will be used and you won't be
prompted for your username and password later when you push.

    git clone git@github.com:YOUR_GITHUB_USERNAME/app.git

Change directory into the cloned repo:

    cd app

View which branch you're on:

    git branch

Create a new branch based on the current branch you're on:

    git checkout -b NAME_OF_NEW_BRANCH

You'll now see the new branch name is the one you're one:

    git branch

Edit some files (you can use any editor you want such as `nano` or `vi`).

Have git show you what files you've changed:

    git status

Have git show you what the actual changes are:

    git diff

Tell git that you want to "stage" these changes so you can commit them:

    git add NAME_OF_ADDED_OR_MODIFIED_FILE

If you'd instead removed a file, use:

    git rm NAME_OF_DELETED_FILE

Have git show you which changes are staged and which aren't yet staged:

    git status

Have git show you the actual changes in the staged files you're going to commit:

    git diff --cached

Commit the staged changes:

    git commit -m "Put a description of your changes here"

Now push your branch with this new commit:

    git push

You'll be promoted for your GitHub username and password. (If you're instead
using public key authentication, you may be prompted for your private key's
passphrase in order to temporarily decrypt your key so it can be used for
public key authentication.)

Next, head back over to https://github.com/YOUR_GITHUB_USERNAME/app

Click on "branches" and then on the line where you see your new branch
you've created, click the "New pull request" button on the right.

Since you've forked the StudentDevs/app repo, by default GitHub may
ask if you want to open a pull request into the StudentDevs/app repo
rather than into your own repo. Right now you just want to merge into
your own repo.

Change the "base repository" option in the "open pull request" form
from "StudentDevs/app" to "YOUR_GITHUB_USERNAME/app". Now click
"Create pull request".

Click on "Files changed" to sanity check these are the files you want
to merge into your master branch. Then, click back to the "conversation"
tab and click "Merge pull request".

## SQL

Structured Query Language (SQL) is the language used to communicate with most
relational databases. You'll hear people refer to "SQL databases" and they just
mean one of these many databases that uses SQL.

SQL has only a few common commands you'll want to learn well:

    SELECT
    INSERT
    UPDATE
    DELETE

There's also other commands like `CREATE TABLE` and `ALTER TABLE` that you'll
need to use when you're a developer using databases, but you'll often just
Google the right syntax to use for those when you need them.

### SQL Databases

There are many different SQL databases. They all use basically the same SQL
but with some minor differences when you get into complicated stuff. Some
SQL databases are free and open source, others are expensive and commercial.
Many of the free and open source SQL databases are extremely good and used
commercially, including by big companies.

So far we're just using SQLite, a very lightweight SQL database that's good
for development (and other things, like embedding in standalone desktop
applications---Chrome and Firefox have SQLite embedded in them).

### Database Tables

A database consists of one or more tables. You can think of a table as a
single sheet/tab/page in a spreadsheet: there are columns and rows, each
column has a name, each row is a single record.

For example, here's a table named `people`:

```
---------------------------------------------------
| id      | first_name        | last_name         |
---------------------------------------------------
| 1       | Joe               | Shmoe             |
| 2       | Jane              | Doe               |
| 3       | Mike              | Diamond           |
---------------------------------------------------
```

### SELECT

To get records out of a table, you use `SELECT`. The simplest format is:

```sql
SELECT [list of columns] FROM [table]
```

For example:

```sql
SELECT * FROM people
```

That would return all columns for all records in the `people` table.

You can also select only records that match certain criteria using a `WHERE` clause.

```sql
SELECT * FROM people WHERE id = 2
```

That would select all columns for all records that have an `id` value equal to `2`.
Which, in the example above, is just the one record for Jane Doe.

There is all sorts of fanciness you can do with selecting. For example, selecting
only certain fields with criteria using wildcards and returning the results in
a certain order:

```sql
SELECT first_name, last_name
FROM people
WHERE first_name LIKE 'J%'
ORDER BY first_name
```

### INSERT

To put data into a database table, you use `INSERT`

The format is:

```sql
INSERT INTO [table] ( [comma-separated list of column names] )
VALUES ( [comma-separated list values for the column names you listed] )
```

For example:

```sql
INSERT INTO people (id, first_name, last_name)
VALUES (4, 'Jack', 'Ryan')
```

In general, you don't have to specify and provide every column for a table.
And the order of columns doesn't matter as long as you provide the values
in the same order as the column names you listed.

### UPDATE

To modify existing records, you use `UPDATE`.

The format is:

```sql
UPDATE [table] SET [column] = [value] WHERE [...]
```

Caution: The `UPDATE` command will update all records that match the criteria
you specify. Be sure to provide a `WHERE` clause if you aren't
trying to update every record in the table.

The `WHERE` clause is just like when you do a `SELECT`: you can be as fancy as
you need to be.

For example:

```sql
UPDATE people SET last_name = 'Smith' WHERE id = 2
```

### DELETE

To modify existing records, you use `DELETE`.

The format is:

```sql
DELETE FROM [table] WHERE [...]
```

Caution: Just like `UDPATE`, `DELETE` will delete everything in a table
unless you narrow down what to delete using a `WHERE` clause.

### Joins

There's a whole extra level of power using `SELECT` than just selecting from
a single table: joining two or more tables and selecting from the joined tables.

There are few different syntaxes in SQL for this and there is some difference.
We'll just use what I think is the most generally useful and easy to remember:

Example:

Imagine you had a `pets` table with at least two columns, `peopleid` and `name`:

```sql
SELECT people.id, people.first_name, pets.name
FROM people, pets
WHERE people.id = pets.peopleid
```

This would return a list like this:

```
| 1       | Joe               | Rover            |
| 1       | Joe               | Spot             |
| 3       | Mike              | Fluffy           |
```

### Using the `sqlite3` command line interface

An easy way to play around with SQL is to open your sqlite database
from the command line:

    sqlite3 FILENAME

Press TAB twice to see a list of all commands.

Use this sqlite command to list which tables exist in the database:

    .tables
