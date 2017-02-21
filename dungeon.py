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
        'monsters'      : None,
        'generate'      : mapgen.make_map_beach,
        'connect'       : ['marsh', 'badlands']
    },
    'badlands': {
        'name'          : 'the badlands',
        'default_wall'  : 'dark shale wall',
        'default_floor' : 'shale',
        'default_ramp'  : 'shale slope',
        'scaling'       : 0,
        'loot_level':0,
        'loot':{
            'armor_1':25,
            'weapons_1':20,
            'consumables_1':40,
            'tomes_1':5,
            'gems_1':5
        },
        'loot_dice':'1d4',
        'encounter_dice':'1d4+5',
        'xp_amount':7,
        'encounter_range':7,
        'monsters':[
            {'encounter':['monster_cockroach'], 'party':'2d2+1'},
            {'encounter':['monster_rotting_zombie'], 'party':'1d4'},
            {'encounter':['monster_goblin']},
            {'encounter':['monster_centipede']},
            {'encounter':['monster_snow_kite']},
            {'encounter':['monster_tunnel_spider']},
            {'encounter':['monster_cockroach'], 'party':'3d2'},
            {'encounter':['monster_rotting_zombie'], 'party':'1d4+2'},
            {'encounter':['monster_goblin','monster_goblin_warrior'],'party':'2d3'},
            {'encounter':['monster_golem']},
            {'encounter':['monster_rotting_zombie'], 'party':'3d4+2'},
            {'encounter':['monster_necroling']},
            {'encounter':['monster_witch']},
            {'encounter':['monster_necroling', 'monster_goblin'], 'party':'1d3+3'},
        ],
        'generate'      : mapgen.make_map_badlands,
        'connect'       : ['beach', 'forest', 'goblin']
    },
    'marsh': {
        'name'          : 'the marshes',
        'default_wall'  : 'mossy stone wall',
        'default_floor' : 'damp soil',
        'default_ramp'  : 'stone ramp',
        'scaling'       : 0,
        'loot_level':0,
        'loot':{
            'armor_1':25,
            'weapons_1':20,
            'consumables_1':40,
            'tomes_1':5,
            'gems_1':5
        },
        'loot_dice':'1d4',
        'encounter_dice':'1d4+5',
        'xp_amount':7,
        'encounter_range':6,
        'monsters':[
            {'encounter':['monster_cockroach'], 'party':'2d2+2'},
            {'encounter':['monster_centipede']},
            {'encounter':['monster_reeker'],'party':'1d2'},
            {'encounter':['monster_tunnel_spider']},
            {'encounter':['monster_bomb_beetle'],'party':'1d2'},
            {'encounter':['monster_cockroach'], 'party':'3d2'},
            {'encounter':['monster_giant_frog']},
            {'encounter':['monster_bear']},
            {'encounter':['monster_verman']},
            {'encounter':['monster_cockroach','monster_centipede','monster_bomb_beetle'],'party':'2d3'},
        ],
        'generate':mapgen.make_map_marsh,
        'connect':['beach', 'garden', 'goblin']
    },
    'forest': {
        'name'          :"the frozen forest",
        'default_wall'  : 'pine tree',
        'default_floor' : 'snowy ground',
        'default_ramp'  : 'snowy slope',
        'scaling'       : 0,
        'loot':{},
        'loot_level':0,
        'loot_dice':'1d4',
        'encounter_dice':'1d4+5',
        'xp_amount':7,
        'encounter_range':6,
        'monsters':[
            {'encounter':['monster_cockroach'], 'party':'2d2+2'},
        ],
        'generate':mapgen.make_map_forest,
    },
    'garden': {
        'name'          :"the gardens",
        'default_wall'  : 'stone wall',
        'default_floor' : 'stone floor',
        'default_ramp'  : 'stone ramp',
        'scaling'       : 0,
        'loot':{},
        'loot_level':0,
        'loot_dice':'1d4',
        'encounter_dice':'1d4+5',
        'xp_amount':7,
        'encounter_range':6,
        'monsters':[

        ],
        'generate':mapgen.make_map_garden,
    }
}