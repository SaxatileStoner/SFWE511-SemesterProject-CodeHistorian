from enum import Enum

# Enumeration for all Input Register types, i.e. %IW0
class InputRegisters(Enum):
    FlowRateSensor0 = 0
    FlowRateSensor1 = 1
    FlowRateSensor2 = 2
    IsolationValveStatus0 = 3
    IsolationValveStatus1 = 4
    IsolationValveStatus2 = 5
    EductorValveStatus0 = 6
    EductorValveStatus1 = 7
    EductorValveStatus2 = 8
    UltrasonicTankLevelSensor0 = 9
    UltrasonicTankLevelSensor1 = 10
    UltrasonicTankLevelSensor2 = 11
    DisposalValveStatus = 12
    pHSensor = 13

# Enumeration for all Input Status types, i.e. %IX0.0
class InputStatus(Enum):
    BoosterPumpStatus0 = 0
    BoosterPumpStatus1 = 1
    BoosterPumpStatus2 = 2
    GeneralSiteAlarm0 = 3
    DistributionPumpStatus = 4
    HighPressureSwitch0 = 5
    HighPressureSwitch1 = 6
    HighPressureSwitch2 = 7

# Enumeration for all Holder Register types, i.e. %QW0
class HoldingRegisters(Enum):
    IsolationValveCommand0 = 0
    IsolationValveCommand1 = 1
    IsolationValveCommand2 = 2
    EductorValveCommand0 = 3
    EductorValveCommand1 = 4
    EductorValveCommand2 = 5
    DistributionPumpSpeedCommand = 6
    DisposalValveCommand = 7

# Enumeration for all Coil Status types, i.e. %QX0.0
class CoilStatus(Enum):
    BoosterPumpCommand0 = 0
    BoosterPumpCommand1 = 1
    BoosterPumpCommand2 = 2
    pHAlertAlarm = 3
    pHCriticalAlarm = 4
    BoosterPumpAlarm0 = 5
    BoosterPumpAlarm1 = 6
    BoosterPumpAlarm2 = 7
    IsolationValveAlarm0 = 8
    IsolationValveAlarm1 = 9
    IsolationValveAlarm2 = 10
    FlowSensorAlarm0 = 11
    FlowSensorAlarm1 = 12
    FlowSensorAlarm2 = 13
    ExcessiveFlowAlarm0 = 14
    ExcessiveFlowAlarm1 = 15
    ExcessiveFlowAlarm2 = 16
    EductorValveAlarm0 = 17
    EductorValveAlarm1 = 18
    EductorValveAlarm2 = 19
    DistributionPumpCommand = 20
    DistributionPumpAlarm = 21
    HighPressureSwitchAlarm0 = 22
    HighPressureSwitchAlarm1 = 23
    HighPressureSwitchAlarm2 = 24
    askHMIContainmentUnitAttached = 25
    askHMIContainmentUnitFull = 26
    DisposalValveAlarm = 27
    Tank0_CapacityAlarm = 28
    Tank1_CapacityAlarm = 29
    Tank2_CapacityAlarm = 30
    CentralTankAlarmSwitch = 31
    ControlCenterHornStrobeAlarm = 32
    pHWarningHMI = 33
    pHCriticalHMI = 34
    HMITankDisposalButton = 35
    isContainmentUnitAttached = 36
    isContainmentUnitFull = 37