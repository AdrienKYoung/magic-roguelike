#part of mrogue, an interactive adventure game
#Copyright (C) 2017 Adrien Young and Tyler Soberanis
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import libtcodpy
import game as main

table = {
    'weapons_0': [
        'weapon_dagger',
        'weapon_hatchet',
        'weapon_longsword',
        'weapon_mace',
        'weapon_spear',
    ],

     'weapons_1': [
        'weapon_dagger',
        'weapon_hatchet',
        'weapon_longsword',
        'weapon_mace',
        'weapon_spear',
        'weapon_pickaxe',
    ],

    'weapons_2' : [
        'weapon_dagger',
        'weapon_messer',
        'weapon_hatchet',
        'weapon_longsword',
        'weapon_greatsword',
        'weapon_mace',
        'weapon_warhammer',
        'weapon_dane_axe',
        'weapon_spear',
        'weapon_halberd',
        'weapon_pickaxe',
        'weapon_katar',
    ],

    'armor_0': [
        'equipment_leather_armor',
        'equipment_cloth_robes',
        'equipment_iron_helm',
        'equipment_gauntlets',
        'shield_leather_buckler',
        'shield_wooden_buckler',
    ],

    'armor_1': [
        'equipment_leather_armor',
        'equipment_leather_armor',
        'equipment_cloth_robes',
        'equipment_iron_helm',
        'equipment_iron_helm',
        'equipment_greaves',
        'equipment_greaves',
        'equipment_gauntlets',
        'equipment_gauntlets',
        'equipment_mail_armor',
        'shield_wooden_buckler',
        'shield_iron_buckler',
        'shield_heater_shield',
        'shield_round_shield',
    ],

    'armor_2' : [
        'equipment_iron_helm',
        'equipment_greaves',
        'equipment_gauntlets',
        'equipment_mail_armor',
        'equipment_brigandine',
        'equipment_great_helm',
        'equipment_greaves',
        'shield_iron_buckler',
        'shield_heater_shield',
        'shield_round_shield',
        'shield_escutcheon',
    ],

    'armor_3' : [
        'equipment_brigandine',
        'equipment_great_helm',
        'equipment_greaves',
        'equipment_gauntlets',
        'equipment_armet_helm',
        'equipment_plate_armor',
        'shield_duelists_buckler',
        'shield_round_shield',
        'shield_escutcheon',
        'shield_kite_shield',
        'shield_tower_shield',
    ],

     'consumables_1': [
        'essence_life',
        'essence_life',
        'essence_life',
        'essence_earth',
        'essence_earth',
        'essence_water',
        'essence_water',
        'essence_fire',
        'essence_air',
        'essence_cold',
        'essence_arcane',
    ],

    'consumables_2': [
        'essence_life',
        'essence_life',
        'essence_life',
        'essence_earth',
        'essence_water',
        'essence_fire',
        'essence_air',
        'essence_cold',
        'essence_arcane',
        'essence_death',
        'essence_radiance',
    ],

    'tomes_1': [
        'book_lesser_fire',
        'book_lesser_death',
        'book_lesser_cold',
        'book_lesser_life',
        'book_lesser_radiance',
    ],

    'gems_1': [
        'gem_lesser_fire',
        'gem_lesser_water',
        'gem_lesser_earth',
        'gem_lesser_air',
        'gem_lesser_cold',
        'gem_lesser_life',
        'gem_lesser_arcane',
    ],

    'gems_2': [
        'gem_lesser_fire',
        'gem_lesser_water',
        'gem_lesser_earth',
        'gem_lesser_air',
        'gem_lesser_cold',
        'gem_lesser_life',
        'gem_lesser_arcane',
        'gem_lesser_death',
        'gem_lesser_radiance',
    ],

    'keys_1': [
        'glass_key'
    ],

    'charms_1': [
        'charm_farmers_talisman',
        'charm_primal_totem',
        'charm_holy_symbol',
        'charm_shard_of_creation',
        'charm_volatile_orb',
        'charm_prayer_beads',
    ],

    'charms_2': [
        'charm_holy_symbol',
        'charm_volatile_orb',
        'charm_elementalists_lens',
        'charm_prayer_beads',
    ],

    'rings_1': [
        'equipment_ring_of_stamina',
        'equipment_ring_of_evasion',
        'equipment_ring_of_accuracy',
        'equipment_ring_of_vengeance',
        'equipment_ring_of_rage',
        'equipment_ring_of_fortitude',
        'equipment_ring_of_tenacity',
        'equipment_ring_of_vampirism',
        'equipment_ring_of_mending',
        'equipment_ring_of_waterbreathing',
        'equipment_ring_of_burdens',
        'equipment_ring_of_alchemy',
        'equipment_ring_of_poison_immunity',
        'equipment_ring_of_freedom',
        'equipment_ring_of_salvation',
        'equipment_ring_of_blessings',
        'equipment_ring_of_levitation',
    ],

    'elixirs_0': [
        'elixir_con',
        'elixir_str',
        'elixir_agi',
        'elixir_int',
        'elixir_wis',
    ],

    'chest_0': [
        'elixirs_0',
        'elixir_life',
        'rings_1',
        'charms_1',
        'keys_1',
        'tomes_1',
        'armor_2',
        'weapons_2',
        'scroll_forge',
        'treasure_0'
    ],

    'treasure_0': [
        'treasure_bejeweled_chalice',
        'treasure_burial_mask',
        'treasure_chest_of_coins',
        'treasure_giant_pearl',
        'treasure_jade_necklace',
        'treasure_silver_tiara',
        'treasure_music_box',
    ],

}

def item_from_table(branch,loot_table=None):
    if loot_table is None:
        loot_table = choose_loot_table(branch)

    if loot_table is None:
        return None

    if not loot_table in table:
        split = loot_table.split('_')
        i = int(split[1]) - 1
        while i >= 0:
            lower = split[0]+'_'+str(i)
            if lower in table:
                loot_table = lower
                break
            i -= 1
        if loot_table not in table:
            return None

    loot_level=int(loot_table.split('_')[1])
    category=loot_table.split('_')[0]

    while main.roll_dice('1d20') == 20:
        loot_level += 1 #oh lawdy
        tmp = category+'_'+str(loot_level)
        if not tmp in table.keys():
            loot_level-=1
            break

    loot_table = category+'_'+str(loot_level)

    item_id = table[loot_table][libtcodpy.random_get_int(0,0,len(table[loot_table]))-1]
    if item_id in table.keys():
        return item_from_table(branch, loot_table=item_id)

    material = None
    quality = ''
    if category == 'weapon':
        material = choose_weapon_material(loot_level)
        quality = choose_quality(loot_level)
    if category == 'armor':
        quality = choose_quality(loot_level)
        material = choose_armor_material(loot_level)

    return main.create_item(item_id, material, quality)

def choose_loot_table(branch):
    import dungeon
    b = dungeon.branches[branch]
    if b.get('loot') is None:
        return None
    else:
        return main.random_choice(b['loot'])

def choose_weapon_material(loot_level=0):
    roll = libtcodpy.random_get_int(0, 0, min(100 + 25 * loot_level, 150))
    if roll < 5:
        return choose_weapon_material(loot_level + 1)
    elif roll < 15:
        return 'wooden'
    elif roll < 30:
        return 'bronze'
    elif roll < 95:
        return 'iron'
    elif roll < 105:
        return 'steel'
    elif roll < 120:
        return 'crystal'
    elif roll < 130:
        return 'meteor'
    elif roll < 140:
        return 'aetherwood'
    else:
        return 'blightstone'

def choose_armor_material(loot_level=0):
    roll = libtcodpy.random_get_int(0, 0, min(100 + 30 * loot_level, 150))
    if roll > 100:
        ops = armor_materials.keys()
        return ops[libtcodpy.random_get_int(0,0,len(ops)-1)]
    else:
        return ''


def choose_quality(loot_level=0):
    roll = libtcodpy.random_get_int(0, 0, min(100 + 20 * loot_level, 130))
    if roll < 5:
        return choose_quality(loot_level + 1)
    elif roll < 10:
        return 'broken'
    elif roll < 20:
        return 'crude'
    elif roll < 90:
        return '' # standard
    elif roll < 100:
        return 'military'
    elif roll < 110:
        return 'fine'
    elif roll < 120:
        return 'masterwork'
    else:
        return 'artifact'

elixir_life_ticker = 0
elixir_stat_ticker = 0
scroll_forge_ticker = 0

def check_special_drop():
    global elixir_life_ticker, elixir_stat_ticker, scroll_forge_ticker
    elixir_stat_ticker += 1
    scroll_forge_ticker += 1
    elixir_life_ticker += 1
    if main.roll_dice('1d850') <= elixir_life_ticker:
        elixir_life_ticker = 0
        return 'elixir_life'
    elif main.roll_dice('1d300') <= elixir_stat_ticker:
        elixir_stat_ticker = 0
        return table['elixirs_0'][libtcodpy.random_get_int(0,0,len(table['elixirs_0']))-1]
    elif main.roll_dice('1d200') <= scroll_forge_ticker:
        scroll_forge_ticker = 0
        return 'scroll_forge'
    else:
        return None

item_categories = {
    'weapon' : { 'plural' : 'weapons' },
    'armor' : { 'plural' : 'armor' },
    'scroll' : { 'plural' : 'scrolls' },
    'potion' : { 'plural' : 'potions' },
    'book' : { 'plural' : 'books' },
    'charm' : { 'plural' : 'charms'},
    'gem' : { 'plural' : 'gems'},
    'key' : { 'plural' : 'keys'},
    'treasure' : { 'plural' : 'treasure' },
    'accessory' : {'plural': 'accessories'},
}

quality_progression = [
    'broken',
    'crude',
    '',
    'military',
    'fine',
    'masterwork',
    'artifact'
]

qualities = {
    'broken' : {
        'color' : libtcodpy.desaturated_red,
        'weapon': {
            'strength_dice_bonus' : -3,
            'accuracy_bonus' : -3,
            'shred_bonus' : -1,
        },
        'armor': {
            'evasion_bonus' : -5,
            'armor_bonus' : -1,
            'weight_bonus' : 0,
            'sh_max_bonus' : 0,
            'sh_recovery_bonus' : 5,
            'sh_raise_cost_bonus' : 10,
        }
    },
    'crude' : {
        'color' : libtcodpy.dark_sepia,
        'weapon': {
            'strength_dice_bonus' : -2,
            'accuracy_bonus' : -1,
            'break_chance_bonus' : 5.0,
        },
        'armor': {
            'evasion_bonus' : -1,
            'armor_bonus' : 0,
            'weight_bonus' : 1,
            'sh_max_bonus' : 0,
            'sh_recovery_bonus' : 2,
            'sh_raise_cost_bonus' : 5,
        }
    },
    '' : { # standard
        'color' : libtcodpy.light_gray,
        'weapon': {
            'strength_dice_bonus' : 0,
            'accuracy_bonus' : 0,
        },
        'armor': {
            'evasion_bonus' : 0,
            'armor_bonus' : 0,
            'weight_bonus' : 0,
            'sh_max_bonus' : 0,
            'sh_recovery_bonus' : 0,
            'sh_raise_cost_bonus' : 0,
        }
    },
    'military' : {
        'color' : libtcodpy.dark_orange,
        'weapon': {
            'strength_dice_bonus' : 1,
            'accuracy_bonus' : 1,
        },
        'armor': {
            'evasion_bonus' : 0,
            'armor_bonus' : 0,
            'weight_bonus' : -1,
            'sh_max_bonus' : 1,
            'sh_recovery_bonus' : 0,
            'sh_raise_cost_bonus' : -1,
        }
    },
    'fine' : {
        'color' : libtcodpy.sea,
        'weapon':{
            'strength_dice_bonus' : 2,
            'accuracy_bonus' : 2,
            'break_chance_bonus' : -1.5,
        },
        'armor': {
            'evasion_bonus' : 1,
            'armor_bonus' : 0,
            'weight_bonus' : -2,
            'sh_max_bonus' : 3,
            'sh_recovery_bonus' : -1,
            'sh_raise_cost_bonus' : -2,
        }
    },
    'masterwork' : {
        'color' : libtcodpy.green,
        'weapon':{
            'strength_dice_bonus' : 3,
            'accuracy_bonus' : 3,
            'shred_bonus' : 1,
            'break_chance_bonus' : -10.0,
        },
        'armor':{
            'evasion_bonus' : 1,
            'armor_bonus' : 0,
            'weight_bonus' : -3,
            'sh_max_bonus' : 6,
            'sh_recovery_bonus' : -2,
            'sh_raise_cost_bonus' : -3,
        }
    },
    'artifact' : {
        'color' : libtcodpy.purple,
        'weapon':{
            'strength_dice_bonus' : 5,
            'accuracy_bonus' : 5,
            'shred_bonus' : 1,
            'peirce_bonus' : 1,
            'break_chance_bonus' : -1000.0,
        },
        'armor':{
            'evasion_bonus' : 2,
            'armor_bonus' : 1,
            'weight_bonus' : -5,
            'sh_max_bonus' : 10,
            'sh_recovery_bonus' : -3,
            'sh_raise_cost_bonus' : -5,
        }
    },
}

weapon_materials = {
    'wooden' : {
        'strength_dice_bonus' : -2,
        'accuracy_bonus' : 1,
        'break_chance_bonus' : 5.0
    },
    'bronze' : {
        'strength_dice_bonus' : 0,
        'accuracy_bonus' : 0,
        'break_chance_bonus' : 1.5
    },
    'iron' : {
        'strength_dice_bonus' : 0,
        'accuracy_bonus' : 0,
        'shred_bonus' : 1
    },
    'steel' : {
        'strength_dice_bonus' : 1,
        'accuracy_bonus' : 1,
        'shred_bonus' : 2,
        'break_chance_bonus' : -5.0
    },
    'crystal' : {
        'strength_dice_bonus' : 3,
        'accuracy_bonus' : -2,
        'pierce_bonus' : 1,
        'break_chance_bonus' : -1000.0
    },
    'meteor' : {
        'strength_dice_bonus' : 5,
        'accuracy_bonus' : -2,
        'shred_bonus' : 1,
        'break_chance_bonus' : -5.0
    },
    'aetherwood' : {
        'strength_dice_bonus' : 2,
        'accuracy_bonus' : 3,
        'shred_bonus' : 1,
        'break_chance_bonus' : -15.0
    },
    'blightstone' : {
        'strength_dice_bonus' : 0,
        'accuracy_bonus' : 0,
        'guaranteed_shred_bonus' : 1,
        'break_chance_bonus' : -5.0
    },
    '' : {
        'strength_dice_bonus' : 0,
        'accuracy_bonus' : 0,
        'shred_bonus' : 0
    },
}

armor_materials = {
    ''              :   {},
    'heavy'         :   {'armor_bonus': 1, 'weight_bonus' : 3},
    'fire-proof'    :   {'resistance': ('fire', 1)},
    'insulated'     :   {'resistance': ('lightning', 1)},
    'fur-lined'     :   {'resistance': ('cold', 1)},
    'blessed'       :   {'resistance': ('death', 1)},
    'infernal'      :   {'resistance': ('radiance', 1)},
    'enchanted'     :   {'will_bonus': 1}
}