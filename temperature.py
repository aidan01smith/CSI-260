"""Classes for working with Temperatures."""


class TemperatureError(Exception):
    """Error raised for invalid temperatures."""
    pass


class Temperature:
    """Represents a temperature.

    Temperatures are expressable in degrees Fahrenheit, degrees celsius,
    or Kelvins.
    """

    def __init__(self, degrees=0):
        """Initialize temperature with specified degrees.

        Args:
            degrees, which can be one of the following:
                (1) a number, or a string containing a number
                    in which case it is interpreted as degrees celsius
                (2) a string containing a number followed by one of the
                    following symbols:
                       C, in which case it is interpreted as degrees celsius
                       F, in which case it is interpreted as degrees Fahrenheit
                       K, in which case it is interpreted as Kelvins

        Raises:
            TemperatureError: if degrees is not one of the specified
                                     forms

        """
        if isinstance(degrees, str):
            degrees = degrees.strip()
            if degrees[-1].upper() == 'C':
                self._degrees = float(degrees[:-1])
            elif degrees[-1].upper() == 'F':
                self._degrees = (float(degrees[:-1]) - 32) * 5 / 9
            elif degrees[-1].upper() == 'K':
                self._degrees = float(degrees[:-1]) - 273.15
            else:
                raise TemperatureError("invalid temperature")
        else:
            self._degrees = float(degrees)
        if self._degrees < -273.15:
            raise TemperatureError("invalid temperature")


    @classmethod
    def average(cls, temperatures):
        """Compute the average of a list of temperatures.

        Args:
            temperatures: a list of Temperature objects
        Returns:
            a Temperature object with average (mean) of the given temperatures

        """
        if not temperatures:
            raise TemperatureError("invalid temperature")
        total = sum(temp._degrees for temp in temperatures)
        return cls(total / len(temperatures))
