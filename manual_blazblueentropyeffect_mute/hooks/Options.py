# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions, OptionSet
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any
from ..Items import item_name_groups

####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################

class IncludeDLCPrototypes(Toggle):
    """Whether DLC Prototypes should be included in generation. If you don't want all of them, you can exclude them in excluded_prototypes"""
    display_name = "Include DLC Prototypes"

class ExcludedPrototypes(OptionSet):
    """Protoypes in this list will be excluded from generation completely. There must be at least 6 unique Protoypes in the pool. 
    Valid list of Prototypes:
    'Hibiki', 'Ragna', 'Noel', 'Λ -No.11-', 'Es', 'Rachel', 'Taokaka', 'Jin', 'Kokonoe', 'Hakumen', 'Mai', 'Hazama', 'ICEY', 'Bullet', 'The Prisoner', 'Naoto'"""
    display_name = "Excluded Prototypes"
    valid_keys = item_name_groups["Prototypes"]
    default = []

class DuplicatePrototypes(OptionSet):
    """Prototypes in this list will be duplicated in generation, increasing the chances of getting them.
    Getting a Prototype twice does nothing. Excluded Protoypes are ignored. 
    Valid list of Prototypes: 
    'Hibiki', 'Ragna', 'Noel', 'Λ -No.11-', 'Es', 'Rachel', 'Taokaka', 'Jin', 'Kokonoe', 'Hakumen', 'Mai', 'Hazama', 'ICEY', 'Bullet', 'The Prisoner', 'Naoto'"""
    display_name = "Duplicate Prototypes"
    valid_keys = item_name_groups["Prototypes"]
    default = []

class PrototypeWinCount(Range):
    """The number of Prototypes that need to complete Extreme 80 Entropy to complete the goal.
    Will automatically be lowered to the number of unique Prototypes in the pool if higher."""
    display_name = "Prototype Win Count"
    range_start = 3
    range_end = 16
    default = 5

class ReducedStageUnlocks(Toggle):
    """If enabled, the number of progressive stage unlock items for each Prototype will be reduced from 4 to 2.
    By default with this option off, each Prototype has 4 stage unlock items for stages 2-5.
    If on, instead stages 2 & 3 are unlocked from the 1st unlock item and stages 4 & 5 unlocked from the 2nd.
    Only recommended if the default playthrough feels too long."""
    display_name = "Reduced Stage Unlocks"

class ExtraEvotypeSlots(Range):
    """Adds extra Evotype slots to the item pool to increase the chances of getting them.
    Having more than the default 2 does nothing."""
    display_name = "Extra Evotype Slots"
    range_start = 0
    range_end = 2
    default = 0

class ExtraMindCrystalSlots(Range):
    """Adds extra Mind Crystal slots to the item pool to increase the chances of getting them.
    Having more than the default 6 does nothing."""
    display_name = "Extra Mind Crystal Slots"
    range_start = 0
    range_end = 6
    default = 0

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["include_dlc_prototypes"] = IncludeDLCPrototypes
    options["excluded_prototypes"] = ExcludedPrototypes
    options["duplicate_prototypes"] = DuplicatePrototypes
    options["prototype_win_count"] = PrototypeWinCount
    options["reduced_stage_unlocks"] = ReducedStageUnlocks
    options["extra_evotype_slots"] = ExtraEvotypeSlots
    options["extra_mind_crystal_slots"] = ExtraMindCrystalSlots
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
