"""A Unit contains info about a single unit."""
from dataclasses import dataclass
from unittype import UnitType

@dataclass(frozen=True)
class Unit:
    """The attributes of a Unit object."""
    name: str
    value: float
    unittype: UnitType

    """dataclass provides constructor, getter properties,
      __eq__ method, and others."""

    def __str__(self):
        return self.name

    def __lt__(self, other):
        """Less than comparison, used for sorting units."""
        return self.name < other.name
    
    def __repr__(self):
        classname = type(self).__name__
        return f"{classname}('{self.name}', {self.value}, UnitType.{self.unittype.name})"


# For lack of a better place, define a units dictionary.
# Keys: the unittype as a UnitType (enum) member
# Values: an array of Unit objects for the given UnitType

units = {
    # Length units
    Unit("Meter", 1.0, UnitType.LENGTH),
    Unit("Kilometer",  1000.0, UnitType.LENGTH),
    Unit("Centimeter",  1.0E-2, UnitType.LENGTH),
    Unit("Nanometer", 1.0E-9, UnitType.LENGTH),
    Unit("Mile",  1609.344, UnitType.LENGTH ),
    Unit("Foot", 0.3048, UnitType.LENGTH),
    Unit("Inch", 0.0254, UnitType.LENGTH),
    Unit("Yard",  0.9144, UnitType.LENGTH),
    Unit("Wa", 2.0, UnitType.LENGTH),
    Unit("Light-year", 9460730472580800.0, UnitType.LENGTH),
    # Area Units
    Unit("Sq.m.", 1.0, UnitType.AREA),
    Unit("Sq.wa", 4.0, UnitType.AREA),
    Unit("Rai", 400.0, UnitType.AREA)
    # TODO need more Area units

}

if __name__ == '__main__':
    print("Length units")
   
    for unit in units:
        if unit.unittype == UnitType.LENGTH:
            print(f"'{unit.name}' is ", repr(unit))
