from tkinter import *
from tkinter import messagebox
import math
import random
import os


class As_Purchaser:
    def __init__(self, root):
        self.root = root
        self.root.title("As Purchaser Window")
        self.root.geometry("1550x850")
        self.root.resizable(True, True)
        self.bgcolor = "#074463"
        self.bgcolor1 = "grey"
        self.bgcolor2 = "#ECF0F1"
        self.bgcolor3 = "#A1F9F8"
        self.bgcolor4 = "white"
        self.bgcolor5 = "#A4F5F4"
        self.total_bb = IntVar()
        self.total_bb.set(0)
        self.total_mw = IntVar()
        self.total_mw.set(0)
        self.total_ww = IntVar()
        self.total_ww.set(0)
        self.total_ku = IntVar()
        self.total_ku.set(0)
        self.total_ele = IntVar()
        self.total_ele.set(0)
        self.total_stnry = IntVar()
        self.total_stnry.set(0)
        self.total_final_sum = 0
        self.partial_bb = 0
        self.partial_mw = 0
        self.partial_ww = 0
        self.partial_ku = 0
        self.partial_ele = 0
        self.partial_stnry = 0
        self.bb_1_confirm_bool = False
        self.bb_2_confirm_bool = False
        self.bb_3_confirm_bool = False
        self.bb_4_confirm_bool = False
        self.bb_5_confirm_bool = False
        self.bb_6_confirm_bool = False
        self.bb_7_confirm_bool = False
        self.bb_8_confirm_bool = False
        self.bb_9_confirm_bool = False
        self.bb_10_confirm_bool = False
        self.mw_1_confirm_bool = False
        self.mw_2_confirm_bool = False
        self.mw_3_confirm_bool = False
        self.mw_4_confirm_bool = False
        self.mw_5_confirm_bool = False
        self.mw_6_confirm_bool = False
        self.mw_7_confirm_bool = False
        self.mw_8_confirm_bool = False
        self.mw_9_confirm_bool = False
        self.mw_10_confirm_bool = False
        self.ww_1_confirm_bool = False
        self.ww_2_confirm_bool = False
        self.ww_3_confirm_bool = False
        self.ww_4_confirm_bool = False
        self.ww_5_confirm_bool = False
        self.ww_6_confirm_bool = False
        self.ww_7_confirm_bool = False
        self.ww_8_confirm_bool = False
        self.ww_9_confirm_bool = False
        self.ww_10_confirm_bool = False
        self.ku_1_confirm_bool = False
        self.ku_2_confirm_bool = False
        self.ku_3_confirm_bool = False
        self.ku_4_confirm_bool = False
        self.ku_5_confirm_bool = False
        self.ku_6_confirm_bool = False
        self.ku_7_confirm_bool = False
        self.ku_8_confirm_bool = False
        self.ku_9_confirm_bool = False
        self.ku_10_confirm_bool = False
        self.ele_1_confirm_bool = False
        self.ele_2_confirm_bool = False
        self.ele_3_confirm_bool = False
        self.ele_4_confirm_bool = False
        self.ele_5_confirm_bool = False
        self.ele_6_confirm_bool = False
        self.ele_7_confirm_bool = False
        self.ele_8_confirm_bool = False
        self.ele_9_confirm_bool = False
        self.ele_10_confirm_bool = False
        self.stnry_1_confirm_bool = False
        self.stnry_2_confirm_bool = False
        self.stnry_3_confirm_bool = False
        self.stnry_4_confirm_bool = False
        self.stnry_5_confirm_bool = False
        self.stnry_6_confirm_bool = False
        self.stnry_7_confirm_bool = False
        self.stnry_8_confirm_bool = False
        self.stnry_9_confirm_bool = False
        self.stnry_10_confirm_bool = False
        self.bill_bb_confirm_bool = False
        self.bill_mw_confirm_bool = False
        self.bill_ww_confirm_bool = False
        self.bill_ele_confirm_bool = False
        self.bill_ku_confirm_bool = False
        self.bill_stnry_confirm_bool = False
        # ======================wholeseller_name_variable============================================================================
        self.wsname = StringVar()
        self.clicked_wholeseller_name = StringVar()
        self.ws_contact = StringVar()
        self.clicked_wholeseller_contact = StringVar()
        self.random_bill = 0
        self.bill_no = StringVar()

        # ===========Whole seller details================================================================================================

        self.wholeseller_detail_frame = LabelFrame(self.root, text="WholeSeller Details", font=(
            "Aparajita", 15, "bold"), fg="yellow", bd=8, bg=self.bgcolor, relief=GROOVE)
        self.wholeseller_detail_frame.place(x=0, y=0, relwidth=1)
        self.wholeseller_name = Label(self.wholeseller_detail_frame, text="WholeSeller Name", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white").grid(row=0, column=0, padx=5, pady=4)
        self.wholeseller_name_entry = Entry(self.wholeseller_detail_frame, textvariable=self.wsname, width=18,
                                            font=(
                                                "Aparajita", 15, "bold"), bd=7, relief=GROOVE).grid(row=0, column=1, padx=5, pady=4)

        self.clicked_wholeseller_name.set("Select Wholeseller")
        self.whole_seller_option_list = ["Born Baby Items", "Men's Wear",
                                         "Women's wear ", "Kitchen Utensis ", "Electronics Item ", "Stationary Items"]

        # self.clicked_wholeseller_name is the variable used in the OptionMenu() functions
        self.wholeseller_name_option = OptionMenu(
            self.wholeseller_detail_frame, self.clicked_wholeseller_name, *self.whole_seller_option_list, command=self.WholeSellerName)
        self.wholeseller_name_option.grid(row=0, column=2, padx=5, pady=4)

        # fixing drop down menu width ...............( important )>>>>>>>>>>>>>>>>>>>>!!
        self.wholeseller_name_option.config(width=20)

        self.whole_seller_contact_list = ["Born Baby Items: 7854123458", "Men's Wear: 5478954364", "Women's Wear: 4521357894",
                                          "Kitchen Utensils: 8456214789", "Electronics Items: 9875612548", "Stationary Items : 3451278956"]
        self.wholeseller_contact = Label(self.wholeseller_detail_frame, text="WholeSeller Contact Number", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white").grid(row=0, column=3, padx=5, pady=4)
        self.wholeseller_contact_entry = Entry(
            self.wholeseller_detail_frame, textvariable=self.ws_contact, width=18, font=(
                "Aparajita", 15, "bold"), bd=7, relief=GROOVE).grid(row=0, column=4, padx=5, pady=4)

        self.clicked_wholeseller_contact.set("Select Wholeseller Contact")

        # self.clicked_wholeseller_contact is the variable used in the OptionMenu() functions
        self.wholeseller_contact_option = OptionMenu(
            self.wholeseller_detail_frame, self.clicked_wholeseller_contact, *self.whole_seller_contact_list, command=self.WholeSellerContact)
        self.wholeseller_contact_option.grid(row=0, column=5, padx=5, pady=4)

        # fixing drop down menu width ...............( important )>>>>>>>>>>>>>>>>>>>>!!
        self.wholeseller_contact_option.config(width=24)

# ==========================<<<<<<<<<<<<<<<<<<<bill button>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>=============================

        self.billno = Label(self.wholeseller_detail_frame, text="Bill Number", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white").grid(row=0, column=6, padx=5, pady=4)
        self.billno_entry = Entry(self.wholeseller_detail_frame, width=15, font=("Aparajita", 15, "bold"), textvariable=self.bill_no,
                                  bd=7, relief=GROOVE).grid(row=0, column=7, padx=5, pady=4)

        self.bill_btn = Button(self.wholeseller_detail_frame, text="Search", width=10, bd=7, font=(
            "Arial", 10, "bold"), command=self.search_bill).grid(row=0, column=8, padx=5, pady=10)

       # ==========================<<<<<<<<<<<<<<<<<<<billing area>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>=============================

        self.bill_frame = Frame(
            self.root, bd=10, relief=GROOVE, bg=self.bgcolor4)
        self.bill_frame.place(x=925, y=180, width=605, height=530)
        self.bill_title = Label(self.bill_frame, text="Billing Area", font=(
            "Aparajita", 15, "bold"), fg="black", bd=10, bg=self.bgcolor4, relief=GROOVE).pack(fill="x")
        self.bill_scroll_y = Scrollbar(self.bill_frame, orient=VERTICAL)
        self.bill_scroll_x = Scrollbar(self.bill_frame, orient=HORIZONTAL)
        self.textarea = Text(
            self.bill_frame, yscrollcommand=self.bill_scroll_y.set, xscrollcommand=self.bill_scroll_x)
        self.bill_scroll_y.pack(side=RIGHT, fill=Y)
        self.bill_scroll_x.pack(side=BOTTOM, fill=X)
        # yview is inbuilt function..........!!!!!!!!!!!!
        self.bill_scroll_y.config(command=self.textarea.yview)
        self.bill_scroll_x.config(command=self.textarea.xview)
        self.textarea.pack(fill=BOTH, expand=1)

    # ==========================<<<<<<<<<<<<<<<<<<<Bill menu frame>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>=============================

        self.billmenu_frame = LabelFrame(self.root, bd=10, bg=self.bgcolor, text="Bill Menu", font=(
            "Aparajita", 15, "bold"), fg="yellow", relief=GROOVE)
        self.billmenu_frame.place(x=0, y=710, width=250,
                                  height=128, relwidth=0.83)
        self.total_born_baby = Label(self.billmenu_frame, text="Total Born Baby Price", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white").grid(row=0, column=0)

        self.total_born_baby_entry = Entry(self.billmenu_frame, font=(
            "Aparajita", 15, "bold"), textvariable=self.total_bb, bd=2, width=15).grid(row=0, column=1, padx=2)
        self.total_mens_wear = Label(self.billmenu_frame, text="Total Mens Wear Price", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white").grid(row=1, column=0)
        self.total_mens_wear_entry = Entry(self.billmenu_frame, textvariable=self.total_mw, font=(
            "Aparajita", 15, "bold"), bd=2, width=15).grid(row=1, column=1, padx=2)
        self.total_womens_wear = Label(self.billmenu_frame, text="Total Womens Wear Price", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white").grid(row=2, column=0)
        self.total_womens_wear_entry = Entry(self.billmenu_frame, textvariable=self.total_ww, font=(
            "Aparajita", 15, "bold"), bd=2, width=15).grid(row=2, column=1, padx=2)
        self.total_kitchen = Label(self.billmenu_frame, text="Total Kitchen Utensils Price", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white").grid(row=0, column=2)
        self.total_kitchen_entry = Entry(self.billmenu_frame, textvariable=self.total_ku, font=(
            "Aparajita", 15, "bold"), bd=2, width=15).grid(row=0, column=3, padx=2)
        self.total_electronics = Label(self.billmenu_frame, text="Total Electronics Price", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white").grid(row=1, column=2)
        self.total_electronics_entry = Entry(self.billmenu_frame, textvariable=self.total_ele, font=(
            "Aparajita", 15, "bold"), bd=2, width=15).grid(row=1, column=3, padx=2)
        self.total_stationary = Label(self.billmenu_frame, text="Total Stationary Price", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white").grid(row=2, column=2)
        self.total_stationary_entry = Entry(self.billmenu_frame, textvariable=self.total_stnry, font=(
            "Aparajita", 15, "bold"), bd=2, width=15).grid(row=2, column=3, padx=2)
        self.billing_address = Label(self.billmenu_frame, text="Billing_Address", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white").grid(row=0, column=4)

        self.billing_address_value = StringVar()
        self.billing_address_entry = Entry(self.billmenu_frame, textvariable=self.billing_address_value, font=(
            "Aparajita", 15, "bold"), bd=2, width=19).grid(row=0, column=5, padx=2, sticky="w")

        self.wholeseller_email = Label(self.billmenu_frame, text="WholeSeller Email", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white").grid(row=1, column=4, sticky="w")

        self.wholeseller_email_value = StringVar()
        self.wholeseller_email_entry = Entry(self.billmenu_frame, textvariable=self.wholeseller_email_value, font=(
            "Aparajita", 15, "bold"), bd=2, width=19).grid(row=1, column=5, padx=2)

        self.payment_option = ["Offline", "Online"]
        self.payment_mode = Label(self.billmenu_frame, text="Payment Mode", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white").grid(row=2, column=4)
        self.payment_mode = StringVar()
        self.payment_mode.set("Select Payment Mode")
        self.payment_mode_option = OptionMenu(
            self.billmenu_frame, self.payment_mode, *self.payment_option).grid(row=2, column=5, padx=2, pady=2, sticky="ew")

    # # ================ confirmation button frames======================================================================================

        self.button_frame = Frame(
            self.billmenu_frame, bd=5, bg=self.bgcolor4, relief=GROOVE)
        self.button_frame.place(x=950, y=0, width=250,
                                height=80, relwidth=0.2)

        self.total_button = Button(self.button_frame, text="Total", width=10, height=1, bd=7, font=(
            "Aparajita", 15, "bold"), relief=GROOVE, bg=self.bgcolor3, fg="darkred", command=self.total_function).grid(row=0, column=0, padx=7, pady=10)
        self.generate_bill_button = Button(self.button_frame, text="Generate Bill", width=10, height=1, bd=7, font=(
            "Aparajita", 15, "bold"), relief=GROOVE, bg=self.bgcolor3, fg="darkred", command=self.generate_bill_function).grid(row=0, column=1, padx=7, pady=10)
        self.clear_button = Button(self.button_frame, text="Clear", width=10, height=1, bd=7, font=(
            "Aparajita", 15, "bold"), relief=GROOVE, bg=self.bgcolor3, fg="darkred", command=self.clear_function).grid(row=0, column=2, padx=7, pady=10)
        self.exit_button = Button(self.button_frame, text="Exit", width=10, height=1, bd=7, font=(
            "Aparajita", 15, "bold"), relief=GROOVE, bg=self.bgcolor3, fg="darkred", command=self.exit_function).grid(row=0, column=3, padx=7, pady=10)

        # To display the name of the store in the bill initially..................!!!!!!!!!!!!!!
        self.welcome_bill()
    # # ================ item details=================================================================================================

        self.item_detail_frame = LabelFrame(self.root, text="Item Category Details", font=(
            "Aparajita", 15, "bold"), fg="yellow", bd=10, bg=self.bgcolor1, relief=GROOVE)
        self.item_detail_frame.place(x=0, y=95, relwidth=1)

        self.categories = StringVar()
        self.categories.set("Born Baby")
        self.categories_label = Label(
            self.item_detail_frame, text="Item Categories", font=(
                "Aparajita", 18, "bold"), bg=self.bgcolor1, fg="darkred").grid(column=0, row=0, padx=5, pady=4)
        self.born_baby_button = Radiobutton(self.item_detail_frame, text="Born Baby Items",
                                            variable=self.categories, value="Born Baby", font=(
                                                "Aparajita", 18, "bold"), bg=self.bgcolor1, fg="black", command=self.select_categories).grid(row=0, column=1, padx=2, pady=4)

        self.mens_button = Radiobutton(self.item_detail_frame, text="Men's Wear Items", variable=self.categories,
                                       value="Men's Wear", font=(
                                           "Aparajita", 18, "bold"), bg=self.bgcolor1, fg="black", command=self.select_categories).grid(row=0, column=3, padx=2, pady=4)
        self.women_button = Radiobutton(self.item_detail_frame, text="Women's Wear Items", variable=self.categories,
                                        value="Women's Wear", font=(
                                            "Aparajita", 18, "bold"), bg=self.bgcolor1, fg="black", command=self.select_categories).grid(row=0, column=4, padx=2, pady=4)
        self.kitchen_button = Radiobutton(self.item_detail_frame, text="Kitchen Utensils Items", variable=self.categories,
                                          value="Kitchen Utensils", font=(
                                              "Aparajita", 18, "bold"), bg=self.bgcolor1, fg="black", command=self.select_categories).grid(row=0, column=5, padx=2, pady=4)
        self.electronic_button = Radiobutton(self.item_detail_frame, text="Electronics Items", variable=self.categories,
                                             value="Electronics", font=(
                                                 "Aparajita", 18, "bold"), bg=self.bgcolor1, fg="black", command=self.select_categories).grid(row=0, column=6, padx=2, pady=4)
        self.Stationary_button = Radiobutton(self.item_detail_frame, text="Stationary Items", variable=self.categories,
                                             value="Stationary", font=(
                                                 "Aparajita", 18, "bold"), bg=self.bgcolor1, fg="black", command=self.select_categories).grid(row=0, column=7, padx=2, pady=4)

        # ========================================items details description ===================================================

        self.item_detail_desc = LabelFrame(self.root, text="Born Baby", font=(
            "Aparajita", 15, "bold"), fg="yellow", bd=8, bg=self.bgcolor, relief=GROOVE)
        self.item_detail_desc.place(x=0, y=180, relwidth=0.6, relheight=0.63)

        self.selection_label = Label(self.item_detail_frame, text="Born Baby Selected", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor1, fg="darkred", height=1, width=18).grid(row=0, column=8, padx=5, pady=4)

        # function call for default case..............!!!!!!!!!!!!(initially)
        self.categories.set("Born Baby")
        self.clicked_wholeseller_contact.set("Born Baby Items: 7854123458")
        self.clicked_wholeseller_name.set("Born Baby Items")
        self.wsname.set(self.whole_seller_option_list[0])
        self.ws_contact.set("7854123458")
        self.born_baby()

    def select_categories(self):
        if self.categories.get() == "Born Baby":
            self.wsname.set(self.whole_seller_option_list[0])
            self.ws_contact.set("7854123458")
            self.clicked_wholeseller_contact.set("Born Baby Items: 7854123458")
            self.clicked_wholeseller_name.set("Born Baby Items")
            self.selection_label = Label(self.item_detail_frame, text="Born Baby Selected", font=(
                "Aparajita", 15, "bold"), bg=self.bgcolor1, fg="darkred", height=1, width=18).grid(row=0, column=8, padx=5, pady=4)

            self.item_detail_desc = LabelFrame(self.root, text="Born Baby Items", font=(
                "Aparajita", 15, "bold"), fg="yellow", bd=8, bg=self.bgcolor, relief=GROOVE)
            self.item_detail_desc.place(
                x=0, y=180, relwidth=0.6, relheight=0.63)

            self.born_baby()

        elif self.categories.get() == "Men's Wear":
            self.wsname.set(self.whole_seller_option_list[1])
            self.clicked_wholeseller_contact.set("Men's Wear: 5478954364")
            self.clicked_wholeseller_name.set("Men's Wear")
            self.ws_contact.set("5478954364")
            self.selection_label = Label(self.item_detail_frame, text="Men's Wear Selected", font=(
                "Aparajita", 15, "bold"), bg=self.bgcolor1, fg="darkred", height=1, width=18).grid(row=0, column=8, padx=5, pady=4)

            self.item_detail_desc = LabelFrame(self.root, text="Men's Wear Items", font=(
                "Aparajita", 15, "bold"), fg="yellow", bd=8, bg=self.bgcolor, relief=GROOVE)
            self.item_detail_desc.place(
                x=0, y=180, relwidth=0.6, relheight=0.63)

            self.mens_wear()

        elif self.categories.get() == "Women's Wear":
            self.wsname.set(self.whole_seller_option_list[2])
            self.ws_contact.set("4521357894")
            self.clicked_wholeseller_contact.set("Women's Wear: 4521357894")
            self.clicked_wholeseller_name.set("Women's wear")

            self.selection_label = Label(self.item_detail_frame, text="Women's Wear Selected", font=(
                "Aparajita", 15, "bold"), bg=self.bgcolor1, fg="darkred", height=1, width=18).grid(row=0, column=8, padx=5, pady=4)

            self.item_detail_desc = LabelFrame(self.root, text="Women's Wear Items", font=(
                "Aparajita", 15, "bold"), fg="yellow", bd=8, bg=self.bgcolor, relief=GROOVE)
            self.item_detail_desc.place(
                x=0, y=180, relwidth=0.6, relheight=0.63)

            self.womens_wear()

        elif self.categories.get() == "Kitchen Utensils":
            self.wsname.set(self.whole_seller_option_list[3])
            self.ws_contact.set("8456214789")
            self.clicked_wholeseller_contact.set(
                "Kitchen Utensils: 8456214789")
            self.clicked_wholeseller_name.set("Kitchen Utensis")

            self.selection_label = Label(self.item_detail_frame, text="Kitchen Utensils Selected", font=(
                "Aparajita", 15, "bold"), bg=self.bgcolor1, fg="darkred", height=1, width=18).grid(row=0, column=8, padx=5, pady=4)

            self.item_detail_desc = LabelFrame(self.root, text="Kitchen Utensils Items", font=(
                "Aparajita", 15, "bold"), fg="yellow", bd=8, bg=self.bgcolor, relief=GROOVE)
            self.item_detail_desc.place(
                x=0, y=180, relwidth=0.6, relheight=0.63)

            self.kitchen_utensils()

        elif self.categories.get() == "Electronics":
            self.wsname.set(self.whole_seller_option_list[4])
            self.ws_contact.set("9875612548")
            self.clicked_wholeseller_contact.set(
                "Electronics Items: 9875612548")
            self.clicked_wholeseller_name.set("Electronics Item ")

            self.selection_label = Label(self.item_detail_frame, text="Electronics Selected", font=(
                "Aparajita", 15, "bold"), bg=self.bgcolor1, fg="darkred", height=1, width=18).grid(row=0, column=8, padx=5, pady=4)

            self.item_detail_desc = LabelFrame(self.root, text="Electronics Items", font=(
                "Aparajita", 15, "bold"), fg="yellow", bd=8, bg=self.bgcolor, relief=GROOVE)
            self.item_detail_desc.place(
                x=0, y=180, relwidth=0.6, relheight=0.63)

            self.electronics()

        elif self.categories.get() == "Stationary":
            self.wsname.set(self.whole_seller_option_list[5])
            self.ws_contact.set("3451278956")
            self.clicked_wholeseller_contact.set(
                "Stationary Items : 3451278956")
            self.clicked_wholeseller_name.set("Stationary Items")

            self.selection_label = Label(self.item_detail_frame, text="Stationary Selected", font=(
                "Aparajita", 15, "bold"), bg=self.bgcolor1, fg="darkred", height=1, width=18).grid(row=0, column=8, padx=5, pady=4)

            self.item_detail_desc = LabelFrame(self.root, text="Stationary Items", font=(
                "Aparajita", 15, "bold"), fg="yellow", bd=8, bg=self.bgcolor, relief=GROOVE)
            self.item_detail_desc.place(
                x=0, y=180, relwidth=0.6, relheight=0.63)

            self.stationary()


# ================================ list of items with size prize and quantity or company===============================================

    def born_baby(self):
        self.itemlabel1 = Label(self.item_detail_desc, text="Items", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=0, padx=3, pady=4)

        self.sizelabel1 = Label(self.item_detail_desc, text="Size", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=1, padx=3, pady=4)

        self.pricelabel1 = Label(self.item_detail_desc, text="Price", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=2, padx=3, pady=4)

        self.quantitylabel1 = Label(self.item_detail_desc, text="Quantity", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=3, padx=3, pady=4)

        self.confirmlabel1 = Label(self.item_detail_desc, text="Confirmation", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=28, bd=10, relief=RAISED).grid(row=0, column=4, padx=3, pady=4, columnspan=2)


# ===================================================================[ item -1 ]=============================================================
        self.bb_item1 = Label(self.item_detail_desc, text="Shirts", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=1, column=0, padx=3, pady=4)

        self.bb_item1_size_value = StringVar()
        self.bb_item1_size_value.set("Select the size")
        self.bb_item1_size = OptionMenu(self.item_detail_desc, self.bb_item1_size_value, "Small", "Medium").grid(
            row=1, column=1, padx=3, pady=4, sticky="ew")
# ====================== [ to set the width of the drop down menu constant use sticky="ew" in grid( vvi) ]==============================

        self.bb_item1_price_value = StringVar()
        self.bb_item1_price_value.set("Select the Price")
        self.bb_item1_price = OptionMenu(
            self.item_detail_desc, self.bb_item1_price_value, "250", "500", "800", "1000").grid(row=1, column=2, padx=3, pady=4, sticky="ew")

        self.bb_item1_quantity_value = StringVar()
        self.bb_item1_quantity_value.set("0")
        self.bb_item1_quantity = Entry(self.item_detail_desc, textvariable=self.bb_item1_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=1, column=3, padx=3, pady=4)

        self.bb_item1_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.bbconfirm_1).grid(row=1, column=4, padx=3, pady=2, columnspan=2)

# ===================================================================[ item -2 ]=============================================================
        self.bb_item2 = Label(self.item_detail_desc, text="Jeans", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=2, column=0, padx=3, pady=4)

        self.bb_item2_size_value = StringVar()
        self.bb_item2_size_value.set("Select the size")
        self.bb_item2_size = OptionMenu(self.item_detail_desc, self.bb_item2_size_value, "Small", "Medium").grid(
            row=2, column=1, padx=3, pady=4, sticky="ew")

        self.bb_item2_price_value = StringVar()
        self.bb_item2_price_value.set("Select the Price")
        self.bb_item2_price = OptionMenu(
            self.item_detail_desc, self.bb_item2_price_value, "250", "500", "800", "1000").grid(row=2, column=2, padx=3, pady=4, sticky="ew")

        self.bb_item2_quantity_value = StringVar()
        self.bb_item2_quantity_value.set("0")
        self.bb_item2_quantity = Entry(self.item_detail_desc, textvariable=self.bb_item2_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=2, column=3, padx=3, pady=4)

        self.bb_item2_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.bbconfirm_2).grid(row=2, column=4, padx=3, pady=2, columnspan=2)


# ===================================================================[ item -3]=============================================================
        self.bb_item3 = Label(self.item_detail_desc, text="Shoes", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=3, column=0, padx=3, pady=4)

        self.bb_item3_size_value = StringVar()
        self.bb_item3_size_value.set("Select the size")
        self.bb_item3_size = OptionMenu(self.item_detail_desc, self.bb_item3_size_value, "Size 1", "Size 2").grid(
            row=3, column=1, padx=3, pady=4, sticky="ew")

        self.bb_item3_price_value = StringVar()
        self.bb_item3_price_value.set("Select the Price")
        self.bb_item3_price = OptionMenu(
            self.item_detail_desc, self.bb_item3_price_value, "250", "500", "800", "1000").grid(row=3, column=2, padx=3, pady=4, sticky="ew")

        self.bb_item3_quantity_value = StringVar()
        self.bb_item3_quantity_value.set("0")
        self.bb_item3_quantity = Entry(self.item_detail_desc, textvariable=self.bb_item3_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=3, column=3, padx=3, pady=4)

        self.bb_item3_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.bbconfirm_3).grid(row=3, column=4, padx=3, pady=2, columnspan=2)

# ===================================================================[ item -4 ]=============================================================
        self.bb_item4 = Label(self.item_detail_desc, text="Frock", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=4, column=0, padx=3, pady=4)

        self.bb_item4_size_value = StringVar()
        self.bb_item4_size_value.set("Select the size")
        self.bb_item4_size = OptionMenu(self.item_detail_desc, self.bb_item4_size_value, "Small", "Medium").grid(
            row=4, column=1, padx=3, pady=4, sticky="ew")

        self.bb_item4_price_value = StringVar()
        self.bb_item4_price_value.set("Select the Price")
        self.bb_item4_price = OptionMenu(
            self.item_detail_desc, self.bb_item4_price_value, "250", "500", "800", "1000").grid(row=4, column=2, padx=3, pady=4, sticky="ew")

        self.bb_item4_quantity_value = StringVar()
        self.bb_item4_quantity_value.set("0")
        self.bb_item4_quantity = Entry(self.item_detail_desc, textvariable=self.bb_item4_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=4, column=3, padx=3, pady=4)

        self.bb_item4_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.bbconfirm_4).grid(row=4, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -5 ]=============================================================
        self.bb_item5 = Label(self.item_detail_desc, text="T-Shirts", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=5, column=0, padx=3, pady=4)

        self.bb_item5_size_value = StringVar()
        self.bb_item5_size_value.set("Select the size")
        self.bb_item5_size = OptionMenu(self.item_detail_desc, self.bb_item5_size_value, "Small", "Medium").grid(
            row=5, column=1, padx=3, pady=4, sticky="ew")

        self.bb_item5_price_value = StringVar()
        self.bb_item5_price_value.set("Select the Price")
        self.bb_item5_price = OptionMenu(
            self.item_detail_desc, self.bb_item5_price_value,  "250", "500", "800", "1000").grid(row=5, column=2, padx=3, pady=4, sticky="ew")

        self.bb_item5_quantity_value = StringVar()
        self.bb_item5_quantity_value.set("0")
        self.bb_item5_quantity = Entry(self.item_detail_desc, textvariable=self.bb_item5_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=5, column=3, padx=3, pady=4)

        self.bb_item5_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.bbconfirm_5).grid(row=5, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -6 ]=============================================================
        self.bb_item6 = Label(self.item_detail_desc, text="Pants", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=6, column=0, padx=3, pady=4)

        self.bb_item6_size_value = StringVar()
        self.bb_item6_size_value.set("Select the size")
        self.bb_item6_size = OptionMenu(self.item_detail_desc, self.bb_item6_size_value, "Small", "Medium").grid(
            row=6, column=1, padx=3, pady=4, sticky="ew")

        self.bb_item6_price_value = StringVar()
        self.bb_item6_price_value.set("Select the Price")
        self.bb_item6_price = OptionMenu(
            self.item_detail_desc, self.bb_item6_price_value, "250", "500", "800", "1000").grid(row=6, column=2, padx=3, pady=4, sticky="ew")

        self.bb_item6_quantity_value = StringVar()
        self.bb_item6_quantity_value.set("0")
        self.bb_item6_quantity = Entry(self.item_detail_desc, textvariable=self.bb_item6_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=6, column=3, padx=3, pady=4)

        self.bb_item6_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.bbconfirm_6).grid(row=6, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -7 ]=============================================================
        self.bb_item7 = Label(self.item_detail_desc, text="Sweater", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=7, column=0, padx=3, pady=4)

        self.bb_item7_size_value = StringVar()
        self.bb_item7_size_value.set("Select the size")
        self.bb_item7_size = OptionMenu(self.item_detail_desc, self.bb_item7_size_value, "Small", "Medium").grid(
            row=7, column=1, padx=3, pady=4, sticky="ew")

        self.bb_item7_price_value = StringVar()
        self.bb_item7_price_value.set("Select the Price")
        self.bb_item7_price = OptionMenu(
            self.item_detail_desc, self.bb_item7_price_value, "250", "500", "800", "1000").grid(row=7, column=2, padx=3, pady=4, sticky="ew")

        self.bb_item7_quantity_value = StringVar()
        self.bb_item7_quantity_value.set("0")
        self.bb_item7_quantity = Entry(self.item_detail_desc, textvariable=self.bb_item7_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=7, column=3, padx=3, pady=4)

        self.bb_item7_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.bbconfirm_7).grid(row=7, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -8 ]=============================================================
        self.bb_item8 = Label(self.item_detail_desc, text="Jackets", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=8, column=0, padx=3, pady=4)

        self.bb_item8_size_value = StringVar()
        self.bb_item8_size_value.set("Select the size")
        self.bb_item8_size = OptionMenu(self.item_detail_desc, self.bb_item8_size_value, "Small", "Medium").grid(
            row=8, column=1, padx=3, pady=4, sticky="ew")

        self.bb_item8_price_value = StringVar()
        self.bb_item8_price_value.set("Select the Price")
        self.bb_item8_price = OptionMenu(
            self.item_detail_desc, self.bb_item8_price_value, "250", "500", "800", "1000").grid(row=8, column=2, padx=3, pady=4, sticky="ew")

        self.bb_item8_quantity_value = StringVar()
        self.bb_item8_quantity_value.set("0")
        self.bb_item8_quantity = Entry(self.item_detail_desc, textvariable=self.bb_item8_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=8, column=3, padx=3, pady=4)

        self.bb_item8_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.bbconfirm_8).grid(row=8, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -9 ]=============================================================
        self.bb_item9 = Label(self.item_detail_desc, text="Baby Caps", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=9, column=0, padx=3, pady=4)

        self.bb_item9_size_value = StringVar()
        self.bb_item9_size_value.set("Select the size")
        self.bb_item9_size = OptionMenu(self.item_detail_desc, self.bb_item9_size_value, "Small", "Medium").grid(
            row=9, column=1, padx=3, pady=4, sticky="ew")

        self.bb_item9_price_value = StringVar()
        self.bb_item9_price_value.set("Select the Price")
        self.bb_item9_price = OptionMenu(
            self.item_detail_desc, self.bb_item9_price_value, "100", "150", "200", "250").grid(row=9, column=2, padx=3, pady=4, sticky="ew")

        self.bb_item9_quantity_value = StringVar()
        self.bb_item9_quantity_value.set("0")
        self.bb_item9_quantity = Entry(self.item_detail_desc, textvariable=self.bb_item9_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=9, column=3, padx=3, pady=4)

        self.bb_item9_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.bbconfirm_9).grid(row=9, column=4, padx=3, pady=2, columnspan=2)

# ===================================================================[ item -10 ]=============================================================
        self.bb_item10 = Label(self.item_detail_desc, text="Shocks", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=10, column=0, padx=3, pady=4)

        self.bb_item10_size_value = StringVar()
        self.bb_item10_size_value.set("Select the size")
        self.bb_item10_size = OptionMenu(self.item_detail_desc, self.bb_item10_size_value, "Small", "Medium").grid(
            row=10, column=1, padx=3, pady=4, sticky="ew")

        self.bb_item10_price_value = StringVar()
        self.bb_item10_price_value.set("Select the Price")
        self.bb_item10_price = OptionMenu(
            self.item_detail_desc, self.bb_item10_price_value, "100", "150", "200", "250").grid(row=10, column=2, padx=3, pady=4, sticky="ew")

        self.bb_item10_quantity_value = StringVar()
        self.bb_item10_quantity_value.set("0")
        self.bb_item10_quantity = Entry(self.item_detail_desc, textvariable=self.bb_item10_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=10, column=3, padx=3, pady=4)

        self.bb_item10_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.bbconfirm_10).grid(row=10, column=4, padx=3, pady=2, columnspan=2)


# ===========================================================================================================================================


    def mens_wear(self):
        self.itemlabel2 = Label(self.item_detail_desc, text="Items", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=0, padx=3, pady=4)

        self.sizelabel2 = Label(self.item_detail_desc, text="Size", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=1, padx=3, pady=4)

        self.pricelabel2 = Label(self.item_detail_desc, text="Price", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=2, padx=3, pady=4)

        self.quantitylabel2 = Label(self.item_detail_desc, text="Quantity", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=3, padx=3, pady=4)

        self.confirmlabel2 = Label(self.item_detail_desc, text="Confirmation", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=28, bd=10, relief=RAISED).grid(row=0, column=4, padx=3, pady=4, columnspan=2)


# ===================================================================[ item -1 ]=============================================================
        self.mens_item1 = Label(self.item_detail_desc, text="Formal Shirts", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=1, column=0, padx=3, pady=4)

        self.mens_item1_size_value = StringVar()
        self.mens_item1_size_value.set("Select the size")
        self.mens_item1_size = OptionMenu(self.item_detail_desc, self.mens_item1_size_value, "S", "M", "L", "XL", "XXL", "XXXL").grid(
            row=1, column=1, padx=3, pady=4, sticky="ew")

        self.mens_item1_price_value = StringVar()
        self.mens_item1_price_value.set("Select the Price")
        self.mens_item1_price = OptionMenu(
            self.item_detail_desc, self.mens_item1_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=1, column=2, padx=3, pady=4, sticky="ew")

        self.mens_item1_quantity_value = StringVar()
        self.mens_item1_quantity_value.set("0")
        self.mens_item1_quantity = Entry(self.item_detail_desc, textvariable=self.mens_item1_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=1, column=3, padx=3, pady=4)

        self.mens_item1_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.menswearconfirm_1).grid(row=1, column=4, padx=3, pady=2, columnspan=2)


# ===================================================================[ item -2 ]=============================================================
        self.mens_item2 = Label(self.item_detail_desc, text="T-Shirts", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=2, column=0, padx=3, pady=4)

        self.mens_item2_size_value = StringVar()
        self.mens_item2_size_value.set("Select the size")
        self.mens_item2_size = OptionMenu(self.item_detail_desc, self.mens_item2_size_value, "S", "M", "L", "XL", "XXL", "XXXL").grid(
            row=2, column=1, padx=3, pady=4, sticky="ew")

        self.mens_item2_price_value = StringVar()
        self.mens_item2_price_value.set("Select the Price")
        self.mens_item2_price = OptionMenu(
            self.item_detail_desc, self.mens_item2_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=2, column=2, padx=3, pady=4, sticky="ew")

        self.mens_item2_quantity_value = StringVar()
        self.mens_item2_quantity_value.set("0")
        self.mens_item2_quantity = Entry(self.item_detail_desc, textvariable=self.mens_item2_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=2, column=3, padx=3, pady=4)

        self.mens_item2_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.menswearconfirm_2).grid(row=2, column=4, padx=3, pady=2, columnspan=2)
# ===================================================================[ item -3]=============================================================
        self.mens_item3 = Label(self.item_detail_desc, text="Formal Pants", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=3, column=0, padx=3, pady=4)

        self.mens_item3_size_value = StringVar()
        self.mens_item3_size_value.set("Select the size")
        self.mens_item3_size = OptionMenu(self.item_detail_desc, self.mens_item3_size_value, "Size 28", "Size 30", "Size 32", "Size 34", "Size 36", "Size 38").grid(
            row=3, column=1, padx=3, pady=4, sticky="ew")

        self.mens_item3_price_value = StringVar()
        self.mens_item3_price_value.set("Select the Price")
        self.mens_item3_price = OptionMenu(
            self.item_detail_desc, self.mens_item3_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=3, column=2, padx=3, pady=4, sticky="ew")

        self.mens_item3_quantity_value = StringVar()
        self.mens_item3_quantity_value.set("0")
        self.mens_item3_quantity = Entry(self.item_detail_desc, textvariable=self.mens_item3_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=3, column=3, padx=3, pady=4)

        self.mens_item3_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.menswearconfirm_3).grid(row=3, column=4, padx=3, pady=2, columnspan=2)


# ===================================================================[ item -4 ]=============================================================
        self.mens_item4 = Label(self.item_detail_desc, text="Jeans", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=4, column=0, padx=3, pady=4)

        self.mens_item4_size_value = StringVar()
        self.mens_item4_size_value.set("Select the size")
        self.mens_item4_size = OptionMenu(self.item_detail_desc, self.mens_item4_size_value, "Size 28", "Size 30", "Size 32", "Size 34", "Size 36", "Size 38").grid(
            row=4, column=1, padx=3, pady=4, sticky="ew")

        self.mens_item4_price_value = StringVar()
        self.mens_item4_price_value.set("Select the Price")
        self.mens_item4_price = OptionMenu(
            self.item_detail_desc, self.mens_item4_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=4, column=2, padx=3, pady=4, sticky="ew")

        self.mens_item4_quantity_value = StringVar()
        self.mens_item4_quantity_value.set("0")
        self.mens_item4_quantity = Entry(self.item_detail_desc, textvariable=self.mens_item4_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=4, column=3, padx=3, pady=4)

        self.mens_item4_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.menswearconfirm_4).grid(row=4, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -5 ]=============================================================
        self.mens_item5 = Label(self.item_detail_desc, text="Coats", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=5, column=0, padx=3, pady=4)

        self.mens_item5_size_value = StringVar()
        self.mens_item5_size_value.set("Select the size")
        self.mens_item5_size = OptionMenu(self.item_detail_desc, self.mens_item5_size_value, "S", "M", "L", "XL", "XXL", "XXXL").grid(
            row=5, column=1, padx=3, pady=4, sticky="ew")

        self.mens_item5_price_value = StringVar()
        self.mens_item5_price_value.set("Select the Price")
        self.mens_item5_price = OptionMenu(
            self.item_detail_desc, self.mens_item5_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=5, column=2, padx=3, pady=4, sticky="ew")

        self.mens_item5_quantity_value = StringVar()
        self.mens_item5_quantity_value.set("0")
        self.mens_item5_quantity = Entry(self.item_detail_desc, textvariable=self.mens_item5_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=5, column=3, padx=3, pady=4)

        self.mens_item5_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.menswearconfirm_5).grid(row=5, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -6 ]=============================================================
        self.mens_item6 = Label(self.item_detail_desc, text="Hoodies", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=6, column=0, padx=3, pady=4)

        self.mens_item6_size_value = StringVar()
        self.mens_item6_size_value.set("Select the size")
        self.mens_item6_size = OptionMenu(self.item_detail_desc, self.mens_item6_size_value, "S", "M", "L", "XL", "XXL", "XXXL").grid(
            row=6, column=1, padx=3, pady=4, sticky="ew")

        self.mens_item6_price_value = StringVar()
        self.mens_item6_price_value.set("Select the Price")
        self.mens_item6_price = OptionMenu(
            self.item_detail_desc, self.mens_item6_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=6, column=2, padx=3, pady=4, sticky="ew")

        self.mens_item6_quantity_value = StringVar()
        self.mens_item6_quantity_value.set("0")
        self.mens_item6_quantity = Entry(self.item_detail_desc, textvariable=self.mens_item6_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=6, column=3, padx=3, pady=4)

        self.mens_item6_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.menswearconfirm_6).grid(row=6, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -7 ]=============================================================
        self.mens_item7 = Label(self.item_detail_desc, text="Jackets", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=7, column=0, padx=3, pady=4)

        self.mens_item7_size_value = StringVar()
        self.mens_item7_size_value.set("Select the size")
        self.mens_item7_size = OptionMenu(self.item_detail_desc, self.mens_item7_size_value, "S", "M", "L", "XL", "XXL", "XXXL").grid(
            row=7, column=1, padx=3, pady=4, sticky="ew")

        self.mens_item7_price_value = StringVar()
        self.mens_item7_price_value.set("Select the Price")
        self.mens_item7_price = OptionMenu(
            self.item_detail_desc, self.mens_item7_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=7, column=2, padx=3, pady=4, sticky="ew")

        self.mens_item7_quantity_value = StringVar()
        self.mens_item7_quantity_value.set("0")
        self.mens_item7_quantity = Entry(self.item_detail_desc, textvariable=self.mens_item7_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=7, column=3, padx=3, pady=4)

        self.mens_item7_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.menswearconfirm_7).grid(row=7, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -8 ]=============================================================
        self.mens_item8 = Label(self.item_detail_desc, text="Sweaters", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=8, column=0, padx=3, pady=4)

        self.mens_item8_size_value = StringVar()
        self.mens_item8_size_value.set("Select the size")
        self.mens_item8_size = OptionMenu(self.item_detail_desc, self.mens_item8_size_value, "S", "M", "L", "XL", "XXL", "XXXL").grid(
            row=8, column=1, padx=3, pady=4, sticky="ew")

        self.mens_item8_price_value = StringVar()
        self.mens_item8_price_value.set("Select the Price")
        self.mens_item8_price = OptionMenu(
            self.item_detail_desc, self.mens_item8_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=8, column=2, padx=3, pady=4, sticky="ew")

        self.mens_item8_quantity_value = StringVar()
        self.mens_item8_quantity_value.set("0")
        self.mens_item8_quantity = Entry(self.item_detail_desc, textvariable=self.mens_item8_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=8, column=3, padx=3, pady=4)

        self.mens_item8_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.menswearconfirm_8).grid(row=8, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -9 ]=============================================================
        self.mens_item9 = Label(self.item_detail_desc, text="Shoes", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=9, column=0, padx=3, pady=4)

        self.mens_item9_size_value = StringVar()
        self.mens_item9_size_value.set("Select the size")
        self.mens_item9_size = OptionMenu(self.item_detail_desc, self.mens_item9_size_value, "Size 7", "Size 8", "Size 9", "Size 10").grid(
            row=9, column=1, padx=3, pady=4, sticky="ew")

        self.mens_item9_price_value = StringVar()
        self.mens_item9_price_value.set("Select the Price")
        self.mens_item9_price = OptionMenu(
            self.item_detail_desc, self.mens_item9_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=9, column=2, padx=3, pady=4, sticky="ew")

        self.mens_item9_quantity_value = StringVar()
        self.mens_item9_quantity_value.set("0")
        self.mens_item9_quantity = Entry(self.item_detail_desc, textvariable=self.mens_item9_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=9, column=3, padx=3, pady=4)

        self.mens_item9_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.menswearconfirm_9).grid(row=9, column=4, padx=3, pady=2, columnspan=2)

# ===================================================================[ item -10 ]=============================================================
        self.mens_item10 = Label(self.item_detail_desc, text="Kurtas", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=10, column=0, padx=3, pady=4)

        self.mens_item10_size_value = StringVar()
        self.mens_item10_size_value.set("Select the size")
        self.mens_item10_size = OptionMenu(self.item_detail_desc, self.mens_item10_size_value, "M", "L", "XI", "2XI", "3XI", "4XI").grid(
            row=10, column=1, padx=3, pady=4, sticky="ew")

        self.mens_item10_price_value = StringVar()
        self.mens_item10_price_value.set("Select the Price")
        self.mens_item10_price = OptionMenu(
            self.item_detail_desc, self.mens_item10_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=10, column=2, padx=3, pady=4, sticky="ew")

        self.mens_item10_quantity_value = StringVar()
        self.mens_item10_quantity_value.set("0")
        self.mens_item10_quantity = Entry(self.item_detail_desc, textvariable=self.mens_item10_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=10, column=3, padx=3, pady=4)

        self.mens_item10_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.menswearconfirm_10).grid(row=10, column=4, padx=3, pady=2, columnspan=2)
# ===========================================================================================================================================

    def womens_wear(self):
        self.itemlabel3 = Label(self.item_detail_desc, text="Items", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=0, padx=3, pady=4)

        self.sizelabel3 = Label(self.item_detail_desc, text="Size", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=1, padx=3, pady=4)

        self.pricelabel3 = Label(self.item_detail_desc, text="Price", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=2, padx=3, pady=4)

        self.quantitylabel3 = Label(self.item_detail_desc, text="Quantity", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=3, padx=3, pady=4)

        self.confirmlabel3 = Label(self.item_detail_desc, text="Confirmation", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=28, bd=10, relief=RAISED).grid(row=0, column=4, padx=3, pady=4, columnspan=2)


# ===================================================================[ item -1 ]=============================================================
        self.womens_item1 = Label(self.item_detail_desc, text="Kurta Sets", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=1, column=0, padx=3, pady=4)

        self.womens_item1_size_value = StringVar()
        self.womens_item1_size_value.set("Select the size")
        self.womens_item1_size = OptionMenu(self.item_detail_desc, self.womens_item1_size_value, "M", "L", "XI", "2XI", "3XI", "4XI").grid(
            row=1, column=1, padx=3, pady=4, sticky="ew")

        self.womens_item1_price_value = StringVar()
        self.womens_item1_price_value.set("Select the Price")
        self.womens_item1_price = OptionMenu(
            self.item_detail_desc, self.womens_item1_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=1, column=2, padx=3, pady=4, sticky="ew")

        self.womens_item1_quantity_value = StringVar()
        self.womens_item1_quantity_value.set("0")
        self.womens_item1_quantity = Entry(self.item_detail_desc, textvariable=self.womens_item1_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=1, column=3, padx=3, pady=4)

        self.womens_item1_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.womenswearconfirm_1).grid(row=1, column=4, padx=3, pady=2, columnspan=2)


# ===================================================================[ item -2 ]=============================================================
        self.womens_item2 = Label(self.item_detail_desc, text="Jeans", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=2, column=0, padx=3, pady=4)

        self.womens_item2_size_value = StringVar()
        self.womens_item2_size_value.set("Select the size")
        self.womens_item2_size = OptionMenu(self.item_detail_desc, self.womens_item2_size_value, "Size 28", "Size 30", "Size 32", "Size 34", "Size 36", "Size 38").grid(
            row=2, column=1, padx=3, pady=4, sticky="ew")

        self.womens_item2_price_value = StringVar()
        self.womens_item2_price_value.set("Select the Price")
        self.womens_item2_price = OptionMenu(
            self.item_detail_desc, self.womens_item2_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=2, column=2, padx=3, pady=4, sticky="ew")

        self.womens_item2_quantity_value = StringVar()
        self.womens_item2_quantity_value.set("0")
        self.womens_item2_quantity = Entry(self.item_detail_desc, textvariable=self.womens_item2_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=2, column=3, padx=3, pady=4)

        self.womens_item2_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.womenswearconfirm_2).grid(row=2, column=4, padx=3, pady=2, columnspan=2)
# ===================================================================[ item -3]=============================================================
        self.womens_item3 = Label(self.item_detail_desc, text="T-Shirts", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=3, column=0, padx=3, pady=4)

        self.womens_item3_size_value = StringVar()
        self.womens_item3_size_value.set("Select the size")
        self.womens_item3_size = OptionMenu(self.item_detail_desc, self.womens_item3_size_value, "S", "M", "L", "XL", "XXL", "XXXL").grid(
            row=3, column=1, padx=3, pady=4, sticky="ew")

        self.womens_item3_price_value = StringVar()
        self.womens_item3_price_value.set("Select the Price")
        self.womens_item3_price = OptionMenu(
            self.item_detail_desc, self.womens_item3_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=3, column=2, padx=3, pady=4, sticky="ew")

        self.womens_item3_quantity_value = StringVar()
        self.womens_item3_quantity_value.set("0")
        self.womens_item3_quantity = Entry(self.item_detail_desc, textvariable=self.womens_item3_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=3, column=3, padx=3, pady=4)

        self.womens_item3_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.womenswearconfirm_3).grid(row=3, column=4, padx=3, pady=2, columnspan=2)
# ===================================================================[ item -4 ]=============================================================
        self.womens_item4 = Label(self.item_detail_desc, text="Jackets", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=4, column=0, padx=3, pady=4)

        self.womens_item4_size_value = StringVar()
        self.womens_item4_size_value.set("Select the size")
        self.womens_item4_size = OptionMenu(self.item_detail_desc, self.womens_item4_size_value, "S", "M", "L", "XL", "XXL", "XXXL").grid(
            row=4, column=1, padx=3, pady=4, sticky="ew")

        self.womens_item4_price_value = StringVar()
        self.womens_item4_price_value.set("Select the Price")
        self.womens_item4_price = OptionMenu(
            self.item_detail_desc, self.womens_item4_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=4, column=2, padx=3, pady=4, sticky="ew")

        self.womens_item4_quantity_value = StringVar()
        self.womens_item4_quantity_value.set("0")
        self.womens_item4_quantity = Entry(self.item_detail_desc, textvariable=self.womens_item4_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=4, column=3, padx=3, pady=4)

        self.womens_item4_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.womenswearconfirm_4).grid(row=4, column=4, padx=3, pady=2, columnspan=2)
        # ===================================================================[ item -5 ]=============================================================
        self.womens_item5 = Label(self.item_detail_desc, text="Dresses", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=5, column=0, padx=3, pady=4)

        self.womens_item5_size_value = StringVar()
        self.womens_item5_size_value.set("Select the size")
        self.womens_item5_size = OptionMenu(self.item_detail_desc, self.womens_item5_size_value, "S", "M", "L", "XL", "XXL", "XXXL").grid(
            row=5, column=1, padx=3, pady=4, sticky="ew")

        self.womens_item5_price_value = StringVar()
        self.womens_item5_price_value.set("Select the Price")
        self.womens_item5_price = OptionMenu(
            self.item_detail_desc, self.womens_item5_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=5, column=2, padx=3, pady=4, sticky="ew")

        self.womens_item5_quantity_value = StringVar()
        self.womens_item5_quantity_value.set("0")
        self.womens_item5_quantity = Entry(self.item_detail_desc, textvariable=self.womens_item5_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=5, column=3, padx=3, pady=4)

        self.womens_item5_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.womenswearconfirm_5).grid(row=5, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -6 ]=============================================================
        self.womens_item6 = Label(self.item_detail_desc, text="Shoes", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=6, column=0, padx=3, pady=4)

        self.womens_item6_size_value = StringVar()
        self.womens_item6_size_value.set("Select the size")
        self.womens_item6_size = OptionMenu(self.item_detail_desc, self.womens_item6_size_value, "Size 7", "Size 8", "Size 9", "Size 10").grid(
            row=6, column=1, padx=3, pady=4, sticky="ew")

        self.womens_item6_price_value = StringVar()
        self.womens_item6_price_value.set("Select the Price")
        self.womens_item6_price = OptionMenu(
            self.item_detail_desc, self.womens_item6_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=6, column=2, padx=3, pady=4, sticky="ew")

        self.womens_item6_quantity_value = StringVar()
        self.womens_item6_quantity_value.set("0")
        self.womens_item6_quantity = Entry(self.item_detail_desc, textvariable=self.womens_item6_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=6, column=3, padx=3, pady=4)

        self.womens_item6_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.womenswearconfirm_6).grid(row=6, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -7 ]=============================================================
        self.womens_item7 = Label(self.item_detail_desc, text="Kafri Gowns", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=7, column=0, padx=3, pady=4)

        self.womens_item7_size_value = StringVar()
        self.womens_item7_size_value.set("Select the size")
        self.womens_item7_size = OptionMenu(self.item_detail_desc, self.womens_item7_size_value, "S", "M", "L", "XL", "XXL", "XXXL").grid(
            row=7, column=1, padx=3, pady=4, sticky="ew")

        self.womens_item7_price_value = StringVar()
        self.womens_item7_price_value.set("Select the Price")
        self.womens_item7_price = OptionMenu(
            self.item_detail_desc, self.womens_item7_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=7, column=2, padx=3, pady=4, sticky="ew")

        self.womens_item7_quantity_value = StringVar()
        self.womens_item7_quantity_value.set("0")
        self.womens_item7_quantity = Entry(self.item_detail_desc, textvariable=self.womens_item7_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=7, column=3, padx=3, pady=4)

        self.womens_item7_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.womenswearconfirm_7).grid(row=7, column=4, padx=3, pady=2, columnspan=2)
        # ===================================================================[ item -8 ]=============================================================
        self.womens_item8 = Label(self.item_detail_desc, text="Leggings", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=8, column=0, padx=3, pady=4)

        self.womens_item8_size_value = StringVar()
        self.womens_item8_size_value.set("Select the size")
        self.womens_item8_size = OptionMenu(self.item_detail_desc, self.womens_item8_size_value, "Size 28", "Size 30", "Size 32", "Size 34", "Size 36", "Size 38").grid(
            row=8, column=1, padx=3, pady=4, sticky="ew")

        self.womens_item8_price_value = StringVar()
        self.womens_item8_price_value.set("Select the Price")
        self.womens_item8_price = OptionMenu(
            self.item_detail_desc, self.womens_item8_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=8, column=2, padx=3, pady=4, sticky="ew")

        self.womens_item8_quantity_value = StringVar()
        self.womens_item8_quantity_value.set("0")
        self.womens_item8_quantity = Entry(self.item_detail_desc, textvariable=self.womens_item8_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=8, column=3, padx=3, pady=4)

        self.womens_item8_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.womenswearconfirm_8).grid(row=8, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -9 ]=============================================================
        self.womens_item9 = Label(self.item_detail_desc, text="Scarfs", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=9, column=0, padx=3, pady=4)

        self.womens_item9_size_value = StringVar()
        self.womens_item9_size_value.set("Select the size")
        self.womens_item9_size = OptionMenu(self.item_detail_desc, self.womens_item9_size_value, "Small", "Medium", "Large").grid(
            row=9, column=1, padx=3, pady=4, sticky="ew")

        self.womens_item9_price_value = StringVar()
        self.womens_item9_price_value.set("Select the Price")
        self.womens_item9_price = OptionMenu(
            self.item_detail_desc, self.womens_item9_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=9, column=2, padx=3, pady=4, sticky="ew")

        self.womens_item9_quantity_value = StringVar()
        self.womens_item9_quantity_value.set("0")
        self.womens_item9_quantity = Entry(self.item_detail_desc, textvariable=self.womens_item9_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=9, column=3, padx=3, pady=4)

        self.womens_item9_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.womenswearconfirm_9).grid(row=9, column=4, padx=3, pady=2, columnspan=2)
# ===================================================================[ item -10 ]=============================================================
        self.womens_item10 = Label(self.item_detail_desc, text="Skirts", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=10, column=0, padx=3, pady=4)

        self.womens_item10_size_value = StringVar()
        self.womens_item10_size_value.set("Select the size")
        self.womens_item10_size = OptionMenu(self.item_detail_desc, self.womens_item10_size_value, "S", "M", "L", "XL", "XXL", "XXXL").grid(
            row=10, column=1, padx=3, pady=4, sticky="ew")

        self.womens_item10_price_value = StringVar()
        self.womens_item10_price_value.set("Select the Price")
        self.womens_item10_price = OptionMenu(
            self.item_detail_desc, self.womens_item10_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=10, column=2, padx=3, pady=4, sticky="ew")

        self.womens_item10_quantity_value = StringVar()
        self.womens_item10_quantity_value.set("0")
        self.womens_item10_quantity = Entry(self.item_detail_desc, textvariable=self.womens_item10_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=10, column=3, padx=3, pady=4)

        self.womens_item10_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.womenswearconfirm_10).grid(row=10, column=4, padx=3, pady=2, columnspan=2)

# ===========================================================================================================================================

    def kitchen_utensils(self):
        self.itemlabel4 = Label(self.item_detail_desc, text="Items", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=0, padx=3, pady=4)

        self.companylabel1 = Label(self.item_detail_desc, text="Company", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=1, padx=3, pady=4)

        self.pricelabel4 = Label(self.item_detail_desc, text="Price", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=2, padx=3, pady=4)

        self.quantitylabel4 = Label(self.item_detail_desc, text="Quantity", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=3, padx=3, pady=4)

        self.confirmlabel4 = Label(self.item_detail_desc, text="Confirmation", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=28, bd=10, relief=RAISED).grid(row=0, column=4, padx=3, pady=4, columnspan=2)


# ===================================================================[ item -1 ]=============================================================
        self.kitchen_item1 = Label(self.item_detail_desc, text="Pressure Cooker", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=1, column=0, padx=3, pady=4)

        self.kitchen_item1_company_value = StringVar()
        self.kitchen_item1_company_value.set("Select the company")
        self.kitchen_item1_company = OptionMenu(self.item_detail_desc, self.kitchen_item1_company_value, "United", "Hawkins", "Prestige", "Milton").grid(
            row=1, column=1, padx=3, pady=4, sticky="ew")

        self.kitchen_item1_price_value = StringVar()
        self.kitchen_item1_price_value.set("Select the Price")
        self.kitchen_item1_price = OptionMenu(
            self.item_detail_desc, self.kitchen_item1_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=1, column=2, padx=3, pady=4, sticky="ew")

        self.kitchen_item1_quantity_value = StringVar()
        self.kitchen_item1_quantity_value.set("0")
        self.kitchen_item1_quantity = Entry(self.item_detail_desc, textvariable=self.kitchen_item1_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=1, column=3, padx=3, pady=4)

        self.kitchen_item1_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.kitchenconfirm_1).grid(row=1, column=4, padx=3, pady=2, columnspan=2)
# ===================================================================[ item -2 ]=============================================================
        self.kitchen_item2 = Label(self.item_detail_desc, text="Induction", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=2, column=0, padx=3, pady=4)

        self.kitchen_item2_company_value = StringVar()
        self.kitchen_item2_company_value.set("Select the company")
        self.kitchen_item2_company = OptionMenu(self.item_detail_desc, self.kitchen_item2_company_value, "Bajaj", "Usha", "Prestige", "LG").grid(
            row=2, column=1, padx=3, pady=4, sticky="ew")

        self.kitchen_item2_price_value = StringVar()
        self.kitchen_item2_price_value.set("Select the Price")
        self.kitchen_item2_price = OptionMenu(
            self.item_detail_desc, self.kitchen_item2_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=2, column=2, padx=3, pady=4, sticky="ew")

        self.kitchen_item2_quantity_value = StringVar()
        self.kitchen_item2_quantity_value.set("0")
        self.kitchen_item2_quantity = Entry(self.item_detail_desc, textvariable=self.kitchen_item2_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=2, column=3, padx=3, pady=4)

        self.kitchen_item2_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.kitchenconfirm_2).grid(row=2, column=4, padx=3, pady=2, columnspan=2)
# ===================================================================[ item -3]=============================================================
        self.kitchen_item3 = Label(self.item_detail_desc, text="Mixer Grinder", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=3, column=0, padx=3, pady=4)

        self.kitchen_item3_company_value = StringVar()
        self.kitchen_item3_company_value.set("Select the company")
        self.kitchen_item3_company = OptionMenu(self.item_detail_desc, self.kitchen_item3_company_value, "Bajaj", "Sumit", "Philips", "Orient").grid(
            row=3, column=1, padx=3, pady=4, sticky="ew")

        self.kitchen_item3_price_value = StringVar()
        self.kitchen_item3_price_value.set("Select the Price")
        self.kitchen_item3_price = OptionMenu(
            self.item_detail_desc, self.kitchen_item3_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=3, column=2, padx=3, pady=4, sticky="ew")

        self.kitchen_item3_quantity_value = StringVar()
        self.kitchen_item3_quantity_value.set("0")
        self.kitchen_item3_quantity = Entry(self.item_detail_desc, textvariable=self.kitchen_item3_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=3, column=3, padx=3, pady=4)

        self.kitchen_item3_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.kitchenconfirm_3).grid(row=3, column=4, padx=3, pady=2, columnspan=2)
# ===================================================================[ item -4 ]=============================================================
        self.kitchen_item4 = Label(self.item_detail_desc, text="Micro Oven", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=4, column=0, padx=3, pady=4)

        self.kitchen_item4_company_value = StringVar()
        self.kitchen_item4_company_value.set("Select the company")
        self.kitchen_item4_company = OptionMenu(self.item_detail_desc, self.kitchen_item4_company_value, "Samsung", "Whirpool", "Bajaj", "LG").grid(
            row=4, column=1, padx=3, pady=4, sticky="ew")

        self.kitchen_item4_price_value = StringVar()
        self.kitchen_item4_price_value.set("Select the Price")
        self.kitchen_item4_price = OptionMenu(
            self.item_detail_desc, self.kitchen_item4_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=4, column=2, padx=3, pady=4, sticky="ew")

        self.kitchen_item4_quantity_value = StringVar()
        self.kitchen_item4_quantity_value.set("0")
        self.kitchen_item4_quantity = Entry(self.item_detail_desc, textvariable=self.kitchen_item4_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=4, column=3, padx=3, pady=4)

        self.kitchen_item4_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.kitchenconfirm_4).grid(row=4, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -5 ]=============================================================
        self.kitchen_item5 = Label(self.item_detail_desc, text="Dinner Set", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=5, column=0, padx=3, pady=4)

        self.kitchen_item5_company_value = StringVar()
        self.kitchen_item5_company_value.set("Select the company")
        self.kitchen_item5_company = OptionMenu(self.item_detail_desc, self.kitchen_item5_company_value, "La Opala", "Nayasa", "Corelle", "Borosil Mimosa").grid(
            row=5, column=1, padx=3, pady=4, sticky="ew")

        self.kitchen_item5_price_value = StringVar()
        self.kitchen_item5_price_value.set("Select the Price")
        self.kitchen_item5_price = OptionMenu(
            self.item_detail_desc, self.kitchen_item5_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=5, column=2, padx=3, pady=4, sticky="ew")

        self.kitchen_item5_quantity_value = StringVar()
        self.kitchen_item5_quantity_value.set("0")
        self.kitchen_item5_quantity = Entry(self.item_detail_desc, textvariable=self.kitchen_item5_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=5, column=3, padx=3, pady=4)

        self.kitchen_item5_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.kitchenconfirm_5).grid(row=5, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -6 ]=============================================================
        self.kitchen_item6 = Label(self.item_detail_desc, text="Utensils Stand", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=6, column=0, padx=3, pady=4)

        self.kitchen_item6_company_value = StringVar()
        self.kitchen_item6_company_value.set("Select the company")
        self.kitchen_item6_company = OptionMenu(self.item_detail_desc, self.kitchen_item6_company_value, "Krishna Wares", "Hindware", "Deo Dap").grid(
            row=6, column=1, padx=3, pady=4, sticky="ew")

        self.kitchen_item6_price_value = StringVar()
        self.kitchen_item6_price_value.set("Select the Price")
        self.kitchen_item6_price = OptionMenu(
            self.item_detail_desc, self.kitchen_item6_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=6, column=2, padx=3, pady=4, sticky="ew")

        self.kitchen_item6_quantity_value = StringVar()
        self.kitchen_item6_quantity_value.set("0")
        self.kitchen_item6_quantity = Entry(self.item_detail_desc, textvariable=self.kitchen_item6_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=6, column=3, padx=3, pady=4)

        self.kitchen_item6_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.kitchenconfirm_6).grid(row=6, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -7 ]=============================================================
        self.kitchen_item7 = Label(self.item_detail_desc, text="Frying Pan", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=7, column=0, padx=3, pady=4)

        self.kitchen_item7_company_value = StringVar()
        self.kitchen_item7_company_value.set("Select the company")
        self.kitchen_item7_company = OptionMenu(self.item_detail_desc, self.kitchen_item7_company_value, "All-Clad", "Le-Creuset", "T-Fal", "Calphalon").grid(
            row=7, column=1, padx=3, pady=4, sticky="ew")

        self.kitchen_item7_price_value = StringVar()
        self.kitchen_item7_price_value.set("Select the Price")
        self.kitchen_item7_price = OptionMenu(
            self.item_detail_desc, self.kitchen_item7_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=7, column=2, padx=3, pady=4, sticky="ew")

        self.kitchen_item7_quantity_value = StringVar()
        self.kitchen_item7_quantity_value.set("0")
        self.kitchen_item7_quantity = Entry(self.item_detail_desc, textvariable=self.kitchen_item7_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=7, column=3, padx=3, pady=4)

        self.kitchen_item7_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.kitchenconfirm_7).grid(row=7, column=4, padx=3, pady=2, columnspan=2)
        # ===================================================================[ item -8 ]=============================================================
        self.kitchen_item8 = Label(self.item_detail_desc, text="Spoon Set", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=8, column=0, padx=3, pady=4)

        self.kitchen_item8_company_value = StringVar()
        self.kitchen_item8_company_value.set("Select the company")
        self.kitchen_item8_company = OptionMenu(self.item_detail_desc, self.kitchen_item8_company_value, "Solimo", "Signoraware", "Prestige", "Bergen Bagutee").grid(
            row=8, column=1, padx=3, pady=4, sticky="ew")

        self.kitchen_item8_price_value = StringVar()
        self.kitchen_item8_price_value.set("Select the Price")
        self.kitchen_item8_price = OptionMenu(
            self.item_detail_desc, self.kitchen_item8_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=8, column=2, padx=3, pady=4, sticky="ew")

        self.kitchen_item8_quantity_value = StringVar()
        self.kitchen_item8_quantity_value.set("0")
        self.kitchen_item8_quantity = Entry(self.item_detail_desc, textvariable=self.kitchen_item8_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=8, column=3, padx=3, pady=4)

        self.kitchen_item8_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.kitchenconfirm_8).grid(row=8, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -9 ]=============================================================
        self.kitchen_item9 = Label(self.item_detail_desc, text="Cooking Pots", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=9, column=0, padx=3, pady=4)

        self.kitchen_item9_company_value = StringVar()
        self.kitchen_item9_company_value.set("Select the company")
        self.kitchen_item9_company = OptionMenu(self.item_detail_desc, self.kitchen_item9_company_value, "Bajaj", "Usha", "Prestige", "LG").grid(
            row=9, column=1, padx=3, pady=4, sticky="ew")

        self.kitchen_item9_price_value = StringVar()
        self.kitchen_item9_price_value.set("Select the Price")
        self.kitchen_item9_price = OptionMenu(
            self.item_detail_desc, self.kitchen_item9_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=9, column=2, padx=3, pady=4, sticky="ew")

        self.kitchen_item9_quantity_value = StringVar()
        self.kitchen_item9_quantity_value.set("0")
        self.kitchen_item9_quantity = Entry(self.item_detail_desc, textvariable=self.kitchen_item9_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=9, column=3, padx=3, pady=4)

        self.kitchen_item9_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.kitchenconfirm_9).grid(row=9, column=4, padx=3, pady=2, columnspan=2)


# ===================================================================[ item -10 ]=============================================================
        self.kitchen_item10 = Label(self.item_detail_desc, text="Juicer", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=10, column=0, padx=3, pady=4)

        self.kitchen_item10_company_value = StringVar()
        self.kitchen_item10_company_value.set("Select the company")
        self.kitchen_item10_company = OptionMenu(self.item_detail_desc, self.kitchen_item10_company_value, "Bajaj", "Usha", "Prestige", "LG").grid(
            row=10, column=1, padx=3, pady=4, sticky="ew")

        self.kitchen_item10_price_value = StringVar()
        self.kitchen_item10_price_value.set("Select the Price")
        self.kitchen_item10_price = OptionMenu(
            self.item_detail_desc, self.kitchen_item10_price_value, "250", "500", "800", "1000", "3000", "5000").grid(row=10, column=2, padx=3, pady=4, sticky="ew")

        self.kitchen_item10_quantity_value = StringVar()
        self.kitchen_item10_quantity_value.set("0")
        self.kitchen_item10_quantity = Entry(self.item_detail_desc, textvariable=self.kitchen_item10_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=10, column=3, padx=3, pady=4)

        self.kitchen_item10_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.kitchenconfirm_10).grid(row=10, column=4, padx=3, pady=2, columnspan=2)

# ===========================================================================================================================================

    def electronics(self):
        self.itemlabel5 = Label(self.item_detail_desc, text="Items", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=0, padx=3, pady=4)

        self.companylabel2 = Label(self.item_detail_desc, text="Company", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=1, padx=3, pady=4)

        self.pricelabel5 = Label(self.item_detail_desc, text="Price", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=2, padx=3, pady=4)

        self.quantitylabel5 = Label(self.item_detail_desc, text="Quantity", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=3, padx=3, pady=4)

        self.confirmlabel5 = Label(self.item_detail_desc, text="Confirmation", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=28, bd=10, relief=RAISED).grid(row=0, column=4, padx=3, pady=4, columnspan=2)


# ===================================================================[ item -1 ]=============================================================
        self.electronic_item1 = Label(self.item_detail_desc, text="Refrigerators", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=1, column=0, padx=3, pady=4)

        self.electronic_item1_company_value = StringVar()
        self.electronic_item1_company_value.set("Select the company")
        self.electronic_item1_company = OptionMenu(self.item_detail_desc, self.electronic_item1_company_value, "Samsung", "Whirpool", "Haier", "LG").grid(
            row=1, column=1, padx=3, pady=4, sticky="ew")

        self.electronic_item1_price_value = StringVar()
        self.electronic_item1_price_value.set("Select the Price")
        self.electronic_item1_price = OptionMenu(
            self.item_detail_desc, self.electronic_item1_price_value, "8000", "10000", "12000", "15000", "20000", "25000", "50000").grid(row=1, column=2, padx=3, pady=4, sticky="ew")

        self.electronic_item1_quantity_value = StringVar()
        self.electronic_item1_quantity_value.set("0")
        self.electronic_item1_quantity = Entry(self.item_detail_desc, textvariable=self.electronic_item1_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=1, column=3, padx=3, pady=4)

        self.electronic_item1_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.electronicsconfirm_1).grid(row=1, column=4, padx=3, pady=2, columnspan=2)

# ===================================================================[ item -2 ]=============================================================
        self.electronic_item2 = Label(self.item_detail_desc, text="Television", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=2, column=0, padx=3, pady=4)

        self.electronic_item2_company_value = StringVar()
        self.electronic_item2_company_value.set("Select the company")
        self.electronic_item2_company = OptionMenu(self.item_detail_desc, self.electronic_item2_company_value, "LG", "Samsung", "Sony", "Panasonic").grid(
            row=2, column=1, padx=3, pady=4, sticky="ew")

        self.electronic_item2_price_value = StringVar()
        self.electronic_item2_price_value.set("Select the Price")
        self.electronic_item2_price = OptionMenu(
            self.item_detail_desc, self.electronic_item2_price_value, "8000", "10000", "12000", "15000", "20000", "25000", "50000").grid(row=2, column=2, padx=3, pady=4, sticky="ew")

        self.electronic_item2_quantity_value = StringVar()
        self.electronic_item2_quantity_value.set("0")
        self.electronic_item2_quantity = Entry(self.item_detail_desc, textvariable=self.electronic_item2_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=2, column=3, padx=3, pady=4)

        self.electronic_item2_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.electronicsconfirm_2).grid(row=2, column=4, padx=3, pady=2, columnspan=2)

# ===================================================================[ item -3]=============================================================
        self.electronic_item3 = Label(self.item_detail_desc, text="Air Cooler", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=3, column=0, padx=3, pady=4)

        self.electronic_item3_company_value = StringVar()
        self.electronic_item3_company_value.set("Select the company")
        self.electronic_item3_company = OptionMenu(self.item_detail_desc, self.electronic_item3_company_value, "Samsung", "Whirpool", "Voltas", "LG").grid(
            row=3, column=1, padx=3, pady=4, sticky="ew")

        self.electronic_item3_price_value = StringVar()
        self.electronic_item3_price_value.set("Select the Price")
        self.electronic_item3_price = OptionMenu(
            self.item_detail_desc, self.electronic_item3_price_value, "8000", "10000", "12000", "15000", "20000", "25000", "50000").grid(row=3, column=2, padx=3, pady=4, sticky="ew")

        self.electronic_item3_quantity_value = StringVar()
        self.electronic_item3_quantity_value.set("0")
        self.electronic_item3_quantity = Entry(self.item_detail_desc, textvariable=self.electronic_item3_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=3, column=3, padx=3, pady=4)

        self.electronic_item3_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.electronicsconfirm_3).grid(row=3, column=4, padx=3, pady=2, columnspan=2)

# ===================================================================[ item -4 ]=============================================================
        self.electronic_item4 = Label(self.item_detail_desc, text="Air Conditioners", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=4, column=0, padx=3, pady=4)

        self.electronic_item4_company_value = StringVar()
        self.electronic_item4_company_value.set("Select the company")
        self.electronic_item4_company = OptionMenu(self.item_detail_desc, self.electronic_item4_company_value, "Samsung", "Whirpool", "Voltas", "LG").grid(
            row=4, column=1, padx=3, pady=4, sticky="ew")

        self.electronic_item4_price_value = StringVar()
        self.electronic_item4_price_value.set("Select the Price")
        self.electronic_item4_price = OptionMenu(
            self.item_detail_desc, self.electronic_item4_price_value, "8000", "10000", "12000", "15000", "20000", "25000", "50000").grid(row=4, column=2, padx=3, pady=4, sticky="ew")

        self.electronic_item4_quantity_value = StringVar()
        self.electronic_item4_quantity_value.set("0")
        self.electronic_item4_quantity = Entry(self.item_detail_desc, textvariable=self.electronic_item4_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=4, column=3, padx=3, pady=4)

        self.electronic_item4_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.electronicsconfirm_4).grid(row=4, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -5 ]=============================================================
        self.electronic_item5 = Label(self.item_detail_desc, text="Washing Machine", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=5, column=0, padx=3, pady=4)

        self.electronic_item5_company_value = StringVar()
        self.electronic_item5_company_value.set("Select the company")
        self.electronic_item5_company = OptionMenu(self.item_detail_desc, self.electronic_item5_company_value, "Samsung", "Whirpool", "Voltas", "LG").grid(
            row=5, column=1, padx=3, pady=4, sticky="ew")

        self.electronic_item5_price_value = StringVar()
        self.electronic_item5_price_value.set("Select the Price")
        self.electronic_item5_price = OptionMenu(
            self.item_detail_desc, self.electronic_item5_price_value, "8000", "10000", "12000", "15000", "20000", "25000", "50000").grid(row=5, column=2, padx=3, pady=4, sticky="ew")

        self.electronic_item5_quantity_value = StringVar()
        self.electronic_item5_quantity_value.set("0")
        self.electronic_item5_quantity = Entry(self.item_detail_desc, textvariable=self.electronic_item5_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=5, column=3, padx=3, pady=4)

        self.electronic_item5_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.electronicsconfirm_5).grid(row=5, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -6 ]=============================================================
        self.electronic_item6 = Label(self.item_detail_desc, text="Laptops", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=6, column=0, padx=3, pady=4)

        self.electronic_item6_company_value = StringVar()
        self.electronic_item6_company_value.set("Select the company")
        self.electronic_item6_company = OptionMenu(self.item_detail_desc, self.electronic_item6_company_value, "Dell", "HP", "Lenovo", "Asus", "Apple").grid(
            row=6, column=1, padx=3, pady=4, sticky="ew")

        self.electronic_item6_price_value = StringVar()
        self.electronic_item6_price_value.set("Select the Price")
        self.electronic_item6_price = OptionMenu(
            self.item_detail_desc, self.electronic_item6_price_value, "30000", "35000", "40000", "45000", "50000", "55000", "60000", "65000", "70000", "80000", "90000", "1000000").grid(row=6, column=2, padx=3, pady=4, sticky="ew")

        self.electronic_item6_quantity_value = StringVar()
        self.electronic_item6_quantity_value.set("0")
        self.electronic_item6_quantity = Entry(self.item_detail_desc, textvariable=self.electronic_item6_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=6, column=3, padx=3, pady=4)

        self.electronic_item6_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.electronicsconfirm_6).grid(row=6, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -7 ]=============================================================
        self.electronic_item7 = Label(self.item_detail_desc, text="Smart Phones", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=7, column=0, padx=3, pady=4)

        self.electronic_item7_company_value = StringVar()
        self.electronic_item7_company_value.set("Select the company")
        self.electronic_item7_company = OptionMenu(self.item_detail_desc, self.electronic_item7_company_value, "Samsung", "Oppo", "Vivo", "Motorola", "Apple", "One Plus").grid(
            row=7, column=1, padx=3, pady=4, sticky="ew")

        self.electronic_item7_price_value = StringVar()
        self.electronic_item7_price_value.set("Select the Price")
        self.electronic_item7_price = OptionMenu(
            self.item_detail_desc, self.electronic_item7_price_value, "10000", "15000", "18000", "21000", "27000", "30000", "35000", "40000", "45000", "50000", "55000", "60000", "65000", "70000", "80000", "90000", "1000000").grid(row=7, column=2, padx=3, pady=4, sticky="ew")

        self.electronic_item7_quantity_value = StringVar()
        self.electronic_item7_quantity_value.set("0")
        self.electronic_item7_quantity = Entry(self.item_detail_desc, textvariable=self.electronic_item7_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=7, column=3, padx=3, pady=4)

        self.electronic_item7_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.electronicsconfirm_7).grid(row=7, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -8 ]=============================================================
        self.electronic_item8 = Label(self.item_detail_desc, text="Desktop Sets", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=8, column=0, padx=3, pady=4)

        self.electronic_item8_company_value = StringVar()
        self.electronic_item8_company_value.set("Select the company")
        self.electronic_item8_company = OptionMenu(self.item_detail_desc, self.electronic_item8_company_value, "Dell", "HP", "HCL", "Acer").grid(
            row=8, column=1, padx=3, pady=4, sticky="ew")

        self.electronic_item8_price_value = StringVar()
        self.electronic_item8_price_value.set("Select the Price")
        self.electronic_item8_price = OptionMenu(
            self.item_detail_desc, self.electronic_item8_price_value, "30000", "35000", "40000", "45000", "50000", "55000", "60000", "70000").grid(row=8, column=2, padx=3, pady=4, sticky="ew")

        self.electronic_item8_quantity_value = StringVar()
        self.electronic_item8_quantity_value.set("0")
        self.electronic_item8_quantity = Entry(self.item_detail_desc, textvariable=self.electronic_item8_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=8, column=3, padx=3, pady=4)

        self.electronic_item8_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.electronicsconfirm_8).grid(row=8, column=4, padx=3, pady=2, columnspan=2)
        # ===================================================================[ item -9 ]=============================================================
        self.electronic_item9 = Label(self.item_detail_desc, text="Fans", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=9, column=0, padx=3, pady=4)

        self.electronic_item9_company_value = StringVar()
        self.electronic_item9_company_value.set("Select the company")
        self.electronic_item9_company = OptionMenu(self.item_detail_desc, self.electronic_item9_company_value, "Usha", "Orient", "Bajaj", "Havells").grid(
            row=9, column=1, padx=3, pady=4, sticky="ew")

        self.electronic_item9_price_value = StringVar()
        self.electronic_item9_price_value.set("Select the Price")
        self.electronic_item9_price = OptionMenu(
            self.item_detail_desc, self.electronic_item9_price_value, "1000", "2000", "2500", "3000", "3500", "4000", "4500", "5000").grid(row=9, column=2, padx=3, pady=4, sticky="ew")

        self.electronic_item9_quantity_value = StringVar()
        self.electronic_item9_quantity_value.set("0")
        self.electronic_item9_quantity = Entry(self.item_detail_desc, textvariable=self.electronic_item9_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=9, column=3, padx=3, pady=4)

        self.electronic_item9_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.electronicsconfirm_9).grid(row=9, column=4, padx=3, pady=2, columnspan=2)
# ===================================================================[ item -10 ]=============================================================
        self.electronic_item10 = Label(self.item_detail_desc, text="Printers", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=10, column=0, padx=3, pady=4)

        self.electronic_item10_company_value = StringVar()
        self.electronic_item10_company_value.set("Select the company")
        self.electronic_item10_company = OptionMenu(self.item_detail_desc, self.electronic_item10_company_value, "HP", "Canon", "Epson", "Panasonic").grid(
            row=10, column=1, padx=3, pady=4, sticky="ew")

        self.electronic_item10_price_value = StringVar()
        self.electronic_item10_price_value.set("Select the Price")
        self.electronic_item10_price = OptionMenu(
            self.item_detail_desc, self.electronic_item10_price_value, "30000", "35000", "40000", "45000", "50000", "55000", "60000", "70000", "75000", "80000").grid(row=10, column=2, padx=3, pady=4, sticky="ew")

        self.electronic_item10_quantity_value = StringVar()
        self.electronic_item10_quantity_value.set("0")
        self.electronic_item10_quantity = Entry(self.item_detail_desc, textvariable=self.electronic_item10_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=10, column=3, padx=3, pady=4)

        self.electronic_item10_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.electronicsconfirm_10).grid(row=10, column=4, padx=3, pady=2, columnspan=2)
# ===========================================================================================================================================

    def stationary(self):
        self.itemlabel6 = Label(self.item_detail_desc, text="Items", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=0, padx=3, pady=4)

        self.companylabel3 = Label(self.item_detail_desc, text="Company", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=1, padx=3, pady=4)

        self.pricelabel6 = Label(self.item_detail_desc, text="Price", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=2, padx=3, pady=4)

        self.quantitylabel6 = Label(self.item_detail_desc, text="Quantity", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=12, bd=10, relief=RAISED).grid(row=0, column=3, padx=3, pady=4)

        self.confirmlabel6 = Label(self.item_detail_desc, text="Confirmation", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor3, fg="darkred", height=1, width=28, bd=10, relief=RAISED).grid(row=0, column=4, padx=3, pady=4, columnspan=2)


# ===================================================================[ item -1 ]=============================================================
        self.stationary_item1 = Label(self.item_detail_desc, text="Notebooks", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=1, column=0, padx=3, pady=4)

        self.stationary_item1_company_value = StringVar()
        self.stationary_item1_company_value.set("Select the company")
        self.stationary_item1_company = OptionMenu(self.item_detail_desc, self.stationary_item1_company_value, "Classmate", "Universal Impex", "Papermint", "Spectras").grid(
            row=1, column=1, padx=3, pady=4, sticky="ew")

        self.stationary_item1_price_value = StringVar()
        self.stationary_item1_price_value.set("Select the Price")
        self.stationary_item1_price = OptionMenu(
            self.item_detail_desc, self.stationary_item1_price_value, "50", "80", "100", "150", "250", "300").grid(row=1, column=2, padx=3, pady=4, sticky="ew")

        self.stationary_item1_quantity_value = StringVar()
        self.stationary_item1_quantity_value.set("0")
        self.stationary_item1_quantity = Entry(self.item_detail_desc, textvariable=self.stationary_item1_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=1, column=3, padx=3, pady=4)

        self.stationary_item1_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.stationaryconfirm_1).grid(row=1, column=4, padx=3, pady=2, columnspan=2)

# ===================================================================[ item -2 ]=============================================================
        self.stationary_item2 = Label(self.item_detail_desc, text="Pencils", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=2, column=0, padx=3, pady=4)

        self.stationary_item2_company_value = StringVar()
        self.stationary_item2_company_value.set("Select the company")
        self.stationary_item2_company = OptionMenu(self.item_detail_desc, self.stationary_item2_company_value, "Nataraj", "Apsara", "FunFun", "Classmate").grid(
            row=2, column=1, padx=3, pady=4, sticky="ew")

        self.stationary_item2_price_value = StringVar()
        self.stationary_item2_price_value.set("Select the Price")
        self.stationary_item2_price = OptionMenu(
            self.item_detail_desc, self.stationary_item2_price_value, "50", "70", "80", "100").grid(row=2, column=2, padx=3, pady=4, sticky="ew")

        self.stationary_item2_quantity_value = StringVar()
        self.stationary_item2_quantity_value.set("0")
        self.stationary_item2_quantity = Entry(self.item_detail_desc, textvariable=self.stationary_item2_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=2, column=3, padx=3, pady=4)

        self.stationary_item2_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.stationaryconfirm_2).grid(row=2, column=4, padx=3, pady=2, columnspan=2)


# ===================================================================[ item -3]=============================================================
        self.stationary_item3 = Label(self.item_detail_desc, text="Pens", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=3, column=0, padx=3, pady=4)

        self.stationary_item3_company_value = StringVar()
        self.stationary_item3_company_value.set("Select the company")
        self.stationary_item3_company = OptionMenu(self.item_detail_desc, self.stationary_item3_company_value, "Flair", "Link Smart", "Parker", "Cello").grid(
            row=3, column=1, padx=3, pady=4, sticky="ew")

        self.stationary_item3_price_value = StringVar()
        self.stationary_item3_price_value.set("Select the Price")
        self.stationary_item3_price = OptionMenu(
            self.item_detail_desc, self.stationary_item3_price_value, "10", "20", "50", "100", "500").grid(row=3, column=2, padx=3, pady=4, sticky="ew")

        self.stationary_item3_quantity_value = StringVar()
        self.stationary_item3_quantity_value.set("0")
        self.stationary_item3_quantity = Entry(self.item_detail_desc, textvariable=self.stationary_item3_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=3, column=3, padx=3, pady=4)

        self.stationary_item3_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.stationaryconfirm_3).grid(row=3, column=4, padx=3, pady=2, columnspan=2)


# ===================================================================[ item -4 ]=============================================================
        self.stationary_item4 = Label(self.item_detail_desc, text="Files", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=4, column=0, padx=3, pady=4)

        self.stationary_item4_company_value = StringVar()
        self.stationary_item4_company_value.set("Select the company")
        self.stationary_item4_company = OptionMenu(self.item_detail_desc, self.stationary_item4_company_value, "Ambassador", "Neelkamal", "Cobra").grid(
            row=4, column=1, padx=3, pady=4, sticky="ew")

        self.stationary_item4_price_value = StringVar()
        self.stationary_item4_price_value.set("Select the Price")
        self.stationary_item4_price = OptionMenu(
            self.item_detail_desc, self.stationary_item4_price_value, "50", "100", "150", "200").grid(row=4, column=2, padx=3, pady=4, sticky="ew")

        self.stationary_item4_quantity_value = StringVar()
        self.stationary_item4_quantity_value.set("0")
        self.stationary_item4_quantity = Entry(self.item_detail_desc, textvariable=self.stationary_item4_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=4, column=3, padx=3, pady=4)

        self.stationary_item4_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.stationaryconfirm_4).grid(row=4, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -5 ]=============================================================
        self.stationary_item5 = Label(self.item_detail_desc, text="Colors Sets", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=5, column=0, padx=3, pady=4)

        self.stationary_item5_company_value = StringVar()
        self.stationary_item5_company_value.set("Select the company")
        self.stationary_item5_company = OptionMenu(self.item_detail_desc, self.stationary_item5_company_value, "Camelin", "Classmate", "FunFun").grid(
            row=5, column=1, padx=3, pady=4, sticky="ew")

        self.stationary_item5_price_value = StringVar()
        self.stationary_item5_price_value.set("Select the Price")
        self.stationary_item5_price = OptionMenu(
            self.item_detail_desc, self.stationary_item5_price_value, "50", "80", "100", "150").grid(row=5, column=2, padx=3, pady=4, sticky="ew")

        self.stationary_item5_quantity_value = StringVar()
        self.stationary_item5_quantity_value.set("0")
        self.stationary_item5_quantity = Entry(self.item_detail_desc, textvariable=self.stationary_item5_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=5, column=3, padx=3, pady=4)

        self.stationary_item5_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.stationaryconfirm_5).grid(row=5, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -6 ]=============================================================
        self.stationary_item6 = Label(self.item_detail_desc, text="Geometry Boxes", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=6, column=0, padx=3, pady=4)

        self.stationary_item6_company_value = StringVar()
        self.stationary_item6_company_value.set("Select the company")
        self.stationary_item6_company = OptionMenu(self.item_detail_desc, self.stationary_item6_company_value, "FunFun", "Classmate", "Discovery", "Camel").grid(
            row=6, column=1, padx=3, pady=4, sticky="ew")

        self.stationary_item6_price_value = StringVar()
        self.stationary_item6_price_value.set("Select the Price")
        self.stationary_item6_price = OptionMenu(
            self.item_detail_desc, self.stationary_item6_price_value, "50", "100", "150", "200").grid(row=6, column=2, padx=3, pady=4, sticky="ew")

        self.stationary_item6_quantity_value = StringVar()
        self.stationary_item6_quantity_value.set("0")
        self.stationary_item6_quantity = Entry(self.item_detail_desc, textvariable=self.stationary_item6_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=6, column=3, padx=3, pady=4)

        self.stationary_item6_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.stationaryconfirm_6).grid(row=6, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -7 ]=============================================================
        self.stationary_item7 = Label(self.item_detail_desc, text="Printer Pages", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=7, column=0, padx=3, pady=4)

        self.stationary_item7_company_value = StringVar()
        self.stationary_item7_company_value.set("Select the company")
        self.stationary_item7_company = OptionMenu(self.item_detail_desc, self.stationary_item7_company_value, "Century", "TNPL", "Bill Matrix", "J.K Copies").grid(
            row=7, column=1, padx=3, pady=4, sticky="ew")

        self.stationary_item7_price_value = StringVar()
        self.stationary_item7_price_value.set("Select the Price")
        self.stationary_item7_price = OptionMenu(
            self.item_detail_desc, self.stationary_item7_price_value, "150", "200", "250", "300").grid(row=7, column=2, padx=3, pady=4, sticky="ew")

        self.stationary_item7_quantity_value = StringVar()
        self.stationary_item7_quantity_value.set("0")
        self.stationary_item7_quantity = Entry(self.item_detail_desc, textvariable=self.stationary_item7_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=7, column=3, padx=3, pady=4)

        self.stationary_item7_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.stationaryconfirm_7).grid(row=7, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -8 ]=============================================================
        self.stationary_item8 = Label(self.item_detail_desc, text="Calculators", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=8, column=0, padx=3, pady=4)

        self.stationary_item8_company_value = StringVar()
        self.stationary_item8_company_value.set("Select the company")
        self.stationary_item8_company = OptionMenu(self.item_detail_desc, self.stationary_item8_company_value, "Casio", "Citizen", "Orapt", "Flair").grid(
            row=8, column=1, padx=3, pady=4, sticky="ew")

        self.stationary_item8_price_value = StringVar()
        self.stationary_item8_price_value.set("Select the Price")
        self.stationary_item8_price = OptionMenu(
            self.item_detail_desc, self.stationary_item8_price_value, "250", "500", "900", "1200", "1500").grid(row=8, column=2, padx=3, pady=4, sticky="ew")

        self.stationary_item8_quantity_value = StringVar()
        self.stationary_item8_quantity_value.set("0")
        self.stationary_item8_quantity = Entry(self.item_detail_desc, textvariable=self.stationary_item8_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=8, column=3, padx=3, pady=4)

        self.stationary_item8_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.stationaryconfirm_8).grid(row=8, column=4, padx=3, pady=2, columnspan=2)

        # ===================================================================[ item -9 ]=============================================================
        self.stationary_item9 = Label(self.item_detail_desc, text="Printer Cartrages", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=9, column=0, padx=3, pady=4)

        self.stationary_item9_company_value = StringVar()
        self.stationary_item9_company_value.set("Select the company")
        self.stationary_item9_company = OptionMenu(self.item_detail_desc, self.stationary_item9_company_value, "Sony", "HP", "Canon", "Epson").grid(
            row=9, column=1, padx=3, pady=4, sticky="ew")

        self.stationary_item9_price_value = StringVar()
        self.stationary_item9_price_value.set("Select the Price")
        self.stationary_item9_price = OptionMenu(
            self.item_detail_desc, self.stationary_item9_price_value, "5000", "7000", "10000", "15000", "20000").grid(row=9, column=2, padx=3, pady=4, sticky="ew")

        self.stationary_item9_quantity_value = StringVar()
        self.stationary_item9_quantity_value.set("0")
        self.stationary_item9_quantity = Entry(self.item_detail_desc, textvariable=self.stationary_item9_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=9, column=3, padx=3, pady=4)

        self.stationary_item9_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.stationaryconfirm_9).grid(row=9, column=4, padx=3, pady=2, columnspan=2)


# ===================================================================[ item -10 ]=============================================================
        self.stationary_item10 = Label(self.item_detail_desc, text="Marker Pens", font=(
            "Aparajita", 15, "bold"), bg=self.bgcolor, fg="white", height=1, bd=0, width=12, relief=GROOVE).grid(row=10, column=0, padx=3, pady=4)

        self.stationary_item10_company_value = StringVar()
        self.stationary_item10_company_value.set("Select the company")
        self.stationary_item10_company = OptionMenu(self.item_detail_desc, self.stationary_item10_company_value, "Camlin", "Link Smart", "Cello", "Flora").grid(
            row=10, column=1, padx=3, pady=4, sticky="ew")

        self.stationary_item10_price_value = StringVar()
        self.stationary_item10_price_value.set("Select the Price")
        self.stationary_item10_price = OptionMenu(
            self.item_detail_desc, self.stationary_item10_price_value, "20", "50", "70", "90", "100").grid(row=10, column=2, padx=3, pady=4, sticky="ew")

        self.stationary_item10_quantity_value = StringVar()
        self.stationary_item10_quantity_value.set("0")
        self.stationary_item10_quantity = Entry(self.item_detail_desc, textvariable=self.stationary_item10_quantity_value, font=(
            "Aparajita", 15, "bold"), width=17, bd=3).grid(row=10, column=3, padx=3, pady=4)

        self.stationary_item10_confirmation = Button(self.item_detail_desc, text="Confirm", font=(
            "Aparajita", 15, "bold"), width=29, bd=2, relief=RAISED, command=self.stationaryconfirm_10).grid(row=10, column=4, padx=3, pady=2, columnspan=2)


# ===========================================================================================================================================
# =========================================[ wholeseller name and contact number ]======================================================


    def WholeSellerContact(self, whole_seller_contact_list):
        if self.clicked_wholeseller_contact.get() == self.whole_seller_contact_list[0]:
            self.ws_contact.set("7854123458")
        elif self.clicked_wholeseller_contact.get() == self.whole_seller_contact_list[1]:
            self.ws_contact.set("5478954364")
        elif self.clicked_wholeseller_contact.get() == self.whole_seller_contact_list[2]:
            self.ws_contact.set("4521357894")
        elif self.clicked_wholeseller_contact.get() == self.whole_seller_contact_list[3]:
            self.ws_contact.set("8456214789")
        elif self.clicked_wholeseller_contact.get() == self.whole_seller_contact_list[4]:
            self.ws_contact.set("9875612548")
        elif self.clicked_wholeseller_contact.get() == self.whole_seller_contact_list[5]:
            self.ws_contact.set("3451278956")

    def WholeSellerName(self, whole_seller_option_list):
        if self.clicked_wholeseller_name.get() == self.whole_seller_option_list[0]:
            self.wsname.set(self.whole_seller_option_list[0])
        elif self.clicked_wholeseller_name.get() == self.whole_seller_option_list[1]:
            self.wsname.set(self.whole_seller_option_list[1])
        elif self.clicked_wholeseller_name.get() == self.whole_seller_option_list[2]:
            self.wsname.set(self.whole_seller_option_list[2])
        elif self.clicked_wholeseller_name.get() == self.whole_seller_option_list[3]:
            self.wsname.set(self.whole_seller_option_list[3])
        elif self.clicked_wholeseller_name.get() == self.whole_seller_option_list[4]:
            self.wsname.set(self.whole_seller_option_list[4])
        elif self.clicked_wholeseller_name.get() == self.whole_seller_option_list[5]:
            self.wsname.set(self.whole_seller_option_list[5])


# ===========================================================================================================================================
# =========================================[ confirm button functioning]======================================================


    def bbconfirm_1(self):
        if self.bb_1_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_bb = self.partial_bb + \
                    int(int(self.bb_item1_price_value.get()) *
                        int(self.bb_item1_quantity_value.get()))
                self.total_bb.set(self.partial_bb)
                self.total_final_sum = self.partial_bb
                count = count+1
            self.bb_1_confirm_bool = True

        return

    def bbconfirm_2(self):
        if self.bb_2_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_bb = self.partial_bb + \
                    int(int(self.bb_item2_price_value.get()) *
                        int(self.bb_item2_quantity_value.get()))
                self.total_bb.set(self.partial_bb)
                self.total_final_sum = self.partial_bb
                count = count+1
            self.bb_2_confirm_bool = True

    def bbconfirm_3(self):
        if self.bb_3_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_bb = self.partial_bb + \
                    int(int(self.bb_item3_price_value.get()) *
                        int(self.bb_item3_quantity_value.get()))
                self.total_bb.set(self.partial_bb)
                self.total_final_sum = self.partial_bb
                count = count+1
            self.bb_3_confirm_bool = True

    def bbconfirm_4(self):
        if self.bb_4_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_bb = self.partial_bb + \
                    int(int(self.bb_item4_price_value.get()) *
                        int(self.bb_item4_quantity_value.get()))
                self.total_bb.set(self.partial_bb)
                self.total_final_sum = self.partial_bb
                count = count+1
            self.bb_4_confirm_bool = True

    def bbconfirm_5(self):
        if self.bb_5_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_bb = self.partial_bb + \
                    int(int(self.bb_item5_price_value.get()) *
                        int(self.bb_item5_quantity_value.get()))
                self.total_bb.set(self.partial_bb)
                self.total_final_sum = self.partial_bb
                count = count+1
            self.bb_5_confirm_bool = True

    def bbconfirm_6(self):
        if self.bb_6_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_bb = self.partial_bb + \
                    int(int(self.bb_item6_price_value.get()) *
                        int(self.bb_item6_quantity_value.get()))
                self.total_bb.set(self.partial_bb)
                self.total_final_sum = self.partial_bb
                count = count+1
            self.bb_6_confirm_bool = True

    def bbconfirm_7(self):
        if self.bb_7_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_bb = self.partial_bb + \
                    int(int(self.bb_item7_price_value.get()) *
                        int(self.bb_item7_quantity_value.get()))
                self.total_bb.set(self.partial_bb)
                self.total_final_sum = self.partial_bb
                count = count+1
            self.bb_7_confirm_bool = True

    def bbconfirm_8(self):
        if self.bb_8_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_bb = self.partial_bb + \
                    int(int(self.bb_item8_price_value.get()) *
                        int(self.bb_item8_quantity_value.get()))
                self.total_bb.set(self.partial_bb)
                self.total_final_sum = self.partial_bb
                count = count+1
            self.bb_8_confirm_bool = True

    def bbconfirm_9(self):
        if self.bb_9_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_bb = self.partial_bb + \
                    int(int(self.bb_item9_price_value.get()) *
                        int(self.bb_item9_quantity_value.get()))
                self.total_bb.set(self.partial_bb)
                self.total_final_sum = self.partial_bb
                count = count+1
            self.bb_9_confirm_bool = True

    def bbconfirm_10(self):
        if self.bb_10_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_bb = self.partial_bb + \
                    int(int(self.bb_item10_price_value.get()) *
                        int(self.bb_item10_quantity_value.get()))
                self.total_bb.set(self.partial_bb)
                self.total_final_sum = self.partial_bb
                count = count+1
            self.bb_10_confirm_bool = True

    def menswearconfirm_1(self):
        if self.mw_1_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_mw = self.partial_mw + \
                    int(int(self.mens_item1_price_value.get()) *
                        int(self.mens_item1_quantity_value.get()))
                self.total_mw.set(self.partial_mw)
                self.total_final_sum = self.partial_mw
                count = count+1
            self.mw_1_confirm_bool = True

        return

    def menswearconfirm_2(self):
        if self.mw_2_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_mw = self.partial_mw + \
                    int(int(self.mens_item2_price_value.get()) *
                        int(self.mens_item2_quantity_value.get()))
                self.total_mw.set(self.partial_mw)
                self.total_final_sum = self.partial_mw
                count = count+1
            self.mw_2_confirm_bool = True

        return

    def menswearconfirm_3(self):
        if self.mw_3_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_mw = self.partial_mw + \
                    int(int(self.mens_item3_price_value.get()) *
                        int(self.mens_item3_quantity_value.get()))
                self.total_mw.set(self.partial_mw)
                self.total_final_sum = self.partial_mw
                count = count+1
            self.mw_3_confirm_bool = True

        return

    def menswearconfirm_4(self):
        if self.mw_4_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_mw = self.partial_mw + \
                    int(int(self.mens_item4_price_value.get()) *
                        int(self.mens_item4_quantity_value.get()))
                self.total_mw.set(self.partial_mw)
                self.total_final_sum = self.partial_mw
                count = count+1
            self.mw_4_confirm_bool = True

        return

    def menswearconfirm_5(self):
        if self.mw_5_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_mw = self.partial_mw + \
                    int(int(self.mens_item5_price_value.get()) *
                        int(self.mens_item5_quantity_value.get()))
                self.total_mw.set(self.partial_mw)
                self.total_final_sum = self.partial_mw
                count = count+1
            self.mw_5_confirm_bool = True

        return

    def menswearconfirm_6(self):
        if self.mw_6_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_mw = self.partial_mw + \
                    int(int(self.mens_item6_price_value.get()) *
                        int(self.mens_item6_quantity_value.get()))
                self.total_mw.set(self.partial_mw)
                self.total_final_sum = self.partial_mw
                count = count+1
            self.mw_6_confirm_bool = True

        return

    def menswearconfirm_7(self):
        if self.mw_7_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_mw = self.partial_mw + \
                    int(int(self.mens_item7_price_value.get()) *
                        int(self.mens_item7_quantity_value.get()))
                self.total_mw.set(self.partial_mw)
                self.total_final_sum = self.partial_mw
                count = count+1
            self.mw_7_confirm_bool = True

        return

    def menswearconfirm_8(self):
        if self.mw_8_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_mw = self.partial_mw + \
                    int(int(self.mens_item8_price_value.get()) *
                        int(self.mens_item8_quantity_value.get()))
                self.total_mw.set(self.partial_mw)
                self.total_final_sum = self.partial_mw
                count = count+1
            self.mw_8_confirm_bool = True

        return

    def menswearconfirm_9(self):
        if self.mw_9_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_mw = self.partial_mw + \
                    int(int(self.mens_item9_price_value.get()) *
                        int(self.mens_item9_quantity_value.get()))
                self.total_mw.set(self.partial_mw)
                self.total_final_sum = self.partial_mw
                count = count+1
            self.mw_9_confirm_bool = True

        return

    def menswearconfirm_10(self):
        if self.mw_10_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_mw = self.partial_mw + \
                    int(int(self.mens_item10_price_value.get()) *
                        int(self.mens_item10_quantity_value.get()))
                self.total_mw.set(self.partial_mw)
                self.total_final_sum = self.partial_mw
                count = count+1
            self.mw_10_confirm_bool = True

        return

    def womenswearconfirm_1(self):
        if self.ww_1_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ww = self.partial_ww + \
                    int(int(self.womens_item1_price_value.get()) *
                        int(self.womens_item1_quantity_value.get()))
                self.total_ww.set(self.partial_ww)
                self.total_final_sum = self.partial_ww
                count = count+1
            self.ww_1_confirm_bool = True

        return

    def womenswearconfirm_2(self):
        if self.ww_2_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ww = self.partial_ww + \
                    int(int(self.womens_item2_price_value.get()) *
                        int(self.womens_item2_quantity_value.get()))
                self.total_ww.set(self.partial_ww)
                self.total_final_sum = self.partial_ww
                count = count+1
            self.ww_2_confirm_bool = True

        return

    def womenswearconfirm_3(self):
        if self.ww_3_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ww = self.partial_ww + \
                    int(int(self.womens_item3_price_value.get()) *
                        int(self.womens_item3_quantity_value.get()))
                self.total_ww.set(self.partial_ww)
                self.total_final_sum = self.partial_ww
                count = count+1
            self.ww_3_confirm_bool = True

        return

    def womenswearconfirm_4(self):
        if self.ww_4_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ww = self.partial_ww + \
                    int(int(self.womens_item4_price_value.get()) *
                        int(self.womens_item4_quantity_value.get()))
                self.total_ww.set(self.partial_ww)
                self.total_final_sum = self.partial_ww
                count = count+1
            self.ww_4_confirm_bool = True

        return

    def womenswearconfirm_5(self):
        if self.ww_5_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ww = self.partial_ww + \
                    int(int(self.womens_item5_price_value.get()) *
                        int(self.womens_item5_quantity_value.get()))
                self.total_ww.set(self.partial_ww)
                self.total_final_sum = self.partial_ww
                count = count+1
            self.ww_5_confirm_bool = True

        return

    def womenswearconfirm_6(self):
        if self.ww_6_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ww = self.partial_ww + \
                    int(int(self.womens_item6_price_value.get()) *
                        int(self.womens_item6_quantity_value.get()))
                self.total_ww.set(self.partial_ww)
                self.total_final_sum = self.partial_ww
                count = count+1
            self.ww_6_confirm_bool = True

        return

    def womenswearconfirm_7(self):
        if self.ww_7_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ww = self.partial_ww + \
                    int(int(self.womens_item7_price_value.get()) *
                        int(self.womens_item7_quantity_value.get()))
                self.total_ww.set(self.partial_ww)
                self.total_final_sum = self.partial_ww
                count = count+1
            self.ww_7_confirm_bool = True

        return

    def womenswearconfirm_8(self):
        if self.ww_8_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ww = self.partial_ww + \
                    int(int(self.womens_item8_price_value.get()) *
                        int(self.womens_item8_quantity_value.get()))
                self.total_ww.set(self.partial_ww)
                self.total_final_sum = self.partial_ww
                count = count+1
            self.ww_8_confirm_bool = True

        return

    def womenswearconfirm_9(self):
        if self.ww_9_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ww = self.partial_ww + \
                    int(int(self.womens_item9_price_value.get()) *
                        int(self.womens_item9_quantity_value.get()))
                self.total_ww.set(self.partial_ww)
                self.total_final_sum = self.partial_ww
                count = count+1
            self.ww_9_confirm_bool = True

        return

    def womenswearconfirm_10(self):
        if self.ww_10_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ww = self.partial_ww + \
                    int(int(self.womens_item10_price_value.get()) *
                        int(self.womens_item10_quantity_value.get()))
                self.total_ww.set(self.partial_ww)
                self.total_final_sum = self.partial_ww
                count = count+1
            self.ww_10_confirm_bool = True

        return

    def kitchenconfirm_1(self):
        if self.ku_1_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ku = self.partial_ku + \
                    int(int(self.kitchen_item1_price_value.get()) *
                        int(self.kitchen_item1_quantity_value.get()))
                self.total_ku.set(self.partial_ku)
                self.total_final_sum = self.partial_ku
                count = count+1
            self.ku_1_confirm_bool = True

        return

    def kitchenconfirm_2(self):
        if self.ku_2_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ku = self.partial_ku + \
                    int(int(self.kitchen_item2_price_value.get()) *
                        int(self.kitchen_item2_quantity_value.get()))
                self.total_ku.set(self.partial_ku)
                self.total_final_sum = self.partial_ku
                count = count+1
            self.ku_2_confirm_bool = True

        return

    def kitchenconfirm_3(self):
        if self.ku_3_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ku = self.partial_ku + \
                    int(int(self.kitchen_item3_price_value.get()) *
                        int(self.kitchen_item3_quantity_value.get()))
                self.total_ku.set(self.partial_ku)
                self.total_final_sum = self.partial_ku
                count = count+1
            self.ku_3_confirm_bool = True

        return

    def kitchenconfirm_4(self):
        if self.ku_4_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ku = self.partial_ku + \
                    int(int(self.kitchen_item4_price_value.get()) *
                        int(self.kitchen_item4_quantity_value.get()))
                self.total_ku.set(self.partial_ku)
                self.total_final_sum = self.partial_ku
                count = count+1
            self.ku_4_confirm_bool = True

        return

    def kitchenconfirm_5(self):
        if self.ku_5_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ku = self.partial_ku + \
                    int(int(self.kitchen_item5_price_value.get()) *
                        int(self.kitchen_item5_quantity_value.get()))
                self.total_ku.set(self.partial_ku)
                self.total_final_sum = self.partial_ku
                count = count+1
            self.ku_5_confirm_bool = True

        return

    def kitchenconfirm_6(self):
        if self.ku_6_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ku = self.partial_ku + \
                    int(int(self.kitchen_item6_price_value.get()) *
                        int(self.kitchen_item6_quantity_value.get()))
                self.total_ku.set(self.partial_ku)
                self.total_final_sum = self.partial_ku
                count = count+1
            self.ku_6_confirm_bool = True

        return

    def kitchenconfirm_7(self):
        if self.ku_7_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ku = self.partial_ku + \
                    int(int(self.kitchen_item7_price_value.get()) *
                        int(self.kitchen_item7_quantity_value.get()))
                self.total_ku.set(self.partial_ku)
                self.total_final_sum = self.partial_ku
                count = count+1
            self.ku_7_confirm_bool = True

        return

    def kitchenconfirm_8(self):
        if self.ku_8_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ku = self.partial_ku + \
                    int(int(self.kitchen_item8_price_value.get()) *
                        int(self.kitchen_item8_quantity_value.get()))
                self.total_ku.set(self.partial_ku)
                self.total_final_sum = self.partial_ku
                count = count+1
            self.ku_8_confirm_bool = True

        return

    def kitchenconfirm_9(self):
        if self.ku_9_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ku = self.partial_ku + \
                    int(int(self.kitchen_item9_price_value.get()) *
                        int(self.kitchen_item9_quantity_value.get()))
                self.total_ku.set(self.partial_ku)
                self.total_final_sum = self.partial_ku
                count = count+1
            self.ku_9_confirm_bool = True

        return

    def kitchenconfirm_10(self):
        if self.ku_10_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ku = self.partial_ku + \
                    int(int(self.kitchen_item10_price_value.get()) *
                        int(self.kitchen_item10_quantity_value.get()))
                self.total_ku.set(self.partial_ku)
                self.total_final_sum = self.partial_ku
                count = count+1
            self.ku_10_confirm_bool = True

        return

    def electronicsconfirm_1(self):
        if self.ele_1_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ele = self.partial_ele + \
                    int(int(self.electronic_item1_price_value.get()) *
                        int(self.electronic_item1_quantity_value.get()))
                self.total_ele.set(self.partial_ele)
                self.total_final_sum = self.partial_ele
                count = count+1
            self.ele_1_confirm_bool = True

        return

    def electronicsconfirm_2(self):
        if self.ele_2_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ele = self.partial_ele + \
                    int(int(self.electronic_item2_price_value.get()) *
                        int(self.electronic_item2_quantity_value.get()))
                self.total_ele.set(self.partial_ele)
                self.total_final_sum = self.partial_ele
                count = count+1
            self.ele_2_confirm_bool = True

        return

    def electronicsconfirm_3(self):
        if self.ele_3_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ele = self.partial_ele + \
                    int(int(self.electronic_item3_price_value.get()) *
                        int(self.electronic_item3_quantity_value.get()))
                self.total_ele.set(self.partial_ele)
                self.total_final_sum = self.partial_ele
                count = count+1
            self.ele_3_confirm_bool = True

        return

    def electronicsconfirm_4(self):
        if self.ele_4_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ele = self.partial_ele + \
                    int(int(self.electronic_item4_price_value.get()) *
                        int(self.electronic_item4_quantity_value.get()))
                self.total_ele.set(self.partial_ele)
                self.total_final_sum = self.partial_ele
                count = count+1
            self.ele_4_confirm_bool = True

        return

    def electronicsconfirm_5(self):
        if self.ele_5_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ele = self.partial_ele + \
                    int(int(self.electronic_item5_price_value.get()) *
                        int(self.electronic_item5_quantity_value.get()))
                self.total_ele.set(self.partial_ele)
                self.total_final_sum = self.partial_ele
                count = count+1
            self.ele_5_confirm_bool = True

        return

    def electronicsconfirm_6(self):
        if self.ele_6_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ele = self.partial_ele + \
                    int(int(self.electronic_item6_price_value.get()) *
                        int(self.electronic_item6_quantity_value.get()))
                self.total_ele.set(self.partial_ele)
                self.total_final_sum = self.partial_ele
                count = count+1
            self.ele_6_confirm_bool = True

        return

    def electronicsconfirm_7(self):
        if self.ele_7_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ele = self.partial_ele + \
                    int(int(self.electronic_item7_price_value.get()) *
                        int(self.electronic_item7_quantity_value.get()))
                self.total_ele.set(self.partial_ele)
                self.total_final_sum = self.partial_ele
                count = count+1
            self.ele_7_confirm_bool = True

        return

    def electronicsconfirm_8(self):
        if self.ele_8_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ele = self.partial_ele + \
                    int(int(self.electronic_item8_price_value.get()) *
                        int(self.electronic_item8_quantity_value.get()))
                self.total_ele.set(self.partial_ele)
                self.total_final_sum = self.partial_ele
                count = count+1
            self.ele_8_confirm_bool = True

        return

    def electronicsconfirm_9(self):
        if self.ele_9_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ele = self.partial_ele + \
                    int(int(self.electronic_item9_price_value.get()) *
                        int(self.electronic_item9_quantity_value.get()))
                self.total_ele.set(self.partial_ele)
                self.total_final_sum = self.partial_ele
                count = count+1
            self.ele_9_confirm_bool = True

        return

    def electronicsconfirm_10(self):
        if self.ele_10_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_ele = self.partial_ele + \
                    int(int(self.electronic_item10_price_value.get()) *
                        int(self.electronic_item10_quantity_value.get()))
                self.total_ele.set(self.partial_ele)
                self.total_final_sum = self.partial_ele
                count = count+1
            self.ele_10_confirm_bool = True

        return

    def stationaryconfirm_1(self):
        if self.stnry_1_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_stnry = self.partial_stnry + \
                    int(int(self.stationary_item1_price_value.get()) *
                        int(self.stationary_item1_quantity_value.get()))
                self.total_stnry.set(self.partial_stnry)
                self.total_final_sum = self.partial_stnry
                count = count+1
            self.stnry_1_confirm_bool = True

        return

    def stationaryconfirm_2(self):
        if self.stnry_2_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_stnry = self.partial_stnry + \
                    int(int(self.stationary_item2_price_value.get()) *
                        int(self.stationary_item2_quantity_value.get()))
                self.total_stnry.set(self.partial_stnry)
                self.total_final_sum = self.partial_stnry
                count = count+1
            self.stnry_2_confirm_bool = True

        return

    def stationaryconfirm_3(self):
        if self.stnry_3_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_stnry = self.partial_stnry + \
                    int(int(self.stationary_item3_price_value.get()) *
                        int(self.stationary_item3_quantity_value.get()))
                self.total_stnry.set(self.partial_stnry)
                self.total_final_sum = self.partial_stnry
                count = count+1
            self.stnry_3_confirm_bool = True

        return

    def stationaryconfirm_4(self):
        if self.stnry_4_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_stnry = self.partial_stnry + \
                    int(int(self.stationary_item4_price_value.get()) *
                        int(self.stationary_item4_quantity_value.get()))
                self.total_stnry.set(self.partial_stnry)
                self.total_final_sum = self.partial_stnry
                count = count+1
            self.stnry_4_confirm_bool = True

        return

    def stationaryconfirm_5(self):
        if self.stnry_5_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_stnry = self.partial_stnry + \
                    int(int(self.stationary_item5_price_value.get()) *
                        int(self.stationary_item5_quantity_value.get()))
                self.total_stnry.set(self.partial_stnry)
                self.total_final_sum = self.partial_stnry
                count = count+1
            self.stnry_5_confirm_bool = True

        return

    def stationaryconfirm_6(self):
        if self.stnry_6_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_stnry = self.partial_stnry + \
                    int(int(self.stationary_item6_price_value.get()) *
                        int(self.stationary_item6_quantity_value.get()))
                self.total_stnry.set(self.partial_stnry)
                self.total_final_sum = self.partial_stnry
                count = count+1
            self.stnry_6_confirm_bool = True

        return

    def stationaryconfirm_7(self):
        if self.stnry_7_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_stnry = self.partial_stnry + \
                    int(int(self.stationary_item7_price_value.get()) *
                        int(self.stationary_item7_quantity_value.get()))
                self.total_stnry.set(self.partial_stnry)
                self.total_final_sum = self.partial_stnry
                count = count+1
            self.stnry_7_confirm_bool = True

        return

    def stationaryconfirm_8(self):
        if self.stnry_8_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_stnry = self.partial_stnry + \
                    int(int(self.stationary_item8_price_value.get()) *
                        int(self.stationary_item8_quantity_value.get()))
                self.total_stnry.set(self.partial_stnry)
                self.total_final_sum = self.partial_stnry
                count = count+1
            self.stnry_8_confirm_bool = True

        return

    def stationaryconfirm_9(self):
        if self.stnry_9_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_stnry = self.partial_stnry + \
                    int(int(self.stationary_item9_price_value.get()) *
                        int(self.stationary_item9_quantity_value.get()))
                self.total_stnry.set(self.partial_stnry)
                self.total_final_sum = self.partial_stnry
                count = count+1
            self.stnry_9_confirm_bool = True

        return

    def stationaryconfirm_10(self):
        if self.stnry_10_confirm_bool == False:
            count = 0
            while(count < 1):
                self.partial_stnry = self.partial_stnry + \
                    int(int(self.stationary_item10_price_value.get()) *
                        int(self.stationary_item10_quantity_value.get()))
                self.total_stnry.set(self.partial_stnry)
                self.total_final_sum = self.partial_stnry
                count = count+1
            self.stnry_10_confirm_bool = True

        return

    def total_function(self):
        messagebox.showinfo(
            "Total", f"Your Total Amount is : {self.total_final_sum}")

    def clear_function(self):
        ans = messagebox.askyesno("Clear", "Do You Really Want To Clear?")
        if ans > 0:
            self.textarea.delete(1.0, END)
            self.welcome_bill()
            self.total_bb.set(0)
            self.total_mw.set(0)
            self.total_ww.set(0)
            self.total_ku.set(0)
            self.total_ele.set(0)
            self.total_stnry.set(0)
            self.total_final_sum = 0
            self.partial_bb = 0
            self.partial_mw = 0
            self.partial_ww = 0
            self.partial_ku = 0
            self.partial_ele = 0
            self.partial_stnry = 0
            self.bb_1_confirm_bool = False
            self.bb_2_confirm_bool = False
            self.bb_3_confirm_bool = False
            self.bb_4_confirm_bool = False
            self.bb_5_confirm_bool = False
            self.bb_6_confirm_bool = False
            self.bb_7_confirm_bool = False
            self.bb_8_confirm_bool = False
            self.bb_9_confirm_bool = False
            self.bb_10_confirm_bool = False
            self.mw_1_confirm_bool = False
            self.mw_2_confirm_bool = False
            self.mw_3_confirm_bool = False
            self.mw_4_confirm_bool = False
            self.mw_5_confirm_bool = False
            self.mw_6_confirm_bool = False
            self.mw_7_confirm_bool = False
            self.mw_8_confirm_bool = False
            self.mw_9_confirm_bool = False
            self.mw_10_confirm_bool = False
            self.ww_1_confirm_bool = False
            self.ww_2_confirm_bool = False
            self.ww_3_confirm_bool = False
            self.ww_4_confirm_bool = False
            self.ww_5_confirm_bool = False
            self.ww_6_confirm_bool = False
            self.ww_7_confirm_bool = False
            self.ww_8_confirm_bool = False
            self.ww_9_confirm_bool = False
            self.ww_10_confirm_bool = False
            self.ku_1_confirm_bool = False
            self.ku_2_confirm_bool = False
            self.ku_3_confirm_bool = False
            self.ku_4_confirm_bool = False
            self.ku_5_confirm_bool = False
            self.ku_6_confirm_bool = False
            self.ku_7_confirm_bool = False
            self.ku_8_confirm_bool = False
            self.ku_9_confirm_bool = False
            self.ku_10_confirm_bool = False
            self.ele_1_confirm_bool = False
            self.ele_2_confirm_bool = False
            self.ele_3_confirm_bool = False
            self.ele_4_confirm_bool = False
            self.ele_5_confirm_bool = False
            self.ele_6_confirm_bool = False
            self.ele_7_confirm_bool = False
            self.ele_8_confirm_bool = False
            self.ele_9_confirm_bool = False
            self.ele_10_confirm_bool = False
            self.stnry_1_confirm_bool = False
            self.stnry_2_confirm_bool = False
            self.stnry_3_confirm_bool = False
            self.stnry_4_confirm_bool = False
            self.stnry_5_confirm_bool = False
            self.stnry_6_confirm_bool = False
            self.stnry_7_confirm_bool = False
            self.stnry_8_confirm_bool = False
            self.stnry_9_confirm_bool = False
            self.stnry_10_confirm_bool = False
            self.bill_bb_confirm_bool = False
            self.bill_mw_confirm_bool = False
            self.bill_ww_confirm_bool = False
            self.bill_ele_confirm_bool = False
            self.bill_ku_confirm_bool = False
            self.bill_stnry_confirm_bool = False
            self.billing_address_value.set("")
            self.wholeseller_email_value.set("")
            self.payment_mode.set("Select Payment Mode")
            self.clicked_wholeseller_contact.set("Born Baby Items: 7854123458")
            self.clicked_wholeseller_name.set("Born Baby Items")
            self.wsname.set(self.whole_seller_option_list[0])
            self.ws_contact.set("7854123458")
            self.random_bill = 0

            self.bb_item1_size_value.set("Select the size")
            self.bb_item1_price_value.set("Select the Price")
            self.bb_item1_quantity_value.set("0")

            self.bb_item2_size_value.set("Select the size")
            self.bb_item2_price_value.set("Select the Price")
            self.bb_item2_quantity_value.set("0")

            self.bb_item3_size_value.set("Select the size")
            self.bb_item3_price_value.set("Select the Price")
            self.bb_item3_quantity_value.set("0")

            self.bb_item4_size_value.set("Select the size")
            self.bb_item4_price_value.set("Select the Price")
            self.bb_item4_quantity_value.set("0")

            self.bb_item5_size_value.set("Select the size")
            self.bb_item5_price_value.set("Select the Price")
            self.bb_item5_quantity_value.set("0")

            self.bb_item6_size_value.set("Select the size")
            self.bb_item6_price_value.set("Select the Price")
            self.bb_item6_quantity_value.set("0")

            self.bb_item7_size_value.set("Select the size")
            self.bb_item7_price_value.set("Select the Price")
            self.bb_item7_quantity_value.set("0")

            self.bb_item8_size_value.set("Select the size")
            self.bb_item8_price_value.set("Select the Price")
            self.bb_item8_quantity_value.set("0")

            self.bb_item9_size_value.set("Select the size")
            self.bb_item9_price_value.set("Select the Price")
            self.bb_item9_quantity_value.set("0")

            self.bb_item10_size_value.set("Select the size")
            self.bb_item10_price_value.set("Select the Price")
            self.bb_item10_quantity_value.set("0")

            if self.categories.get() == "Men's Wear":

                self.mens_item1_size_value.set("Select the size")
                self.mens_item1_price_value.set("Select the Price")
                self.mens_item1_quantity_value.set("0")

                self.mens_item2_size_value.set("Select the size")
                self.mens_item2_price_value.set("Select the Price")
                self.mens_item2_quantity_value.set("0")

                self.mens_item3_size_value.set("Select the size")
                self.mens_item3_price_value.set("Select the Price")
                self.mens_item3_quantity_value.set("0")

                self.mens_item4_size_value.set("Select the size")
                self.mens_item4_price_value.set("Select the Price")
                self.mens_item4_quantity_value.set("0")

                self.mens_item5_size_value.set("Select the size")
                self.mens_item5_price_value.set("Select the Price")
                self.mens_item5_quantity_value.set("0")

                self.mens_item6_size_value.set("Select the size")
                self.mens_item6_price_value.set("Select the Price")
                self.mens_item6_quantity_value.set("0")

                self.mens_item7_size_value.set("Select the size")
                self.mens_item7_price_value.set("Select the Price")
                self.mens_item7_quantity_value.set("0")

                self.mens_item8_size_value.set("Select the size")
                self.mens_item8_price_value.set("Select the Price")
                self.mens_item8_quantity_value.set("0")

                self.mens_item9_size_value.set("Select the size")
                self.mens_item9_price_value.set("Select the Price")
                self.mens_item9_quantity_value.set("0")

                self.mens_item10_size_value.set("Select the size")
                self.mens_item10_price_value.set("Select the Price")
                self.mens_item10_quantity_value.set("0")

            elif self.categories.get() == "Women's Wear":
                self.womens_item1_size_value.set("Select the size")
                self.womens_item1_price_value.set("Select the Price")
                self.womens_item1_quantity_value.set("0")

                self.womens_item2_size_value.set("Select the size")
                self.womens_item2_price_value.set("Select the Price")
                self.womens_item2_quantity_value.set("0")

                self.womens_item3_size_value.set("Select the size")
                self.womens_item3_price_value.set("Select the Price")
                self.womens_item3_quantity_value.set("0")

                self.womens_item4_size_value.set("Select the size")
                self.womens_item4_price_value.set("Select the Price")
                self.womens_item4_quantity_value.set("0")

                self.womens_item5_size_value.set("Select the size")
                self.womens_item5_price_value.set("Select the Price")
                self.womens_item5_quantity_value.set("0")

                self.womens_item6_size_value.set("Select the size")
                self.womens_item6_price_value.set("Select the Price")
                self.womens_item6_quantity_value.set("0")

                self.womens_item7_size_value.set("Select the size")
                self.womens_item7_price_value.set("Select the Price")
                self.womens_item7_quantity_value.set("0")

                self.womens_item8_size_value.set("Select the size")
                self.womens_item8_price_value.set("Select the Price")
                self.womens_item8_quantity_value.set("0")

                self.womens_item9_size_value.set("Select the size")
                self.womens_item9_price_value.set("Select the Price")
                self.womens_item9_quantity_value.set("0")

                self.womens_item10_size_value.set("Select the size")
                self.womens_item10_price_value.set("Select the Price")
                self.womens_item10_quantity_value.set("0")

            elif self.categories.get() == "Kitchen Utensils":

                self.kitchen_item1_company_value.set("Select the company")
                self.kitchen_item1_price_value.set("Select the Price")
                self.kitchen_item1_quantity_value.set("0")

                self.kitchen_item2_company_value.set("Select the company")
                self.kitchen_item2_price_value.set("Select the Price")
                self.kitchen_item2_quantity_value.set("0")

                self.kitchen_item3_company_value.set("Select the company")
                self.kitchen_item3_price_value.set("Select the Price")
                self.kitchen_item3_quantity_value.set("0")

                self.kitchen_item4_company_value.set("Select the company")
                self.kitchen_item4_price_value.set("Select the Price")
                self.kitchen_item4_quantity_value.set("0")

                self.kitchen_item5_company_value.set("Select the company")
                self.kitchen_item5_price_value.set("Select the Price")
                self.kitchen_item5_quantity_value.set("0")

                self.kitchen_item6_company_value.set("Select the company")
                self.kitchen_item6_price_value.set("Select the Price")
                self.kitchen_item6_quantity_value.set("0")

                self.kitchen_item7_company_value.set("Select the company")
                self.kitchen_item7_price_value.set("Select the Price")
                self.kitchen_item7_quantity_value.set("0")

                self.kitchen_item8_company_value.set("Select the company")
                self.kitchen_item8_price_value.set("Select the Price")
                self.kitchen_item8_quantity_value.set("0")

                self.kitchen_item9_company_value.set("Select the company")
                self.kitchen_item9_price_value.set("Select the Price")
                self.kitchen_item9_quantity_value.set("0")

                self.kitchen_item10_company_value.set("Select the company")
                self.kitchen_item10_price_value.set("Select the Price")
                self.kitchen_item10_quantity_value.set("0")

            elif self.categories.get() == "Electronics":

                self.electronic_item1_company_value.set("Select the company")
                self.electronic_item1_price_value.set("Select the Price")
                self.electronic_item1_quantity_value.set("0")

                self.electronic_item2_company_value.set("Select the company")
                self.electronic_item2_price_value.set("Select the Price")
                self.electronic_item2_quantity_value.set("0")

                self.electronic_item3_company_value.set("Select the company")
                self.electronic_item3_price_value.set("Select the Price")
                self.electronic_item3_quantity_value.set("0")

                self.electronic_item4_company_value.set("Select the company")
                self.electronic_item4_price_value.set("Select the Price")
                self.electronic_item4_quantity_value.set("0")

                self.electronic_item5_company_value.set("Select the company")
                self.electronic_item5_price_value.set("Select the Price")
                self.electronic_item5_quantity_value.set("0")

                self.electronic_item6_company_value.set("Select the company")
                self.electronic_item6_price_value.set("Select the Price")
                self.electronic_item6_quantity_value.set("0")

                self.electronic_item7_company_value.set("Select the company")
                self.electronic_item7_price_value.set("Select the Price")
                self.electronic_item7_quantity_value.set("0")

                self.electronic_item8_company_value.set("Select the company")
                self.electronic_item8_price_value.set("Select the Price")
                self.electronic_item8_quantity_value.set("0")

                self.electronic_item9_company_value.set("Select the company")
                self.electronic_item9_price_value.set("Select the Price")
                self.electronic_item9_quantity_value.set("0")

                self.electronic_item10_company_value.set("Select the company")
                self.electronic_item10_price_value.set("Select the Price")
                self.electronic_item10_quantity_value.set("0")

            elif self.categories.get() == "Stationary":
                self.stationary_item1_company_value.set("Select the company")
                self.stationary_item1_price_value.set("Select the Price")
                self.stationary_item1_quantity_value.set("0")

                self.stationary_item2_company_value.set("Select the company")
                self.stationary_item2_price_value.set("Select the Price")
                self.stationary_item2_quantity_value.set("0")

                self.stationary_item3_company_value.set("Select the company")
                self.stationary_item3_price_value.set("Select the Price")
                self.stationary_item3_quantity_value.set("0")

                self.stationary_item4_company_value.set("Select the company")
                self.stationary_item4_price_value.set("Select the Price")
                self.stationary_item4_quantity_value.set("0")

                self.stationary_item5_company_value.set("Select the company")
                self.stationary_item5_price_value.set("Select the Price")
                self.stationary_item5_quantity_value.set("0")

                self.stationary_item6_company_value.set("Select the company")
                self.stationary_item6_price_value.set("Select the Price")
                self.stationary_item6_quantity_value.set("0")

                self.stationary_item7_company_value.set("Select the company")
                self.stationary_item7_price_value.set("Select the Price")
                self.stationary_item7_quantity_value.set("0")

                self.stationary_item8_company_value.set("Select the company")
                self.stationary_item8_price_value.set("Select the Price")
                self.stationary_item8_quantity_value.set("0")

                self.stationary_item9_company_value.set("Select the company")
                self.stationary_item9_price_value.set("Select the Price")
                self.stationary_item9_quantity_value.set("0")

                self.stationary_item10_company_value.set("Select the company")
                self.stationary_item10_price_value.set("Select the Price")
                self.stationary_item10_quantity_value.set("0")

            self.categories.set("Born Baby")
        else:
            return

    def generate_bill_function(self):
        if (self.categories.get() == "Born Baby" and self.bill_bb_confirm_bool is False):
            self.random_bill = random.randint(1000, 9999)
            self.textarea.insert(END, f"\nBill No : {self.random_bill}")
            self.textarea.insert(
                END, f"\nWholeseller Name : {self.clicked_wholeseller_name.get()}")
            self.textarea.insert(
                END, f"\nWholeseller Contact Number : {self.ws_contact.get()}")
            self.textarea.insert(
                END, f"\nBilling Address : {self.billing_address_value.get()}")
            self.textarea.insert(
                END, f"\nWholeseller Email : {self.wholeseller_email_value.get()}")
            self.textarea.insert(
                END, f"\nPayment Mode : {self.payment_mode.get()}")

            self.textarea.insert(
                END, f"\n======================================================================")
            self.textarea.insert(
                END, f"\nProduct\t\t    Size\t\t        Quantity\t\t\t       Price")
            self.textarea.insert(
                END, f"\n======================================================================")

            if (self.bb_item1_price_value.get() is not None and self.bb_item1_quantity_value.get() != "0" and self.bb_item1_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nShirt\t\t    {self.bb_item1_size_value.get()}\t\t        {self.bb_item1_quantity_value.get()}\t\t\t       {str(int(self.bb_item1_price_value.get())*int(self.bb_item1_quantity_value.get()))}")

            if (self.bb_item2_price_value.get() is not None and self.bb_item2_quantity_value.get() != "0" and self.bb_item2_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nJeans\t\t    {self.bb_item2_size_value.get()}\t\t        {self.bb_item2_quantity_value.get()}\t\t\t       {str(int(self.bb_item2_price_value.get())*int(self.bb_item2_quantity_value.get()))}")

            if (self.bb_item3_price_value.get() is not None and self.bb_item3_quantity_value.get() != "0" and self.bb_item3_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nShoes\t\t    {self.bb_item3_size_value.get()}\t\t        {self.bb_item3_quantity_value.get()}\t\t\t       {str(int(self.bb_item3_price_value.get())*int(self.bb_item3_quantity_value.get()))}")

            if (self.bb_item4_price_value.get() is not None and self.bb_item4_quantity_value.get() != "0" and self.bb_item4_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nFrock\t\t    {self.bb_item4_size_value.get()}\t\t        {self.bb_item4_quantity_value.get()}\t\t\t       {str(int(self.bb_item4_price_value.get())*int(self.bb_item4_quantity_value.get()))}")

            if (self.bb_item5_price_value.get() is not None and self.bb_item5_quantity_value.get() != "0" and self.bb_item5_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nT-Shirts\t\t    {self.bb_item5_size_value.get()}\t\t        {self.bb_item5_quantity_value.get()}\t\t\t       {str(int(self.bb_item5_price_value.get())*int(self.bb_item5_quantity_value.get()))}")

            if (self.bb_item6_price_value.get() is not None and self.bb_item6_quantity_value.get() != "0" and self.bb_item6_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nPants\t\t    {self.bb_item6_size_value.get()}\t\t        {self.bb_item6_quantity_value.get()}\t\t\t       {str(int(self.bb_item6_price_value.get())*int(self.bb_item6_quantity_value.get()))}")

            if (self.bb_item7_price_value.get() is not None and self.bb_item7_quantity_value.get() != "0" and self.bb_item7_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nSweater\t\t    {self.bb_item7_size_value.get()}\t\t        {self.bb_item7_quantity_value.get()}\t\t\t       {str(int(self.bb_item7_price_value.get())*int(self.bb_item7_quantity_value.get()))}")

            if (self.bb_item8_price_value.get() is not None and self.bb_item8_quantity_value.get() != "0" and self.bb_item8_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nJacket\t\t    {self.bb_item8_size_value.get()}\t\t        {self.bb_item8_quantity_value.get()}\t\t\t       {str(int(self.bb_item8_price_value.get())*int(self.bb_item8_quantity_value.get()))}")

            if (self.bb_item9_price_value.get() is not None and self.bb_item9_quantity_value.get() != "0" and self.bb_item9_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nBaby Caps\t\t    {self.bb_item9_size_value.get()}\t\t        {self.bb_item9_quantity_value.get()}\t\t\t       {str(int(self.bb_item9_price_value.get())*int(self.bb_item9_quantity_value.get()))}")

            if (self.bb_item10_price_value.get() is not None and self.bb_item10_quantity_value.get() != "0"and self.bb_item10_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nShocks\t\t    {self.bb_item10_size_value.get()}\t\t        {self.bb_item10_quantity_value.get()}\t\t\t       {str(int(self.bb_item10_price_value.get())*int(self.bb_item10_quantity_value.get()))}")

            self.textarea.insert(
                END, f"\n\n----------------------------------------------------------------------")
            self.textarea.insert(
                END, f"\n                                                 Total Amount : {self.total_final_sum}")

            self.textarea.insert(
                END, f"\n----------------------------------------------------------------------")
            self.total_final_sum = 0
            self.bill_bb_confirm_bool = True
            self.save_bill()

        elif (self.categories.get() == "Men's Wear"and self.bill_mw_confirm_bool is False):
            self.random_bill = random.randint(1000, 9999)
            self.textarea.insert(END, f"\nBill No : {self.random_bill}")
            self.textarea.insert(
                END, f"\nWholeseller Name : {self.clicked_wholeseller_name.get()}")
            self.textarea.insert(
                END, f"\nWholeseller Contact Number : {self.ws_contact.get()}")

            self.textarea.insert(
                END, f"\nBilling Address : {self.billing_address_value.get()}")
            self.textarea.insert(
                END, f"\nWholeseller Email : {self.wholeseller_email_value.get()}")
            self.textarea.insert(
                END, f"\nPayment Mode : {self.payment_mode.get()}")

            self.textarea.insert(
                END, f"\n======================================================================")
            self.textarea.insert(
                END, f"\nProduct\t\t    Size\t\t        Quantity\t\t\t       Price")
            self.textarea.insert(
                END, f"\n======================================================================")

            if (self.mens_item1_price_value.get() is not None and self.mens_item1_quantity_value.get() != "0" and self.mens_item1_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nFormal Shirts\t\t    {self.mens_item1_size_value.get()}\t\t        {self.mens_item1_quantity_value.get()}\t\t\t       {int(self.mens_item1_price_value.get())*int(self.mens_item1_quantity_value.get())}")

            if (self.mens_item2_price_value.get() is not None and self.mens_item2_quantity_value.get() != "0" and self.mens_item2_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nT-Shirts\t\t    {self.mens_item2_size_value.get()}\t\t        {self.mens_item2_quantity_value.get()}\t\t\t       {int(self.mens_item2_price_value.get())*int(self.mens_item2_quantity_value.get())}")

            if (self.mens_item3_price_value.get() is not None and self.mens_item3_quantity_value.get() != "0" and self.mens_item3_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nFormal Pants\t\t    {self.mens_item3_size_value.get()}\t\t        {self.mens_item3_quantity_value.get()}\t\t\t       {int(self.mens_item3_price_value.get())*int(self.mens_item3_quantity_value.get())}")

            if (self.mens_item4_price_value.get() is not None and self.mens_item4_quantity_value.get() != "0" and self.mens_item4_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nJeans\t\t    {self.mens_item4_size_value.get()}\t\t        {self.mens_item4_quantity_value.get()}\t\t\t       {int(self.mens_item4_price_value.get())*int(self.mens_item4_quantity_value.get())}")

            if (self.mens_item5_price_value.get() is not None and self.mens_item5_quantity_value.get() != "0" and self.mens_item5_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nCoats\t\t    {self.mens_item5_size_value.get()}\t\t        {self.mens_item5_quantity_value.get()}\t\t\t       {int(self.mens_item5_price_value.get())*int(self.mens_item5_quantity_value.get())}")

            if (self.mens_item6_price_value.get() is not None and self.mens_item6_quantity_value.get() != "0" and self.mens_item6_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nHoodies\t\t    {self.mens_item6_size_value.get()}\t\t        {self.mens_item6_quantity_value.get()}\t\t\t       {int(self.mens_item6_price_value.get())*int(self.mens_item6_quantity_value.get())}")

            if (self.mens_item7_price_value.get() is not None and self.mens_item7_quantity_value.get() != "0" and self.mens_item7_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nJackets\t\t    {self.mens_item7_size_value.get()}\t\t        {self.mens_item7_quantity_value.get()}\t\t\t       {int(self.mens_item7_price_value.get())*int(self.mens_item7_quantity_value.get())}")

            if (self.mens_item8_price_value.get() is not None and self.mens_item8_quantity_value.get() != "0" and self.mens_item8_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nSweaters\t\t    {self.mens_item8_size_value.get()}\t\t        {self.mens_item8_quantity_value.get()}\t\t\t       {int(self.mens_item8_price_value.get())*int(self.mens_item8_quantity_value.get())}")

            if (self.mens_item9_price_value.get() is not None and self.mens_item9_quantity_value.get() != "0" and self.mens_item9_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nShoes\t\t    {self.mens_item9_size_value.get()}\t\t        {self.mens_item9_quantity_value.get()}\t\t\t       {int(self.mens_item9_price_value.get())*int(self.mens_item9_quantity_value.get())}")

            if (self.mens_item10_price_value.get() is not None and self.mens_item10_quantity_value.get() != "0" and self.mens_item10_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nKurtas\t\t    {self.mens_item10_size_value.get()}\t\t        {self.mens_item10_quantity_value.get()}\t\t\t       {int(self.mens_item10_price_value.get())*int(self.mens_item10_quantity_value.get())}")

            self.textarea.insert(
                END, f"\n\n----------------------------------------------------------------------")
            self.textarea.insert(
                END, f"\n                                                 Total Amount : {self.total_final_sum}")

            self.textarea.insert(
                END, f"\n----------------------------------------------------------------------")
            self.total_final_sum = 0

            self.bill_mw_confirm_bool = True

            self.save_bill()
        elif (self.categories.get() == "Women's Wear"and self.bill_ww_confirm_bool is False):
            self.random_bill = random.randint(1000, 9999)
            self.textarea.insert(END, f"\nBill No : {self.random_bill}")
            self.textarea.insert(
                END, f"\nWholeseller Name : {self.clicked_wholeseller_name.get()}")
            self.textarea.insert(
                END, f"\nWholeseller Contact Number : {self.ws_contact.get()}")

            self.textarea.insert(
                END, f"\nBilling Address : {self.billing_address_value.get()}")
            self.textarea.insert(
                END, f"\nWholeseller Email : {self.wholeseller_email_value.get()}")
            self.textarea.insert(
                END, f"\nPayment Mode : {self.payment_mode.get()}")

            self.textarea.insert(
                END, f"\n======================================================================")
            self.textarea.insert(
                END, f"\nProduct\t\t    Size\t\t        Quantity\t\t\t       Price")
            self.textarea.insert(
                END, f"\n======================================================================")

            if (self.womens_item1_price_value.get() is not None and self.womens_item1_quantity_value.get() != "0" and self.womens_item1_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nKurta Sets\t\t    {self.womens_item1_size_value.get()}\t\t        {self.womens_item1_quantity_value.get()}\t\t\t       {int(self.womens_item1_price_value.get())*int(self.womens_item1_quantity_value.get())}")

            if (self.womens_item2_price_value.get() is not None and self.womens_item2_quantity_value.get() != "0" and self.womens_item2_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nJeans\t\t    {self.womens_item2_size_value.get()}\t\t        {self.womens_item2_quantity_value.get()}\t\t\t       {int(self.womens_item2_price_value.get())*int(self.womens_item2_quantity_value.get())}")

            if (self.womens_item3_price_value.get() is not None and self.womens_item3_quantity_value.get() != "0" and self.womens_item3_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nT-Shirts\t\t    {self.womens_item3_size_value.get()}\t\t        {self.womens_item3_quantity_value.get()}\t\t\t       {int(self.womens_item3_price_value.get())*int(self.womens_item3_quantity_value.get())}")

            if (self.womens_item4_price_value.get() is not None and self.womens_item4_quantity_value.get() != "0" and self.womens_item4_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nJackets\t\t    {self.womens_item4_size_value.get()}\t\t        {self.womens_item4_quantity_value.get()}\t\t\t       {int(self.womens_item4_price_value.get())*int(self.womens_item4_quantity_value.get())}")

            if (self.womens_item5_price_value.get() is not None and self.womens_item5_quantity_value.get() != "0" and self.womens_item5_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nDresses\t\t    {self.womens_item5_size_value.get()}\t\t        {self.womens_item5_quantity_value.get()}\t\t\t       {int(self.womens_item5_price_value.get())*int(self.womens_item5_quantity_value.get())}")

            if (self.womens_item6_price_value.get() is not None and self.womens_item6_quantity_value.get() != "0" and self.womens_item6_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nShoes\t\t    {self.womens_item6_size_value.get()}\t\t        {self.womens_item6_quantity_value.get()}\t\t\t       {int(self.womens_item6_price_value.get())*int(self.womens_item6_quantity_value.get())}")

            if (self.womens_item7_price_value.get() is not None and self.womens_item7_quantity_value.get() != "0" and self.womens_item7_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nKafri Gowns\t\t    {self.womens_item7_size_value.get()}\t\t        {self.womens_item7_quantity_value.get()}\t\t\t       {int(self.womens_item7_price_value.get())*int(self.womens_item7_quantity_value.get())}")

            if (self.womens_item8_price_value.get() is not None and self.womens_item8_quantity_value.get() != "0" and self.womens_item8_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nLeggings\t\t    {self.womens_item8_size_value.get()}\t\t        {self.womens_item8_quantity_value.get()}\t\t\t       {int(self.womens_item8_price_value.get())*int(self.womens_item8_quantity_value.get())}")

            if (self.womens_item9_price_value.get() is not None and self.womens_item9_quantity_value.get() != "0" and self.womens_item9_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nScarfs\t\t    {self.womens_item9_size_value.get()}\t\t        {self.womens_item9_quantity_value.get()}\t\t\t       {int(self.womens_item9_price_value.get())*int(self.womens_item9_quantity_value.get())}")

            if (self.womens_item10_price_value.get() is not None and self.womens_item10_quantity_value.get() != "0" and self.womens_item10_size_value.get() is not None):
                self.textarea.insert(
                    END, f"\nSkirts\t\t    {self.womens_item10_size_value.get()}\t\t        {self.womens_item10_quantity_value.get()}\t\t\t       {int(self.womens_item10_price_value.get())*int(self.womens_item10_quantity_value.get())}")

            self.textarea.insert(
                END, f"\n\n----------------------------------------------------------------------")
            self.textarea.insert(
                END, f"\n                                                 Total Amount : {self.total_final_sum}")

            self.textarea.insert(
                END, f"\n----------------------------------------------------------------------")
            self.total_final_sum = 0

            self.bill_ww_confirm_bool = True

            self.save_bill()
        elif (self.categories.get() == "Kitchen Utensils" and self.bill_ku_confirm_bool is False):
            self.random_bill = random.randint(1000, 9999)
            self.textarea.insert(END, f"\nBill No : {self.random_bill}")
            self.textarea.insert(
                END, f"\nWholeseller Name : {self.clicked_wholeseller_name.get()}")
            self.textarea.insert(
                END, f"\nWholeseller Contact Number : {self.ws_contact.get()}")

            self.textarea.insert(
                END, f"\nBilling Address : {self.billing_address_value.get()}")
            self.textarea.insert(
                END, f"\nWholeseller Email : {self.wholeseller_email_value.get()}")
            self.textarea.insert(
                END, f"\nPayment Mode : {self.payment_mode.get()}")

            self.textarea.insert(
                END, f"\n======================================================================")
            self.textarea.insert(
                END, f"\nProduct\t\t    Company\t\t        Quantity\t\t\t       Price")
            self.textarea.insert(
                END, f"\n======================================================================")

            if (self.kitchen_item1_price_value.get() is not None and self.kitchen_item1_quantity_value.get() != "0" and self.kitchen_item1_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nPressure Cookers\t\t    {self.kitchen_item1_company_value.get()}\t\t        {self.kitchen_item1_quantity_value.get()}\t\t\t       {int(self.kitchen_item1_price_value.get())*int(self.kitchen_item1_quantity_value.get())}")

            if (self.kitchen_item2_price_value.get() is not None and self.kitchen_item2_quantity_value.get() != "0" and self.kitchen_item2_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nInduction\t\t    {self.kitchen_item2_company_value.get()}\t\t        {self.kitchen_item2_quantity_value.get()}\t\t\t       {int(self.kitchen_item2_price_value.get())*int(self.kitchen_item2_quantity_value.get())}")

            if (self.kitchen_item3_price_value.get() is not None and self.kitchen_item3_quantity_value.get() != "0" and self.kitchen_item3_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nMixer Grider\t\t    {self.kitchen_item3_company_value.get()}\t\t        {self.kitchen_item3_quantity_value.get()}\t\t\t       {int(self.kitchen_item3_price_value.get())*int(self.kitchen_item3_quantity_value.get())}")

            if (self.kitchen_item4_price_value.get() is not None and self.kitchen_item4_quantity_value.get() != "0" and self.kitchen_item4_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nMicro Oven\t\t    {self.kitchen_item4_company_value.get()}\t\t        {self.kitchen_item4_quantity_value.get()}\t\t\t       {int(self.kitchen_item4_price_value.get())*int(self.kitchen_item4_quantity_value.get())}")

            if (self.kitchen_item5_price_value.get() is not None and self.kitchen_item5_quantity_value.get() != "0" and self.kitchen_item5_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nDinner Sets\t\t    {self.kitchen_item5_company_value.get()}\t\t        {self.kitchen_item5_quantity_value.get()}\t\t\t       {int(self.kitchen_item5_price_value.get())*int(self.kitchen_item5_quantity_value.get())}")

            if (self.kitchen_item6_price_value.get() is not None and self.kitchen_item6_quantity_value.get() != "0" and self.kitchen_item6_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nUtensils Stands\t\t    {self.kitchen_item6_company_value.get()}\t\t        {self.kitchen_item6_quantity_value.get()}\t\t\t       {int(self.kitchen_item6_price_value.get())*int(self.kitchen_item6_quantity_value.get())}")

            if (self.kitchen_item7_price_value.get() is not None and self.kitchen_item7_quantity_value.get() != "0"and self.kitchen_item7_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nFrying Pans\t\t    {self.kitchen_item7_company_value.get()}\t\t        {self.kitchen_item7_quantity_value.get()}\t\t\t       {int(self.kitchen_item7_price_value.get())*int(self.kitchen_item7_quantity_value.get())}")

            if (self.kitchen_item8_price_value.get() is not None and self.kitchen_item8_quantity_value.get() != "0" and self.kitchen_item8_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nSpoon Sets\t\t    {self.kitchen_item8_company_value.get()}\t\t        {self.kitchen_item8_quantity_value.get()}\t\t\t       {int(self.kitchen_item8_price_value.get())*int(self.kitchen_item8_quantity_value.get())}")

            if (self.kitchen_item9_price_value.get() is not None and self.kitchen_item9_quantity_value.get() != "0" and self.kitchen_item9_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nCooking Pots\t\t    {self.kitchen_item9_company_value.get()}\t\t        {self.kitchen_item9_quantity_value.get()}\t\t\t       {int(self.kitchen_item9_price_value.get())*int(self.kitchen_item9_quantity_value.get())}")

            if (self.kitchen_item10_price_value.get() is not None and self.kitchen_item10_quantity_value.get() != "0" and self.kitchen_item10_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nJuicer\t\t    {self.kitchen_item10_company_value.get()}\t\t        {self.kitchen_item10_quantity_value.get()}\t\t\t       {int(self.kitchen_item10_price_value.get())*int(self.kitchen_item10_quantity_value.get())}")

            self.textarea.insert(
                END, f"\n\n----------------------------------------------------------------------")
            self.textarea.insert(
                END, f"\n                                                 Total Amount : {self.total_final_sum}")

            self.textarea.insert(
                END, f"\n----------------------------------------------------------------------")
            self.total_final_sum = 0

            self.bill_ku_confirm_bool = True

            self.save_bill()
        elif (self.categories.get() == "Electronics"and self.bill_ele_confirm_bool is False):
            self.random_bill = random.randint(1000, 9999)
            self.textarea.insert(END, f"\nBill No : {self.random_bill}")
            self.textarea.insert(
                END, f"\nWholeseller Name : {self.clicked_wholeseller_name.get()}")
            self.textarea.insert(
                END, f"\nWholeseller Contact Number : {self.ws_contact.get()}")

            self.textarea.insert(
                END, f"\nBilling Address : {self.billing_address_value.get()}")
            self.textarea.insert(
                END, f"\nWholeseller Email : {self.wholeseller_email_value.get()}")
            self.textarea.insert(
                END, f"\nPayment Mode : {self.payment_mode.get()}")

            self.textarea.insert(
                END, f"\n======================================================================")
            self.textarea.insert(
                END, f"\nProduct\t\t    Company\t\t        Quantity\t\t\t       Price")
            self.textarea.insert(
                END, f"\n======================================================================")

            if (self.electronic_item1_price_value.get() is not None and self.electronic_item1_quantity_value.get() != "0" and self.electronic_item1_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nRefrigerators\t\t    {self.electronic_item1_company_value.get()}\t\t        {self.electronic_item1_quantity_value.get()}\t\t\t       {int(self.electronic_item1_price_value.get())*int(self.electronic_item1_quantity_value.get())}")

            if (self.electronic_item2_price_value.get() is not None and self.electronic_item2_quantity_value.get() != "0"and self.electronic_item2_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nTelevisions\t\t    {self.electronic_item2_company_value.get()}\t\t        {self.electronic_item2_quantity_value.get()}\t\t\t       {int(self.electronic_item2_price_value.get())*int(self.electronic_item2_quantity_value.get())}")

            if (self.electronic_item3_price_value.get() is not None and self.electronic_item3_quantity_value.get() != "0"and self.electronic_item3_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nAir Coolers\t\t    {self.electronic_item3_company_value.get()}\t\t        {self.electronic_item3_quantity_value.get()}\t\t\t       {int(self.electronic_item3_price_value.get())*int(self.electronic_item3_quantity_value.get())}")

            if (self.electronic_item4_price_value.get() is not None and self.electronic_item4_quantity_value.get() != "0" and self.electronic_item4_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nAir Conditioners\t\t    {self.electronic_item4_company_value.get()}\t\t        {self.electronic_item4_quantity_value.get()}\t\t\t       {int(self.electronic_item4_price_value.get())*int(self.electronic_item4_quantity_value.get())}")

            if (self.electronic_item5_price_value.get() is not None and self.electronic_item5_quantity_value.get() != "0" and self.electronic_item5_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nWashing Machines\t\t    {self.electronic_item5_company_value.get()}\t\t        {self.electronic_item5_quantity_value.get()}\t\t\t       {int(self.electronic_item5_price_value.get())*int(self.electronic_item5_quantity_value.get())}")

            if (self.electronic_item6_price_value.get() is not None and self.electronic_item6_quantity_value.get() != "0" and self.electronic_item6_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nLaptops\t\t    {self.electronic_item6_company_value.get()}\t\t        {self.electronic_item6_quantity_value.get()}\t\t\t       {int(self.electronic_item6_price_value.get())*int(self.electronic_item6_quantity_value.get())}")

            if (self.electronic_item7_price_value.get() is not None and self.electronic_item7_quantity_value.get() != "0" and self.electronic_item7_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nSmart Phones\t\t    {self.electronic_item7_company_value.get()}\t\t        {self.electronic_item7_quantity_value.get()}\t\t\t       {int(self.electronic_item7_price_value.get())*int(self.electronic_item7_quantity_value.get())}")

            if (self.electronic_item8_price_value.get() is not None and self.electronic_item8_quantity_value.get() != "0" and self.electronic_item8_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nDesktop Sets\t\t    {self.electronic_item8_company_value.get()}\t\t        {self.electronic_item8_quantity_value.get()}\t\t\t       {int(self.electronic_item8_price_value.get())*int(self.electronic_item8_quantity_value.get())}")

            if (self.electronic_item9_price_value.get() is not None and self.electronic_item9_quantity_value.get() != "0" and self.electronic_item9_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nFans\t\t    {self.electronic_item9_company_value.get()}\t\t        {self.electronic_item9_quantity_value.get()}\t\t\t       {int(self.electronic_item9_price_value.get())*int(self.electronic_item9_quantity_value.get())}")

            if (self.electronic_item10_price_value.get() is not None and self.electronic_item10_quantity_value.get() != "0" and self.electronic_item10_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nPrinters\t\t    {self.electronic_item10_company_value.get()}\t\t        {self.electronic_item10_quantity_value.get()}\t\t\t       {int(self.electronic_item10_price_value.get())*int(self.electronic_item10_quantity_value.get())}")

            self.textarea.insert(
                END, f"\n\n----------------------------------------------------------------------")
            self.textarea.insert(
                END, f"\n                                                Total Amount : {self.total_final_sum}")

            self.textarea.insert(
                END, f"\n----------------------------------------------------------------------")
            self.total_final_sum = 0

            self.bill_ele_confirm_bool = True

            self.save_bill()
        elif (self.categories.get() == "Stationary" and self.bill_stnry_confirm_bool is False):
            self.random_bill = random.randint(1000, 9999)
            self.textarea.insert(END, f"\nBill No : {self.random_bill}")
            self.textarea.insert(
                END, f"\nWholeseller Name : {self.clicked_wholeseller_name.get()}")
            self.textarea.insert(
                END, f"\nWholeseller Contact Number : {self.ws_contact.get()}")

            self.textarea.insert(
                END, f"\nBilling Address : {self.billing_address_value.get()}")
            self.textarea.insert(
                END, f"\nWholeseller Email : {self.wholeseller_email_value.get()}")
            self.textarea.insert(
                END, f"\nPayment Mode : {self.payment_mode.get()}")

            self.textarea.insert(
                END, f"\n======================================================================")
            self.textarea.insert(
                END, f"\nProduct\t\t    Company\t\t        Quantity\t\t\t       Price")
            self.textarea.insert(
                END, f"\n======================================================================")

            if (self.stationary_item1_price_value.get() is not None and self.stationary_item1_quantity_value.get() != "0" and self.stationary_item1_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nNotebooks\t\t    {self.stationary_item1_company_value.get()}\t\t        {self.stationary_item1_quantity_value.get()}\t\t\t       {int(self.stationary_item1_price_value.get())*int(self.stationary_item1_quantity_value.get())}")

            if (self.stationary_item2_price_value.get() is not None and self.stationary_item2_quantity_value.get() != "0" and self.stationary_item2_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nPencils\t\t    {self.stationary_item2_company_value.get()}\t\t        {self.stationary_item2_quantity_value.get()}\t\t\t       {int(self.stationary_item2_price_value.get())*int(self.stationary_item2_quantity_value.get())}")

            if (self.stationary_item3_price_value.get() is not None and self.stationary_item3_quantity_value.get() != "0"and self.stationary_item3_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nPens\t\t    {self.stationary_item3_company_value.get()}\t\t        {self.stationary_item3_quantity_value.get()}\t\t\t       {int(self.stationary_item3_price_value.get())*int(self.stationary_item3_quantity_value.get())}")

            if (self.stationary_item4_price_value.get() is not None and self.stationary_item4_quantity_value.get() != "0" and self.stationary_item4_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nFiles\t\t    {self.stationary_item4_company_value.get()}\t\t        {self.stationary_item4_quantity_value.get()}\t\t\t       {int(self.stationary_item4_price_value.get())*int(self.stationary_item4_quantity_value.get())}")

            if (self.stationary_item5_price_value.get() is not None and self.stationary_item5_quantity_value.get() != "0" and self.stationary_item5_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nColor Sets\t\t    {self.stationary_item5_company_value.get()}\t\t        {self.stationary_item5_quantity_value.get()}\t\t\t       {int(self.stationary_item5_price_value.get())*int(self.stationary_item5_quantity_value.get())}")

            if (self.stationary_item6_price_value.get() is not None and self.stationary_item6_quantity_value.get() != "0" and self.stationary_item6_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nGeometry Boxes\t\t    {self.stationary_item6_company_value.get()}\t\t        {self.stationary_item6_quantity_value.get()}\t\t\t       {int(self.stationary_item6_price_value.get())*int(self.stationary_item6_quantity_value.get())}")

            if (self.stationary_item7_price_value.get() is not None and self.stationary_item7_quantity_value.get() != "0" and self.stationary_item7_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nPrinter Pages\t\t    {self.stationary_item7_company_value.get()}\t\t        {self.stationary_item7_quantity_value.get()}\t\t\t       {int(self.stationary_item7_price_value.get())*int(self.stationary_item7_quantity_value.get())}")

            if (self.stationary_item8_price_value.get() is not None and self.stationary_item8_quantity_value.get() != "0" and self.stationary_item8_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nCalculators\t\t    {self.stationary_item8_company_value.get()}\t\t        {self.stationary_item8_quantity_value.get()}\t\t\t       {int(self.stationary_item8_price_value.get())*int(self.stationary_item8_quantity_value.get())}")

            if (self.stationary_item9_price_value.get() is not None and self.stationary_item9_quantity_value.get() != "0" and self.stationary_item9_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nPrinter Cartrages\t\t    {self.stationary_item9_company_value.get()}\t\t        {self.stationary_item9_quantity_value.get()}\t\t\t       {int(self.stationary_item9_price_value.get())*int(self.stationary_item9_quantity_value.get())}")

            if (self.stationary_item10_price_value.get() is not None and self.stationary_item10_quantity_value.get() != "0" and self.stationary_item10_company_value.get() is not None):
                self.textarea.insert(
                    END, f"\nMarker Pens\t\t    {self.stationary_item10_company_value.get()}\t\t        {self.stationary_item10_quantity_value.get()}\t\t\t       {int(self.stationary_item10_price_value.get())*int(self.stationary_item10_quantity_value.get())}")

            self.textarea.insert(
                END, f"\n\n----------------------------------------------------------------------")
            self.textarea.insert(
                END, f"\n\n                                                 Total Amount : {self.total_final_sum}")

            self.textarea.insert(
                END, f"\n----------------------------------------------------------------------")
            self.total_final_sum = 0

            self.bill_stnry_confirm_bool = True

            self.save_bill()

    def welcome_bill(self):
        # using f string................!!!!!!!
        self.textarea.insert(END, f"\t\t\tWelcome To M.H.S Store\n")
        return

    def exit_function(self):
        ans = messagebox.askyesno("Exit", "Do you really want to exit?")
        if ans > 0:
            exit()
        else:
            return

    def save_bill(self):
        # askyesno always generate 0 for false and 1 for true !!!!!!!!( important)
        ans = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if ans > 0:
            self.bill_data = self.textarea.get(1.0, END)
            f1 = open("saved bill as purchaser\\"+str(self.random_bill)+".txt", "w")
            f1.write(self.bill_data)
            f1.close()

            messagebox.showinfo(
                "Confirmation", f"Bill No : {self.random_bill} is Generated and saved successfully.")
        else:
            return

    def search_bill(self):
        # os.listdir hume input directory mein jitne bhi items hoge wo saare ko list mein de dega

        # we should mark all bill true because here we are not creating new bill that why genereate bill should not work
        self.bill_bb_confirm_bool = True
        self.bill_mw_confirm_bool = True
        self.bill_ww_confirm_bool = True
        self.bill_ele_confirm_bool = True
        self.bill_ku_confirm_bool = True
        self.bill_stnry_confirm_bool = True
        present = False
        if self.bill_no.get() == "":
            messagebox.showwarning(
                "Warning", "Bill Number not entered please enter the Bill Number.")
            self.bill_no.set("0")
        elif self.bill_no.get() is not None:
            for i in os.listdir("saved bill as purchaser\\"):
                if i.split(".")[0] == self.bill_no.get():
                    f1 = open("saved bill as purchaser\\" +
                              str(self.bill_no.get())+".txt", "r")
                    self.textarea.delete(1.0, END)
                    for char in f1:
                        self.textarea.insert(END, char)
                    f1.close()
                    present = True
            if present == False:
                messagebox.showwarning(
                    "Search", f"Invalid Bill Number.\n\n Please Enter the Valid Bill Number")
                self.bill_no.set("0")


root = Tk()
obj = As_Purchaser(root)
root.mainloop()


# =============================================== [ DONE]=============================================================================
