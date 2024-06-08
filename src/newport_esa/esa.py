from enum import Enum

import pyvisa


class ControlMode(Enum):
    LOCAL = "LOCAL"
    REMOTE = "REMOTE"


class Axis(Enum):
    X = "1"
    Y = "2"
    Z = "3"


class NewportESA:
    """

    """
    def __init__(self) -> None:
        """

        """
        self.dev = None

    def connect(self, gpib_address: str, timeout: int = 3000) -> None:
        """

        :param gpib_address:
        :type gpib_address: str
        :param timeout: timeout period in units of milliseconds (ms)
        :type timeout: int
        """
        rm = pyvisa.ResourceManager()
        self.dev = rm.open_resource(resource_name=gpib_address)
        self.dev.read_termination = "\n"
        self.dev.write_termination = "\r\n"
        self.dev.timeout = timeout

    def tear(self) -> None:
        """

        """
        self.dev.close()

    def identify(self) -> str:
        """

        :return:
        :rtype: str
        """
        esa_id: str = self.dev.query("*IDN?")
        return esa_id

    def set_control_mode(self, mode: ControlMode):
        """

        :param mode:
        :type mode: ControlMode
        """
        self.dev.write(f"{mode.value}")

    def get_control_mode(self):
        """

        :return:
        :rtype: ControlMode
        """
        return ControlMode(self.dev.query("MODE?"))

    def move_relative(self, axis: Axis, voltage: float):
        """

        :param axis:
        :type axis: Axis
        :param voltage: signed voltage relative move value
        :type voltage: float
        """
        self.dev.write(f"DV{axis.value} {voltage}")  # relative move

    def move_absolute(self, axis: Axis):
        """

        """
        raise NotImplementedError

    def get_axis_voltage(self, axis: Axis):
        """

        :return:
        :rtype: str
        """
        return self.dev.query(f"R{axis.value}?")  # leading space character in ESA-C response for unknown reason
