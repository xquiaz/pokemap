# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Requests/RequestType.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Requests/RequestType.proto',
  package='POGOProtos.Networking.Requests',
  syntax='proto3',
  serialized_pb=_b('\n0POGOProtos/Networking/Requests/RequestType.proto\x12\x1ePOGOProtos.Networking.Requests*\xc1\x0c\n\x0bRequestType\x12\x10\n\x0cMETHOD_UNSET\x10\x00\x12\x11\n\rPLAYER_UPDATE\x10\x01\x12\x0e\n\nGET_PLAYER\x10\x02\x12\x11\n\rGET_INVENTORY\x10\x04\x12\x15\n\x11\x44OWNLOAD_SETTINGS\x10\x05\x12\x1b\n\x17\x44OWNLOAD_ITEM_TEMPLATES\x10\x06\x12\"\n\x1e\x44OWNLOAD_REMOTE_CONFIG_VERSION\x10\x07\x12\x0f\n\x0b\x46ORT_SEARCH\x10\x65\x12\r\n\tENCOUNTER\x10\x66\x12\x11\n\rCATCH_POKEMON\x10g\x12\x10\n\x0c\x46ORT_DETAILS\x10h\x12\x0c\n\x08ITEM_USE\x10i\x12\x13\n\x0fGET_MAP_OBJECTS\x10j\x12\x17\n\x13\x46ORT_DEPLOY_POKEMON\x10n\x12\x17\n\x13\x46ORT_RECALL_POKEMON\x10o\x12\x13\n\x0fRELEASE_POKEMON\x10p\x12\x13\n\x0fUSE_ITEM_POTION\x10q\x12\x14\n\x10USE_ITEM_CAPTURE\x10r\x12\x11\n\rUSE_ITEM_FLEE\x10s\x12\x13\n\x0fUSE_ITEM_REVIVE\x10t\x12\x10\n\x0cTRADE_SEARCH\x10u\x12\x0f\n\x0bTRADE_OFFER\x10v\x12\x12\n\x0eTRADE_RESPONSE\x10w\x12\x10\n\x0cTRADE_RESULT\x10x\x12\x16\n\x12GET_PLAYER_PROFILE\x10y\x12\x11\n\rGET_ITEM_PACK\x10z\x12\x11\n\rBUY_ITEM_PACK\x10{\x12\x10\n\x0c\x42UY_GEM_PACK\x10|\x12\x12\n\x0e\x45VOLVE_POKEMON\x10}\x12\x14\n\x10GET_HATCHED_EGGS\x10~\x12\x1f\n\x1b\x45NCOUNTER_TUTORIAL_COMPLETE\x10\x7f\x12\x15\n\x10LEVEL_UP_REWARDS\x10\x80\x01\x12\x19\n\x14\x43HECK_AWARDED_BADGES\x10\x81\x01\x12\x11\n\x0cUSE_ITEM_GYM\x10\x85\x01\x12\x14\n\x0fGET_GYM_DETAILS\x10\x86\x01\x12\x15\n\x10START_GYM_BATTLE\x10\x87\x01\x12\x0f\n\nATTACK_GYM\x10\x88\x01\x12\x1b\n\x16RECYCLE_INVENTORY_ITEM\x10\x89\x01\x12\x18\n\x13\x43OLLECT_DAILY_BONUS\x10\x8a\x01\x12\x16\n\x11USE_ITEM_XP_BOOST\x10\x8b\x01\x12\x1b\n\x16USE_ITEM_EGG_INCUBATOR\x10\x8c\x01\x12\x10\n\x0bUSE_INCENSE\x10\x8d\x01\x12\x18\n\x13GET_INCENSE_POKEMON\x10\x8e\x01\x12\x16\n\x11INCENSE_ENCOUNTER\x10\x8f\x01\x12\x16\n\x11\x41\x44\x44_FORT_MODIFIER\x10\x90\x01\x12\x13\n\x0e\x44ISK_ENCOUNTER\x10\x91\x01\x12!\n\x1c\x43OLLECT_DAILY_DEFENDER_BONUS\x10\x92\x01\x12\x14\n\x0fUPGRADE_POKEMON\x10\x93\x01\x12\x19\n\x14SET_FAVORITE_POKEMON\x10\x94\x01\x12\x15\n\x10NICKNAME_POKEMON\x10\x95\x01\x12\x10\n\x0b\x45QUIP_BADGE\x10\x96\x01\x12\x19\n\x14SET_CONTACT_SETTINGS\x10\x97\x01\x12\x15\n\x10GET_ASSET_DIGEST\x10\xac\x02\x12\x16\n\x11GET_DOWNLOAD_URLS\x10\xad\x02\x12\x1c\n\x17GET_SUGGESTED_CODENAMES\x10\x91\x03\x12\x1d\n\x18\x43HECK_CODENAME_AVAILABLE\x10\x92\x03\x12\x13\n\x0e\x43LAIM_CODENAME\x10\x93\x03\x12\x0f\n\nSET_AVATAR\x10\x94\x03\x12\x14\n\x0fSET_PLAYER_TEAM\x10\x95\x03\x12\x1b\n\x16MARK_TUTORIAL_COMPLETE\x10\x96\x03\x12\x16\n\x11LOAD_SPAWN_POINTS\x10\xf4\x03\x12\t\n\x04\x45\x43HO\x10\x9a\x05\x12\x1b\n\x16\x44\x45\x42UG_UPDATE_INVENTORY\x10\xbc\x05\x12\x18\n\x13\x44\x45\x42UG_DELETE_PLAYER\x10\xbd\x05\x12\x17\n\x12SFIDA_REGISTRATION\x10\xa0\x06\x12\x15\n\x10SFIDA_ACTION_LOG\x10\xa1\x06\x12\x18\n\x13SFIDA_CERTIFICATION\x10\xa2\x06\x12\x11\n\x0cSFIDA_UPDATE\x10\xa3\x06\x12\x11\n\x0cSFIDA_ACTION\x10\xa4\x06\x12\x11\n\x0cSFIDA_DOWSER\x10\xa5\x06\x12\x12\n\rSFIDA_CAPTURE\x10\xa6\x06\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='POGOProtos.Networking.Requests.RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='METHOD_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER_UPDATE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_PLAYER', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_INVENTORY', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWNLOAD_SETTINGS', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWNLOAD_ITEM_TEMPLATES', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWNLOAD_REMOTE_CONFIG_VERSION', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORT_SEARCH', index=7, number=101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCOUNTER', index=8, number=102,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATCH_POKEMON', index=9, number=103,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORT_DETAILS', index=10, number=104,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_USE', index=11, number=105,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_MAP_OBJECTS', index=12, number=106,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORT_DEPLOY_POKEMON', index=13, number=110,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORT_RECALL_POKEMON', index=14, number=111,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RELEASE_POKEMON', index=15, number=112,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ITEM_POTION', index=16, number=113,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ITEM_CAPTURE', index=17, number=114,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ITEM_FLEE', index=18, number=115,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ITEM_REVIVE', index=19, number=116,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRADE_SEARCH', index=20, number=117,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRADE_OFFER', index=21, number=118,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRADE_RESPONSE', index=22, number=119,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRADE_RESULT', index=23, number=120,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_PLAYER_PROFILE', index=24, number=121,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_ITEM_PACK', index=25, number=122,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUY_ITEM_PACK', index=26, number=123,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUY_GEM_PACK', index=27, number=124,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EVOLVE_POKEMON', index=28, number=125,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_HATCHED_EGGS', index=29, number=126,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCOUNTER_TUTORIAL_COMPLETE', index=30, number=127,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEVEL_UP_REWARDS', index=31, number=128,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECK_AWARDED_BADGES', index=32, number=129,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ITEM_GYM', index=33, number=133,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_GYM_DETAILS', index=34, number=134,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START_GYM_BATTLE', index=35, number=135,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATTACK_GYM', index=36, number=136,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RECYCLE_INVENTORY_ITEM', index=37, number=137,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLECT_DAILY_BONUS', index=38, number=138,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ITEM_XP_BOOST', index=39, number=139,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ITEM_EGG_INCUBATOR', index=40, number=140,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_INCENSE', index=41, number=141,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_INCENSE_POKEMON', index=42, number=142,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCENSE_ENCOUNTER', index=43, number=143,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADD_FORT_MODIFIER', index=44, number=144,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISK_ENCOUNTER', index=45, number=145,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLECT_DAILY_DEFENDER_BONUS', index=46, number=146,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPGRADE_POKEMON', index=47, number=147,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_FAVORITE_POKEMON', index=48, number=148,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NICKNAME_POKEMON', index=49, number=149,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EQUIP_BADGE', index=50, number=150,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_CONTACT_SETTINGS', index=51, number=151,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_ASSET_DIGEST', index=52, number=300,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_DOWNLOAD_URLS', index=53, number=301,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_SUGGESTED_CODENAMES', index=54, number=401,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECK_CODENAME_AVAILABLE', index=55, number=402,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLAIM_CODENAME', index=56, number=403,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_AVATAR', index=57, number=404,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_PLAYER_TEAM', index=58, number=405,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MARK_TUTORIAL_COMPLETE', index=59, number=406,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOAD_SPAWN_POINTS', index=60, number=500,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ECHO', index=61, number=666,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEBUG_UPDATE_INVENTORY', index=62, number=700,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEBUG_DELETE_PLAYER', index=63, number=701,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SFIDA_REGISTRATION', index=64, number=800,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SFIDA_ACTION_LOG', index=65, number=801,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SFIDA_CERTIFICATION', index=66, number=802,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SFIDA_UPDATE', index=67, number=803,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SFIDA_ACTION', index=68, number=804,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SFIDA_DOWSER', index=69, number=805,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SFIDA_CAPTURE', index=70, number=806,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=85,
  serialized_end=1686,
)
_sym_db.RegisterEnumDescriptor(_REQUESTTYPE)

RequestType = enum_type_wrapper.EnumTypeWrapper(_REQUESTTYPE)
METHOD_UNSET = 0
PLAYER_UPDATE = 1
GET_PLAYER = 2
GET_INVENTORY = 4
DOWNLOAD_SETTINGS = 5
DOWNLOAD_ITEM_TEMPLATES = 6
DOWNLOAD_REMOTE_CONFIG_VERSION = 7
FORT_SEARCH = 101
ENCOUNTER = 102
CATCH_POKEMON = 103
FORT_DETAILS = 104
ITEM_USE = 105
GET_MAP_OBJECTS = 106
FORT_DEPLOY_POKEMON = 110
FORT_RECALL_POKEMON = 111
RELEASE_POKEMON = 112
USE_ITEM_POTION = 113
USE_ITEM_CAPTURE = 114
USE_ITEM_FLEE = 115
USE_ITEM_REVIVE = 116
TRADE_SEARCH = 117
TRADE_OFFER = 118
TRADE_RESPONSE = 119
TRADE_RESULT = 120
GET_PLAYER_PROFILE = 121
GET_ITEM_PACK = 122
BUY_ITEM_PACK = 123
BUY_GEM_PACK = 124
EVOLVE_POKEMON = 125
GET_HATCHED_EGGS = 126
ENCOUNTER_TUTORIAL_COMPLETE = 127
LEVEL_UP_REWARDS = 128
CHECK_AWARDED_BADGES = 129
USE_ITEM_GYM = 133
GET_GYM_DETAILS = 134
START_GYM_BATTLE = 135
ATTACK_GYM = 136
RECYCLE_INVENTORY_ITEM = 137
COLLECT_DAILY_BONUS = 138
USE_ITEM_XP_BOOST = 139
USE_ITEM_EGG_INCUBATOR = 140
USE_INCENSE = 141
GET_INCENSE_POKEMON = 142
INCENSE_ENCOUNTER = 143
ADD_FORT_MODIFIER = 144
DISK_ENCOUNTER = 145
COLLECT_DAILY_DEFENDER_BONUS = 146
UPGRADE_POKEMON = 147
SET_FAVORITE_POKEMON = 148
NICKNAME_POKEMON = 149
EQUIP_BADGE = 150
SET_CONTACT_SETTINGS = 151
GET_ASSET_DIGEST = 300
GET_DOWNLOAD_URLS = 301
GET_SUGGESTED_CODENAMES = 401
CHECK_CODENAME_AVAILABLE = 402
CLAIM_CODENAME = 403
SET_AVATAR = 404
SET_PLAYER_TEAM = 405
MARK_TUTORIAL_COMPLETE = 406
LOAD_SPAWN_POINTS = 500
ECHO = 666
DEBUG_UPDATE_INVENTORY = 700
DEBUG_DELETE_PLAYER = 701
SFIDA_REGISTRATION = 800
SFIDA_ACTION_LOG = 801
SFIDA_CERTIFICATION = 802
SFIDA_UPDATE = 803
SFIDA_ACTION = 804
SFIDA_DOWSER = 805
SFIDA_CAPTURE = 806


DESCRIPTOR.enum_types_by_name['RequestType'] = _REQUESTTYPE


# @@protoc_insertion_point(module_scope)
