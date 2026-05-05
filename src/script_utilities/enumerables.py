import enum as en

class Region(en.Enum):
    JAP = "J"
    KOR = "K"
    PAL = "P"
    USA = "U"

class Language(en.Enum):
    Dutch = "N", "Dutch", "nl"
    PFrench = "F", "French (PAL)", "fr"
    NFrench = "Q", "French (NTSC)", "ca"
    German = "G", "German", "de"
    Italian = "I", "Italian", "it"
    Japanese = "J", "Japanese", "ja"
    Korean = "K", "Korean", "ko"
    PPortuguese = "P", "Portuguese (PAL)", "pt"
    NPortuguese = "B", "Portuguese (NTSC)", "br"
    Russian = "R", "Russian", "ru"
    PSpanish = "S", "Spanish (PAL)", "es"
    NSpanish = "M", "Spanish (NTSC)", "mx"
    Greek = "L", "Greek", "el"
    Polish = "O", "Polish", "pl"
    Finnish = "H", "Finnish", "fi"
    Swedish = "W", "Swedish", "sv"
    Czech = "Z", "Czech", "cs"
    Danish = "D", "Danish", "da"
    
    def letter(self) -> str:
        """Returns the language identifier."""
        
        return self.value[0]
    
    def language(self) -> str:
        """Returns the full language name."""
        
        return self.value[1]
    
    def abbreviation(self) -> str:
        """Returns the language abbreviation."""
        
        return self.value[2]

class TrackInfo(str, en.Enum):
    name: str
    abbreviation: str
    course: str
    cup: int
    track: int
    slot: str
    special_slot: str
    special_music_slot: str
    
    def __new__(cls, name: str, abbreviation: str, course: str,
                cup: int, track: int, slot: str, special_slot: str,
                special_music_slot: str) -> None:
        obj = str.__new__(cls, name)
        obj._value_ = name
        obj.abbreviation = abbreviation
        obj.course = course
        obj.cup = cup
        obj.track = track
        obj.slot = slot
        obj.special_slot = special_slot
        obj.special_music_slot = special_music_slot
        return obj
    
    LuigiCircuit = ("Luigi Circuit", "LC", "track", 1, 1, "LC", "0x08", "0x75")
    MooMooMeadows = ("Moo Moo Meadows", "MMM", "track", 1, 2, "MMM", "0x01", "0x77")
    MushroomGorge = ("Mushroom Gorge", "MG", "track", 1, 3, "MG", "0x02", "0x70")
    ToadsFactory = ("Toad's Factory", "TF", "track", 1, 4, "TF", "0x04", "0x7b")
    
    MarioCircuit = ("Mario Circuit", "MC", "track", 2, 1, "MC", "0x00", "0x7d")
    CoconutMall = ("Coconut Mall", "CM", "track", 2, 2, "CM", "0x05", "0x7f")
    DKSummit = ("DK Summit", "DKS", "DKS", "track", 2, 3, "0x06", "0x81")
    WariosGoldMine = ("Wario's Gold Mine", "track", 2, 4, "WGM", "WGM", "0x07", "0x83")
    
    DaisyCircuit = ("Daisy Circuit", "DC", "track", 3, 1, "DC", "0x09", "0x87")
    KoopaCape = ("Koopa Cape", "KC", "track", 3, 2, "KC", "0x0f", "0x85")
    MapleTreeway = ("Maple Treeway", "MT", "track", 3, 3, "MT", "0x0b", "0x8f")
    GrumbleVolcano = ("Grumble Volcano", "GV", "track", 3, 4, "GV", "0x03", "0x8b")
    
    DryDryRuins = ("Dry Dry Ruins", "DDR", "track", 4, 1, "DDR", "0x0e", "0x89")
    MoonviewHighway = ("Moonview Highway", "MH", "track", 4, 2, "MH", "0x0a", "0x8d")
    BowsersCastle = ("Bowser's Castle", "BC", "track", 4, 3, "BC", "0x0c", "0x91")
    RainbowRoad = ("Rainbow Road", "RR", "track", 4, 4, "RR", "0x0d", "0x93")
    
    GCNPeachBeach = ("GCN Peach Beach", "GCN PB", "track", 5, 1, "rPB", "0x10", "0xa5")
    DSYoshiFalls = ("DS Yoshi Falls", "DS YF", "track", 5, 2, "rYF", "0x14", "0xad")
    SNESGhostValley2 = ("SNES Ghost Valley 2", "SNES GV2", "track", 5, 3, "rGV2", "0x19", "0x97")
    N64MarioRaceway = ("N64 Mario Raceway", "N64 MR", "track", 5, 4, "rMR", "0x1a", "0x9f")
    
    N64SherbetLand = ("N64 Sherbet Land", "N64 SL", "track", 6, 1, "rSL", "0x1b", "0x9d")
    GBAShyGuyBeach = ("GBA Shy Guy Beach", "GBA SGB", "track", 6, 2, "rSGB", "0x1f", "0x95")
    DSDelfinoSquare = ("DS Delfino Square", "DS DS", "track", 6, 3, "rDS", "0x17", "0xaf")
    GCNWaluigiStadium = ("GCN Waluigi Stadium", "GCN WS", "track", 6, 4, "rWS", "0x12", "0xa9")
    
    DSDesertHills = ("DS Desert Hills", "DS DH", "track", 7, 1, "rDH", "0x15", "0xb1")
    GBABowserCastle3 = ("GBA Bowser Castle 3", "GBA BC3", "track", 7, 2, "rBC3", "0x1e", "0x9b")
    N64DKsJungleParkway = ("N64 DK's Jungle Parkway", "N64 DKJP", "track", 7, 3, "rDKJP", "0x1d", "0xa1")
    GCNMarioCircuit = ("GCN Mario Circuit", "GCN MC", "track", 7, 4, "rMC", "0x11", "0xa7")
    
    SNESMarioCircuit3 = ("SNES Mario Circuit 3", "SNES MC3", "track", 8, 1, "rMC3", "0x18", "0x99")
    DSPeachGardens = ("DS Peach Gardens", "DS PG", "track", 8, 2, "rPG", "0x16", "0xb3")
    GCNDKMountain = ("GCN DK Mountain", "GCN DKM", "track", 8, 3, "rDKM", "0x13", "0xab")
    N64BowsersCastle = ("N64 Bowser's Castle", "N64 BC", "track", 8, 4, "rBC", "0x1c", "0xa3")
    
    BlockPlaza = ("Block Plaza", "BP", "arena", 1, 1, "aBP", "0x21", "0xb7")
    DelfinoPier = ("Delfino Pier", "DP", "arena", 1, 2, "aDP", "0x20", "0xb5")
    FunkyStadium = ("Funky Stadium", "FS", "arena", 1, 3, "aFS", "0x23", "0xb9")
    ChainChompWheel = ("Chain Chomp Wheel", "arena", 1, 4, "CCW", "aCCW", "0x22", "0xbb")
    ThwompDesert = ("Thwomp Desert", "TD", "arena", 1, 5, "aTD", "0x24", "0xbd")
    
    SNESBattleCourse4 = ("SNES Battle Course 4", "SNES BC4", "arena", 2, 1, "arBC4", "0x27", "0xc3")
    GBABattleCourse3 = ("GBA Battle Course 3", "GBA BC3", "arena", 2, 2, "arBC3", "0x28", "0xc5")
    N64Skyscraper = ("N64 Skyscraper", "N64 S", "arena", 2, 3, "arS", "0x29", "0xc7")
    GCNCookieLand = ("GCN Cookie Land", "GCN CL", "arena", 2, 4, "arCL", "0x25", "0xbf")
    DSTwilightHouse = ("DS Twilight House", "DS TH", "arena", 2, 5, "arTH", "0x26", "0xc1")
    
    GalaxyColosseum = ("Galaxy Colosseum", "GC", "competition", 0, 0, "GC", "0x36", "0xc9")
