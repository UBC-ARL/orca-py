from enum import IntEnum


class ORCA_REGISTER(IntEnum):
    CTRL_REG_0 = 0  # Control Register 1
    CTRL_REG_1 = 1  # Control Register 2
    CTRL_REG_2 = 2  # Control Register 3
    CTRL_REG_3 = 3  # Control Register 4
    CTRL_REG_4 = 4  # Control Register 5
    CTRL_REG_5 = 5  # Control Register 6
    CTRL_REG_6 = 6  # Control Register 7
    CTRL_REG_7 = 7  # Control Register 8
    GUI_PERIOD_CMD = (
        8  # Commanded period between IrisControls GUI frames in milliseconds.
    )
    KIN_SW_TRIGGER = (
        9  # Software trigger for initiating kinematic movements over Modbus.
    )

    # Non-contiguous addresses. 10 free registers. 10 - 19

    HBA_DUTY_CMD = 20  # Manual control of Hbridge A duty (-32767 to 32767)
    HBB_DUTY_CMD = 21  # Manual control of Hbridge B duty (-32767 to 32767)
    HBC_DUTY_CMD = 22  # Manual control of Hbridge C duty (-32767 to 32767)
    HBD_DUTY_CMD = 23  # Manual control of Hbridge D duty (-32767 to 32767)
    HBA_CURRENT_CMD = 24  # Manual control of Hbridge A current in mA
    HBB_CURRENT_CMD = 25  # Manual control of Hbridge B current in mA
    HBC_CURRENT_CMD = 26  # Manual control of Hbridge C current in mA
    HBD_CURRENT_CMD = 27  # Manual control of Hbridge D current in mA
    FORCE_CMD = 28  # Commanded actuator output force in millinewtons. Lower 2 bytes.
    FORCE_CMD_H = 29  # Commanded actuator output force in millinewtons. Upper 2 bytes.
    POSITION_CMD = 30  # Commanded actuator position in encoder counts. Lower 2 bytes.
    POSITION_CMD_H = 31  # Commanded actuator position in encoder counts. Upper 2 bytes.

    # Non-contiguous addresses. 1 free registers. 32 - 32

    STATOR_CAL_VERSION = 33  # Stator calibration version.
    BS_GAIN_CMD = 34  # Hall sensor analog circuit gain.
    CS_GAIN_CMD = 35  # Current sensor analog circuit gain.
    H0Z = 36  # Saved zero value for Hall sensor 0.
    H1Z = 37  # Saved zero value for Hall sensor 1.
    H2Z = 38  # Saved zero value for Hall sensor 2.
    H3Z = 39  # Saved zero value for Hall sensor 3.
    H4Z = 40  # Saved zero value for Hall sensor 4.
    H5Z = 41  # Saved zero value for Hall sensor 5.
    H6Z = 42  # Saved zero value for Hall sensor 6.
    H7Z = 43  # Saved zero value for Hall sensor 7.
    C0Z = 44  # Saved zero value for current sensor 0.
    C1Z = 45  # Saved zero value for current sensor 1.
    C2Z = 46  # Saved zero value for current sensor 2.
    C3Z = 47  # Saved zero value for current sensor 3.
    C4Z = 48  # Saved zero value for current sensor 4.
    C5Z = 49  # Saved zero value for current sensor 5.
    C6Z = 50  # Saved zero value for current sensor 6.
    C7Z = 51  # Saved zero value for current sensor 7.
    CTFN = 52  # -
    R0 = 53  # Total resistance of motor phase 0.
    R1 = 54  # Total resistance of motor phase 1.
    R2 = 55  # Total resistance of motor phase 2.
    R3 = 56  # Total resistance of motor phase 3.
    I0A = 57  # STATOR_CAL_SECTION | Width: 1 | -
    I1A = 58  # STATOR_CAL_SECTION | Width: 1 | -
    I2A = 59  # STATOR_CAL_SECTION | Width: 1 | -
    I3A = 60  # STATOR_CAL_SECTION | Width: 1 | -
    I4A = 61  # STATOR_CAL_SECTION | Width: 1 | -
    I5A = 62  # STATOR_CAL_SECTION | Width: 1 | -
    I6A = 63  # STATOR_CAL_SECTION | Width: 1 | -
    I7A = 64  # STATOR_CAL_SECTION | Width: 1 | -
    I0B = 65  # STATOR_CAL_SECTION | Width: 1 | -
    I1B = 66  # STATOR_CAL_SECTION | Width: 1 | -
    I2B = 67  # STATOR_CAL_SECTION | Width: 1 | -
    I3B = 68  # STATOR_CAL_SECTION | Width: 1 | -
    I4B = 69  # STATOR_CAL_SECTION | Width: 1 | -
    I5B = 70  # STATOR_CAL_SECTION | Width: 1 | -
    I6B = 71  # STATOR_CAL_SECTION | Width: 1 | -
    I7B = 72  # STATOR_CAL_SECTION | Width: 1 | -
    I0C = 73  # STATOR_CAL_SECTION | Width: 1 | -
    I1C = 74  # STATOR_CAL_SECTION | Width: 1 | -
    I2C = 75  # STATOR_CAL_SECTION | Width: 1 | -
    I3C = 76  # STATOR_CAL_SECTION | Width: 1 | -
    I4C = 77  # STATOR_CAL_SECTION | Width: 1 | -
    I5C = 78  # STATOR_CAL_SECTION | Width: 1 | -
    I6C = 79  # STATOR_CAL_SECTION | Width: 1 | -
    I7C = 80  # STATOR_CAL_SECTION | Width: 1 | -
    I0D = 81  # STATOR_CAL_SECTION | Width: 1 | -
    I1D = 82  # STATOR_CAL_SECTION | Width: 1 | -
    I2D = 83  # STATOR_CAL_SECTION | Width: 1 | -
    I3D = 84  # STATOR_CAL_SECTION | Width: 1 | -
    I4D = 85  # STATOR_CAL_SECTION | Width: 1 | -
    I5D = 86  # STATOR_CAL_SECTION | Width: 1 | -
    I6D = 87  # STATOR_CAL_SECTION | Width: 1 | -
    I7D = 88  # STATOR_CAL_SECTION | Width: 1 | -

    # Non-contiguous addresses. 7 free registers. 89 - 95

    SHAFT_CAL_VERSION = 96  # SHAFT_CAL_SECTION | Width: 1 | Shaft calibration version.
    H0M = 97  # SHAFT_CAL_SECTION | Width: 1 | Maximum value read by Hall sensor 0.
    H1M = 98  # SHAFT_CAL_SECTION | Width: 1 | Maximum value read by Hall sensor 1.
    H2M = 99  # SHAFT_CAL_SECTION | Width: 1 | Maximum value read by Hall sensor 2.
    H3M = 100  # SHAFT_CAL_SECTION | Width: 1 | Maximum value read by Hall sensor 3.
    H4M = 101  # SHAFT_CAL_SECTION | Width: 1 | Maximum value read by Hall sensor 4.
    H5M = 102  # SHAFT_CAL_SECTION | Width: 1 | Maximum value read by Hall sensor 5.
    H6M = 103  # SHAFT_CAL_SECTION | Width: 1 | Maximum value read by Hall sensor 6.
    H7M = 104  # SHAFT_CAL_SECTION | Width: 1 | Maximum value read by Hall sensor 7.
    S45 = 105  # SHAFT_CAL_SECTION | Width: 1 | -
    S90 = 106  # SHAFT_CAL_SECTION | Width: 1 | -

    # Non-contiguous addresses. 5 free registers. 107 - 111

    FORCE_CAL_VERSION = 112  # FORCE_CAL_SECTION | Width: 1 | Force calibration version.
    AAL = 113  # FORCE_CAL_SECTION | Width: 1 | -
    BAL = 114  # FORCE_CAL_SECTION | Width: 1 | -
    CAL = 115  # FORCE_CAL_SECTION | Width: 1 | -
    DAL = 116  # FORCE_CAL_SECTION | Width: 1 | -
    F30 = 117  # FORCE_CAL_SECTION | Width: 1 | -
    F60 = 118  # FORCE_CAL_SECTION | Width: 1 | -
    F90 = 119  # FORCE_CAL_SECTION | Width: 1 | -

    # Non-contiguous addresses. 8 free registers. 120 - 127

    TUNING_VERSION = 128  # TUNING_SECTION | Width: 1 | Tuning calibration version.
    CC_PGAIN = 129  # TUNING_SECTION | Width: 1 | Current controller proportional gain.
    CC_IGAIN = 130  # TUNING_SECTION | Width: 1 | Current controller integral gain.
    CC_FGAIN = 131  # TUNING_SECTION | Width: 1 | Current controller forward gain.
    CC_MAX_DUTY = (
        132  # TUNING_SECTION | Width: 1 | Current controller maximum duty cycle.
    )
    PC_PGAIN = 133  # TUNING_SECTION | Width: 1 | Position controller proportional gain.
    PC_IGAIN = 134  # TUNING_SECTION | Width: 1 | Position controller integral gain.
    PC_DVGAIN = 135  # TUNING_SECTION | Width: 1 | Position controller velocity gain.
    PC_DEGAIN = (
        136  # TUNING_SECTION | Width: 1 | Position controller error derivative gain.
    )
    PC_FSATU = 137  # TUNING_SECTION | Width: 1 | Position controller maximum force output. Lower 2 bytes.
    PC_FSATU_H = 138  # TUNING_SECTION | Width: 1 | Position controller maximum force output. Upper 2 bytes.
    USER_MAX_TEMP = 139  # TUNING_SECTION | Width: 1 | User configurable maximum motor temperature before over temperature error in degrees Celsius.
    USER_MAX_FORCE = 140  # TUNING_SECTION | Width: 1 | User configurable maximum force output in millinewtons. Lower 2 bytes.
    USER_MAX_FORCE_H = 141  # TUNING_SECTION | Width: 1 | User configurable maximum force output in millinewtons. Upper 2 bytes.
    USER_MAX_POWER = 142  # TUNING_SECTION | Width: 1 | User configurable maximum power burn in watts.
    SAFETY_DGAIN = 143  # TUNING_SECTION | Width: 1 | Speed damping gain value used when communications are interrupted.

    # Non-contiguous addresses. 6 free registers. 144 - 149

    PC_SOFTSTART_PERIOD = 150  # TUNING_SECTION | Width: 1 | Time in ms over which the position controller max force output will ramp from zero any time a mode of operation in which the position controller used is entered
    FORCE_UNITS = 151  # TUNING_SECTION | Width: 1 | Determines whether forces will interpreted in legacy unitless form or in millinewtons.

    # Non-contiguous addresses. 8 free registers. 152 - 159

    USR_OPT_VERSION = (
        160  # USER_OPTIONS_SECTION | Width: 1 | User options section version.
    )

    # Non-contiguous addresses. 1 free registers. 161 - 161

    LOG_PERIOD = (
        162  # USER_OPTIONS_SECTION | Width: 1 | Period between data log entries.
    )
    USER_COMMS_TIMEOUT = 163  # USER_OPTIONS_SECTION | Width: 1 | Time between successful force or position commands before a communications error occurs. In milliseconds.
    USR_MB_BAUD_LO = 164  # USER_OPTIONS_SECTION | Width: 1 | Default Modbus baudrate low 16 bits. Leaving this register at 0 will use the system default of 19200 bps.
    USR_MB_BAUD_HI = 165  # USER_OPTIONS_SECTION | Width: 1 | Default Modbus baudrate high 16 bits. Leaving this register at 0 will use the system default of 19200 bps.
    FORCE_FILT = 166  # USER_OPTIONS_SECTION | Width: 1 | Force output IIR filter alpha value. Maps 0-65535 to alpha values of 0 to 1.
    POS_FILT = 167  # USER_OPTIONS_SECTION | Width: 1 | Position output IIR filter alpha value. Maps 0-65535 to alpha values of 0 to 1.
    USR_MB_DELAY = 168  # USER_OPTIONS_SECTION | Width: 1 | Default Modbus interframe delay in microseconds. Default value is 2000 us.
    USR_MB_ADDR = 169  # USER_OPTIONS_SECTION | Width: 1 | Start up Modbus address. Default value is 1.
    MB_RS485_MODE = 170  # USER_OPTIONS_SECTION | Width: 1 | Determines whether the Modbus transmitter will be disabled during reception to enable RS485 compliant communications.

    # Non-contiguous addresses. 92 free registers. 171 - 262

    UART0_UP_RATE = 263  # COUNT_SECTION | Width: 1 | Number of bytes transmitted in the last second by UART0.
    UART1_UP_RATE = 264  # COUNT_SECTION | Width: 1 | Number of bytes transmitted in the last second by UART1.
    UART0_DOWN_RATE = 265  # COUNT_SECTION | Width: 1 | Number of bytes received in the last second by UART0.
    UART1_DOWN_RATE = 266  # COUNT_SECTION | Width: 1 | Number of bytes received in the last second by UART1.
    GUI_DROPPED_FRAMES = 267  # COUNT_SECTION | Width: 1 | Total number of skipped IrisControls GUI transactions.
    GUI_DROPPED_FPS = (
        268  # COUNT_SECTION | Width: 1 | Number of dropped frames per second.
    )
    LOOP_FREQ = 269  # COUNT_SECTION | Width: 1 | Main loop run frequency in kilohertz.
    SHAFT_CAL_COUNT = 270  # COUNT_SECTION | Width: 1 | -
    STATOR_CAL_COUNT = 271  # COUNT_SECTION | Width: 1 | -
    MOTOR_FRAME_COUNT = 272  # COUNT_SECTION | Width: 1 | Number of complete motor frames in the last second.
    MB_FREQ = 273  # COUNT_SECTION | Width: 1 | Number of successful Modbus messages in the last second.

    # Non-contiguous addresses. 39 free registers. 274 - 312

    GUI_PERIOD = 313  # STATUS_SECTION | Width: 1 | Period between IrisControls GUI communications in milliseconds.
    SHAFT_SIGNAL_STR = 314  # STATUS_SECTION | Width: 1 | -
    BS_GAIN_ACT = 315  # STATUS_SECTION | Width: 1 | Hall sensor analog circuit gain.
    CS_GAIN_ACT = 316  # STATUS_SECTION | Width: 1 | Current sensor analog circuit gain.
    MODE_OF_OPERATION = 317  # STATUS_SECTION | Width: 1 | Active mode the actuator is currently running in.
    CALIBRATION_STATUS = 318  # STATUS_SECTION | Width: 1 | A value other than zero indicates a calibration routine is in process.
    KINEMATIC_STATUS = 319  # STATUS_SECTION | Width: 1 | Indicates the state of the kinematic controller, and which motion is currently being performed.
    HBA_TARGET = 320  # STATUS_SECTION | Width: 1 | Active Hbridge A target duty cycle value. Ranges from -32768 to 32767.
    HBB_TARGET = 321  # STATUS_SECTION | Width: 1 | Active Hbridge B target duty cycle value. Ranges from -32768 to 32767.
    HBC_TARGET = 322  # STATUS_SECTION | Width: 1 | Active Hbridge C target duty cycle value. Ranges from -32768 to 32767.
    HBD_TARGET = 323  # STATUS_SECTION | Width: 1 | Active Hbridge D target duty cycle value. Ranges from -32768 to 32767.
    CCA_TARGET = 324  # STATUS_SECTION | Width: 1 | Active current controller Hbridge A target current value in milliamps.
    CCB_TARGET = 325  # STATUS_SECTION | Width: 1 | Active current controller Hbridge B target current value in milliamps.
    CCC_TARGET = 326  # STATUS_SECTION | Width: 1 | Active current controller Hbridge C target current value in milliamps.
    CCD_TARGET = 327  # STATUS_SECTION | Width: 1 | Active current controller Hbridge D target current value in milliamps.
    FC_TARGET = 328  # STATUS_SECTION | Width: 1 | Active force controller target force value in millinewtons. Low 2 bytes.
    FC_TARGET_H = 329  # STATUS_SECTION | Width: 1 | Active force controller target force value in millinewtons. High 2 bytes.
    PC_TARGET = 330  # STATUS_SECTION | Width: 1 | Active position controller target position value in micrometers. Low 2 bytes.
    PC_TARGET_H = 331  # STATUS_SECTION | Width: 1 | Active position controller target position value in micrometers. High 2 bytes.

    # Non-contiguous addresses. 4 free registers. 332 - 335

    STATOR_TEMP = 336  # SENSOR_SECTION | Width: 1 | Temperature of the motor stator in degrees Celsius.
    DRIVER_TEMP = 337  # SENSOR_SECTION | Width: 1 | Temperature of the motor driver in degrees Celsius.
    VDD_FINAL = 338  # SENSOR_SECTION | Width: 1 | Motor supply voltage in volts.
    SHAFT_PHASE_FINAL = 339  # SENSOR_SECTION | Width: 1 | -
    SHAFT_PIXEL = 340  # SENSOR_SECTION | Width: 1 | -
    SHAFT_PIXEL_H = 341  # SENSOR_SECTION | Width: 1 | -
    SHAFT_POS_UM = 342  # SENSOR_SECTION | Width: 1 | Shaft absolute position in micrometers. Lower 2 bytes.
    SHAFT_POSITION_H = 343  # SENSOR_SECTION | Width: 1 | Shaft absolute position in micrometers. Upper 2 bytes.
    SHAFT_SPEED_MMPS = 344  # SENSOR_SECTION | Width: 1 | Shaft speed in millimeters per second. Lower 2 bytes.
    SHAFT_SHEED_H = 345  # SENSOR_SECTION | Width: 1 | Shaft speed in millimeters per second. Upper 2 bytes.
    SHAFT_ACCEL_MMPSS = 346  # SENSOR_SECTION | Width: 1 | Shaft acceleration in millimeters per second per second. Lower 2 bytes.
    SHAFT_ACCEL_H = 347  # SENSOR_SECTION | Width: 1 | Shaft acceleration in millimeters per second per second. Upper 2 bytes.
    FORCE = 348  # SENSOR_SECTION | Width: 1 | Sensed actuator output force in millinewtons. Lower 2 bytes.
    FORCE_H = 349  # SENSOR_SECTION | Width: 1 | Sensed actuator output force in millinewtons. Upper 2 bytes.
    POWER = 350  # SENSOR_SECTION | Width: 1 | Sensed actuator output power in watts.
    HBA_CURRENT = 351  # SENSOR_SECTION | Width: 1 | Sensed phase current for Hbridge A, in milliamps.
    HBB_CURRENT = 352  # SENSOR_SECTION | Width: 1 | Sensed phase current for Hbridge B, in milliamps.
    HBC_CURRENT = 353  # SENSOR_SECTION | Width: 1 | Sensed phase current for Hbridge C, in milliamps.
    HBD_CURRENT = 354  # SENSOR_SECTION | Width: 1 | Sensed phase current for Hbridge D, in milliamps.
    AVG_POWER = 355  # SENSOR_SECTION | Width: 1 | Average sensed actuator output power in watts.
    COIL_TEMP = 356  # SENSOR_SECTION | Width: 1 | Estimated coil temperature in degrees Celsius.

    # Non-contiguous addresses. 7 free registers. 357 - 363

    RAW_LOCK = 364  # RAW_SENSOR_SECTION | Width: 1 |
    H0_RAW = 365  # RAW_SENSOR_SECTION | Width: 1 |
    H1_RAW = 366  # RAW_SENSOR_SECTION | Width: 1 |
    H2_RAW = 367  # RAW_SENSOR_SECTION | Width: 1 |
    H3_RAW = 368  # RAW_SENSOR_SECTION | Width: 1 |
    H4_RAW = 369  # RAW_SENSOR_SECTION | Width: 1 |
    H5_RAW = 370  # RAW_SENSOR_SECTION | Width: 1 |
    H6_RAW = 371  # RAW_SENSOR_SECTION | Width: 1 |
    H7_RAW = 372  # RAW_SENSOR_SECTION | Width: 1 |
    C0_RAW = 373  # RAW_SENSOR_SECTION | Width: 1 |
    C1_RAW = 374  # RAW_SENSOR_SECTION | Width: 1 |
    C2_RAW = 375  # RAW_SENSOR_SECTION | Width: 1 |
    C3_RAW = 376  # RAW_SENSOR_SECTION | Width: 1 |
    C4_RAW = 377  # RAW_SENSOR_SECTION | Width: 1 |
    C5_RAW = 378  # RAW_SENSOR_SECTION | Width: 1 |
    C6_RAW = 379  # RAW_SENSOR_SECTION | Width: 1 |
    C7_RAW = 380  # RAW_SENSOR_SECTION | Width: 1 |
    VDD_RAW = 381  # RAW_SENSOR_SECTION | Width: 1 |
    T0_RAW = 382  # RAW_SENSOR_SECTION | Width: 1 |
    T1_RAW = 383  # RAW_SENSOR_SECTION | Width: 1 |
    T2_RAW = 384  # RAW_SENSOR_SECTION | Width: 1 |
    T3_RAW = 385  # RAW_SENSOR_SECTION | Width: 1 |

    # Non-contiguous addresses. 14 free registers. 386 - 399

    PARAM_VERSION = 400  # PARAM_SECTION | Width: 1 | Parameter calibration version.
    MAX_TEMP = 401  # PARAM_SECTION | Width: 1 | Absolute maximum motor temperature before over temperature error.
    MIN_VOLTAGE = 402  # PARAM_SECTION | Width: 1 | Minimum motor voltage in volts before invalid voltage error.
    MAX_VOLTAGE = 403  # PARAM_SECTION | Width: 1 | Maximum motor voltage in volts before invalid voltage error.
    MAX_CURRENT = (
        404  # PARAM_SECTION | Width: 1 | Maximum motor current output in milliamps.
    )
    MAX_POWER = 405  # PARAM_SECTION | Width: 1 | Maximum motor power burn in watts.
    SERIAL_NUMBER_LOW = (
        406  # PARAM_SECTION | Width: 1 | Actuator serial number. Lower 2 bytes.
    )
    SERIAL_NUMBER_HIGH = (
        407  # PARAM_SECTION | Width: 1 | Actuator serial number. Upper 2 bytes.
    )
    MAJOR_VERSION = 408  # PARAM_SECTION | Width: 1 | Firmware major version.
    RELEASE_STATE = 409  # PARAM_SECTION | Width: 1 | Firmware minor version.
    REVISION_NUMBER = 410  # PARAM_SECTION | Width: 1 | Firmware revision number.
    COMMIT_ID_LO = 411  # PARAM_SECTION | Width: 1 | Firmware commit ID lower 2 bytes.
    COMMIT_ID_HI = 412  # PARAM_SECTION | Width: 1 | Firmware commit ID upper 2 bytes.
    CC_MIN_CURRENT = 413  # PARAM_SECTION | Width: 1 | Current controller minimum current output in milliamps.
    HW_VERSION = (
        414  # PARAM_SECTION | Width: 1 | Target hardware version for this firmware.
    )
    PWM_FREQ = 415  # PARAM_SECTION | Width: 1 | Frequency of the PWM signals in hertz.
    ADC_FREQ = 416  # PARAM_SECTION | Width: 1 | Frequency of the sensor data acquisition loop in hertz.
    COMMS_TIMEOUT = 417  # PARAM_SECTION | Width: 1 | Time between successful force or position commands before a communications error occurs. In milliseconds.
    STATOR_CONFIG = (
        418  # PARAM_SECTION | Width: 1 | Physical stator configuration type.
    )

    # Non-contiguous addresses. 13 free registers. 419 - 431

    ERROR_0 = 432  # ERROR_SECTION | Width: 1 | Currently active error flags. Only reflects error conditions that have not been cleared.
    ERROR_1 = 433  # ERROR_SECTION | Width: 1 | Latched error flags. Reflects all errors that have occurred since reset.
    RX_TDRE_ERROR = 434  # ERROR_SECTION | Width: 1 |
    RX_TC_ERROR = 435  # ERROR_SECTION | Width: 1 |
    TX_RDRF_ERROR = 436  # ERROR_SECTION | Width: 1 |
    ADC_DATA_COLLISION = 437  # ERROR_SECTION | Width: 1 |

    # Non-contiguous addresses. 26 free registers. 438 - 463

    MB_CNT0 = 464  # MODBUS_SECTION | Width: 1 | Return bus message count. Refer to Modbus specification.
    MB_CNT1 = 465  # MODBUS_SECTION | Width: 1 | Return bus communication error. Refer to Modbus specification.
    MB_CNT2 = 466  # MODBUS_SECTION | Width: 1 | Return server exception error count. Refer to Modbus specification.
    MB_CNT3 = 467  # MODBUS_SECTION | Width: 1 | Return server message count. Refer to Modbus specification.
    MB_CNT4 = 468  # MODBUS_SECTION | Width: 1 | Return server no response count. Refer to Modbus specification.
    MB_CNT5 = 469  # MODBUS_SECTION | Width: 1 | Return server NAK count. Refer to Modbus specification.
    MB_CNT6 = 470  # MODBUS_SECTION | Width: 1 | Return server busy count. Refer to Modbus specification.
    MB_CNT7 = 471  # MODBUS_SECTION | Width: 1 | Return bus character overrun count. Refer to Modbus specification.
    MB_CNT8 = 472  # MODBUS_SECTION | Width: 1 | Rx line error.
    MB_CNT9 = 473  # MODBUS_SECTION | Width: 1 | Ignoring state error.
    MB_CNT10 = 474  # MODBUS_SECTION | Width: 1 | Unexpected interchar.
    MB_CNT11 = 475  # MODBUS_SECTION | Width: 1 | Unexpected interframe.
    MB_CNT12 = 476  # MODBUS_SECTION | Width: 1 | Timeout sequence error.
    MB_CNT13 = 477  # MODBUS_SECTION | Width: 1 | Unexpected emission.
    MB_CNT14 = 478  # MODBUS_SECTION | Width: 1 | Unexpected reception.
    MB_CNT15 = 479  # MODBUS_SECTION | Width: 1 | -
    MB_CNT16 = 480  # MODBUS_SECTION | Width: 1 | -
    MB_CNT17 = 481  # MODBUS_SECTION | Width: 1 | -
    MB_BAUD = 482  # MODBUS_SECTION | Width: 1 | Modbus serial baudrate. Lower 2 bytes.
    MB_BAUD_H = (
        483  # MODBUS_SECTION | Width: 1 | Modbus serial baudrate. Upper 2 bytes.
    )
    MB_IF_DELAY = (
        484  # MODBUS_SECTION | Width: 1 | Modbus interframe delay in microseconds.
    )
    MB_ADDRESS = 485  # MODBUS_SECTION | Width: 1 | Modbus server address.

    # Non-contiguous addresses. 10 free registers. 486 - 495

    MESSAGE_0_SIZE = 496  # MODBUS_SECTION | Width: 1 | Size of last received Modbus message in bytes.
    MESSAGE_0 = 497  # MODBUS_SECTION | Width: 128  | -
    HAPTIC_VERSION = 640  # HAPTIC_SECTION | Width: 1 | Haptic configuration version.

    # Non-contiguous addresses. 15 free registers. 641 - 640

    HAPTIC_STATUS = 641  # HAPTIC_SECTION | Width: 1 | Enabled state of effects
    CONSTANT_FORCE_MN = 642  # HAPTIC_SECTION | Width: 1 | Value of constant force effect in milliwnewtons, low 2 bytes
    CONSTANT_FORCE_MN_H = 643  # HAPTIC_SECTION | Width: 1 | Value of constant force effect in milliwnewtons, high 2 bytes
    S0_GAIN_N_MM = 644  # HAPTIC_SECTION | Width: 1 | Strength of spring force
    S0_CENTER_UM = (
        645  # HAPTIC_SECTION | Width: 1 | Location of spring center, low 2 bytes
    )
    S0_CENTER_UM_H = (
        646  # HAPTIC_SECTION | Width: 1 | Location of spring center, high 2 bytes
    )
    S0_COUPLING = 647  # HAPTIC_SECTION | Width: 1 | Coupling type, 0 (Both), 1 (Positive), 2 (Negative),
    S0_DEAD_ZONE_MM = 648  # HAPTIC_SECTION | Width: 1 | Zone from center where no spring effect exists
    S0_FORCE_SAT_N = (
        649  # HAPTIC_SECTION | Width: 1 | Maximum force that the spring can output
    )
    S1_GAIN_N_MM = 650  # HAPTIC_SECTION | Width: 1 | Strength of spring force
    S1_CENTER_UM = (
        651  # HAPTIC_SECTION | Width: 1 | Location of spring center, low 2 bytes
    )
    S1_CENTER_UM_H = (
        652  # HAPTIC_SECTION | Width: 1 | Location of spring center, high 2 bytes
    )
    S1_COUPLING = 653  # HAPTIC_SECTION | Width: 1 | Coupling type, 0 (Both), 1 (Positive), 2 (Negative),
    S1_DEAD_ZONE_MM = 654  # HAPTIC_SECTION | Width: 1 | Zone from center where no spring effect exists
    S1_FORCE_SAT_N = (
        655  # HAPTIC_SECTION | Width: 1 | Maximum force that the spring can output
    )
    S2_GAIN_N_MM = 656  # HAPTIC_SECTION | Width: 1 | Strength of spring force
    S2_CENTER_UM = (
        657  # HAPTIC_SECTION | Width: 1 | Location of spring center, low 2 bytes
    )
    S2_CENTER_UM_H = (
        658  # HAPTIC_SECTION | Width: 1 | Location of spring center, high 2 bytes
    )
    S2_COUPLING = 659  # HAPTIC_SECTION | Width: 1 | Coupling type, 0 (Both), 1 (Positive), 2 (Negative),
    S2_DEAD_ZONE_MM = 660  # HAPTIC_SECTION | Width: 1 | Zone from center where no spring effect exists
    S2_FORCE_SAT_N = (
        661  # HAPTIC_SECTION | Width: 1 | Maximum force that the spring can output
    )
    D0_GAIN_NS_MM = 662  # HAPTIC_SECTION | Width: 1 | Strength of damping force
    I0_GAIN_NS2_MM = 663  # HAPTIC_SECTION | Width: 1 | Strength of inertia force
    O0_GAIN_N = 664  # HAPTIC_SECTION | Width: 1 | Amplitude of periodic effect
    O0_TYPE = 665  # HAPTIC_SECTION | Width: 1 | Type of periodic effect 0 (square), 1 (sine), 2 (triangle), 3 (sawtooth)
    O0_FREQ_DHZ = 666  # HAPTIC_SECTION | Width: 1 | Period of oscillation
    O0_DUTY = 667  # HAPTIC_SECTION | Width: 1 | Pulse width modulation of signal as a % of duty cycle max value
    O1_GAIN_N = 668  # HAPTIC_SECTION | Width: 1 | Amplitude of periodic effect
    O1_TYPE = 669  # HAPTIC_SECTION | Width: 1 | Type of periodic effect 0 (square), 1 (sine), 2 (triangle), 3 (sawtooth)
    O1_FREQ_DHZ = 670  # HAPTIC_SECTION | Width: 1 | Frequency of periodic effect
    O1_DUTY = 671  # HAPTIC_SECTION | Width: 1 | Pulse width modulation of signal as a % of duty cycle max value
    CONST_FORCE_FILTER = (
        672  # HAPTIC_SECTION | Width: 1 | Amount of filtering on constant force inputs.
    )

    # Non-contiguous addresses. 82 free registers. 673 - 754

    ILOOP_MSG_FLAG = 755  # CURRENT_LOOP_SECTION | Width: 1 | Flag produced by receiving a Seagull modbus command and consumed by the current loop controller
    ILOOP_DIN = 756  # CURRENT_LOOP_SECTION | Width: 1 | Status of Ceagle digital inputs. Each input represented by a bit.
    ILOOP_OUT_CH1 = 757  # CURRENT_LOOP_SECTION | Width: 1 | 4-20 mA output channel 1.
    ILOOP_OUT_CH2 = 758  # CURRENT_LOOP_SECTION | Width: 1 | 4-20 mA output channel 2.
    ILOOP_IN = 759  # CURRENT_LOOP_SECTION | Width: 1 | 4-20 mA input.
    ILOOP_SECTION_VERSION = 760  # CURRENT_LOOP_SECTION | Width: 1 |
    ILOOP_CONFIG = (
        761  # CURRENT_LOOP_SECTION | Width: 1 | Configuration for 4-20mA control.
    )
    ILOOP_FORCE_MIN = 762  # CURRENT_LOOP_SECTION | Width: 1 | Force that maps to 4 mA. Low 2 bytes. In millinewtons.
    ILOOP_FORCE_MIN_HI = 763  # CURRENT_LOOP_SECTION | Width: 1 | Force that maps to 4 mA. High 2 bytes. In millinewtons.
    ILOOP_FORCE_MAX = 764  # CURRENT_LOOP_SECTION | Width: 1 | Force that maps to 20 mA. Low 2 bytes. In millinewtons.
    ILOOP_FORCE_MAX_HI = 765  # CURRENT_LOOP_SECTION | Width: 1 | Force that maps to 20 mA. High 2 bytes. In millinewtons.
    ILOOP_POS_MIN = 766  # CURRENT_LOOP_SECTION | Width: 1 | Position that maps to 4 mA. Low 2 bytes. In micrometers.
    ILOOP_POS_MIN_HI = 767  # CURRENT_LOOP_SECTION | Width: 1 | Position that maps to 4 mA. High 2 bytes. In micrometers.
    ILOOP_POS_MAX = 768  # CURRENT_LOOP_SECTION | Width: 1 | Position that maps to 20 mA. Low 2 bytes. In micrometers.
    ILOOP_POS_MAX_HI = 769  # CURRENT_LOOP_SECTION | Width: 1 | Position that maps to 20 mA. High 2 bytes. In micrometers.
    ILOOP_KIN_TYPE = 770  # CURRENT_LOOP_SECTION | Width: 1 | Type of trigger behaviour
    ILOOP_D0_HIGH = 771  # CURRENT_LOOP_SECTION | Width: 1 | Motion id value for rising edge digital 0
    ILOOP_D0_LOW = 772  # CURRENT_LOOP_SECTION | Width: 1 | Motion id value for falling edge digital 0
    ILOOP_D2_HIGH = 773  # CURRENT_LOOP_SECTION | Width: 1 | Motion id value for rising edge digital 2
    ILOOP_D2_LOW = 774  # CURRENT_LOOP_SECTION | Width: 1 | Motion id value for falling edge digital 2

    # Non-contiguous addresses. 3 free registers. 775 - 777

    KINEMATIC_SECTION_VERSION = 778  # KINEMATIC_SECTION | Width: 1 |
    KIN_CONFIG = (
        779  # KINEMATIC_SECTION | Width: 1 | Kinematic controller configuration.
    )
    KIN_MOTION_0 = 780  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_1 = 786  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_2 = 792  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_3 = 798  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_4 = 804  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_5 = 810  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_6 = 816  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_7 = 822  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_8 = 828  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_9 = 834  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_10 = 840  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_11 = 846  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_12 = 852  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_13 = 858  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_14 = 864  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_15 = 870  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_16 = 876  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_17 = 882  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_18 = 888  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_19 = 894  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_20 = 900  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_21 = 906  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_22 = 912  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_23 = 918  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_24 = 924  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_25 = 930  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_26 = 936  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_27 = 942  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_28 = 948  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_29 = 954  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_30 = 960  # KINEMATIC_SECTION | Width: 6 |
    KIN_MOTION_31 = 966  # KINEMATIC_SECTION | Width: 6 |
    KIN_HOME_ID = 972  # KINEMATIC_SECTION | Width: 1 | ID of kinematic motion triggered when Kinematic mode enabled or when Home signal asserved from Analog interface
