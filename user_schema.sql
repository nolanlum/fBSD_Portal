-- This database schema, as well as other required tables, are auto-generated
-- by Django's syncdb command.
--
-- There is no need to manually run this SQL query on the SQLite database.
-- This file is only provided for reference, should an external tool wish to
-- interface with the database manually.
--
-- To create these database tables, run `python manage.py syncdb' in the
-- Django environment Python shell.

CREATE TABLE "auth_user" (
    "id" integer NOT NULL PRIMARY KEY,
    "username" varchar(30) NOT NULL UNIQUE,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL,
    "email" varchar(75) NOT NULL,
    "password" varchar(128) NOT NULL,
    "is_staff" bool NOT NULL,
    "is_active" bool NOT NULL,
    "is_superuser" bool NOT NULL,
    "last_login" datetime NOT NULL,
    "date_joined" datetime NOT NULL
)
CREATE TABLE "social_auth_usersocialauth" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "provider" varchar(32) NOT NULL,
    "uid" varchar(255) NOT NULL,
    "extra_data" text NOT NULL,
    UNIQUE ("provider", "uid")
)
CREATE INDEX "social_auth_usersocialauth_403f60f" ON "social_auth_usersocialauth" ("user_id")