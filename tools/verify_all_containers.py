from playwright.sync_api import sync_playwright
import time

BASE = 'http://localhost:8000/index.html'
TYPES = [
    'generic_54', 'large_trapped_chest', 'large_copper_chest',
    'generic_27', 'trapped_chest', 'copper_chest', 'barrel', 'ender_chest',
    'shulker_box', 'minecart_with_chest', 'boat_with_chest',
    'furnace', 'blast_furnace', 'smoker',
    'hopper', 'hopper_minecart', 'dispenser', 'dropper', 'crafter',
    'crafting_table', 'anvil', 'grindstone',
    'brewing_stand', 'enchanting_table', 'loom', 'cartography_table',
    'smithing_table', 'stonecutter', 'beacon',
    'horse', 'inventory', 'merchant'
]

ANIMATION_TYPES = {'furnace', 'blast_furnace', 'smoker', 'brewing_stand'}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.on('console', lambda msg: print(f'[console {msg.type}] {msg.text}'))
    page.on('pageerror', lambda err: print(f'[pageerror] {err}'))

    page.goto(BASE)
    page.wait_for_load_state('networkidle')
    time.sleep(1)

    for t in TYPES:
        page.select_option('#containerType', t)
        time.sleep(1)
        if t in ANIMATION_TYPES:
            page.click('#toggleAnimBtn')
            time.sleep(2.5)
        path = f'screenshots/check_render_{t}.png'
        page.screenshot(path=path, full_page=True)
        status = page.locator('#status').text_content()
        print(f'{t}: {status} -> {path}')

    browser.close()
