from typing import List
from unittype import UnitType
from units import *

class UnitConverter:
    """Perform the convertion a quantity of one unit to another unit,
    and provide the collection of available units of different types,
    such as Length, Area.

    See: unittype.UnitType for known unit types,
         units module for actual units.
    """

    def __init__(self):
        # create a map of unit_name -> Unit for use in convert method
        # so the UI can invoke convert using string names of units
        self.units = {u.name: u for u in units}

    def get_units(self, unittype: UnitType) -> List[Unit]:
        """Return all the units of the requested unittype.
        
        :param unittype: the UnitType of the units to return.
        :returns: a list of Unit objects of requested UnitType.
        """
        filter_by_type = lambda unit: unit.unittype==unittype
        return list(filter(filter_by_type, units))

    def unit_by_name(self, name: str):
        """Get a Unit object with the given name.

        :param name: is the name of the Unit
        :returns: a Unit with that name, or None if no match
        """
        # if parameter is already a Unit then just use it
        if isinstance(name, Unit): return name
        try:
            return self.units[name]
        except KeyError:
            return None


    def convert(self, amount: float, from_unit_name: str, to_unit_name: str):
        """Convert a quantity (amount) of fromunit to equivalent in tounit.

        :param amount: the quantity to convert
        :param from_unit_name: the string name of the unit to convert from
        :param to_unit_name: the string name of the unit to convert to

        3 kilometers should equal 1,500 wa
        >>> convert(3, "Kilometer", "Wa")
        1500.0
        >>> convert(5, "Meter", "Centimeter")
        500.0
        """
        fromunit = self.units[from_unit_name]
        tounit = self.units[to_unit_name]

        #TODO convert an amount of fromunit to equivalent value of tounit
        #     See the doctest comment for example.
        return 0
