import traceback
from src.controller.menus.base_menu import Menu


class LowerLevelMenu(Menu):

    def bundle_chosen(self, ussd_text_dict, position, offset):
        pass

    def buy_bundles(self, offset, position):
        pass

    def execute(self):

        user_string = ["*502*114*141#", "*114*141#", "*141#"]

        if self.level[:9] == "PCB_MENU_":
            pass

        # PCB_YOU_HAVE_SELECTED_OFFSET_POSITION_USER-CHOICE
        elif self.level[:22] == "PCB_YOU_HAVE_SELECTED_":
            pass
