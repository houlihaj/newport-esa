from newport_esa.esa import NewportESA, ControlMode, Axis


if __name__ == "__main__":
    esa_address: str = "GPIB0::6::INSTR"
    esa = NewportESA()
    esa.connect(gpib_address=esa_address)
    print(esa.identify())
    print("\n", end="")

    # esa.dev.write("REMOTE")
    esa.set_control_mode(mode=ControlMode.REMOTE)
    print(esa.get_control_mode())
    print("\n", end="")

    print(esa.dev.query("R1?"))
    esa.move_relative(axis=Axis.X, voltage=10.1)  # relative move
    # print(esa.dev.query("R1?"))
    print(esa.get_axis_voltage(Axis.X))
    print(esa.get_axis_voltage(Axis.X).encode())
    # print(float(esa.get_axis_voltage(Axis.X)))
    print("\n", end="")

    # esa.dev.write("LOCAL")
    esa.set_control_mode(mode=ControlMode.LOCAL)
    print(esa.get_control_mode())
    esa.tear()
