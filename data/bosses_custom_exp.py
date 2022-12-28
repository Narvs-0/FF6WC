from data.bosses import name_enemy

custom_exp = {
    name_enemy["Marshal"]               : 80,
    name_enemy["BR Tentacle"]           : 40,
    name_enemy["BL Tentacle"]           : 40,
    name_enemy["TR Tentacle"]           : 40,
    name_enemy["TL Tentacle"]           : 40,
    name_enemy["Left Crane"]            : 66,
    name_enemy["Right Crane"]           : 66,
    name_enemy["Curley"]                : 60,
    name_enemy["Larry"]                 : 60,
    name_enemy["Moe"]                   : 60,
    name_enemy["Head"]                  : 90,
    name_enemy["Whelk"]                 : 10,
    name_enemy["Ipooh"]                 : 5,
    name_enemy["Vargas"]                : 90,
    name_enemy["Ultros 1"]              : 100,
    name_enemy["TunnelArmr"]            : 105,
    name_enemy["Leader"]                : 90,
    name_enemy["GhostTrain"]            : 110,
    name_enemy["Piranha"]               : 0,
    name_enemy["Rizopas"]               : 105,
    name_enemy["Kefka (Narshe)"]        : 115,
    name_enemy["Dadaluma"]              : 110,
    name_enemy["Ultros 2"]              : 120,
    name_enemy["Ifrit"]                 : 125,
    name_enemy["Shiva"]                 : 125,
    name_enemy["Number 024"]            : 130,
    name_enemy["Right Blade"]           : 0,
    name_enemy["Left Blade"]            : 0,
    name_enemy["Number 128"]            : 135,
    name_enemy["FlameEater"]            : 140,
    name_enemy["Ultros 3"]              : 145,
    name_enemy["Ultros 4"]              : 150,
    name_enemy["Laser Gun"]             : 15,
    name_enemy["Speck"]                 : 0,
    name_enemy["MissileBay"]            : 15,
    name_enemy["Air Force"]             : 125,
    name_enemy["AtmaWeapon"]            : 200,
    name_enemy["Nerapa"]                : 120,
    name_enemy["Dullahan"]              : 165,
    name_enemy["Phunbaba 3"]            : 155,
    name_enemy["Phunbaba 4"]            : 180,
    name_enemy["SoulSaver"]             : 0,
    name_enemy["Wrexsoul"]              : 175,
    name_enemy["SrBehemoth"]            : 185,
    name_enemy["Chadarnook (Painting)"] : 0,
    name_enemy["Chadarnook (Demon)"]    : 195,
    name_enemy["Hidonite1"]             : 0,
    name_enemy["Hidonite2"]             : 0,
    name_enemy["Hidonite3"]             : 0,
    name_enemy["Hidonite4"]             : 0,
    name_enemy["Hidon"]                 : 165,
    name_enemy["Tritoch"]               : 160,
    name_enemy["Umaro"]                 : 170,
    name_enemy["Doom Gaze"]             : 205,
    name_enemy["MagiMaster"]            : 210,
    name_enemy["Atma"]                  : 215,
    name_enemy["Rough"]                 : 0,
    name_enemy["Striker"]               : 0,
    name_enemy["Inferno"]               : 215,
    name_enemy["Guardian"]              : 220,
    name_enemy["Doom"]                  : 230,
    name_enemy["Goddess"]               : 230,
    name_enemy["Poltrgeist"]            : 230,
}

dragons = [
    name_enemy["Ice Dragon"],
    name_enemy["Storm Drgn"],
    name_enemy["Dirt Drgn"],
    name_enemy["Gold Drgn"],
    name_enemy["Skull Drgn"],
    name_enemy["Blue Drgn"],
    name_enemy["Red Dragon"],
    name_enemy["White Drgn"],
]

class DragonExp:
    HIGH = "high"
    MEDIUM = "med"
    LOW = "low"
    NONE = "none"

    ALL = [HIGH, MEDIUM, LOW, NONE]

dragon_exp_values = {
  DragonExp.HIGH    :  {key: 200 for (idx, key) in enumerate(dragons)},
  DragonExp.MEDIUM  : {key: 155 for (idx, key) in enumerate(dragons)},
  DragonExp.LOW     : {key: 125 for (idx, key) in enumerate(dragons)},
  DragonExp.NONE    : {key: 0 for (idx, key) in enumerate(dragons)},
}