CREATE DATABASE CompanyDatabase;
GO

USE CompanyDatabase;
GO


CREATE TABLE Employee (
    id UNIQUEIDENTIFIER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    birth_year DATE,
    employment_start datetime
);

CREATE TABLE Complaint (
    id UNIQUEIDENTIFIER PRIMARY KEY,
    return_id UNIQUEIDENTIFIER,
    issue_date datetime,
    resolve_date datetime,
    complaint VARCHAR(1000)
);

CREATE TABLE Products (
    id UNIQUEIDENTIFIER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    issue_year SMALLINT,
    main_building_material VARCHAR(255)
);

CREATE TABLE ReturnProcessing (
    employee_id UNIQUEIDENTIFIER,
    return_id UNIQUEIDENTIFIER,
    -- PRIMARY KEY (employee_id, return_id),
    FOREIGN KEY (employee_id) REFERENCES Employee(id)
);

CREATE TABLE ReturnsTable (
    id UNIQUEIDENTIFIER PRIMARY KEY,
    product_id UNIQUEIDENTIFIER,
    status VARCHAR(50),
    employee_id UNIQUEIDENTIFIER,
    company_cost DECIMAL(18, 2),
    description VARCHAR(1000),
    processing_started datetime,
    processing_finished datetime,
    FOREIGN KEY (product_id) REFERENCES Products(id),
    FOREIGN KEY (employee_id) REFERENCES Employee(id)
);
GO
