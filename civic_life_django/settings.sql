-- settings.sql
CREATE DATABASE civic_life;
CREATE USER civic_user WITH PASSWORD 'civic';
GRANT ALL PRIVILEGES ON DATABASE civic_life TO civic_user;