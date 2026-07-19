from typing import Optional, Any
from BaseClasses import MultiWorld
from .. import Helpers

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    if category_name == "DLC" and not Helpers.is_option_enabled(multiworld, player, "include_dlc_prototypes"):
        return False
    from ..Items import item_name_groups
    if category_name in item_name_groups["Prototypes"]:
        return category_name not in Helpers.get_option_value(multiworld, player, "excluded_prototypes")
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    from ..Helpers import get_option_value
    if "Prototypes" in item["category"]:
        if "DLC" in item["category"] and not Helpers.is_option_enabled(multiworld, player, "include_dlc_prototypes"):
            return False
        return item["name"] not in get_option_value(multiworld, player, "excluded_prototypes")
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
