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

import libtcodpy as libtcod
import mapgen

branches = {
    'beach': {
        'name'          : 'the shore',
        'default_wall'  : 'sea cliff',
        'default_floor' : 'sand',
        'default_ramp'  : 'stone ramp',
        'scaling'       : 0,
        'loot'          : None,
        'loot_level'    : 0,
        'loot_dice'     : '1d1',
        'monsters'      : None,
        'generate'      : mapgen.make_map_beach,
        'map_color'     : libtcod.Color(0, 95, 191),
    },
    'badlands': {
        'name'          : 'the badlands',
        'default_wall'  : 'dark shale wall',
        'default_floor' : 'shale',
        'default_ramp'  : 'shale slope',
        'scaling'       : 0,
        'loot_level':0,
        'loot':{
            'consumables_1':30,
            'armor_1':20,
            'weapons_1':15,
            'gems_1':10,
            'charms_1':10,
            'rings_1':10,
            'tomes_1':4,
            'keys_1':1,
        },
        'loot_dice':'2d3',
        'encounter_dice':'1d4+5',
        'xp_amount':4,
        'encounter_range':7,
        'monsters':[
            {'encounter':['monster_cockroach'], 'party':'2d2+1'},
            {'encounter':['monster_rotting_zombie'], 'party':'1d3'},
            {'encounter':['monster_bloodfly'], 'party':'1d3'},
            {'encounter':['monster_goblin']},
            {'encounter':['monster_centipede']},
            {'encounter':['monster_tunnel_spider']},
            {'encounter':['monster_necroling']},
            {'encounter':['monster_cockroach'], 'party':'3d2'},
            {'encounter':['monster_bloodfly'], 'party':'3d2'},
            {'encounter':['monster_goblin','monster_goblin_warrior'],'party':'2d3'},
            {'encounter':['monster_snow_kite']},
            {'encounter':['monster_plague_wight']},
            {'encounter':['monster_witch']},
            {'encounter':['monster_necroling', 'monster_goblin'], 'party':'1d3+3'},
            {'encounter':['monster_infested_treant']},
            {'encounter':['monster_demon_hunter']},
        ],
        'generate'      : mapgen.make_map_badlands,
        'map_color'     : libtcod.Color(96, 96, 96),
    },
    'marsh': {
        'name'          : 'the marshes',
        'default_wall'  : 'mossy stone wall',
        'default_floor' : 'damp soil',
        'default_ramp'  : 'stone ramp',
        'scaling'       : 0,
        'loot_level':0,
        'loot':{
            'consumables_1':30,
            'armor_1':20,
            'weapons_1':15,
            'gems_1':10,
            'charms_1':10,
            'rings_1':10,
            'tomes_1':4,
            'keys_1':1,
        },
        'loot_dice':'2d3',
        'encounter_dice':'1d4+5',
        'xp_amount':4,
        'encounter_range':7,
        'monsters':[
            {'encounter':['monster_cockroach'], 'party':'2d2+2'},
            {'encounter':['monster_centipede']},
            {'encounter':['monster_reeker'],'party':'1d2'},
            {'encounter':['monster_tunnel_spider']},
            {'encounter':['monster_bomb_beetle'],'party':'1d2'},
            {'encounter':['monster_marsh_hunter']},
            {'encounter':['monster_cockroach'], 'party':'3d2'},
            {'encounter':['monster_giant_frog']},
            {'encounter':['monster_alligator']},
            {'encounter':['monster_verman']},
            {'encounter':['monster_cockroach','monster_centipede','monster_bomb_beetle'],'party':'2d3'},
            {'encounter':['monster_infested_treant']},
            {'encounter':['monster_demon_hunter']},
        ],
        'generate':mapgen.make_map_marsh,
        'map_color'     : libtcod.Color(255, 191, 0),
    },
    'gtunnels': {
        'name'          : 'the goblin tunnels',
        'default_wall'  : 'tunnel wall',
        'default_floor' : 'tunnel floor',
        'default_ramp'  : 'tunnel slope',
        'terrain_types' : ['tunnel floor','tunnel floor','shallow water','mud', 'oil'],
        'scaling'       : 0,
        'generate'      : mapgen.make_map_gtunnels,
        'map_color'     : libtcod.dark_yellow,
        'encounter_dice':'1d4+5',
        'xp_amount':4,
        'loot_level':1,
        'loot':{
            'consumables_1':27,
            'armor_1':5,
            'armor_2':13,
            'weapons_1':5,
            'weapons_2':13,
            'gems_1':15,
            'charms_1':5,
            'charms_2':5,
            'rings_1':7,
            'tomes_1':4,
            'keys_1':1,
        },
        'loot_dice':'3d3',
        'encounter_range':8,
        'monsters':[
            {'encounter':['monster_goblin'], 'party':'1d2+1'},
            {'encounter':['monster_goblin_warrior']},
            {'encounter':['monster_reeker']},
            {'encounter':['monster_verman']},
            {'encounter':['monster_goblin_wizard']},
            {'encounter':['monster_tunnel_spider']},
            {'encounter':['monster_goblin', 'monster_goblin_warrior', 'monster_goblin_priest', 'monster_goblin_wizard'],'party':'1d3'},
            {'encounter':['monster_scum_glob']},
            {'encounter':['monster_bear']},
            {'encounter':['monster_goblin','monster_goblin_warrior', 'monster_goblin_wizard'],'party':'2d3'},
            {'encounter':['monster_goblin','monster_goblin_warrior', 'monster_goblin_priest'],'party':'2d4'},
            {'encounter':['monster_goblin_champion']},
            {'encounter':['monster_arachnomancer']},
            {'encounter':['monster_mycosaur']},
        ],
    },
    'forest': {
        'name'          :"the frozen forest",
        'default_wall'  : 'pine tree',
        'default_floor' : 'snowy ground',
        'default_ramp'  : 'snowy slope',
        'scaling'       : 0,
        'loot_level':2,
        'loot':{
            'consumables_1':27,
            'armor_1':5,
            'armor_2':13,
            'weapons_1':5,
            'weapons_2':13,
            'gems_1':15,
            'charms_1':5,
            'charms_2':5,
            'rings_1':7,
            'tomes_1':4,
            'keys_1':1,
        },
        'loot_dice':'2d4',
        'encounter_dice':'1d4+5',
        'xp_amount':5,
        'encounter_range':7,
        'monsters':[
            {'encounter':['monster_bloodfly'], 'party':'1d4'},
            {'encounter':['monster_wolf']},
            {'encounter':['monster_wolf'], 'party':'1d2+2'},
            {'encounter':['monster_frost_wraith']},
            {'encounter':['monster_witch']},
            {'encounter':['monster_corvid_silencer']},
            {'encounter':['monster_corvid_acolyte']},
            {'encounter':['monster_frost_wraith'], 'party':'1d3+1'},
            {'encounter':['monster_necromancer','monster_skeleton','monster_skeleton']},
            {'encounter':['monster_corvid_silencer','monster_corvid_acolyte'], 'party':'2d2'},
            {'encounter':['monster_infested_treant']},
            {'encounter':['monster_arachnomancer']},
            {'encounter':['monster_dragon']},
        ],
        'generate':mapgen.make_map_forest,
        'map_color'     : libtcod.darkest_sky,
    },
    'garden': {
        'name'          :"the gardens",
        'default_wall'  : 'marble wall',
        'default_floor' : 'marble path',
        'default_ramp'  : 'stone ramp',
        'scaling'       : 0,
        'loot':{},
        'loot_level':0,
        'loot_dice':'2d4',
        'encounter_dice':'1d4+5',
        'xp_amount':4,
        'encounter_range':6,
        'monsters':[

        ],
        'generate':mapgen.make_map_garden,
        'map_color'     : libtcod.darker_green,
    },
    'catacombs': {
        'name'          :"the catacombs",
        'default_wall'  : 'stone wall',
        'default_floor' : 'stone floor',
        'default_ramp'  : 'stone ramp',
        'scaling'       : 0,
        'loot':{},
        'loot_level':0,
        'loot_dice':'2d4',
        'encounter_dice':'1d4+5',
        'xp_amount':4,
        'encounter_range':6,
        'monsters':[

        ],
        'generate':mapgen.make_map_catacombs,
        'map_color'     : libtcod.darker_blue,
    },
    'grotto': {
        'name'          :"pilgrim's grotto",
        'default_wall'  : 'sea cliff',
        'default_floor' : 'sand',
        'default_ramp'  : 'shale slope',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_map_grotto,
        'map_color'     : libtcod.dark_sea,
    }
}