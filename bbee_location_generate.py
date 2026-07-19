import json

def ordinal(n: int):
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix

char_list = [ 'Hibiki', 'Ragna', 'Noel', 'Lambda -No.11-', 'Es', 'Rachel', 'Taokaka', 'Jin', 'Kokonoe', 'Hakumen', 'Mai', 'Hazama', 'ICEY', 'Bullet', 'The Prisoner', 'Naoto' ]
elite_list = [ 'Watcher', 'Sweeper', 'Serpent of Destruction', 'Tree of Origin', 'Arakune', 'Defiling Eye', 'Oread', 'NAN-FIRE BITE', 'Floating Mind', 'NAN-01' ]
# end_elite_list = [ 'Susanoo', 'Reki' ]

final_json = {
    "$schema": "https://github.com/ManualForArchipelago/Manual/raw/main/schemas/Manual.locations.schema.json",
    "data": [] 
}

for char in char_list:
    # stage clears
    for i in range(5):
        final_json["data"].append({
            "name": f"{char} {ordinal(i+1)} Stage Clear (Advanced)",
            "region": "Advanced Difficulty",
            "category": [char],
            "requires": f"|{char}|" if i == 0 else f"|{char}| AND |Progressive Advanced Stage ({char}):{i}|"
        })

    # elite enemy defeats
    for i, elite in enumerate(elite_list):
        final_json["data"].append({
            "name": f"{char} {ordinal((i//2)+1)} Stage Elite Enemy: {elite}",
            "region": "Advanced Difficulty",
            "category": [char, "Elite Enemy"],
            "requires": f"|{char}|" if i < 2 else f"|{char}| AND |Progressive Advanced Stage ({char}):{i//2}|"
        })

    final_json["data"].append({
        "name": f"{char} Advanced Dive Final Elite Enemy: Susanoo",
        "region": "Advanced Difficulty",
        "category": [char, "Elite Enemy"],
        "requires": f"|{char}| AND |Progressive Advanced Stage ({char}):4|"
    })

    # advanced dive clears
    for i in range(6):
        dive_block = {
            "name": f"{char} Dive Complete (Advanced {i*20} Entropy)",
            "region": "Advanced Difficulty",
            "category": [char],
            "requires": f"|{char}| AND |Progressive Advanced Stage ({char}):4|" + ("" if i == 0 else f" AND |Progressive Advanced Entropy Limit:{i}|")
        }
        if (i == 4):
            dive_block["place_item"] = [f"Advanced 80 Entropy Clear ({char})"]
        final_json["data"].append(dive_block)

    # extreme dive clears
    for i in range(6):
        dive_block = {
            "name": f"{char} Dive Complete (Extreme {i*20} Entropy)",
            "region": "Extreme Difficulty",
            "category": [char],
            "requires": f"|{char}| AND |Advanced 80 Entropy Clear ({char})|" + ("" if i == 0 else f" AND |Progressive Extreme Entropy Limit:{i}|")
        }
        if (i == 4):
            dive_block["place_item"] = [f"Extreme 80 Entropy Clear ({char})"]
        final_json["data"].append(dive_block)

    final_json["data"].append({
        "name": f"{char} Extreme Dive Final Elite Enemy: Reki",
        "region": "Extreme Difficulty",
        "category": [char, "Elite Enemy"],
        "requires": f"|{char}| AND |Advanced 80 Entropy Clear ({char})|"
    })

final_json["data"].append({
    "name": "Required Dives Complete (Goal Completed)",
    "victory": True,
    "region": "Extreme Difficulty",
    "category": ["! Goal"],
    "requires": "|@Extreme Clear:5|"
})

with open('locations.json', 'w') as f:
	f.writelines(json.dumps(final_json, indent=2))