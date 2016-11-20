import libtcodpy as libtcod

table = {
    'dungeon_1': {
        'loot_profile':'early',
        'versions':[
            { 'weight': 80,  'spawns': {'monster_goblin': [0,1]}},
            { 'weight': 20,  'spawns': {'monster_goblin': [2,3]}}
        ]
    },
    'dungeon_2': {
        'loot_profile':'early',
        'versions': [
            { 'weight': 75,  'spawns': {'monster_goblin': [0,2]}},
            { 'weight': 15,  'spawns': {'monster_goblin': [3,5]}},
            { 'weight': 10,  'spawns': {'monster_golem': [1,1]}}
        ]
    },
    'dungeon_3': {
        'loot_profile':'early',
        'versions': [
            {'weight': 75, 'spawns': {'monster_goblin': [0, 2]}},
            {'weight': 15, 'spawns': {'monster_goblin': [3, 5]}},
            {'weight': 10, 'spawns': {'monster_golem': [1, 1], 'monster_goblin': [0, 3]}}
        ]
    },
}

bosses = {
    'monster_nosferatu': { 'dungeon_2':10, 'dungeon_3':15, 'dungeon_4':15, 'dungeon_5':20 }
}