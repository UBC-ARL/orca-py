import asyncio

import numpy as np

from orca_py.actuator import Actuator
from orca_py.orca_constant import ORCA_MODE

A1_SERIAL_ADDRESS = "/dev/tty.usbserial-FT878BFG"
A2_SERIAL_ADDRESS = "/dev/tty.usbserial-FT8ESWCO"
A3_SERIAL_ADDRESS = "/dev/tty.usbserial-FT8F0YKB"
A4_SERIAL_ADDRESS = "/dev/tty.usbserial-FTU7JPNF"
A5_SERIAL_ADDRESS = "/dev/tty.usbserial-FT8F11PO"
A6_SERIAL_ADDRESS = "/dev/tty.usbserial-FTU7JOOC"
A7_SERIAL_ADDRESS = "/dev/tty.usbserial-FT8F0SER"
A8_SERIAL_ADDRESS = "/dev/tty.usbserial-FT8EQ4MF"
A9_SERIAL_ADDRESS = "/dev/tty.usbserial-FT878A04"


async def async_main():
    foo = [int(x) for x in 25 * 1000 * (1 - np.cos(np.linspace(0, 2 * np.pi, 512)))]
    trajectories = np.array([foo for _ in range(9)]).T

    actuators = await asyncio.gather(
        Actuator.create(A1_SERIAL_ADDRESS),
        Actuator.create(A2_SERIAL_ADDRESS),
        Actuator.create(A3_SERIAL_ADDRESS),
        Actuator.create(A4_SERIAL_ADDRESS),
        Actuator.create(A5_SERIAL_ADDRESS),
        Actuator.create(A6_SERIAL_ADDRESS),
        Actuator.create(A7_SERIAL_ADDRESS),
        Actuator.create(A8_SERIAL_ADDRESS),
        Actuator.create(A9_SERIAL_ADDRESS),
    )

    # set all actuators to sleep mode
    for a in actuators:
        while await a.get_mode() != ORCA_MODE.SleepMode:
            await a.set_mode(ORCA_MODE.SleepMode)

    kp = 3000
    ki = 300
    kdv = 000
    kde = 500
    time_step = 300
    delay = 0

    # TUNE PID
    for a in actuators:
        await a.tune_pid_controller(300000, kp, ki, kdv, kde)

    # ASSIGN A HOME POSITION (SLOT 0)
    for index, a in enumerate(actuators):
        await a.configure_motion(0, int(trajectories[index][0]), 5000, delay, 1, 0, 0)

    print("Set Kinematic Mode")

    # TRIGGER KINEMATIC MODE. MOTORS WILL GO TO HOME POSITION. MAKE SURE HOME POSITION IS SET PROPERLY!!
    for a in actuators:
        while await a.get_mode() != ORCA_MODE.KinematicMode:
            await a.set_mode(ORCA_MODE.KinematicMode)

    print("Trigger start location")

    # CONFIGURE & TRIGGER THE STARTING LOCATION SLOWLY
    for index, a in enumerate(actuators):
        await a.configure_motion(1, int(trajectories[index][0]), 5000, delay, 2, 0, 0)
    for a in actuators:
        await a.kinematic_trigger(1)

    # START WITH MOTION 1
    current_motion_id = 1
    current_step = 0

    while current_step < trajectories.shape[1] - 1:
        current_step += 1
        next_motion_id = current_motion_id % 2 + 1
        for index, a in enumerate(actuators):
            await a.configure_motion(
                next_motion_id,
                int(trajectories[index][current_step]),
                time_step,
                delay,
                current_motion_id,
                0,
                0,
            )
        for a in actuators:
            await a.kinematic_trigger(next_motion_id)
        current_motion_id = next_motion_id
    print("Done!")


if __name__ == "__main__":
    asyncio.run(async_main())
