import zipfile

NEEDED = [
    # barrel 在 1.21.11 中无独立贴图，代码已回退到 generic_54
    'generic_54', 'shulker_box',
    'hopper', 'furnace', 'blast_furnace', 'smoker', 'dispenser',
    'crafting_table', 'anvil', 'grindstone', 'brewing_stand',
    'enchanting_table', 'loom', 'cartography_table', 'smithing',
    'stonecutter', 'beacon', 'horse', 'inventory', 'villager'
]

with zipfile.ZipFile('assets/packs/vanilla_1.21.11_full.zip') as z:
    names = set(z.namelist())
    for t in NEEDED:
        path = f'assets/minecraft/textures/gui/container/{t}.png'
        exists = path in names
        print(f'{t}: {"OK" if exists else "MISSING"}')
