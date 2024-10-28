USE CompanyDatabase;
GO

BULK INSERT Products FROM 'C:\Users\oenea\Documents\SQL Server Management Studio\generator\output\Products_t2.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT Complaint FROM 'C:\Users\oenea\Documents\SQL Server Management Studio\generator\output\Complaints_t2.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ReturnProcessing FROM 'C:\Users\oenea\Documents\SQL Server Management Studio\generator\output\ReturnProcessing_t2.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ReturnsTable FROM 'C:\Users\oenea\Documents\SQL Server Management Studio\generator\output\Returns_t2.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')

GO