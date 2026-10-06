DROP DATABASE IF EXISTS tool_repair_shop;
CREATE DATABASE tool_repair_shop;
USE tool_repair_shop;

CREATE TABLE Brand(
	BrandID INT PRIMARY KEY,
    BrandName varchar(50) UNIQUE NOT NULL
);

CREATE TABLE BatterySystem(
	BatterySystemID INT AUTO_INCREMENT PRIMARY KEY,
    BatterySystemName VARCHAR(20) NOT NULL,
    BrandID INT NOT NULL,
    Voltage DECIMAL(4,2) NOT NULL,
    CONSTRAINT fk_BatterySystemOwnerBrand
    FOREIGN KEY (BrandID)
    REFERENCES Brand(BrandID)
);

CREATE TABLE PowerTool(
	PowerToolID VARCHAR(20) PRIMARY KEY,
    PowerToolMarketingName VARCHAR(20) NOT NULL,
    BrandID INT NOT NULL,
    BatterySystemID INT NOT NULL,
	CONSTRAINT fk_BatterySystemID
    FOREIGN KEY (BatterySystemID)
    REFERENCES BatterySystem(BatterySystemID),
    CONSTRAINT fk_PowerToolBrand
    FOREIGN KEY (BrandID)
    REFERENCES Brand(BrandID)
);

CREATE TABLE Customer(
	GovID VARCHAR(11) PRIMARY KEY,
    FirstName VARCHAR(20),
    MiddleName VARCHAR(20),
    LastName VARCHAR(20),
    Birth DATE NOT NULL
);

CREATE TABLE ServiceOrder(
	ServiceID INT PRIMARY KEY,
    ServiceDescription VARCHAR(100),
    PowerToolID VARCHAR(20),
    CustomerID VARCHAR(11),
	Price DECIMAL(6,2) NOT NULL,
	CheckInDate DATE NOT NULL,
    CheckOutDate DATE,
    
	CONSTRAINT fk_PowerToolID
    FOREIGN KEY (PowerToolID)
    REFERENCES PowerTool(PowerToolID),
    CONSTRAINT fk_CustomerID
    FOREIGN KEY (CustomerID)
    REFERENCES Customer(GovID)
);


INSERT INTO Brand(BrandID, BrandName) 
VALUES
(1, 'STIHL'),
(2, 'KAERCHER'),
(3, 'MAKITA'),
(4, 'BOSCH'),
(5, 'MILWAUKEE');

SELECT * FROM Brand;

INSERT INTO BatterySystem(BatterySystemID, BatterySystemName, BrandID, Voltage)
VALUES
(1, 'AllPro', 1, 36.00),
(2, 'AK', 1, 36.00),
(3, 'AS', 1, 12.00),
(4, 'CXT', 3, 12.00),
(5, 'LXT', 3, 12.00),
(6, 'XGT', 3, 12.00),
(7, 'AmpShare', 4, 18.00),
(8, 'M12', 5, 12.00),
(9, 'M18', 5, 18.00);

SELECT * FROM BatterySystem;

INSERT INTO PowerTool(PowerToolID, PowerToolMarketingName, BrandID, BatterySystemID)
VALUES
(1, "MSA600", 1, 1),
(2, "DTD173", 3, 5);

SELECT * FROM PowerTool;

INSERT INTO Customer(GovId, FirstName, MiddleName, LastName, Birth)
VALUES
('12345678900', 'matheus', 'silveira', 'venturini','1994-09-03');


INSERT INTO ServiceOrder(ServiceID, ServiceDescription, PowerToolID, CustomerID, Price, CheckInDate, CheckOutDate)
VALUES
(1, 'Troca do sabre da motosserra', '1', '12345678900', 400.00, '2026-10-05' , '2026-10-05')

