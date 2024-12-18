# SFWE 511 - Semester Project - Code Based Historian

A code based historian that reads and stores information about the 
semester project created PLC program from OpenPLC Runtime and ScadaBR.
Utilizes Python to read data from `127.0.0.1` port 502 and stores that data into 
a database for future analysis.

## Example Database Structure

### InputRegister Table
| ID | Time                       | Name            | Location Type  | Location | Type | Value |
|----|----------------------------|-----------------|----------------|----------|------|-------|
| 1  | 2024-12-08 00:23:34.949717 | FlowRateSensor0 | InputRegisters | 0        | int  | 4     |

### InputStatus Table
| ID | Time                       | Name               | Location Type | Location | Type    | Value |
|----|----------------------------|--------------------|---------------|----------|---------|-------|
| 1  | 2024-12-08 00:23:34.949717 | BoosterPumpStatus0 | InputStatues  | 0        | boolean | False |

### HoldingRegister Table
| ID | Time                       | Name                   | Location Type    | Location | Type | Value |
|----|----------------------------|------------------------|------------------|----------|------|-------|
| 1  | 2024-12-08 00:23:34.949717 | IsolationValveCommand0 | HoldingRegisters | 0        | int  | 50    |

### CoilStatus Table
| ID | Time                       | Name                | Location Type | Location | Type    | Value |
|----|----------------------------|---------------------|---------------|----------|---------|-------|
| 1  | 2024-12-08 00:23:34.949717 | BoosterPumpCommand0 | CoilStatuses  | 0        | boolean | False |