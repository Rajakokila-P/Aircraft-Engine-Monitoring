CREATE DATABASE create_database.sql;
GO

USE AircraftEngineMonitoring;
GO

CREATE TABLE EngineReadings (
    reading_id INT IDENTITY(1,1) PRIMARY KEY,
    engine_id VARCHAR(20) NOT NULL,
    recorded_at DATETIME2 NOT NULL,
    temperature_c DECIMAL(8,2),
    oil_pressure_psi DECIMAL(8,2),
    vibration_mm_s DECIMAL(8,2),
    fuel_flow_kg_h DECIMAL(10,2),
    engine_speed_percent DECIMAL(8,2),
    flight_hours INT,
    status VARCHAR(20),
    maintenance_required VARCHAR(3)
);
GO
