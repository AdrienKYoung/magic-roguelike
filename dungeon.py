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
    'test': {
        'name'          :"test grounds",
        'default_wall'  : 'stone wall',
        'default_floor' : 'stone floor',
        'default_ramp'  : 'stone ramp',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_test_space,
        'map_color'     : libtcod.dark_red,
    },
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
            {'min_depth':0, 'max_depth': 1, 'encounter':['monster_cockroach'], 'party':'2d2+1'},
            {'min_depth':0, 'max_depth': 1, 'encounter':['monster_rotting_zombie'], 'party':'1d3'},
            {'min_depth':0, 'max_depth': 1, 'encounter':['monster_bloodfly'], 'party':'1d3'},
            {'min_depth':1, 'max_depth': 2, 'encounter':['monster_goblin']},
            {'min_depth':0, 'max_depth': 2, 'encounter':['monster_centipede']},
            {'min_depth':0, 'max_depth': 2, 'encounter':['monster_tunnel_spider']},
            {'min_depth':1, 'max_depth': 3, 'encounter':['monster_necroling']},
            {'min_depth':2, 'max_depth': None, 'encounter':['monster_bloodfly'], 'party':'3d2'},
            {'min_depth':2, 'max_depth': 3, 'encounter':['monster_goblin','monster_goblin_warrior'],'party':'2d3'},
            {'min_depth':1, 'max_depth': 2, 'encounter':['monster_snow_kite']},
            {'min_depth':2, 'max_depth': None, 'encounter':['monster_plague_wight']},
            {'min_depth':3, 'max_depth': None, 'encounter':['monster_necroling', 'monster_goblin'], 'party':'1d3+3'},
            {'min_depth':3, 'max_depth': None, 'encounter':['monster_infested_treant']},
            {'min_depth':3, 'max_depth': None, 'encounter':['monster_demon_hunter']},
        ],
        'generate'      : mapgen.make_map_badlands,
        'map_color'     : libtcod.Color(96, 96, 96),
    },
    'crypt': {
        'name'          : "crypt",
        'default_wall'  : 'stone brick wall',
        'default_floor' : 'shale',
        'default_ramp'  : 'shale slope',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_map_crypt,
        'map_color'     : libtcod.darker_gray,
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
            {'min_depth':0, 'max_depth': 1, 'encounter':['monster_cockroach'], 'party':'2d2+2'},
            {'min_depth':0, 'max_depth': 3, 'encounter':['monster_centipede']},
            {'min_depth':0, 'max_depth': None, 'encounter':['monster_reeker'],'party':'1d2'},
            {'min_depth':0, 'max_depth': 3, 'encounter':['monster_tunnel_spider']},
            {'min_depth':0, 'max_depth': 2, 'encounter':['monster_bomb_beetle'],'party':'1d2'},
            {'min_depth':1, 'max_depth': 3, 'encounter':['monster_marsh_hunter']},
            {'min_depth':1, 'max_depth': 2, 'encounter':['monster_cockroach'], 'party':'4d2'},
            {'min_depth':0, 'max_depth': None, 'encounter':['monster_giant_frog']},
            {'min_depth':2, 'max_depth': None, 'encounter':['monster_alligator']},
            {'min_depth':2, 'max_depth': None, 'encounter':['monster_verman']},
            {'min_depth':2, 'max_depth': None, 'encounter':['monster_cockroach','monster_centipede','monster_bomb_beetle'],'party':'2d3'},
            {'min_depth':3, 'max_depth': None, 'encounter':['monster_infested_treant']},
            {'min_depth':3, 'max_depth': None, 'encounter':['monster_demon_hunter']},
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
            {'min_depth':0, 'max_depth': 1, 'encounter':['monster_goblin'], 'party':'1d2+1'},
            {'min_depth':0, 'max_depth': 1, 'encounter':['monster_goblin_warrior']},
            {'min_depth':0, 'max_depth': 2, 'encounter':['monster_reeker']},
            {'min_depth':0, 'max_depth': 1, 'encounter':['monster_verman']},
            {'min_depth':1, 'max_depth': None, 'encounter':['monster_goblin_wizard']},
            {'min_depth':0, 'max_depth': 1, 'encounter':['monster_tunnel_spider']},
            {'min_depth':0, 'max_depth': None, 'encounter':['monster_goblin', 'monster_goblin_warrior', 'monster_goblin_priest', 'monster_goblin_wizard'],'party':'1d3'},
            {'min_depth':0, 'max_depth': None, 'encounter':['monster_scum_glob']},
            {'min_depth':0, 'max_depth': 2, 'encounter':['monster_bear']},
            {'min_depth':2, 'max_depth': None, 'encounter':['monster_goblin','monster_goblin_warrior', 'monster_goblin_wizard'],'party':'2d3'},
            {'min_depth':2, 'max_depth': None, 'encounter':['monster_goblin','monster_goblin_warrior'],'party':'2d4', 'leader':['monster_goblin_priest']},
            {'min_depth':3, 'max_depth': None, 'encounter':['monster_goblin_champion']},
            {'min_depth':4, 'max_depth': None, 'encounter':['monster_arachnomancer']},
            {'min_depth':5, 'max_depth': None, 'encounter':['monster_mycosaur']},
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
            {'min_depth':0, 'max_depth': 0, 'encounter':['monster_bloodfly'], 'party':'1d4'},
            {'min_depth':0, 'max_depth': 1, 'encounter':['monster_wolf']},
            {'min_depth':1, 'max_depth': 2, 'encounter':['monster_wolf'], 'party':'1d2+2'},
            {'min_depth':1, 'max_depth': 2, 'encounter':['monster_frost_wraith']},
            {'min_depth':1, 'max_depth': 2, 'encounter':['monster_corvid_silencer']},
            {'min_depth':1, 'max_depth': None, 'encounter':['monster_corvid_acolyte']},
            {'min_depth':1, 'max_depth': None, 'encounter':['monster_frost_wraith'], 'party':'1d3+1'},
            {'min_depth':2, 'max_depth': None, 'encounter':['monster_skeleton'], 'party': '2d2', 'leader':['monster_necromancer']},
            {'min_depth':2, 'max_depth': None, 'encounter':['monster_corvid_silencer','monster_corvid_acolyte'], 'party':'2d2'},
            {'min_depth':2, 'max_depth': None, 'encounter':['monster_infested_treant']},
            {'min_depth':2, 'max_depth': None, 'encounter':['monster_arachnomancer']},
            {'min_depth':2, 'max_depth': None, 'encounter':['monster_dragon']},
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
            {'min_depth':3, 'max_depth': None, 'encounter':['monster_dragon']},
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
    'bone': {
        'name'          :"the bone pits",
        'default_wall'  : 'sea cliff',
        'default_floor' : 'sand',
        'default_ramp'  : 'shale slope',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_test_space,
        'map_color'     : libtcod.darker_gray,
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
    },
    'river': {
        'name'          :"stonewater river",
        'default_wall'  : 'mossy stone wall',
        'default_floor' : 'grass floor',
        'default_ramp'  : 'stone ramp',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_map_river,
        'map_color'     : libtcod.darker_sky,
    },
    'crossing': {
        'name'          :"stonewater crossing",
        'default_wall'  : 'mossy stone wall',
        'default_floor' : 'grass floor',
        'default_ramp'  : 'stone ramp',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_map_crossing,
        'map_color'     : libtcod.darker_sky,
    },
    'tower': {
        'name'          :"tower of the mages",
        'default_wall'  : 'sea cliff',
        'default_floor' : 'sand',
        'default_ramp'  : 'shale slope',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_test_space,
        'map_color'     : libtcod.darker_gray,
    },
    'giantwoods': {
        'name'          :"the giant woods",
        'default_wall'  : 'sea cliff',
        'default_floor' : 'sand',
        'default_ramp'  : 'shale slope',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_test_space,
        'map_color'     : libtcod.darker_gray,
    },
    'canopy': {
        'name'          :"the giant woods canopy",
        'default_wall'  : 'sea cliff',
        'default_floor' : 'sand',
        'default_ramp'  : 'shale slope',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_test_space,
        'map_color'     : libtcod.darker_gray,
    },
    'lavalake': {
        'name'          :"the lava lake",
        'default_wall'  : 'dark shale wall',
        'default_floor' : 'shale',
        'default_ramp'  : 'shale slope',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_map_lava_lake,
        'map_color'     : libtcod.darker_gray,
    },
    'slagfields': {
        'name'          :"the slagfields",
        'default_wall'  : 'sea cliff',
        'default_floor' : 'sand',
        'default_ramp'  : 'shale slope',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_test_space,
        'map_color'     : libtcod.darker_gray,
    },
    'foundry': {
        'name'          :"foundry of war",
        'default_wall'  : 'sea cliff',
        'default_floor' : 'sand',
        'default_ramp'  : 'shale slope',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_test_space,
        'map_color'     : libtcod.darker_gray,
    },
    'tomb': {
        'name'          :"the unnamed tomb",
        'default_wall'  : 'sea cliff',
        'default_floor' : 'sand',
        'default_ramp'  : 'shale slope',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_test_space,
        'map_color'     : libtcod.darker_gray,
    },
    'temple': {
        'name'          :"the sunken temple",
        'default_wall'  : 'sea cliff',
        'default_floor' : 'sand',
        'default_ramp'  : 'shale slope',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_test_space,
        'map_color'     : libtcod.darker_gray,
    },
    'mines': {
        'name'          :"the mines",
        'default_wall'  : 'sea cliff',
        'default_floor' : 'sand',
        'default_ramp'  : 'shale slope',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_test_space,
        'map_color'     : libtcod.darker_gray,
    },
    'depths': {
        'name'          :"the depths",
        'default_wall'  : 'sea cliff',
        'default_floor' : 'sand',
        'default_ramp'  : 'shale slope',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_test_space,
        'map_color'     : libtcod.darker_gray,
    },
    'menagerie': {
        'name'          :"the menagerie",
        'default_wall'  : 'sea cliff',
        'default_floor' : 'sand',
        'default_ramp'  : 'shale slope',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_test_space,
        'map_color'     : libtcod.darker_gray,
    },
    'gatehouse': {
        'name'          :"the gatehouse",
        'default_wall'  : 'sea cliff',
        'default_floor' : 'sand',
        'default_ramp'  : 'shale slope',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_test_space,
        'map_color'     : libtcod.darker_gray,
    },
    'battlements': {
        'name'          :"the battlements",
        'default_wall'  : 'sea cliff',
        'default_floor' : 'sand',
        'default_ramp'  : 'shale slope',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_test_space,
        'map_color'     : libtcod.darker_gray,
    },
    'city': {
        'name'          :"the capital",
        'default_wall'  : 'sea cliff',
        'default_floor' : 'sand',
        'default_ramp'  : 'shale slope',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_test_space,
        'map_color'     : libtcod.darker_gray,
    },
    'cathedral': {
        'name'          :"the cathedral",
        'default_wall'  : 'sea cliff',
        'default_floor' : 'sand',
        'default_ramp'  : 'shale slope',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_test_space,
        'map_color'     : libtcod.darker_gray,
    },
    'cursed': {
        'name'          :"the cursed path",
        'default_wall'  : 'sea cliff',
        'default_floor' : 'sand',
        'default_ramp'  : 'shale slope',
        'scaling'       : 0,
        'loot'          : None,
        'monsters'      : None,
        'generate'      : mapgen.make_test_space,
        'map_color'     : libtcod.darker_gray,
    },
}