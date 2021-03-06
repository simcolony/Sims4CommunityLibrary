"""
The Sims 4 Community Library is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode

Copyright (c) COLONOLNUTTY
"""
from typing import Any
from sims4.resources import Types
from sims4communitylib.enums.icons_enum import CommonIconId
from sims4communitylib.utils.common_resource_utils import CommonResourceUtils


class CommonIconUtils:
    """Utilities for handling icons.

    """
    @staticmethod
    def load_arrow_right_icon() -> Any:
        """load_arrow_right_icon()

        Get the Resource Key for the ARROW_RIGHT_ICON.

        :return: An identifier for the icon.
        :rtype: Any
        """
        return CommonResourceUtils.get_resource_key(Types.PNG, CommonIconId.S4CLIB_ARROW_RIGHT_ICON)

    @staticmethod
    def load_arrow_navigate_into_icon() -> Any:
        """load_arrow_navigate_into_icon()

        Get the Resource Key for the ARROW_NAVIGATE_INTO_ICON.

        :return: An identifier for the icon.
        :rtype: Any
        """
        return CommonResourceUtils.get_resource_key(Types.PNG, CommonIconId.S4CLIB_ARROW_NAVIGATE_INTO_ICON)

    @staticmethod
    def load_question_mark_icon() -> Any:
        """load_question_mark_icon()

        Get the Resource Key for the QUESTION_MARK_ICON.

        :return: An identifier for the icon.
        :rtype: Any
        """
        return CommonResourceUtils.get_resource_key(Types.PNG, CommonIconId.S4CLIB_QUESTION_MARK_ICON)

    @staticmethod
    def load_checked_square_icon() -> Any:
        """load_checked_square_icon()

        Get the Resource Key for the CHECKED_SQUARE_ICON.

        :return: An identifier for the icon.
        :rtype: Any
        """
        return CommonResourceUtils.get_resource_key(Types.PNG, CommonIconId.S4CLIB_CHECKED_SQUARE_ICON)

    @staticmethod
    def load_unchecked_square_icon() -> Any:
        """load_unchecked_square_icon()

        Get the Resource Key for the UNCHECKED_SQUARE_ICON.

        :return: An identifier for the icon.
        :rtype: Any
        """
        return CommonResourceUtils.get_resource_key(Types.PNG, CommonIconId.S4CLIB_UNCHECKED_SQUARE_ICON)

    @staticmethod
    def load_six_sided_dice_icon() -> Any:
        """load_six_sided_dice_icon()

        Get the Resource Key for the SIX_SIDED_DICE_ICON.

        :return: An identifier for the icon.
        :rtype: Any
        """
        return CommonResourceUtils.get_resource_key(Types.PNG, CommonIconId.S4CLIB_SIX_SIDED_DICE_ICON)
    
    @staticmethod
    def _load_icon(icon_id: int) -> Any:
        return CommonResourceUtils.get_resource_key(Types.PNG, icon_id)
