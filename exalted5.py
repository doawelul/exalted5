import sys

unittraits = {"garen": {"storyweaver", "warden"},
              "ahri": {"fated", "arcanist"},
              "caitlyn": {"ghostly", "sniper"},
              "chogath": {"mythic", "behemoth"},
              "darius": {"umbral", "duelist"},
              "jax": {"inkshadow", "warden"},
              "khazix": {"heavenly", "reaper"},
              "kobuko": {"fortune", "bruiser"},
              "kogmaw": {"mythic", "sniper", "invoker"},
              "malphite": {"heavenly", "behemoth"},
              "reksai": {"dryad", "bruiser"},
              "sivir": {"storyweaver", "trickshot"},
              "yasuo": {"fated", "duelist"},
              "aatrox": {"inkshadow", "ghostly", "bruiser"},
              "gnar": {"dryad", "warden"},
              "janna": {"dragonlord", "invoker"},
              "kindred": {"dryad", "fated", "reaper"},
              "lux": {"porcelain", "arcanist"},
              "neeko": {"mythic", "heavenly", "arcanist"},
              "qiyana": {"heavenly", "duelist"},
              "riven": {"storyweaver", "altruist", "bruiser"},
              "senna": {"inkshadow", "sniper"},
              "shen": {"ghostly", "behemoth"},
              "teemo": {"fortune", "trickshot"},
              "yorick": {"umbral", "behemoth"},
              "zyra": {"storyweaver", "sage"},
              "alune": {"umbral", "invoker"},
              "amumu": {"porcelain", "warden"},
              "aphelios": {"fated", "sniper"},
              "bard": {"mythic", "trickshot"},
              "diana": {"dragonlord", "sage"},
              "illaoi": {"ghostly", "arcanist", "warden"},
              "soraka": {"heavenly", "altruist"},
              "tahmkench": {"mythic", "bruiser"},
              "thresh": {"fated", "behemoth"},
              "tristana": {"fortune", "duelist"},
              "volibear": {"inkshadow", "duelist"},
              "yone": {"umbral", "reaper"},
              "zoe": {"storyweaver", "fortune", "arcanist"},
              "annie": {"fortune", "invoker"},
              "ashe": {"porcelain", "sniper"},
              "galio": {"storyweaver", "bruiser"},
              "kaisa": {"inkshadow", "trickshot"},
              "kayn": {"ghostly", "reaper"},
              "leesin": {"dragonlord", "duelist"},
              "lillia": {"mythic", "invoker"},
              "morgana": {"ghostly", "sage"},
              "nautilus": {"mythic", "warden"},
              "ornn": {"dryad", "behemoth"},
              "sylas": {"umbral", "bruiser"},
              "syndra": {"fated", "arcanist"},
              "azir": {"dryad", "invoker"},
              "hwei": {"mythic", "artist"},
              "irelia": {"storyweaver", "duelist"},
              "lissandra": {"porcelain", "arcanist"},
              "rakan": {"dragonlord", "lovers", "altruist"},
              "sett": {"fated", "umbral", "warden"},
              "udyr": {"inkshadow", "behemoth", "spiritwalker"},
              "wukong": {"great", "heavenly", "sage"},
              "xayah": {"dragonlord", "lovers", "trickshot"},}

unitcosts = unittraits.copy()
currcost = 1
for unit in unitcosts:
    if unit == "aatrox" or unit == "alune" or unit == "annie" or unit == "azir":
        currcost += 1
    unitcosts[unit] = currcost

traitbps = {"storyweaver": [0, 3, 5, 7, 10],
            "dragonlord": [0, 2, 3, 4, 5],
            "dryad": [0, 2, 4, 6],
            "fated": [0, 3, 5, 7, 10],
            "fortune": [0, 3, 5, 7],
            "ghostly": [0, 2, 4, 6, 8],
            "heavenly": [0, 2, 3, 4, 5, 6, 7],
            "inkshadow": [0, 3, 5, 7],
            "mythic": [0, 3, 5, 7, 10],
            "porcelain": [0, 2, 4, 6],
            "umbral": [0, 2, 4, 6, 9],
            "sniper": [0, 2, 4, 6],
            "altruist": [0, 2, 3, 4],
            "arcanist": [0, 2, 4, 6, 8],
            "artist": [0, 1],
            "behemoth": [0, 2, 4, 6],
            "bruiser": [0, 2, 4, 6, 8],
            "duelist": [0, 2, 4, 6, 8],
            "exalted": [0, 3, 5],
            "great": [0, 1],
            "invoker": [0, 2, 4, 6],
            "lovers": [0, 1],
            "reaper": [0, 2, 4],
            "sage": [0, 2, 3, 4, 5],
            "spiritwalker": [0, 1],
            "trickshot": [0, 2, 4],
            "warden": [0, 2, 4, 6],}
full0 = traitbps.copy()
for trait in full0:
    full0[trait] = 0

sys.argv = sys.argv[1:]
exaltedunits = set([name.lower() for name in sys.argv])

full8comp = []
full8compcosts = []

def calcTraitsGood(traits):
    traitsused = 0 # amount of contributions to active traits
    for trait in traits:
        traitamt = traits[trait]
        specifictraitbps = traitbps[trait]
        highestbp = 0
        while(highestbp < len(specifictraitbps) - 1 and traitamt >= specifictraitbps[highestbp + 1]):
          highestbp += 1
        traitsused += traitbps[trait][highestbp]
    return traitsused >= 13

def find8comp(already, traits):
    if len(already) == 8:
        if calcTraitsGood(traits) and already not in full8comp:
            compcost = 0
            for unit in already:
                compcost += unitcosts[unit]
            full8comp.append(already.copy())
            full8compcosts.append(compcost)
        return
    for unit in unittraits:
        if unit in already:
            continue
        already.add(unit)
        for newtrait in unittraits[unit]:
            traits[newtrait] += 1
        find8comp(already, traits)
        for newtrait in unittraits[unit]:
            traits[newtrait] -= 1
        already.remove(unit)

startunits = exaltedunits.copy()
if len(startunits) == 5:
    traitsactive = full0.copy()
    for unit in startunits:
        for attribute in unittraits[unit]:
          traitsactive[attribute] += 1
    find8comp(startunits, traitsactive)
else:
    for unit in exaltedunits:
        startunits = exaltedunits.copy()
        startunits.remove(unit)
        traitsactive = full0.copy()
        for unit in startunits:
            for attribute in unittraits[unit]:
              traitsactive[attribute] += 1
        find8comp(startunits, traitsactive)

print("Comps found:")
print(len(full8comp))
for comp, compcost in zip(full8comp, full8compcosts):
    print(str(comp) + " cost: " + str(compcost))



        
 
