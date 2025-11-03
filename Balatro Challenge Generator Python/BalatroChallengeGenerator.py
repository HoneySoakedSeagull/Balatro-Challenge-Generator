import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class LuaGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Balatro Challenge Generator by HoneySoakedSeagull")

        # Info Page
        self.info_page = ttk.Frame(self.root)
        self.info_page.pack(padx=10, pady=10, fill='both', expand=True)

        self.custom_entries = []
        self.modifier_entries = []

        self.authorlabel = ttk.Label(self.info_page, text="Author:")
        self.authorlabel.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.author = tk.Entry(self.info_page, width=15)
        self.author.grid(row=0, column=1, padx=5, pady=5)

        self.modnamelabel = ttk.Label(self.info_page, text="Mod Name:")
        self.modnamelabel.grid(row=0, column=2, padx=5, pady=5, sticky='e')
        self.modname = tk.Entry(self.info_page, width=15)
        self.modname.grid(row=0, column=3, padx=5, pady=5)

        self.modidlabel = ttk.Label(self.info_page, text="Mod ID:")
        self.modidlabel.grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.modid = tk.Entry(self.info_page, width=15)
        self.modid.grid(row=1, column=1, padx=5, pady=5)

        self.versionlabel = ttk.Label(self.info_page, text="Version:")
        self.versionlabel.grid(row=1, column=2, padx=5, pady=5, sticky='e')
        self.version = tk.Entry(self.info_page, width=15)
        self.version.grid(row=1, column=3, padx=5, pady=5)

        self.moddesclabel = ttk.Label(self.info_page, text="Mod Description (Only for SMODS)")
        self.moddesclabel.grid(row=2, column=0, columnspan=4, padx=5, pady=5)
        self.moddesc = tk.Text(self.info_page, width=40, height=4)
        self.moddesc.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

        # Language Section
        self.local_entries = []
        self.local_frame = ttk.LabelFrame(self.info_page, text='Languages (Only for SMODS)')
        self.local_frame.grid(row=4, column=0, columnspan=4, padx=5, pady=5)

        self.local_scroll = ttk.Scrollbar(self.local_frame, orient='vertical')
        self.local_scroll.grid(row=0, column=1, sticky='ns')

        self.local_canvas = tk.Canvas(self.local_frame, yscrollcommand=self.local_scroll.set, height=103)
        self.local_canvas.grid(row=0, column=0, sticky='nsew')

        self.local_scroll.config(command=self.local_canvas.yview)

        self.local_frame_inner = ttk.Frame(self.local_canvas)
        self.local_canvas.create_window((0, 0), window=self.local_frame_inner, anchor='nw')

        self.local_scroll.bind('<Configure>', lambda e: self.local_scroll.config(command=self.local_canvas.yview))
        self.local_frame_inner.bind('<Configure>', lambda e: self.local_canvas.config(scrollregion=self.local_canvas.bbox('all')))

        self.add_local_btn = ttk.Button(self.local_frame, text='Add Language', command=self.add_local)
        self.add_local_btn.grid(row=1, column=0, padx=5, pady=5, sticky='ew',)

        # Map Language Names to Lua Variable Names
        self.local_mapping = {
            "Chinese (Simplified)": "zh_CN",
            "Chinese (Traditional)": "zh_TW",
            "Dutch": "nl",
            "English": "en-us",
            "French": "fr",
            "German": "de",
            "Indonesian": "id",
            "Italian": "it",
            "Japanese": "ja",
            "Korean": "ko",
            "Polish": "pl",
            "Portuguese (Brazil)": "pt_BR",
            "Russian": "ru",
            "Spanish (Latin America)": "es_419",
            "Spanish (Spain)": "es_ES"
        }

        self.next_button = ttk.Button(self.info_page, text="Next", command=self.show_rules_page)
        self.next_button.grid(row=5, column=0, columnspan=4, pady=10)

        # Rules Page
        self.rules_page = ttk.Frame(self.root)

        # Custom Section
        self.custom_entries = []
        self.custom_frame = ttk.LabelFrame(self.rules_page, text='Custom')
        self.custom_frame.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        self.custom_scroll = ttk.Scrollbar(self.custom_frame, orient='vertical')
        self.custom_scroll.grid(row=0, column=1, sticky='ns')

        self.custom_canvas = tk.Canvas(self.custom_frame, yscrollcommand=self.custom_scroll.set, height=100)
        self.custom_canvas.grid(row=0, column=0, sticky='nsew')

        self.custom_scroll.config(command=self.custom_canvas.yview)

        self.custom_frame_inner = ttk.Frame(self.custom_canvas)
        self.custom_canvas.create_window((0, 0), window=self.custom_frame_inner, anchor='nw')

        self.custom_scroll.bind('<Configure>', lambda e: self.custom_scroll.config(command=self.custom_canvas.yview))
        self.custom_frame_inner.bind('<Configure>', lambda e: self.custom_canvas.config(scrollregion=self.custom_canvas.bbox('all')))

        self.add_custom_btn = ttk.Button(self.custom_frame, text='Add Custom', command=self.add_custom)
        self.add_custom_btn.grid(row=1, column=0, padx=5, pady=5, sticky='ew',)

        # Map Customs to Lua Variable
        self.custom_mapping = {
            "All Jokers are Eternal" : "all_eternal",
            "Chips Cannot Exceed Current $" : "chips_dollar_cap",
            "Debuff Played Cards" : "debuff_played_cards",         
            "No Small Blind Reward": "no_reward_specific', value = 'Small",
            "No Big Blind Reward": "no_reward_specific', value = 'Big",
            "No Boss Blind Reward": "no_reward_specific', value = 'Boss",
            "No Blind Rewards": "no_reward",
            "No Extra Hand Money" : "no_extra_hand_money",
            "No Interest" : "no_interest",
            "Prices Increase Each Purchase" : "inflation",
            "No Shop Jokers" : "no_shop_jokers",
            "Cards are Face Down" : "flipped_cards",
#           "Daily Challenge" : "daily", 
            "$X per Discard" : "discard_cost",
            "Fixed Seed" : "set_seed",
            "Hand -1 per $X" : "minus_hand_size_per_X_dollar",
            "Joker Slot Ante" : "set_joker_slots_ante",
            "Eternal Ante" : "set_eternal_ante",
        }

        # Modifier Section
        self.modifier_entries = []
        self.modifier_frame = ttk.LabelFrame(self.rules_page, text='Modifiers')
        self.modifier_frame.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

        self.modifier_scroll = ttk.Scrollbar(self.modifier_frame, orient='vertical')
        self.modifier_scroll.grid(row=0, column=1, sticky='ns')

        self.modifier_canvas = tk.Canvas(self.modifier_frame, yscrollcommand=self.modifier_scroll.set, height=100)
        self.modifier_canvas.grid(row=0, column=0, sticky='nsew')

        self.modifier_scroll.config(command=self.modifier_canvas.yview)

        self.modifier_frame_inner = ttk.Frame(self.modifier_canvas)
        self.modifier_canvas.create_window((0, 0), window=self.modifier_frame_inner, anchor='nw')

        self.modifier_scroll.bind('<Configure>', lambda e: self.modifier_scroll.config(command=self.modifier_canvas.yview))
        self.modifier_frame_inner.bind('<Configure>', lambda e: self.modifier_canvas.config(scrollregion=self.modifier_canvas.bbox('all')))

        self.add_modifier_btn = ttk.Button(self.modifier_frame, text='Add Modifier', command=self.add_modifier)
        self.add_modifier_btn.grid(row=1, column=0, padx=5, pady=5, sticky='ew',)

        # Map Modifiers to Lua Variable
        self.modifier_mapping = {
            "Dollars": "dollars",
            "Discards" : "discards",
            "Hands" : "hands",
            "Reroll Cost" : "reroll_cost",
            "Joker Slots" : "joker_slots",
            "Consumable Slots" : "consumable_slots",
            "Hand Size" : "hand_size",
        }

        self.rules_btn_frame = ttk.Frame(self.rules_page)
        self.rules_btn_frame.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

        self.back_button = ttk.Button(self.rules_btn_frame, text="Back", command=self.show_info_page)
        self.back_button.grid(row=0, column=0, padx=5, pady=5, sticky='e')

        self.next_button = ttk.Button(self.rules_btn_frame, text="Next", command=self.show_joker_page)
        self.next_button.grid(row=0, column=4, padx=5, pady=5, sticky='w')  

        self.rules_btn_frame.grid_columnconfigure(2, weight=1)

        # Jokers Page
        self.joker_page = ttk.Frame(self.root)

        # Joker Section
        self.joker_entries = []
        self.joker_frame = ttk.LabelFrame(self.joker_page, text='Jokers')
        self.joker_frame.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        self.joker_scroll = ttk.Scrollbar(self.joker_frame, orient='vertical')
        self.joker_scroll.grid(row=0, column=1, sticky='ns')

        self.joker_canvas = tk.Canvas(self.joker_frame, yscrollcommand=self.joker_scroll.set, height=268)
        self.joker_canvas.grid(row=0, column=0, sticky='nsew') 

        self.joker_scroll.config(command=self.joker_canvas.yview)

        self.joker_frame_inner = ttk.Frame(self.joker_canvas)
        self.joker_canvas.create_window((0, 0), window=self.joker_frame_inner, anchor='nw')

        self.joker_scroll.bind('<Configure>', lambda e: self.joker_scroll.config(command=self.joker_canvas.yview))
        self.joker_frame_inner.bind('<Configure>', lambda e: self.joker_canvas.config(scrollregion=self.joker_canvas.bbox('all')))

        self.add_joker_btn = ttk.Button(self.joker_frame, text='Add Joker', command=self.add_joker)
        self.add_joker_btn.grid(row=1, column=0, padx=5, pady=5, sticky='ew',)

        # Map Joker Names to Lua Variable Names
        self.joker_mapping = {
			"Joker": "j_joker",
			"Greedy Joker": "j_greedy",
			"Lusty Joker": "j_lusty",
			"Wrathful Joker": "j_wrathful",
			"Gluttonous Joker": "j_gluttonous",
			"Jolly Joker": "j_jolly",
			"Zany Joker": "j_zany",
			"Mad Joker": "j_mad",
			"Crazy Joker": "j_crazy",
			"Droll Joker": "j_droll",
			"Sly Joker": "j_sly",
			"Wily Joker": "j_wily",
			"Clever Joker": "j_clever",
			"Devious Joker": "j_devious",
			"Crafty Joker": "j_crafty",
			"Half Joker": "j_half",
			"Joker Stencil": "j_stencil",
			"Four Fingers": "j_four_fingers",
			"Mime": "j_mime",
			"Credit Card": "j_credit_card",
			"Ceremonial Dagger": "j_ceremonial",
			"Banner": "j_banner",
			"Mystic Summit": "j_mystic_summit",
			"Marble Joker": "j_marble",
			"Loyalty Card": "j_loyalty_card",
			"8 Ball": "j_8_ball",
			"Misprint": "j_misprint",
			"Dusk": "j_dusk",
			"Raised Fist": "j_raised_fist",
			"Chaos the Clown": "j_chaos",
			"Fibonacci": "j_fibonacci",
			"Steel Joker": "j_steel",
			"Scary Face": "j_scary_face",
			"Abstract Joker": "j_abstract",
			"Delayed Gratification": "j_delayed_grat",
			"Hack": "j_hack",
			"Pareidolia": "j_pareidolia",
			"Gros Michel": "j_gros_michel",
			"Even Steven": "j_even_steven",
			"Odd Todd": "j_odd_todd",
			"Scholar": "j_scholar",
			"Business Card": "j_business",
			"Supernova": "j_supernova",
			"Ride the Bus": "j_ride_the_bus",
			"Space Joker": "j_space",
			"Egg": "j_egg",
			"Burglar": "j_burglar",
			"Blackboard": "j_blackboard",
			"Runner": "j_runner",
			"Ice Cream": "j_ice_cream",
			"DNA": "j_dna",
			"Splash": "j_splash",
			"Blue Joker": "j_blue_joker",
			"Sixth Sense": "j_sixth_sense",
			"Constellation": "j_constellation",
			"Hiker": "j_hiker",
			"Faceless Joker": "j_faceless",
			"Green Joker": "j_green_joker",
			"Superposition": "j_superposition",
			"To Do List": "j_todo_list",
			"Cavendish": "j_cavendish",
			"Card Sharp": "j_card_sharp",
			"Red Card": "j_red_card",
			"Madness": "j_madness",
			"Square Joker": "j_square",
			"Séance": "j_seance",
			"Riff-Raff": "j_riff_raff",
			"Vampire": "j_vampire",
			"Shortcut": "j_shortcut",
			"Hologram": "j_hologram",
			"Vagabond": "j_vagabond",
			"Baron": "j_baron",
			"Cloud 9": "j_cloud_9",
			"Rocket": "j_rocket",
			"Obelisk": "j_obelisk",
			"Midas Mask": "j_midas_mask",
			"Luchador": "j_luchador",
			"Photograph": "j_photograph",
			"Gift Card": "j_gift",
			"Turtle Bean": "j_turtle_bean",
			"Erosion": "j_erosion",
			"Reserved Parking": "j_reserved_parking",
			"Mail-In Rebate": "j_mail",
			"To the Moon": "j_to_the_moon",
			"Hallucination": "j_hallucination",
			"Fortune Teller": "j_fortune_teller",
			"Juggler": "j_juggler",
			"Drunkard": "j_drunkard",
			"Stone Joker": "j_stone",
			"Golden Joker": "j_golden",
			"Lucky Cat": "j_lucky_cat",
			"Baseball Card": "j_baseball",
			"Bull": "j_bull",
			"Diet Cola": "j_diet_cola",
			"Trading Card": "j_trading",
			"Flash Card": "j_flash",
			"Popcorn": "j_popcorn",
			"Spare Trousers": "j_trousers",
			"Ancient Joker": "j_ancient",
			"Ramen": "j_ramen",
			"Walkie Talkie": "j_walkie_talkie",
			"Seltzer": "j_seltzer",
			"Castle": "j_castle",
			"Smiley Face": "j_smiley",
			"Campfire": "j_campfire",
			"Golden Ticket": "j_ticket",
			"Mr. Bones": "j_mr_bones",
			"Acrobat": "j_acrobat",
			"Sock and Buskin": "j_sock_and_buskin",
			"Swashbuckler": "j_swashbuckler",
			"Troubadour": "j_troubadour",
			"Certificate": "j_certificate",
			"Smeared Joker": "j_smeared",
			"Throwback": "j_throwback",
			"Hanging Chad": "j_hanging_chad",
			"Rough Gem": "j_rough_gem",
			"Bloodstone": "j_bloodstone",
			"Arrowhead": "j_arrowhead",
			"Onyx Agate": "j_onyx_agate",
			"Glass Joker": "j_glass",
			"Showman": "j_ring_master",
			"Flower Pot": "j_flower_pot",
			"Blueprint": "j_blueprint",
			"Wee Joker": "j_wee",
			"Merry Andy": "j_merry_andy",
			"Oops! All 6s": "j_oops",
			"The Idol": "j_idol",
			"Seeing Double": "j_seeing_double",
			"Matador": "j_matador",
			"Hit the Road": "j_hit_the_road",
			"The Duo": "j_duo",
			"The Trio": "j_trio",
			"The Family": "j_family",
			"The Order": "j_order",
			"The Tribe": "j_tribe",
			"Stuntman": "j_stuntman",
			"Invisible Joker": "j_invisible",
			"Brainstorm": "j_brainstorm",
			"Satellite": "j_satellite",
			"Shoot the Moon": "j_shoot_the_moon",
			"Driver's License": "j_drivers_license",
			"Cartomancer": "j_cartomancer",
			"Astronomer": "j_astronomer",
			"Burnt Joker": "j_burnt",
			"Bootstraps": "j_bootstraps",
			"Canio": "j_caino",
			"Triboulet": "j_triboulet",
			"Yorick": "j_yorick",
			"Chicot": "j_chicot",
			"Perkeo": "j_perkeo",
		}

        # Map Joker Edition Names to Lua Variable Names
        self.joker_edition_mapping = {
            "Base": "base",
            "Foil": "foil",
            "Holographic": "holo",
            "Polychrome": "polychrome",
            "Negative": "negative",
        }

        self.joker_btn_frame = ttk.Frame(self.joker_page)
        self.joker_btn_frame.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

        self.back_button = ttk.Button(self.joker_btn_frame, text="Back", command=self.show_rules_page)
        self.back_button.grid(row=0, column=0, padx=5, pady=5, sticky='e')

        self.next_button = ttk.Button(self.joker_btn_frame, text="Next", command=self.show_deck_page)
        self.next_button.grid(row=0, column=4, padx=5, pady=5, sticky='w')  

        self.joker_btn_frame.grid_columnconfigure(2, weight=1)

        # Deck Page
        self.deck_page = ttk.Frame(self.root)

        self.deck_frame = ttk.Frame(self.deck_page)
        self.deck_frame.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        self.deck_canvas = tk.Canvas(self.deck_frame, height=322, width=399)
        self.deck_canvas.grid(row=0, column=0, sticky='nsew')

        self.deck_frame_inner = ttk.Frame(self.deck_canvas)
        self.deck_canvas.create_window((0, 0), window=self.deck_frame_inner, anchor='nw')

        self.decklabel = ttk.Label(self.deck_frame_inner, text="Deck:")
        self.decklabel.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        self.deck_types = [
            "Red",      
            "Blue",     
            "Yellow",   
            "Green",    
            "Black",    
            "Magic",    
            "Nebula",   
            "Ghost",    
            "Abandoned",
            "Checkered",
            "Zodiac",   
            "Painted",  
            "Anaglyph", 
            "Plasma",   
            "Erratic",  
            "Challenge",
        ]

        self.deckdd = ttk.Combobox(self.deck_frame_inner, values=self.deck_types, width=12) 
        self.deckdd.grid(row=0, column=1, padx=5, pady=5)

        self.excludelabel = ttk.Label(self.deck_frame_inner, text="Suits to Exclude:")
        self.excludelabel.grid(row=0, column=2, padx=5, pady=5, sticky='w')

        self.suits = {
            "spades": (tk.IntVar(), '♠'),
            "hearts": (tk.IntVar(), '♥'),
            "clubs": (tk.IntVar(), '♣'),
            "diamonds": (tk.IntVar(), '♦')
        }

        # Configure the column for the label
        self.deck_frame_inner.grid_columnconfigure(0, weight=0)

        # Configure the columns for the checkboxes
        for index in range(len(self.suits)):
            self.deck_frame_inner.grid_columnconfigure(index + 1, weight=1)  # Giving equal weight

        for index, (suit, (var, label)) in enumerate(self.suits.items()):
            cb = ttk.Checkbutton(self.deck_frame_inner, text=label, variable=var, command=self.limit_checkboxes)
            cb.grid(row=0, column=index + 3, padx=(5, 5), pady=5, sticky='ew')  # Use 'ew' for east-west stretching

        self.limit_checkboxes()
        

        # Map Rank Names to Lua Variable Names
        self.rank_mapping = {
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
            "10": "T",
            "Jack": "J",
            "Queen": "Q",
            "King": "K",
            "Ace": "A",
        }  

        self.enhancementlabel = ttk.Label(self.deck_frame_inner, text="Enhancement:")
        self.enhancementlabel.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        # Map Enhancement Names to Lua Variable Names
        self.enhancement_mapping = {
            "None": "",
			"Bonus": "c_bonus",
			"Mult": "m_mult",
            "Wild Card": "m_wild",
            "Glass Card": "m_glass",
            "Steel Card": "m_steel",
            "Stone Card": "m_stone",
            "Gold Card": "m_gold",
            "Lucky Card": "m_lucky",
        }

        self.enhancementdd = ttk.Combobox(self.deck_frame_inner, values=self.enhancement_mapping, width=12) 
        self.enhancementdd.grid(row=1, column=1, padx=5, pady=5)

        self.cardeditionlabel = ttk.Label(self.deck_frame_inner, text="Edition:")
        self.cardeditionlabel.grid(row=1, column=2, padx=5, pady=5, sticky='w')

        # Map Card Edition Names to Lua Variable Names
        self.card_edition_mapping = {
            "Base": "e_base",
            "Foil": "e_foil",
            "Holographic": "e_holo",
            "Polychrome": "e_polychrome",
        }    

        self.cardeditiondd = ttk.Combobox(self.deck_frame_inner, values=self.card_edition_mapping, width=12) 
        self.cardeditiondd.grid(row=1, column=3, padx=5, pady=5)
        
        # Map Seal Names to Lua Variable Names
        self.seal_mapping = {
            "None": "",
            "Gold": "Gold",
            "Red": "Red",
            "Blue": "Blue",
            "Purple": "Purple",
        }

        # Deck Page Navigation
        self.deck_btn_frame = ttk.Frame(self.deck_page)
        self.deck_btn_frame.grid(row=7, column=0, padx=5, pady=5, sticky='ew')

        self.back_button = ttk.Button(self.deck_btn_frame, text="Back", command=self.show_joker_page)
        self.back_button.grid(row=0, column=0, padx=5, pady=5, sticky='e')

        self.next_button = ttk.Button(self.deck_btn_frame, text="Next", command=self.show_card_page)
        self.next_button.grid(row=0, column=4, padx=5, pady=5, sticky='w')  

        self.deck_btn_frame.grid_columnconfigure(2, weight=1)

        # Card Page
        self.card_page = ttk.Frame(self.root)

        # Disclaimer
        self.warninglabel = ttk.Label(self.card_page, text="WARNING! Adding ANY cards this way for final processing will overwrite \n ALL Deck generation performed on the previous page bar Deck Type.")
        self.warninglabel.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        # Card Section
        self.card_entries = []
        self.card_frame = ttk.LabelFrame(self.card_page, text='Cards')
        self.card_frame.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

        self.card_scroll = ttk.Scrollbar(self.card_frame, orient='vertical')
        self.card_scroll.grid(row=0, column=1, sticky='ns')

        self.card_canvas = tk.Canvas(self.card_frame, yscrollcommand=self.card_scroll.set, height=224)
        self.card_canvas.grid(row=0, column=0, sticky='nsew')

        self.card_scroll.config(command=self.card_canvas.yview)

        self.card_frame_inner = ttk.Frame(self.card_canvas)
        self.card_canvas.create_window((0, 0), window=self.card_frame_inner, anchor='nw')

        self.card_scroll.bind('<Configure>', lambda e: self.card_scroll.config(command=self.card_canvas.yview))
        self.card_frame_inner.bind('<Configure>', lambda e: self.card_canvas.config(scrollregion=self.card_canvas.bbox('all')))

        self.add_card_btn = ttk.Button(self.card_frame, text='Add Card', command=self.add_card)
        self.add_card_btn.grid(row=3, column=0, padx=5, pady=5, sticky='ew')

        self.card_btn_frame = ttk.Frame(self.card_page)
        self.card_btn_frame.grid(row=4, column=0, padx=5, pady=5, sticky='ew')

        self.back_button = ttk.Button(self.card_btn_frame, text="Back", command=self.show_deck_page)
        self.back_button.grid(row=0, column=0, padx=5, pady=5, sticky='e')

        self.next_button = ttk.Button(self.card_btn_frame, text="Next", command=self.show_consum_vouch_page)
        self.next_button.grid(row=0, column=4, padx=5, pady=5, sticky='w')  

        self.card_btn_frame.grid_columnconfigure(2, weight=1)

        # Map Suit Names to Lua Variable Names
        self.suit_mapping = {
            "Hearts": "H",
            "Diamonds": "D",
            "Spades": "S",
            "Clubs": "C",
        }  
        
        # Consumables and Vouchers Page
        self.consum_vouch_page = ttk.Frame(self.root)

        # Consumables Section
        self.consumable_entries = []

        self.consumable_frame = ttk.LabelFrame(self.consum_vouch_page, text='Consumables')
        self.consumable_frame.grid(row=0, column=0, padx=5, pady=5, sticky='ew')
		
        self.consumable_scroll = ttk.Scrollbar(self.consumable_frame, orient='vertical')
        self.consumable_scroll.grid(row=0, column=1, sticky='ns')
		
        self.consumable_canvas = tk.Canvas(self.consumable_frame, yscrollcommand=self.consumable_scroll.set, height=100)
        self.consumable_canvas.grid(row=0, column=0, sticky='nsew')
		
        self.consumable_scroll.config(command=self.consumable_canvas.yview)
		
        self.consumable_frame_inner = ttk.Frame(self.consumable_canvas)
        self.consumable_canvas.create_window((0, 0), window=self.consumable_frame_inner, anchor='nw')
		
        self.consumable_scroll.bind('<Configure>', lambda e: self.consumable_scroll.config(command=self.consumable_canvas.yview))
        self.consumable_frame_inner.bind('<Configure>', lambda e: self.consumable_canvas.config(scrollregion=self.consumable_canvas.bbox('all')))
		
        self.add_consumable_btn = ttk.Button(self.consumable_frame, text='Add Consumable', command=self.add_consumable)
        self.add_consumable_btn.grid(row=1, column=0, padx=5, pady=5, sticky='ew',)
		
        self.consumable_mapping = {
            # Tarot Cards
			"The Fool": "c_fool",
			"The Magician": "c_magician",
			"The High Priestess": "c_high_priestess",
			"The Empress": "c_empress",
			"The Emperor": "c_emperor",
			"The Hierophant": "c_heirophant",
			"The Lovers": "c_lovers",
			"The Chariot": "c_chariot",
			"Justice": "c_justice",
			"The Hermit": "c_hermit",
			"The Wheel of Fortune": "c_wheel_of_fortune",
			"Strength": "c_strength",
			"The Hanged Man": "c_hanged_man",
			"Death": "c_death",
			"Temperance": "c_temperance",
			"The Devil": "c_devil",
			"The Tower": "c_tower",
			"The Star": "c_star",
			"The Moon": "c_moon",
			"The Sun": "c_sun",
			"Judgement": "c_judgement",
			"The World": "c_world",

        # Planet Cards
			"Mercury": "c_mercury",
			"Venus": "c_venus",
			"Earth": "c_earth",
			"Mars": "c_mars",
			"Jupiter": "c_jupiter",
			"Saturn": "c_saturn",
			"Uranus": "c_uranus",
			"Neptune": "c_neptune",
			"Pluto": "c_pluto",
			"Planet X": "c_planet_x",
			"Ceres": "c_ceres",
			"Eris": "c_eris",

        # Spectral Cards
			"Familiar": "c_familiar",
			"Grim": "c_grim",
			"Incantation": "c_incantation",
			"Talisman": "c_talisman",
			"Aura": "c_aura",
			"Wraith": "c_wraith",
			"Sigil": "c_sigil",
			"Ouija": "c_ouija",
			"Ectoplasm": "c_ectoplasm",
			"Immolate": "c_immolate",
			"Ankh": "c_ankh",
			"Deja Vu": "c_deja_vu",
			"Hex": "c_hex",
			"Trance": "c_trance",
			"Medium": "c_medium",
			"Cryptid": "c_cryptid",
			"Soul": "c_soul",
			"Black Hole": "c_black_hole",           
        }

        # Voucher Section
        self.voucher_entries = []
        self.voucher_frame = ttk.LabelFrame(self.consum_vouch_page, text='Vouchers')
        self.voucher_frame.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

        self.voucher_scroll = ttk.Scrollbar(self.voucher_frame, orient='vertical')
        self.voucher_scroll.grid(row=0, column=1, sticky='ns')

        self.voucher_canvas = tk.Canvas(self.voucher_frame, yscrollcommand=self.voucher_scroll.set, height=135)
        self.voucher_canvas.grid(row=0, column=0, sticky='nsew')

        self.voucher_scroll.config(command=self.voucher_canvas.yview)

        self.voucher_frame_inner = ttk.Frame(self.voucher_canvas)
        self.voucher_canvas.create_window((0, 0), window=self.voucher_frame_inner, anchor='nw')

        self.voucher_scroll.bind('<Configure>', lambda e: self.voucher_scroll.config(command=self.voucher_canvas.yview))
        self.voucher_frame_inner.bind('<Configure>', lambda e: self.voucher_canvas.config(scrollregion=self.voucher_canvas.bbox('all')))

        # Map Voucher Names to Lua Variable Names
        self.voucher_mapping = {
            "Overstock": ["v_overstock_norm", "v_overstock_plus"],
            "Clearance Sale": ["v_clearance_sale", "v_liquidation"],
            "Hone": ["v_hone", "v_glow_up"],
            "Reroll Surplus": ["v_reroll_surplus", "v_reroll_glut"],
            "Crystal Ball": ["v_crystal_ball", "v_omen_globe"],
            "Telescope": ["v_telescope", "v_observatory"],
            "Grabber": ["v_grabber", "v_nacho_tong"],
            "Wasteful": ["v_wasteful", "v_recyclomancy"],
            "Tarot Merchant": ["v_tarot_merchant", "v_tarot_tycoon"],
            "Planet Merchant": ["v_planet_merchant", "v_planet_tycoon"],
            "Seed Money": ["v_seed_money", "v_money_tree"],
            "Blank": ["v_blank", "v_antimatter"],
            "Magic Trick": ["v_magic_trick", "v_illusion"],
            "Hieroglyph": ["v_hieroglyph", "v_petroglyph"],
            "Directors Cut": ["v_directors_cut", "v_retcon"],
            "Paint Brush": ["v_paint_brush", "v_palette"]
        }

        # Map Voucher Names to Lua Variable Names for banning vouchers
        self.banned_voucher_mapping = {
            "Overstock": "v_overstock_norm",
            "Overstock Plus": "v_overstock_plus",
            "Clearance Sale": "v_clearance_sale",
            "Liquidation": "v_liquidation",
            "Hone": "v_hone",
            "Glow Up": "v_glow_up",
            "Reroll Surplus": "v_reroll_surplus",
            "Reroll Glut": "v_reroll_glut",
            "Crystal Ball": "v_crystal_ball",
            "Omen Globe": "v_omen_globe",
            "Telescope": "v_telescope",
            "Observatory": "v_observatory",
            "Grabber": "v_grabber",
            "Nacho Tong": "v_nacho_tong",
            "Wasteful": "v_wasteful",
            "Recyclomancy": "v_recyclomancy",
            "Tarot Merchant": "v_tarot_merchant",
            "Tarot Tycoon": "v_tarot_tycoon",
            "Planet Merchant": "v_planet_merchant",
            "Planet Tycoon": "v_planet_tycoon",
            "Seed Money": "v_seed_money",
            "Money Tree": "v_money_tree",
            "Blank": "v_blank",
            "Antimatter": "v_antimatter",
            "Magic Trick": "v_magic_trick",
            "Illusion": "v_illusion",
            "Hieroglyph": "v_hieroglyph",
            "Petroglyph": "v_petroglyph",
            "Directors Cut": "v_directors_cut",
            "Retcon": "v_retcon",
            "Paint Brush": "v_paint_brush",
            "Palette": "v_palette"
        }

        # Store the BooleanVars for voucher checkbox states
        self.voucher_vars = []

        # Create labels for titles
        for i, title in enumerate(self.voucher_mapping.keys()):
            voucher_label = ttk.Label(self.voucher_frame_inner, text=title)
            voucher_label.grid(row=i, column=0, padx=5, pady=5, sticky='w')

            base_var = tk.BooleanVar()
            upgrade_var = tk.BooleanVar()

            # Add the variables to keep track of them
            self.voucher_vars.append((base_var, upgrade_var, title))
    
            # Callback to manage the Checkbutton interactions
            def update_checkbuttons(*args, base_var=base_var, upgrade_var=upgrade_var):
                if upgrade_var.get():  # If Upgrade is checked
                    base_var.set(True)  # Check Base
                if not base_var.get():  # If Base is unchecked
                    upgrade_var.set(False)  # Uncheck Upgrade

            base_checkbutton = ttk.Checkbutton(self.voucher_frame_inner, variable=base_var, text='Base')
            base_checkbutton.grid(row=i, column=1, padx=5, pady=5, sticky='w')

            upgrade_checkbutton = ttk.Checkbutton(self.voucher_frame_inner, variable=upgrade_var, text='Upgrade')
            upgrade_checkbutton.grid(row=i, column=2, padx=5, pady=5, sticky='w')

            # Trace the base variable to update the upgrade checkbox
            base_var.trace_add('write', update_checkbuttons)
            upgrade_var.trace_add('write', update_checkbuttons)

        self.consum_vouch_btn_frame = ttk.Frame(self.consum_vouch_page)
        self.consum_vouch_btn_frame.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

        self.back_button = ttk.Button(self.consum_vouch_btn_frame, text="Back", command=self.show_card_page)
        self.back_button.grid(row=0, column=0, padx=5, pady=5, sticky='e')

        self.next_button = ttk.Button(self.consum_vouch_btn_frame, text="Next", command=self.show_restrictions_page)
        self.next_button.grid(row=0, column=4, padx=5, pady=5, sticky='w')  

        self.consum_vouch_btn_frame.grid_columnconfigure(2, weight=1)

        # Restrictions Page
        self.restrictions_page = ttk.Frame(self.root)

        # Banned Cards Section
        self.banned_card_entries = []
        self.banned_cards_frame = ttk.LabelFrame(self.restrictions_page, text='Banned Cards')
        self.banned_cards_frame.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        self.banned_cards_scroll = ttk.Scrollbar(self.banned_cards_frame, orient='vertical')
        self.banned_cards_scroll.grid(row=0, column=1, sticky='ns')

        self.banned_cards_canvas = tk.Canvas(self.banned_cards_frame, yscrollcommand=self.banned_cards_scroll.set, height=100)
        self.banned_cards_canvas.grid(row=0, column=0, sticky='nsew')

        self.banned_cards_scroll.config(command=self.banned_cards_canvas.yview)

        self.banned_cards_frame_inner = ttk.Frame(self.banned_cards_canvas)
        self.banned_cards_canvas.create_window((0, 0), window=self.banned_cards_frame_inner, anchor='nw')

        self.banned_cards_scroll.bind('<Configure>', lambda e: self.banned_cards_scroll.config(command=self.banned_cards_canvas.yview))
        self.banned_cards_frame_inner.bind('<Configure>', lambda e: self.banned_cards_canvas.config(scrollregion=self.banned_cards_canvas.bbox('all')))

        self.add_banned_card_btn = ttk.Button(self.banned_cards_frame, text='Add Banned Card', command=self.add_banned_card)
        self.add_banned_card_btn.grid(row=1, column=0, padx=5, pady=5, sticky='ew',)

        # Map Packs to Lua Variable
        self.pack_mapping = {
            "Arcana Pack 1": "p_arcana_normal_1",
            "Arcana Pack 2": "p_arcana_normal_2",
            "Arcana Pack 3": "p_arcana_normal_3",
            "Arcana Pack 4": "p_arcana_normal_4",
            "Jumbo Arcana Pack 1": "p_arcana_jumbo_1",
            "Jumbo Arcana Pack 2": "p_arcana_jumbo_2",
            "Mega Arcana Pack 1": "p_arcana_mega_1",
            "Mega Arcana Pack 2": "p_arcana_mega_2",
            "Celestial Pack 1": "p_celestial_normal_1",
            "Celestial Pack 2": "p_celestial_normal_2",
            "Celestial Pack 3": "p_celestial_normal_3",
            "Celestial Pack 4": "p_celestial_normal_4",
            "Jumbo Celestial Pack 1": "p_celestial_jumbo_1",
            "Jumbo Celestial Pack 2": "p_celestial_jumbo_2",
            "Mega Celestial Pack 1": "p_celestial_mega_1",
            "Mega Celestial Pack 2": "p_celestial_mega_2",
            "Spectral Pack 1": "p_spectral_normal_1",
            "Spectral Pack 2": "p_spectral_normal_2",
            "Jumbo Spectral Pack": "p_spectral_jumbo_1",
            "Mega Spectral Pack": "p_spectral_mega_1",
            "Standard Pack 1": "p_standard_normal_1",
            "Standard Pack 2": "p_standard_normal_2",
            "Standard Pack 3": "p_standard_normal_3",
            "Standard Pack 4": "p_standard_normal_4",
            "Jumbo Standard Pack 1": "p_standard_jumbo_1",
            "Jumbo Standard Pack 2": "p_standard_jumbo_2",
            "Mega Standard Pack 1": "p_standard_mega_1",
            "Mega Standard Pack 2": "p_standard_mega_2",
            "Buffoon Pack 1": "p_buffoon_normal_1",
            "Buffoon Pack 2": "p_buffoon_normal_2",
            "Jumbo Buffoon Pack": "p_buffoon_jumbo_1",
            "Mega Buffoon Pack": "p_buffoon_mega_1",
        }

        # Map Banned Cards to Lua Vaiable
        self.banned_card_mapping = {**self.joker_mapping, **self.consumable_mapping, **self.banned_voucher_mapping, **self.pack_mapping}

        # Banned Tags Section
        self.banned_tag_entries = []
        self.banned_tags_frame = ttk.LabelFrame(self.restrictions_page, text='Banned Tags')
        self.banned_tags_frame.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

        self.banned_tags_scroll = ttk.Scrollbar(self.banned_tags_frame, orient='vertical')
        self.banned_tags_scroll.grid(row=0, column=1, sticky='ns')

        self.banned_tags_canvas = tk.Canvas(self.banned_tags_frame, yscrollcommand=self.banned_tags_scroll.set, height=100)
        self.banned_tags_canvas.grid(row=0, column=0, sticky='nsew')

        self.banned_tags_scroll.config(command=self.banned_tags_canvas.yview)

        self.banned_tags_frame_inner = ttk.Frame(self.banned_tags_canvas)
        self.banned_tags_canvas.create_window((0, 0), window=self.banned_tags_frame_inner, anchor='nw')

        self.banned_tags_scroll.bind('<Configure>', lambda e: self.banned_tags_scroll.config(command=self.banned_tags_canvas.yview))
        self.banned_tags_frame_inner.bind('<Configure>', lambda e: self.banned_tags_canvas.config(scrollregion=self.banned_tags_canvas.bbox('all')))

        self.add_banned_tag_btn = ttk.Button(self.banned_tags_frame, text='Add Banned Tag', command=self.add_banned_tag)
        self.add_banned_tag_btn.grid(row=1, column=0, padx=5, pady=5, sticky='ew',)

        # Map Tags to Lua Variable
        self.tag_mapping = {
            'Uncommon Tag': 'tag_uncommon',
            'Rare Tag': 'tag_rare',
            'Negative Tag': 'tag_negative',
            'Foil Tag': 'tag_foil',
            'Holographic Tag': 'tag_holo',
            'Polychrome Tag': 'tag_polychrome',
            'Investment Tag': 'tag_investment',
            'Voucher Tag': 'tag_voucher',
            'Boss Tag': 'tag_boss',
            'Standard Tag': 'tag_standard',
            'Charm Tag': 'tag_charm',
            'Meteor Tag': 'tag_meteor',
            'Buffoon Tag': 'tag_buffoon',
            'Handy Tag': 'tag_handy',
            'Garbage Tag': 'tag_garbage',
            'Ethereal Tag': 'tag_ethereal',
            'Coupon Tag': 'tag_coupon',
            'Double Tag': 'tag_double',
            'Juggle Tag': 'tag_juggle',
            'D6 Tag': 'tag_d_six',
            'Top-up Tag': 'tag_top_up',
            'Skip Tag': 'tag_skip',
            'Orbital Tag': 'tag_orbital',
            'Economy Tag': 'tag_economy',
        }

        self.restrictions_btn_frame = ttk.Frame(self.restrictions_page)
        self.restrictions_btn_frame.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

        self.back_button = ttk.Button(self.restrictions_btn_frame, text="Back", command=self.show_consum_vouch_page)
        self.back_button.grid(row=0, column=0, padx=5, pady=5, sticky='e')

        self.next_button = ttk.Button(self.restrictions_btn_frame, text="Next", command=self.show_save_page)
        self.next_button.grid(row=0, column=4, padx=5, pady=5, sticky='w')  

        self.restrictions_btn_frame.grid_columnconfigure(2, weight=1)

        # Save Page
        self.save_page = ttk.Frame(self.root)

        # Banned Others Section
        self.banned_other_entries = []
        self.banned_others_frame = ttk.LabelFrame(self.save_page, text='Banned Others')
        self.banned_others_frame.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        self.banned_others_scroll = ttk.Scrollbar(self.banned_others_frame, orient='vertical')
        self.banned_others_scroll.grid(row=0, column=1, sticky='ns')

        self.banned_others_canvas = tk.Canvas(self.banned_others_frame, yscrollcommand=self.banned_others_scroll.set, height=232)
        self.banned_others_canvas.grid(row=0, column=0, sticky='nsew')

        self.banned_others_scroll.config(command=self.banned_others_canvas.yview)

        self.banned_others_frame_inner = ttk.Frame(self.banned_others_canvas)
        self.banned_others_canvas.create_window((0, 0), window=self.banned_others_frame_inner, anchor='nw')

        self.banned_others_scroll.bind('<Configure>', lambda e: self.banned_others_scroll.config(command=self.banned_others_canvas.yview))
        self.banned_others_frame_inner.bind('<Configure>', lambda e: self.banned_others_canvas.config(scrollregion=self.banned_others_canvas.bbox('all')))

        self.add_banned_other_btn = ttk.Button(self.banned_others_frame, text='Add Banned Other', command=self.add_banned_other)
        self.add_banned_other_btn.grid(row=1, column=0, padx=5, pady=5, sticky='ew',)

        # Map Others to Lua Variable
        self.other_mapping = {
            "Small Blind": "bl_small",
            "Big Blind": "bl_big",
            "The Ox": "bl_ox",
            "The Hook": "bl_hook",
            "The Mouth": "bl_mouth",
            "The Fish": "bl_fish",
            "The Club": "bl_club",
            "The Manacle": "bl_manacle",
            "The Tooth": "bl_tooth",
            "The Wall": "bl_wall",
            "The House": "bl_house",
            "The Mark": "bl_mark",
            "Cerulean Bell": "bl_final_bell",
            "The Wheel": "bl_wheel",
            "The Arm": "bl_arm",
            "The Psychic": "bl_psychic",
            "The Goad": "bl_goad",
            "The Water": "bl_water",
            "The Eye": "bl_eye",
            "The Plant": "bl_plant",
            "The Needle": "bl_needle",
            "The Head": "bl_head",
            "Verdant Leaf": "bl_final_leaf",
            "Violet Vessel": "bl_final_vessel",
            "The Window": "bl_window",
            "The Serpent": "bl_serpent",
            "The Pillar": "bl_pillar",
            "The Flint": "bl_flint",
            "Amber Acorn": "bl_final_acorn",
            "Crimson Heart": "bl_final_heart",
        }

        # Save Button
        self.save_btn_frame = ttk.Frame(self.save_page)
        self.save_btn_frame.grid(row=1, column=0, padx=5, pady=5)

        self.save_btn = ttk.Button(self.save_btn_frame, text='Save to Lua File', command=self.save_to_file)
        self.save_btn.grid(row=0, column=1, padx=5)
   
        self.SMODS_var = tk.BooleanVar(value=True)
        self.BUCB_var = tk.BooleanVar(value=False)

        def update_output(*args):
            if self.BUCB_var.get():  # If BUCB is checked
                self.SMODS_var.set(False)  # Uncheck SMODS
            elif self.SMODS_var.get():  # If SMODS is checked
                self.BUCB_var.set(False)  # Uncheck BUCB
            if not self.SMODS_var.get() and not self.BUCB_var.get():
                self.SMODS_var.set(True)
        
        SMODS_checkbutton = ttk.Checkbutton(self.save_btn_frame, variable=self.SMODS_var, text='SMODS')
        SMODS_checkbutton.grid(row=0, column=2, padx=5)

        BUCB_checkbutton = ttk.Checkbutton(self.save_btn_frame, variable=self.BUCB_var, text='BU-CB')
        BUCB_checkbutton.grid(row=0, column=3, padx=5)
        
        self.SMODS_var.trace_add('write', update_output)  
        self.BUCB_var.trace_add('write', update_output)

        self.save_page_btn_frame = ttk.Frame(self.save_page)
        self.save_page_btn_frame.grid(row=2, column=0, padx=5, pady=5)

        self.back_button = ttk.Button(self.save_page_btn_frame, text="Back", command=self.show_restrictions_page)
        self.back_button.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        
    def show_info_page(self):
        self.rules_page.pack_forget()
        self.info_page.pack(padx=10, pady=10, fill='both', expand=True)

    def show_rules_page(self):
        self.info_page.pack_forget()
        self.joker_page.pack_forget()
        self.rules_page.pack(padx=10, pady=10, fill='both', expand=True)    

    def show_joker_page(self):
        self.rules_page.pack_forget()
        self.deck_page.pack_forget()
        self.joker_page.pack(padx=10, pady=10, fill='both', expand=True)

    def show_deck_page(self):
        self.joker_page.pack_forget()
        self.card_page.pack_forget()
        self.deck_page.pack(padx=10, pady=10, fill='both', expand=True)

    def limit_checkboxes(self):
        checked_count = sum(var.get() for var, _ in self.suits.values())

        if checked_count > 3:
            for var, _ in self.suits.values():
                if var.get() == 1:
                    var.set(0)
                    checked_count -= 1
                    if checked_count <= 3:
                        break

    def show_card_page(self):
        self.deck_page.pack_forget()
        self.consum_vouch_page.pack_forget()
        self.card_page.pack(padx=10, pady=10, fill='both', expand=True)

    def show_consum_vouch_page(self):
        self.card_page.pack_forget()
        self.restrictions_page.pack_forget()
        self.consum_vouch_page.pack(padx=10, pady=10, fill='both', expand=True) 

    def show_restrictions_page(self):
        self.consum_vouch_page.pack_forget()
        self.save_page.pack_forget()
        self.restrictions_page.pack(padx=10, pady=10, fill='both', expand=True)

    def show_save_page(self):
        self.restrictions_page.pack_forget()
        self.save_page.pack(padx=10, pady=10, fill='both', expand=True)

    def add_local(self):
        entry = LocalEntry(self.local_frame_inner, self.remove_local, self.local_mapping)
        self.local_entries.append(entry)

    def remove_local(self, entry):
        entry.destroy()
        self.local_entries.remove(entry)

    def add_custom(self):
        entry = CustomEntry(self.custom_frame_inner, self.remove_custom, self.custom_mapping)
        self.custom_entries.append(entry)

    def remove_custom(self, entry):
        entry.destroy()
        self.custom_entries.remove(entry)

    def add_modifier(self):
        entry = ModifiersEntry(self.modifier_frame_inner, self.remove_modifier, self.modifier_mapping)
        self.modifier_entries.append(entry)

    def remove_modifier(self, entry):
        entry.destroy()
        self.modifier_entries.remove(entry)

    def add_joker(self):
        entry = JokersEntry(self.joker_frame_inner, self.remove_joker, self.joker_mapping, self.joker_edition_mapping)
        self.joker_entries.append(entry)

    def remove_joker(self, entry):
        entry.destroy()
        self.joker_entries.remove(entry)

    def add_card(self):
        entry = CardsEntry(self.card_frame_inner, self.remove_card, self.suit_mapping, self.rank_mapping, self.enhancement_mapping, self.seal_mapping)
        self.card_entries.append(entry)

    def remove_card(self, entry):
        entry.destroy()
        self.card_entries.remove(entry)

    def add_consumable(self):
        entry = ConsumablesEntry(self.consumable_frame_inner, self.remove_consumable, self.consumable_mapping)
        self.consumable_entries.append(entry)

    def remove_consumable(self, entry):
        entry.destroy()
        self.consumable_entries.remove(entry)

    def add_banned_card(self):
        entry = BannedCardsEntry(self.banned_cards_frame_inner, self.remove_banned_card, self.banned_card_mapping)
        self.banned_card_entries.append(entry)

    def remove_banned_card(self, entry):
        entry.destroy()
        self.banned_card_entries.remove(entry)

    def add_banned_tag(self):
        entry = BannedTagsEntry(self.banned_tags_frame_inner, self.remove_banned_tag, self.tag_mapping)
        self.banned_tag_entries.append(entry)

    def remove_banned_tag(self, entry):
        entry.destroy()
        self.banned_tag_entries.remove(entry)

    def add_banned_other(self):
        entry = BannedOthersEntry(self.banned_others_frame_inner, self.remove_banned_other, self.other_mapping)
        self.banned_other_entries.append(entry)

    def remove_banned_other(self, entry):
        entry.destroy()
        self.banned_other_entries.remove(entry)

    def save_to_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".lua", filetypes=[("Lua files", "*.lua")])
        if file_path:
            try:
                with open(file_path, 'w') as f:
                    f.write(self.generate_lua_code())
                messagebox.showinfo("Success", "Lua file saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

    def generate_lua_code(self):

        lua_code = ""

        # Generate Mod Info for SMODS
        if self.SMODS_var.get():
            lua_code = "--- STEAMODDED HEADER\n"
            
            modnameout = self.modname.get()
            if modnameout:
                lua_code += f"--- MOD_NAME: {modnameout}\n"
            else:
                lua_code += "--- MOD_NAME: Generated Challenge"
            
            modidout = self.modid.get()    
            if modidout:
                lua_code += f"--- MOD_ID: {modidout}\n"
            else:
                lua_code += "--- MOD_ID: genchal\n"
            
            authorout = self.author.get()
            if authorout:
                lua_code += f"--- MOD_AUTHOR: [{authorout}]\n"
            else:
                lua_code += "--- MOD_AUTHOR: [HoneySoakedSeagull's Challenge Generator]\n"
            
            moddescout = self.moddesc.get("1.0", "end")
            if moddescout:
                lua_code += f"--- MOD_DESCRIPTION: {moddescout}\n"
            else:
                lua_code += "--- MOD_DESCRIPTION: A challenge generated with HoneySoakedSeagull's Challenge Generator.\n"

            versionout = self.version.get()
            if versionout:
                lua_code += f"--- VERSION: {versionout}\n\n"
            else:
                lua_code += f"--- VERSION: 1.0.0\n\n"    
            
            lua_code += "SMODS.Challenge {\n"

            if modnameout: 
                lua_code += f"    name = '{modnameout}',\n"
            else:
                lua_code += "    name = 'Custom Generated Challenge',\n"

            if modidout:
                lua_code += f"    key = '{modidout}',\n\n"
            else:
                lua_code += "    key = 'genchal',\n\n"

            # SMODS Localization 'Generation'
            lua_code += "    loc_txt = {\n"
            if self.local_entries:
                for entry in self.local_entries:
                    local_lang = entry.localdd.get()
                    local_name = entry.local_title.get()
                    local_lua = self.local_mapping.get(local_lang, local_lang)
                    lua_code += f"        ['{local_lua}'] = {{name = '{local_name}'}},\n"
            else:
                lua_code += "        ['en-us'] = {name = 'Genchal'}\n"
            lua_code += "    },\n"
            
        # Generate Mod Start for BU-CB
        elif self.BUCB_var.get():
            lua_code +=  "Challenge:new({\n"

            modidout = self.modid.get()    
            if modidout:
                lua_code += f"    id = '{modidout}',\n"
            else:
                lua_code += "    id = 'generated_challenge',\n"

            modnameout = self.modname.get()
            if modnameout:
                lua_code += f"    name = '{modnameout}'\n"
            else:
                lua_code += "    name = 'Generated_Challenge'\n"

            authorout = self.author.get()
            if authorout:
                lua_code += f"    author = '{authorout}'\n"
            else:
                lua_code += "    author = 'HoneySoakedSeagull's Challenge Generator'\n"

            versionout = self.version.get()
            if versionout:
                lua_code += f"    version = '{versionout}'\n"
            else:
                lua_code += f"    version = '1.0.0'\n"

            lua_code += "    config = {\n"

        # Generate Rules    
        lua_code += "    rules = {\n"
        lua_code += "        custom = {\n"
        if self.custom_entries:
            for entry in self.custom_entries:
                custom_name = entry.customdd.get()
                customvalue = entry.get_custom_value()
                custom_lua = self.custom_mapping.get(custom_name, custom_name)
                lua_code += f"            {{id = '{custom_lua}'"
                if customvalue:
                    if custom_lua == 'set_seed':
                        lua_code += f", value = '{customvalue}'"
                    else:
                        lua_code += f", value = {customvalue}"
                lua_code += f"}},\n"
        lua_code += "        },\n"

        lua_code += "        modifiers = {\n"
        if self.modifier_entries:
            for entry in self.modifier_entries:
                modifier_name = entry.modifierdd.get()
                modifier_value = entry.get_modifier_value()
                modifier_lua = self.modifier_mapping.get(modifier_name, modifier_name)
                lua_code += f"            {{id = '{modifier_lua}', value = {modifier_value}}},"
        lua_code += "        }\n"
        lua_code += "    },\n"
        
        # Generate Joker code
        if self.joker_entries:
            lua_code += "    jokers = {\n"
            for entry in self.joker_entries:
                joker_name = entry.jokerdd.get()
                edition_name = entry.jokereddd.get()
                joker_lua = self.joker_mapping.get(joker_name, joker_name)
                eternal_value = entry.eternal_var.get()
                edition_lua = self.joker_edition_mapping.get(edition_name, edition_name)
                lua_code += f"        {{id = '{joker_lua}', eternal = {str(eternal_value).lower()}, edition = '{edition_lua}'}},\n"
            lua_code += "    },\n"

        # Generate Consumable code
        if self.consumable_entries:
            lua_code += "    consumeables = {\n"
            for entry in self.consumable_entries:
                consumable_name = entry.consumabledd.get()
                consumable_lua = self.consumable_mapping.get(consumable_name, consumable_name)
                lua_code += f"        {{id = '{consumable_lua}'}},\n"
            lua_code += "    },\n"

        # Generate Voucher code
        if self.voucher_vars:
            lua_code += "    vouchers = {\n"
            for base_var, upgrade_var, title in self.voucher_vars:
                # Only include if either base or upgrade is checked
                if base_var.get() or upgrade_var.get():
                    lua_var_list = self.voucher_mapping[title]
                    if base_var.get():
                        lua_code += f"        {{id = '{lua_var_list[0]}'}},\n"
                    if upgrade_var.get():
                        lua_code += f"        {{id = '{lua_var_list[1]}'}},\n"
            lua_code += "    },\n"
          
        # Generate Card code
        lua_code += "    deck = {\n"
        if self.card_entries:
            lua_code += "        cards = {"
            for entry in self.card_entries:
                # Get Selected Inputs
                suit_name = entry.suitdd.get()
                rank_name = entry.rankdd.get()
                enhancement_name = entry.enhancementdd.get()
                seal_name = entry.sealdd.get()

                # Get Dictionary Names
                suit_lua = self.suit_mapping.get(suit_name, suit_name)
                rank_lua = self.rank_mapping.get(rank_name, rank_name)
                enhancement_lua = self.enhancement_mapping.get(enhancement_name, enhancement_name)
                seal_lua = self.seal_mapping.get(seal_name, seal_name)

                # Generate Card Code Without Enhancements or Seals
                lua_code += f"{{s='{suit_lua}', r='{rank_lua}'"

                # Add Enhancement code if applicable
                if enhancement_lua:
                    lua_code += f",e='{enhancement_lua}'"

                # Add Seal code if applicable
                if seal_lua:
                    lua_code += f",g='{seal_lua}'"

                lua_code += "},"
            lua_code += "}, \n"
        
        # Generate Deck type
        deck_name = self.deckdd.get()
        if deck_name:
            lua_code += f"        type = '{deck_name}'\n      }},\n"
        else:
            lua_code += "        type = 'Challenge Deck'\n      },\n"

        # Generate restrictions
        lua_code += "    restrictions = {\n"

        lua_code += "        banned_cards = {\n"
        if self.banned_card_entries:
            for entry in self.banned_card_entries:
                banned_card_name = entry.bannedcarddd.get()
                banned_card_lua = self.banned_card_mapping.get(banned_card_name, banned_card_name)
                lua_code += f"            {{id = '{banned_card_lua}'}},\n"
        lua_code += "        },\n"

        lua_code += "        banned_tags = {\n"
        if self.banned_tag_entries:
            for entry in self.banned_tag_entries:
                banned_tag_name = entry.bannedtagdd.get()
                banned_tag_lua = self.tag_mapping.get(banned_tag_name, banned_tag_name)
                lua_code += f"            {{id = '{banned_tag_lua}'}},\n"
        lua_code += "        },\n"

        lua_code += "        banned_other = {\n"
        if self.banned_other_entries:
            for entry in self.banned_other_entries:
                banned_other_name = entry.bannedotherdd.get()
                banned_other_lua = self.other_mapping.get(banned_other_name, banned_other_name)
                lua_code += f"            {{id = '{banned_other_lua}', type = 'blind'}}\n"
        lua_code += "        }\n"
        lua_code += "    }\n"
        lua_code += "}"

        if self.BUCB_var.get():
            lua_code +=  ")"

        return lua_code

class BaseEntry(ttk.Frame):
    def __init__(self, parent, remove_callback, mapping, title=None):
        super().__init__(parent)
        self.remove_callback = remove_callback
        self.mapping = list(mapping.keys())

        # Initialize value placeholder
        self.custom_value = None

        max_width = self.calculate_max_width(self.mapping)

        # Dropdown
        self.dropdown = ttk.Combobox(self, values=self.mapping, width=max_width)
        self.dropdown.grid(row=0, column=0, padx=5, pady=5)
        self.dropdown.bind('<KeyRelease>', self.autocomplete)
        self.dropdown.bind('<<ComboboxSelected>>', self.on_dropdown_change)

        # Title Entry (for classes that require a second entry)
        if title:
            self.title_entry = ttk.Entry(self, width=20)
            self.title_entry.grid(row=0, column=1, padx=5, pady=5)
            self.title_entry.insert(0, title)

        # Input Entry for custom values
        self.input_entry = ttk.Entry(self, width=12)
        self.input_entry.grid(row=0, column=2, padx=5, pady=5)
        self.input_entry.grid_remove()  # Hide initially

        # Remove Button
        self.remove_btn = ttk.Button(self, text='Remove', command=self.remove)
        self.remove_btn.grid(row=0, column=4, padx=5, pady=5)

        self.pack(fill='x')

    def calculate_max_width(self, items):
        """Calculate the maximum width in characters of the dropdown entries."""
        if not items:
            return 20  # Default width if no items are given
        max_length = max(len(item) for item in items)
        return max_length   # Add some padding        

    def autocomplete(self, event):
        typed_text = self.dropdown.get()
        if typed_text == "":
            self.dropdown['values'] = self.mapping
        else:
            filtered_values = [item for item in self.mapping if typed_text.lower() in item.lower()]
            self.dropdown['values'] = filtered_values
            self.dropdown.set(typed_text)

            if len(filtered_values) <= 3:
                if filtered_values:
                    self.dropdown.event_generate('<Down>')

    def on_dropdown_change(self, event):
        selected_value = self.dropdown.get()
        # Show input_entry when the selected value contains a "-"
        self.custom_value = None  # Reset previous value
        if selected_value in ["$X per Discard", "Fixed Seed", "Hand -1 per $X", "Joker Slot Ante", "Eternal Ante", "Cards Are Face Down"]:
            self.input_entry.grid()  # Show the input entry
        else:
            self.input_entry.grid_remove()  # Hide the input entry

    def remove(self):
        self.remove_callback(self)

class LocalEntry(BaseEntry):
    def __init__(self, parent, remove_callback, local_mapping):
        super().__init__(parent, remove_callback, local_mapping, 'Enter Local Title')
        self.localdd = self.dropdown
        if hasattr(self, 'title_entry'):
            self.local_title = self.title_entry

class CustomEntry(BaseEntry):
    def __init__(self, parent, remove_callback, custom_mapping):
        super().__init__(parent, remove_callback, custom_mapping)
        self.customdd = self.dropdown
        self.customvalue = self.input_entry.get()
            
    def get_custom_value(self):
        return self.input_entry.get()
    
class ModifiersEntry(BaseEntry):
    def __init__(self, parent, remove_callback, modifier_mapping):
        super().__init__(parent, remove_callback, modifier_mapping)
        self.modifierdd = self.dropdown

    def get_modifier_value(self):
        return self.input_entry.get()

    def on_dropdown_change(self, event):
        super().on_dropdown_change(event)  # Call the base method
        selected_value = self.dropdown.get()
        if selected_value in self.mapping:
            self.input_entry.grid()  # Show the input entry
        else:
            self.input_entry.grid_remove()  # Hide if not a valid selection

class JokersEntry(BaseEntry):
    def __init__(self, parent, remove_callback, joker_mapping, joker_edition_mapping):
        super().__init__(parent, remove_callback, joker_mapping)
        self.joker_edition_mapping = list(joker_edition_mapping.keys())
        self.jokerdd = self.dropdown

        # Joker Edition Drop Down
        self.jokereddd = ttk.Combobox(self, values=self.joker_edition_mapping, width=11)
        self.jokereddd.grid(row=0, column=1, padx=5, pady=5)
        self.jokereddd.current(0)

        # Joker Eternal Checkbox
        self.eternallabel = ttk.Label(self, text="∞")
        self.eternallabel.grid(row=0, column=2, padx=5, pady=5)

        self.eternal_var = tk.BooleanVar()
        self.eternal = tk.Checkbutton(self, variable=self.eternal_var)
        self.eternal.grid(row=0, column=3)

class CardsEntry(ttk.Frame):
    def __init__(self, parent, remove_callback, suit_mapping, rank_mapping, enhancement_mapping, seal_mapping):
        super().__init__(parent)
        self.remove_callback = remove_callback

        self.suitdd = self.create_combobox(suit_mapping, 0)
        self.rankdd = self.create_combobox(rank_mapping, 1)
        self.enhancementdd = self.create_combobox(enhancement_mapping, 2)
        self.sealdd = self.create_combobox(seal_mapping, 3)

        self.remove_btn = ttk.Button(self, text='Remove', command=self.remove)
        self.remove_btn.grid(row=0, column=4, padx=5, pady=5)

        self.pack(fill='x')

    def create_combobox(self, mapping, column):
        dropdown = ttk.Combobox(self, values=list(mapping.keys()), width=9)
        dropdown.grid(row=0, column=column, padx=5, pady=5)
        dropdown.current(0)
        return dropdown

    def remove(self):
        self.remove_callback(self)

class ConsumablesEntry(BaseEntry):
    def __init__(self, parent, remove_callback, consumable_mapping):
        super().__init__(parent, remove_callback, consumable_mapping)
        self.consumabledd = self.dropdown

class BannedCardsEntry(BaseEntry):
    def __init__(self, parent, remove_callback, banned_card_mapping):
        super().__init__(parent, remove_callback, banned_card_mapping)
        self.bannedcarddd = self.dropdown

class BannedTagsEntry(BaseEntry):
    def __init__(self, parent, remove_callback, tag_mapping):
        super().__init__(parent, remove_callback, tag_mapping)
        self.bannedtagdd = self.dropdown

class BannedOthersEntry(BaseEntry):
    def __init__(self, parent, remove_callback, other_mapping):
        super().__init__(parent, remove_callback, other_mapping)
        self.bannedotherdd = self.dropdown

class Save(ttk.Frame):
    def __init__(self):
        self.SMODS_var = tk.BooleanVar()
        self.SMODS = tk.Checkbutton(self, variable=self.SMODS_var)
        self.SMODS.grid(row=0, column=2)
        self.BUCB_var = tk.BooleanVar()
        self.BUCB = tk.Checkbutton(self, variable=self.BUCB_var)
        self.BUCB.grid(row=0, column=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = LuaGeneratorApp(root)
    root.mainloop()
