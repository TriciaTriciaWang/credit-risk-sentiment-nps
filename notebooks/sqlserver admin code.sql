-- Create a login at the server level
USE master;
GO
CREATE LOGIN CreditUser WITH PASSWORD = 'StrongPassword123!';
GO

-- 🧱 4. Create User in Your Database
-- Now switch to your actual project database (CreditRiskDB):

-- Either change the database from the dropdown

-- Or run this SQL next:

-- Create the user inside your database
USE CreditRiskDB;
GO
CREATE USER CreditUser FOR LOGIN CreditUser;
GO

-- Give read/write access
ALTER ROLE db_datareader ADD MEMBER CreditUser;
ALTER ROLE db_datawriter ADD MEMBER CreditUser;
GO
