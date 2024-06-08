import logging
from newport_esa.esa import NewportESA, ControlMode, Axis


if __name__ == "__main__":
    # start logging
    logging.basicConfig(
        # level=logging.DEBUG,
        level=logging.INFO,
        format="%(asctime)s:%(module)s:%(levelname)s:%(message)s"
    )

    esa_address: str = "GPIB0::6::INSTR"
    esa = NewportESA()
    esa.connect(gpib_address=esa_address)
    print(esa.identify())
    print("\n", end="")

    logging.info(f"{esa.get_control_mode()}\n")

    print(esa.dev.query("R1?"))
    esa.move_relative(axis=Axis.X, voltage=-10.1)  # relative move
    # esa.move_absolute(axis=Axis.X, voltage=80.1)  # relative move
    print(esa.get_axis_voltage(Axis.X))
    print(esa.get_axis_voltage(Axis.X).encode())
    print("\n", end="")

    print(esa.get_velocity(axis=Axis.X))
    print("\n", end="")

    esa.tear()
