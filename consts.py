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

# GAME
MAP_WIDTH = 50
MAP_HEIGHT = 50
LIMIT_FPS = 20
FOV_ALGO = 0
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 10
MAX_ROOM_MONSTERS = 6
MAX_ROOM_ITEMS = 2
RENDER_EVERY_TURN = False

# SPELLS
HEAL_AMOUNT = 50
CONFUSE_NUM_TURNS = 10
CONFUSE_RANGE = 8
FIREBALL_RANGE = 6
FIREBALL_DAMAGE_RATIO = 2.5
FIREBALL_RADIUS = 2
IGNITE_RANGE = 3

# COMBAT STATS
LEVEL_UP_BASE = 200
LEVEL_UP_FACTOR = 150
EVADE_FACTOR = 50.0
ARMOR_FACTOR = 50.0
BASE_JUMP_RANGE = 2
JUMP_STAMINA_COST = 50
UNARMED_STAMINA_COST = 5
JUMP_ATTACK_ACC_MOD = 0.5
JUMP_ATTACK_DMG_MOD = 2.0
BASH_STAMINA_COST = 20
BASH_ACC_MOD = 1.0
BASH_DMG_MOD = 0.25
MEDITATE_CHANNEL_TIME = 3
ARMOR_REDUCTION_BASE = 0.20
ARMOR_REDUCTION_STEP = 0.05
ARMOR_REDUCTION_DROPOFF = 5
ARMOR_LOCATION_RESIST_FACTOR = 4 #influences how effective armor is at protecting against hit-location bonuses. Higher means less effect
XP_ORB_AMOUNT_MIN = 150
XP_ORB_AMOUNT_MAX = 200
RESISTANCE_FACTOR = 0.5
WEAKNESS_FACTOR = 2.0
LEVEL_UP_HEAL = 0.2

# TERRAIN FACTORS
SHALLOW_WATER_COST = 5
MUD_COST = 10
SNOW_COST = 10
DEEP_WATER_COST = 15
STAMINA_REGEN_MOVE = 5
STAMINA_REGEN_CHANNEL = 5
STAMINA_REGEN_WAIT = 20

# MONSTERS
TUNNEL_SPIDER_MAX_WEB_DIST = 8
REEKER_PUFF_MAX = 4
REEKER_PUFF_RADIUS = 3
REEKER_PUFF_DURATION = 6
REEKER_PUFF_DAMAGE = 3
FROG_TONGUE_ACC = 30
FROG_TONGUE_DMG = 18
FROG_TONGUE_RANGE = 4
FROG_TONGUE_COOLDOWN = 3
CENTIPEDE_STING_DURATION = 3
CENTIPEDE_STING_AMPLIFICATION = 1.5
BLASTCAP_STUN_DURATION = 4
BOMB_BEETLE_DAMAGE = 30
VERMAN_MAX_SUMMONS = 8
VERMAN_MIN_COOLDOWN = 3
VERMAN_MAX_COOLDOWN = 9
ZOMBIE_IMMOBILIZE_CHANCE = 20

# MAPGEN
MG_ROOM_MAX_SIZE = 12
MG_ROOM_MIN_SIZE = 6
MG_MAX_ROOMS = 30
MG_CIRCLE_ROOM_MIN_RADIUS = 3
MG_CIRCLE_ROOM_MAX_RADIUS = 6

# DEBUG
DEBUG_ALL_EXPLORED   = False
DEBUG_DETAIL_LOGGING = []
DEBUG_DRAW_PATHS     = False
DEBUG_FREE_PERKS     = False
DEBUG_INFINITE_GEMS  = False
DEBUG_INVINCIBLE     = False
DEBUG_NO_MONSTERS    = False
DEBUG_REVEAL_MAP     = False
DEBUG_STARTING_ITEM  = None
DEBUG_STARTING_MAP   = None
DEBUG_TEST_FEATURE   = None
DEBUG_TEST_MAP       = False
DEBUG_TEST_MONSTER   = None
