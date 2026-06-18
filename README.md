# PostgreSQLdemo

This is a demo project to show how to connect to a PostgreSQL database using Python. It uses the psycopg2 library to connect to the database and execute SQL queries. It also uses SQLAlchemy for ORM and python-dotenv for managing environment variables.

Step 1 -  The changes in the local sytstem should bring to staging area using the command below:

```git add .```

Step 2 - After adding the changes to staging area, we need to commit the changes with a message using the command below:

```git commit -m "Your commit message here"```  

Step 3 - After committing the changes, we need to push the changes to the remote repository using the command below:

```git push origin main```

To connect with the database server made AWS RDS instance and created a database named postgres. The connection details are stored in the .env file.
change the host to the endpoint address of the RDS instance, and the user and password to the credentials you set up when creating the RDS instance.
Create an inbound rule in the security group of the RDS instance to allow incoming traffic on port 5432 from your local machine's IP address. This will allow your local machine to connect to the RDS instance.