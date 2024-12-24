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
        self.add_local_btn.grid(row=1, column=0, padx=5, pady=5)

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
        self.add_custom_btn.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Map Customs to Lua Variable
        self.custom_mapping = {
            "": ""
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
        self.add_modifier_btn.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Map Modifiers to Lua Variable
        self.modifier_mapping = {
            "": ""
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

        self.add_joker()  # Add initial joker entry

        self.joker_btn_frame = ttk.Frame(self.joker_page)
        self.joker_btn_frame.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

        self.back_button = ttk.Button(self.joker_btn_frame, text="Back", command=self.show_rules_page)
        self.back_button.grid(row=0, column=0, padx=5, pady=5, sticky='e')

        self.next_button = ttk.Button(self.joker_btn_frame, text="Next", command=self.show_card_page)
        self.next_button.grid(row=0, column=4, padx=5, pady=5, sticky='w')  

        self.joker_btn_frame.grid_columnconfigure(2, weight=1)

        # Card Page
        self.card_page = ttk.Frame(self.root)

        # Deck Section
        self.deck_frame = ttk.Frame(self.card_page)
        self.deck_frame.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        self.decklabel = ttk.Label(self.deck_frame, text="Deck:")
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

        self.deckdd = ttk.Combobox(self.deck_frame, values=self.deck_types, width=12) 
        self.deckdd.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        # Card Section
        self.card_entries = []
        self.card_frame = ttk.LabelFrame(self.card_page, text='Cards')
        self.card_frame.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

        self.card_scroll = ttk.Scrollbar(self.card_frame, orient='vertical')
        self.card_scroll.grid(row=0, column=1, sticky='ns')

        self.card_canvas = tk.Canvas(self.card_frame, yscrollcommand=self.card_scroll.set, height=227)
        self.card_canvas.grid(row=0, column=0, sticky='nsew')

        self.card_scroll.config(command=self.card_canvas.yview)

        self.card_frame_inner = ttk.Frame(self.card_canvas)
        self.card_canvas.create_window((0, 0), window=self.card_frame_inner, anchor='nw')

        self.card_scroll.bind('<Configure>', lambda e: self.card_scroll.config(command=self.card_canvas.yview))
        self.card_frame_inner.bind('<Configure>', lambda e: self.card_canvas.config(scrollregion=self.card_canvas.bbox('all')))

        self.add_card_btn = ttk.Button(self.card_frame, text='Add Card', command=self.add_card)
        self.add_card_btn.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

        # Map Suit Names to Lua Variable Names
        self.suit_mapping = {
            "Hearts": "H",
            "Diamonds": "D",
            "Spades": "S",
            "Clubs": "C",
        }  

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

        # Map Card Edition Names to Lua Variable Names, currently not functional
        self.card_edition_mapping = {
            "Base": "e_base",
            "Foil": "e_foil",
            "Holographic": "e_holo",
            "Polychrome": "e_polychrome",
        }    

        # Map Seal Names to Lua Variable Names
        self.seal_mapping = {
            "None": "",
            "Gold": "Gold",
            "Red": "Red",
            "Blue": "Blue",
            "Purple": "Purple",
        }        

        self.add_card()  # Add initial card entry

        self.card_btn_frame = ttk.Frame(self.card_page)
        self.card_btn_frame.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

        self.back_button = ttk.Button(self.card_btn_frame, text="Back", command=self.show_joker_page)
        self.back_button.grid(row=0, column=0, padx=5, pady=5, sticky='e')

        self.next_button = ttk.Button(self.card_btn_frame, text="Next", command=self.show_consum_vouch_page)
        self.next_button.grid(row=0, column=4, padx=5, pady=5, sticky='w')  

        self.card_btn_frame.grid_columnconfigure(2, weight=1)

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
        self.add_consumable_btn.grid(row=1, column=0, padx=5, pady=5)
        
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

        self.add_consumable()  # Add initial consumable entry

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

        spacer_frame = ttk.Frame(self.restrictions_page, height=301, width=413)
        spacer_frame.grid(row=0, column=0)

        # Save Button
        self.save_btn_frame = ttk.Frame(self.restrictions_page)
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

        self.restrictions_btn_frame = ttk.Frame(self.restrictions_page)
        self.restrictions_btn_frame.grid(row=2, column=0, padx=5, pady=5)

        self.back_button = ttk.Button(self.restrictions_btn_frame, text="Back", command=self.show_consum_vouch_page)
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
        self.card_page.pack_forget()
        self.joker_page.pack(padx=10, pady=10, fill='both', expand=True)

    def show_card_page(self):
        self.joker_page.pack_forget()
        self.consum_vouch_page.pack_forget()
        self.card_page.pack(padx=10, pady=10, fill='both', expand=True)

    def show_consum_vouch_page(self):
        self.card_page.pack_forget()
        self.restrictions_page.pack_forget()
        self.consum_vouch_page.pack(padx=10, pady=10, fill='both', expand=True) 

    def show_restrictions_page(self):
        self.consum_vouch_page.pack_forget()
        self.restrictions_page.pack(padx=10, pady=10, fill='both', expand=True)

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
        self.modifer_entries.remove(entry)

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
                lua_code += f"            {{id = '{custom_name}'}},\n"
        lua_code += "        },\n"
        lua_code += "        modifiers = {\n"
        if self.modifier_entries:
            for entry in self.modifier_entries:
                modifier_name = entry.modifierdd.get()
                modifier_value = entry.modifiervaltxt.get()
                lua_code += f"            {{id = '{modifier_name}', value = {modifier_value}}},"
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
                lua_code += f"        {{id = '{joker_lua}', eternal = {str(eternal_value).lower()}, edition = '{edition_lua}'}} ,\n"
            lua_code += "    },\n"

        # Generate Consumable code
        if self.consumable_entries:
            lua_code += "    consumeables = {\n"
            for entry in self.consumable_entries:
                consumable_name = entry.consumabledd.get()
                consumable_lua = self.consumable_mapping.get(consumable_name, consumable_name)
                lua_code += f"        {{id = '{consumable_lua}'}} ,\n"
            lua_code += "    },\n"

        # Generate Voucher code
        if self.voucher_vars:
            lua_code += "    vouchers = {\n"
            for base_var, upgrade_var, title in self.voucher_vars:
                # Only include if either base or upgrade is checked
                if base_var.get() or upgrade_var.get():
                    lua_var_list = self.voucher_mapping[title]
                    if base_var.get():
                        lua_code += f"        {{id = '{lua_var_list[0]}'}} ,\n"
                    if upgrade_var.get():
                        lua_code += f"        {{id = '{lua_var_list[1]}'}} ,\n"
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
#        if self.banned_card_entries:
#            for entry in self.consumable_entries:
#                banned_card_name = entry.banned_cardsdd.get()
#                banned_card_lua = self.consumable_mapping.get(consumable_name, consumable_name)
#                lua_code += f"        {{id = '{consumable_lua}'}} ,\n"
        
        lua_code += "        },\n"
        lua_code += "        banned_tags = {\n"
        lua_code += "        },\n"
        lua_code += "        banned_other = {\n"
        lua_code += "        }\n"
        lua_code += "    }\n"
        lua_code += "}"

        if self.BUCB_var.get():
            lua_code +=  ")"

        return lua_code

class LocalEntry(ttk.Frame):
    def __init__(self, parent, remove_callback, local_mapping):
        super().__init__(parent)
        self.remove_callback = remove_callback
        self.local_mapping = list(local_mapping.keys())

        # Language Name Drop Down
        self.localdd = ttk.Combobox(self, values=self.local_mapping, width=20)
        self.localdd.grid(row=0, column=0, padx=5, pady=5)
        self.localdd.current(0)

        # Local Title Text Box
        self.local_title = ttk.Entry(self, width=20)
        self.local_title.grid(row=0, column=1, padx=5, pady=5)
        self.local_title.insert(0, "Enter Local Title")

        self.remove_btn = ttk.Button(self, text='Remove', command=self.remove)
        self.remove_btn.grid(row=0, column=3, padx=5, pady=5)

        self.pack(fill='x')

    def remove(self):
        self.remove_callback(self)

class CustomEntry(ttk.Frame):
    def __init__(self, parent, remove_callback, custom_mapping):
        super().__init__(parent)
        self.remove_callback = remove_callback
        self.custom_mapping = list(custom_mapping.keys())

        # Modifer Name Drop Down
        self.customdd = ttk.Combobox(self, values=self.custom_mapping, width=20)
        self.customdd.grid(row=0, column=0, padx=5, pady=5)
        self.customdd.current(0)

        self.remove_btn = ttk.Button(self, text='Remove', command=self.remove)
        self.remove_btn.grid(row=0, column=3, padx=5, pady=5)

        self.pack(fill='x')

    def remove(self):
        self.remove_callback(self)

class ModifiersEntry(ttk.Frame):
    def __init__(self, parent, remove_callback, modifier_mapping):
        super().__init__(parent)
        self.remove_callback = remove_callback
        self.modifier_mapping = list(modifier_mapping.keys())

        # Modifer Name Drop Down
        self.modifierdd = ttk.Combobox(self, values=self.modifier_mapping, width=20)
        self.modifierdd.grid(row=0, column=0, padx=5, pady=5)
        self.modifierdd.current(0)

        self.remove_btn = ttk.Button(self, text='Remove', command=self.remove)
        self.remove_btn.grid(row=0, column=3, padx=5, pady=5)

        self.pack(fill='x')

    def remove(self):
        self.remove_callback(self)

class JokersEntry(ttk.Frame):
    def __init__(self, parent, remove_callback, joker_mapping, joker_edition_mapping):
        super().__init__(parent)
        self.remove_callback = remove_callback
        self.joker_mapping = list(joker_mapping.keys())
        self.joker_edition_mapping = list(joker_edition_mapping.keys())

        # Joker Name Drop Down
        self.jokerdd = ttk.Combobox(self, values=self.joker_mapping, width=19)
        self.jokerdd.grid(row=0, column=0, padx=5, pady=5)
        self.jokerdd.current(0)

        # Joker Edition Drop Down
        self.jokereddd = ttk.Combobox(self, values=self.joker_edition_mapping, width=11)
        self.jokereddd.grid(row=0, column=1, padx=5, pady=5)
        self.jokereddd.current(0)

        # Joker Eternal Label
        self.eternallabel = ttk.Label(self, text="∞")
        self.eternallabel.grid(row=0, column=2, padx=5, pady=5)

        # Joker Eternal Checkbox
        self.eternal_var = tk.BooleanVar()
        self.eternal = tk.Checkbutton(self, variable=self.eternal_var)
        self.eternal.grid(row=0, column=3)

        self.remove_btn = ttk.Button(self, text='Remove', command=self.remove)
        self.remove_btn.grid(row=0, column=4, padx=5, pady=5)

        self.pack(fill='x')

    def remove(self):
        self.remove_callback(self)


class CardsEntry(ttk.Frame):
    def __init__(self, parent, remove_callback, suit_mapping, rank_mapping, enhancement_mapping, seal_mapping):
        super().__init__(parent)
        self.remove_callback = remove_callback
        self.suit_mapping = list(suit_mapping.keys())
        self.rank_mapping = list(rank_mapping.keys())
        self.enhancement_mapping = list(enhancement_mapping.keys())
        self.seal_mapping = list(seal_mapping.keys())

        self.suitdd = ttk.Combobox(self, values=self.suit_mapping, width=9)
        self.suitdd.grid(row=0, column=0, padx=5, pady=5)
        self.suitdd.current(0)

        self.rankdd = ttk.Combobox(self, values=self.rank_mapping, width=6)
        self.rankdd.grid(row=0, column=1, padx=5, pady=5)
        self.rankdd.current(0)

        self.enhancementdd = ttk.Combobox(self, values=self.enhancement_mapping, width=10)
        self.enhancementdd.grid(row=0, column=2, padx=5, pady=5)
        self.enhancementdd.current(0)

        self.sealdd = ttk.Combobox(self, values=self.seal_mapping, width=6)
        self.sealdd.grid(row=0, column=3, padx=5, pady=5)
        self.sealdd.current(0)

        self.remove_btn = ttk.Button(self, text='Remove', command=self.remove)
        self.remove_btn.grid(row=0, column=4, padx=5, pady=5)

        self.pack(fill='x')

    def remove(self):
        self.remove_callback(self)

class ConsumablesEntry(ttk.Frame):
    def __init__(self, parent, remove_callback, consumable_mapping):
        super().__init__(parent)
        self.remove_callback = remove_callback
        self.consumable_mapping = list(consumable_mapping.keys())

        self.consumabledd = ttk.Combobox(self, values=self.consumable_mapping, width=20)
        self.consumabledd.grid(row=0, column=0, padx=5, pady=5)
        self.consumabledd.current(0)

        self.remove_btn = ttk.Button(self, text='Remove', command=self.remove)
        self.remove_btn.grid(row=0, column=3, padx=5, pady=5)

        self.pack(fill='x')

    def remove(self):
        self.remove_callback(self)

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
