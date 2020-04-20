#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import glob
import os
import math
import sys
import random
import json
import string
from PIL import Image
import base64
from Crypto import Random
from Crypto.Cipher import AES, DES
from shutil import copyfile
import copy
# debug
import pdb
import methodtransfer
import gc
import inserthandler
# sys.path.append("./")
# sys.path.append("insert_sub")
# sys.path.append(os.path.dirname(os.path.realpath(__file__)))
# import ins_objcreatorfactor, ins_objcreatorfactor


class_prefix_str = "RIUD"

# nosearch_directorys = ["Pods", "Pseudo_3DTests", "Pseudo_3DUITests", "ZipfdsdfdArchive"]
nosearch_directorys = ["Pods","ExXX", "Model","Pseudo_3DTests", "Pseudo_3DUITests", "lpaToolsThird", "AppDelegate", "SceneDelegate","LPAOtherMVC","LPAChuanSJ","CQGEvenView","CQGEmploySugarView","XDPagesresView","GKKCover","CQGToleranceView","CQGSpillMarriedView","PirateCottageTests","PirateCottageUITests","CQGTusdpijIUouboiw","CQGReasonableFourthView","CQGSuperiorResponsibleView","CQGExaminationView"]

global_param_name = ""

global_shared_instance = ["standardInstance", "standardManager", "standardTool", "standardHandler", "standardConfiguration", "standardConfig", \
    "sharedInstance", "sharedManager", "sharedTool", "sharedHandler", "sharedConfiguration", "sharedConfig", \
    "defaultInstance", "defaultManager", "defaultTool", "defaultHandler", "defaultConfiguration", "defaultConfig"]

global_property_normal_type = ["int", "long", "long long", "BOOL", "float", "unsigned long long", "double"]
global_property_point_type = ["NSString", "NSMutableString", "NSData", "NSMutableData", "NSDictionary", "NSMutableDictionary", "NSArray", "NSMutableArray"]


global_system_class_list = ["NSObject", "NSString", "NSMutableString", "NSData", "NSMutableData", "NSDictionary", "NSMutableDictionary", 
"NSArray", "NSMutableArray", "NSAssertionHandler", "NSBundle", "NSBundleResourceRequest", "NSCoder", "NSCharacterSet", "NSCountedSet",
"NSConditionLock", "NSConstantString", "NSDate", "NSDateFormatter", "NSDecimalNumber", "NSDateComponents", "NSException", "NSError", 
"NSEnumerator", "NSFileManager", "NSFileWrapper", "NSFileHandle", "NSFormatter", "NSFileSecurity", "NSFileCoordinator" , "NSHTTPCookie", "NSHTTPURLResponse", "NSHTTPCookieStorage",
"NSIndexPath", "NSIndexSet", "NSInputStream", "NSItemProvider", "NSKeyedArchiver", "NSLock",
"NSLayoutAnchor", "NSLayoutManager", "NSMutableSet", "NSMutableOrderedSet", "NSMutableIndexSet",
"UIView", "UIImageView", "UIImage", "UILabel", "UITableView", "UITableViewCell","UICollectionViewCell",
"UITextField", "UITextView", "UIKeyBoard", "UIResponder", "UIControl", "UIWindow", "UIViewController", "UINavigationController",
"UINavigationBar", "UINavigationItem", "UIAlertController", "UIActivity", "UIAlertAction", "UIBarButtonItem", "UIButton", "UIBezierPath", "UIBlurEffect",
"UIColor", "UICollisionBehavior", "UIDevice", "UIDatePicker", "UIDictationPhrase", "UIDynamicAnimator", "UIDynamicItemGroup",
"UIDynamicBehavior", "UIEvent", "UIBlurEffect", "UIFont", "UIFocusGuide", "UIGravityBehavior",
"UIGestureRecognizer", "UIInputView", "UIImageAsset", "UIKeyCommand", "UILexicon", "UILayoutGuide", "UILexiconEntry", "UIMenuItem", "UIMotionEffect",
"UIMenuController", "UIMotionEffectGroup", "UIMarkupTextPrintFormatter", "UIPress", "UIPasteboard", "UIPageControl",
"UIPressesEvent", "UIProgressView", "UIPushBehavior", "UIPreviewAction", "UIPrintFormatter", "UIPageViewController", "UIPreviewActionGroup", "UIRegion",
"UIResponder", "UIRefreshControl", "UIRotationGestureRecognizer", "UIScreen", "UISlider", "UISwitch", "UIStepper", "UISearchBar", "UIStackView",
"UIStatusBar", "UIScreenMode", "UIScrollView", "UIStoryboard", "UISnapBehavior", "UITouch", "UITabBar", "UIToolbar", "UITextRange", "UITabBarItem",
"UITextChecker", "UITextPosition", "UITextInputMode", "UIVisualEffect", "UIVibrancyEffect", "UIVisualEffectView", "UIViewPrintFormatter",
"UIVideoEditorController"]#157
# global_property_point_attribute = ["retain"]

generage_save_path = "already"
handle_target_path = "target"
generage_using_path = "using"
generage_mixed_save_path = "mixed_using"
import_mixed_file_path = "import_mixed_using.txt"

foundation_coder_path = "coder/foundation"
model_coder_path = "coder/model"
import_coder_path = "coder/import"



def anyTrue(predicate, sequence):
	return True in map(predicate, sequence)

# 过滤不查找的路径的形式搜索文件
def get_search_files(targetpath, filetypelist, nosearch_directorys):
	filelist = []
	for fileName in os.listdir(targetpath):
		filepath = targetpath + '/' + fileName
		path_need_search = 0
		for nosearch_item in nosearch_directorys:
			if nosearch_item in filepath:
				path_need_search = 1
				break
		if 1 == path_need_search:
			continue
		
		if os.path.isdir(filepath):
			files = get_search_files(filepath, filetypelist, nosearch_directorys)
			filelist.extend(files)
		elif anyTrue(fileName.endswith, filetypelist):
			filelist.append(filepath)
		else:
			continue
	return filelist

foundation_implamentation_list = get_search_files(foundation_coder_path, [".txt"], [])
model_implamentation_list = get_search_files(model_coder_path, [".txt"], [])

out_random_type_class = 1
out_random_type_method_init = 2
out_random_type_method_name = 3
out_random_type_method_realize = 4

oc_insert_confuse = re.compile(r'//////insert//', re.M)
oc_insert_mixed_depth_confuse = re.compile(r'//////insert_search//', re.M)
object_class_oc_rule = re.compile(r'^@interface\s*(\w+)\s:\s*NSObject', re.M)
object_class_implamentation_oc_rule = re.compile(r'^@implementation\s+(\w+)$', re.M)
oc_func_rule = re.compile(r'^[+-]\s*\(\w+\)\s*\w+\s*[^;|:|\{|\s]', re.M)
oc_func_short_rule = re.compile(r'\w+$')
oc_find_target_ui_varname_rule = re.compile(r'([^\[]*)\s*addSubview:', re.S)

#oc_func_rule2 = re.compile(r'^[+-]\s*\(\s*\w+\s*\**\s*\)\s*\w+\s*[\:]?.*\n$', re.S)
oc_func_rule3 = re.compile(r'^[+-]\s*\(.*\)\s*\w+\s*[^;\{\n]', re.M)

#匹配CGRectMake 只匹配一行
oc_CGRectMake_rule = re.compile(r'CGRectMake\([^\,\;]*\,[^\,\;]*\,[^\,\;]*\,[^\,\;]*\)', re.S)
#分别匹配CGRectMake中的参数
oc_CGRectMake_param1_rule = re.compile(r'CGRectMake\(([^\,\;]*)\,[^\,\;]*\,[^\,\;]*\,[^\,\;]*\)', re.S)
oc_CGRectMake_param2_rule = re.compile(r'CGRectMake\([^\,\;]*\,([^\,\;]*)\,[^\,\;]*\,[^\,\;]*\)', re.S)
oc_CGRectMake_param3_rule = re.compile(r'CGRectMake\([^\,\;]*\,[^\,\;]*\,([^\,\;]*)\,[^\,\;]*\)', re.S)
oc_CGRectMake_param4_rule = re.compile(r'CGRectMake\([^\,\;]*\,[^\,\;]*\,[^\,\;]*\,([^\,\;]*)\)', re.S)

#匹配CGSizeMake 只匹配一行
oc_CGSizeMake_rule = re.compile(r'CGSizeMake\([^\,\;]*\,[^\,\;]*\)', re.S)
#分别匹配CGSizeMake中的参数
oc_CGSizeMake_param1_rule = re.compile(r'CGSizeMake\(([^\,\;]*)\,[^\,\;]*\)', re.S)
oc_CGSizeMake_param2_rule = re.compile(r'CGSizeMake\([^\,\;]*\,([^\,\;]*)\)', re.S)

#匹配CGPointMake 只匹配一行
oc_CGPointMake_rule = re.compile(r'CGPointMake\([^\,\;]*\,[^\,\;]*\)', re.S)
#分别匹配CGPointMake中的参数
oc_CGPointMake_param1_rule = re.compile(r'CGPointMake\(([^\,\;]*)\,[^\,\;]*\)', re.S)
oc_CGPointMake_param2_rule = re.compile(r'CGPointMake\([^\,\;]*\,([^\,\;]*)\)', re.S)

#匹配UIColor colorWithRed:
oc_UIColor_colorWithRed_rule = re.compile(r'\[UIColor colorWithRed\:[^\:\;]* green\:[^\:\;]* blue\:[^\:\;]* alpha\:[^:\;]*\]', re.S)
#分别匹配UIColor colorWithRed中的参数
oc_UIColor_colorWithRed_param1_rule = re.compile(r'\[UIColor colorWithRed\:([^\:\;]*) green\:[^\:\;]* blue\:[^\:\;]* alpha\:[^:\;]*\]', re.S)
oc_UIColor_colorWithRed_param2_rule = re.compile(r'\[UIColor colorWithRed\:[^\:\;]* green\:([^\:\;]*) blue\:[^\:\;]* alpha\:[^:\;]*\]', re.S)
oc_UIColor_colorWithRed_param3_rule = re.compile(r'\[UIColor colorWithRed\:[^\:\;]* green\:[^\:\;]* blue\:([^\:\;]*) alpha\:[^:\;]*\]', re.S)
oc_UIColor_colorWithRed_param4_rule = re.compile(r'\[UIColor colorWithRed\:[^\:\;]* green\:[^\:\;]* blue\:[^\:\;]* alpha\:([^:\;]*)\]', re.S)

double_insert_0905_rule = re.compile(r'[0-9]+\.[0-9]*f?', re.S)
longlong_insert_0905_rule = re.compile(r'[0-9]+', re.S)
NSString_insert_0905_rule = re.compile(r'@"[^"]*"', re.S)
NSArray_insert_0905_rule = re.compile(r'@\[.*\]', re.S)



mixed_type_A_B_C         = 3
mixed_type_A_B_A_C       = 4
mixed_type_A_B_C_D_E     = 5
mixed_type_A_B_C_B_D_A   = 6
mixed_type_A_B_C_B_D_C_A = 7


implamentation_type_get_device_name                 = 0  # 获取设备名称  return:NSString
implamentation_type_get_system_version              = 1  # 获取设备系统版本号
implamentation_type_get_system_name                 = 2  # 获取系统名称
implamentation_type_get_device_model                = 3  # 获取设备型号
implamentation_type_get_reboot_time                 = 4  # 设备上次重启的时间
implamentation_type_get_idfa                        = 5  # 广告位标识符idfa
implamentation_type_get_idfv                        = 6  # idfv
implamentation_type_get_app_version                 = 7  # 获取app版本号
implamentation_type_get_battery_electricity         = 8  # 获取电池电量
implamentation_type_get_battery_status              = 9 # 获取电池状态
implamentation_type_get_battery_capacity            = 10 # 获取电池容量
implamentation_type_get_battery_voltage             = 11 # 获取电池电压
implamentation_type_get_ip                          = 12 # 获取设备ip地址
implamentation_type_get_cpu_frequency               = 13 # 获取CPU实时频率
implamentation_type_get_cpu_quantity                = 14 # 获取CPU数量
implamentation_type_get_cpu_use_capacity            = 15 # 获取单个CPU的使用百分比
implamentation_type_get_thread_frequency            = 16 # 获取总线程频率
implamentation_type_get_ram_capacity                = 17 # 获取当前设备主存
implamentation_type_get_ram_dynamic                 = 18 # 获取活跃的内存空间
implamentation_type_get_ram_lazy                    = 19 # 获取不活跃的内存空间
implamentation_type_get_ram_free                    = 20 # 获取空闲的内存空间
implamentation_type_get_ram_inuse                   = 21 # 获取正在使用的内存空间
implamentation_type_get_ram_kernel                  = 22 # 获取用于存放内核的内存空间
implamentation_type_get_ram_can_release             = 23 # 获取可释放的内存空间
implamentation_type_get_document_path               = 24 # 获取本沙盒文稿路径
implamentation_type_get_document_size               = 25 # 获取本沙盒文稿大小
implamentation_type_get_library_path                = 26 # 获取library路径
implamentation_type_get_library_size                = 27 # 获取library大小
implamentation_type_get_cache_path                  = 28 # 获取cache目录路径
implamentation_type_get_cache_size                  = 29 # 获取cache目录大小
implamentation_type_get_temp_path                   = 30 # 获取temp目录路径
implamentation_type_get_temp_size                   = 31 # 获取temp目录大小
implamentation_type_get_disk_size                   = 32 # 获取磁盘总空间
implamentation_type_get_disk_last                   = 33 # 获取未使用的磁盘空间

implamentation_type_log_string                      = 34 # 打印字符串
implamentation_type_log_mutablestring               = 35 # 打印可变字符串
implamentation_type_log_number                      = 36 # 打印数字

implamentation_type_init_uiview                     = 37 # 初始化uiview
implamentation_type_init_uitableview                = 38 # 初始化uitableview
implamentation_type_init_uitableviewcell            = 39 # 初始化uitableviewcell
implamentation_type_init_imageview                  = 40 # 初始化imageview
implamentation_type_init_uibutton                   = 41 # 初始化uibutton
implamentation_type_init_uilabel                    = 42 # 初始化uilabel
implamentation_type_init_uitextfield                = 43 # 初始化uitextfield
implamentation_type_init_uitextview                 = 44 # 初始化uitextview
implamentation_type_init_uicollectionview           = 45 # 初始化uicollectionview
implamentation_type_init_uicollectionviewcell       = 46 # 初始化uicollectionviewcell

implamentation_type_handle_keychain                 = 47 # 处理keychain
implamentation_type_handle_mutabledictionary        = 48 # 处理可变字典
implamentation_type_handle_dictionary               = 49 # 处理不可变字典
implamentation_type_string_data                     = 50 # 处理字符串的data
implamentation_type_mutablestring_data              = 51 # 处理可变字符串

implamentation_type_mutablestring_data2             = 52 # 处理可变字符串2

implamentation_type_mutablestring_mutabledictionary = 53 # 处理可变字典与可变字符串

implamentation_type_string_array                    = 54 # 定义字符串数组

implamentation_type_string_foundation               = 55 # 定义字符串并调用系统库代码

implamentation_type_0722                            = 56 #0722版插入点
implamentation_type_0723_deathmagic_appeal          = 57 #0723DeathMagic申诉
implamentation_type_0723_defendgarden_appeal        = 58 #0723DefendGarden申诉
implamentation_type_0729_Dragon_Duel                = 59 #0729DragonDuel申诉
implamentation_type_0805_Fantasy_War                = 60 #0805 Fantasy_War插入点
implamentation_type_mutablestring_data_tNSMutableData = 61 #Dragon Combat申诉
implamentation_type_handle_NSMutableAttributedString0817 = 62 # 处理 NSMutableAttributedString




# method_return_type = []
method_return_type = ["NSString *", "NSString *", "NSString *", "NSString *", "NSDate *", "NSString *", "NSString *", "NSString *", "NSString *", "NSInteger",
    "float", "float", "NSString *", "NSUInteger", "NSUInteger", "NSArray *", "NSUInteger", "NSUInteger", "NSString *", "NSString *", 
    "NSString *", "NSString *", "int64_t", "NSString *", "NSString *", "int64_t", "NSString *", "int64_t", "NSString *", "int64_t",
    "NSString *", "int64_t", "NSString *", "NSString *", "void", "NSMutableString *", "void", "UIView *", "UITableView *", "UITableViewCell *",
    "UIImageView *", "UIButton *", "UILabel *", "UITextField *", "UITextView *", "UICollectionView *", "UICollectionViewCell *", "NSData *", "NSDictionary *", "NSDictionary *", "NSString *",
    "NSMutableString *", "NSMutableString *", "NSMutableDictionary *", "NSArray *", "NSString *", "NSMutableData *", "NSString *", "NSMutableString *",
    "NSDate *", "NSMutableData *", "NSMutableString *", "NSMutableAttributedString *"] # 一共63个


# 1104版本在viewDidDisappear函数添加ui
global_need_add_ui = "//need_add_ui//"
global_need_did_remove_ui = "//need_did_remove_ui//"
global_need_will_remove_ui = "//need_will_remove_ui//"
global_remove_tag = 0


# 0905版本插入点
global_0905insert_symbol = "in0905put"
global_0905insert_type_longlong = "//in0905put_longlong&_in0905put//"
global_0905insert_type_double = "//in0905put_double&_in0905put//"
global_0905insert_type_NSString = "//in0905put_NSString&_in0905put//"
global_0905insert_type_NSArray = "//in0905put_NSArray&_in0905put//"

global_0926insert_function_type_handle = "handle"
global_0926insert_function_type_reduction = "reduction"

#0926版本新添加的插入点类别
global_0926insert_type_data = 0
global_0926insert_type_feature = 1


global_0905insert_type_handle_list = [global_0905insert_type_longlong, global_0905insert_type_double, global_0905insert_type_NSString, global_0905insert_type_NSArray]



# 生成中间调用类
def generate_class_list():
    out_class_list = []
    random_depth = 10
    for i in range(random_depth):
        class_name = generate_words_str("property")
        out_class_list.append(class_name)
    return out_class_list


# 随机生成一个十六进制字符
def generate_hex_char():
    out_str = ""
    char_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e']
    out_str = char_list[random.randrange(0, len(char_list))]
    return out_str


class ClassObject(object):
    '''
    oc 类
    '''
    def __init__(self, class_name, property_list, shared_instance_method, method_list):
        self.class_name = class_name
        self.property_list = property_list
        self.shared_instance_method = shared_instance_method
        self.method_list = method_list
    
    def get_class_name(self):
        return self.class_name
    
    def get_shared_method(self):
        return self.shared_instance_method

    def get_property_list(self):
        return self.property_list


    def get_method_list(self):
        return self.method_list
    
    def add_method(self, method_obj):
        self.method_list.append(method_obj)


# 生成函数原型
def generate_method_prototype(method):
    # print("生成函数原型")
    out_str = ""
    out_str += "+ (" + method.returntype + ")" + method.name
    if method.hasparam:
        out_str += ":(" + method.param1type + ")" + method.param1name
    out_str += ";\n"
    return out_str


# 生成中间调用层的实现
def generate_method_implamentation(method, sub_method):
    # print("生成函数实现")

    out_str = ""
    out_str += "+ (" + method.returntype + ")" + method.name
    if method.hasparam:
        out_str += ":(" + method.param1type + ")" + method.param1name
    out_str += "\n{\n"
    
    # 添加插入点
    out_str += "\t//////insert//\n"
    out_str += "\t[" + sub_method.holdclass + " " + sub_method.name
    if sub_method.hasparam:
        out_str += ":" + method.param1name
    out_str += "];\n"
    out_str += "}\n\n"
    return out_str



# 根据文件格式搜索文件
def getfilepath(targetpath, filetypelist):
    filelist = []
    for fileName in os.listdir(targetpath):
        filepath = targetpath + '/' + fileName
        # pdb.set_trace()
        if "Pod" in filepath:
            continue
        if os.path.isdir(filepath):
            files = getfilepath(filepath, filetypelist)
            filelist.extend(files)
        elif anyTrue(fileName.endswith, filetypelist):
            filelist.append(filepath)
        else:
            continue
    return filelist


# 搜索类名
def find_nsobject_class(classfilelist):
	class_list = []
	file_context = ""
	for file in classfilelist:
		with open(file, "r+") as input:
			file_context = input.read()
		result = object_class_oc_rule.findall(file_context)
		class_list.extend(result)
			
	class_list = list(set(class_list))
	return class_list






# 第一个字符大写其他不变
def first_str_capitalize(origin_str):
	first_char_str = origin_str[0:1]
	sub_str = origin_str[1:]
	first_char_str = first_char_str.capitalize()
	return first_char_str + sub_str


# 根据 动词-介词-形容词-名词-副词 的规则生成字符串
def generate_words_str(generate_type):
	# '''
	# parm: random_str func property 或者 其他任何字符
	# 	组合包括：动词+名词
	# 	函数名至少是三种组合
	# 	属性名是两个组合(形容词+名词 或 名词+副词)
	# 	随机字符串至少是两个组合
	# '''

    verb_list = []
    verb_path = "words/verb.txt"

    # 介词
    preposition_list = []
    preposition_path = "words/preposition.txt"

    # 形容词
    adjective_list = []
    adjective_path = "words/adjective.txt"

    # 名词
    noun_list = []
    noun_path = "words/noun.txt"

    # 副词
    adverb_list = []
    adverb_path = "words/adverb.txt"

    random_noun_list = []
    random_noun_path = "words/string.txt"
    
	# 获取内容
    with open(verb_path, "r") as input:
		verb_list = input.readlines()

    with open(preposition_path, "r") as input:
		preposition_list = input.readlines()
	
    with open(adjective_path, "r") as input:
		adjective_list = input.readlines()

    with open(noun_path, "r") as input:
        noun_list = input.readlines()

    with open(adverb_path, "r") as input:
        adverb_list = input.readlines()

    with open(random_noun_path, "r") as input:
        random_noun_list = input.readlines()
	
	#随机出一个动词
	verb_index = random.randrange(0, len(verb_list))
    verb_value = verb_list[verb_index].replace("\n", "")
    verb_value = verb_value.replace("\t", "")
    verb_value = verb_value.replace("-", "")
    verb_value = verb_value.replace(" ", "")
    verb_value = verb_value.replace("\r", "")

	#随机出一个介词
    preposition_index = random.randrange(0, len(preposition_list))
    preposition_value = preposition_list[preposition_index].replace("\n", "")
    preposition_value = preposition_value.replace("-", "")
    preposition_value = preposition_value.replace(" ", "")
    preposition_value = preposition_value.replace("\r", "")

	#随机出一个形容词
    adjective_index = random.randrange(0, len(adjective_list))
    adjective_value = adjective_list[adjective_index].replace("\n", "")
    adjective_value = adjective_value.replace("-", "")
    adjective_value = adjective_value.replace(" ", "")
    adjective_value = adjective_value.replace("\r", "")

	#随机出一个名词
    noun_index = random.randrange(0, len(noun_list))
    noun_value = noun_list[noun_index].replace("\n", "")
    noun_value = noun_value.replace("-", "")
    noun_value = noun_value.replace(" ", "")
    noun_value = noun_value.replace("\r", "")

    #随机出一个副词
    adverb_index = random.randrange(0, len(adverb_list))
    adverb_value = adverb_list[adverb_index].replace("\n", "")
    adverb_value = adverb_value.replace("-", "")
    adverb_value = adverb_value.replace(" ", "")
    adverb_value = adverb_value.replace("\r", "")

    out_str = ""
    if generate_type == "property":
        # (形容词+名词 或 名词+副词)
        random_num = random.randrange(0, 100)
        if random_num % 2 == 0:
            out_str = class_prefix_str + adjective_value + first_str_capitalize(noun_value)
        else:
            out_str = class_prefix_str + noun_value + first_str_capitalize(adverb_value)
    elif generate_type == "func":
        # pdb.set_trace()
		# 函数名至少是三种组合 (动词+名词+副词)或（动词+形容词+名词）
        random_num = random.randrange(0, 100) % 2
        if random_num == 0:
            # 至少是 动词+名词+副词
            need_preposition = random.randrange(0, 100) % 2
            need_adjective = random.randrange(0, 100) % 2
            out_str = class_prefix_str + verb_value
            if need_preposition:
                out_str += first_str_capitalize(preposition_value)
            if need_adjective:
                out_str += first_str_capitalize(adjective_value)
            out_str += first_str_capitalize(noun_value) + first_str_capitalize(adverb_value)
			
        else:
            # 至少是 动词+形容词+名词
            need_preposition = random.randrange(0, 100) % 2
            need_adverb = random.randrange(0, 100) % 2
            out_str = class_prefix_str + verb_value
            if need_preposition:
                out_str += first_str_capitalize(preposition_value)
            out_str += first_str_capitalize(adjective_value) + first_str_capitalize(noun_value)
            if need_adverb:
                out_str += first_str_capitalize(adverb_value)
    elif generate_type == "random_str":
        # 前缀+两个string名词组合
        random_first = random_noun_list[random.randrange(0, len(random_noun_list))].replace("\n", "").replace("\r", "")
        random_last = random_noun_list[random.randrange(0, len(random_noun_list))].replace("\n", "").replace("\r", "")
        out_str = class_prefix_str + first_str_capitalize(random_first) + first_str_capitalize(random_last)
        
    else:
        out_str = class_prefix_str + verb_value + first_str_capitalize(noun_value)

    # print("outstr:" + out_str)
    return out_str


# 查找并替换所有的插入点
def search_replace_insert(file_list):
    transfer_context = []
    if os.path.exists("transfer.txt"):
        with open("transfer.txt", "r") as input:
            transfer_context = input.readlines()

    for file in file_list:
        file_context = []
        
        with open(file, "r+") as input:
            file_context = input.readlines()
        if len(file_context) > 0:
            file_replace_context = []
            for line in file_context:
                if "//////insert//" in line:
                    # 随机出一个函数调用替换掉
                    random_transfer = random.randrange(0, len(transfer_context))
                    random_line = transfer_context[random_transfer]

                    random_line = random_line.replace("\n", "")
                    # print("random_line : " + random_line)
                    class_name = random_line.split("//")[1]
                    

                    # pdb.set_trace()

                    import_using_log_path = "import_using.txt"
                    import_log_str = "#import \"" + class_name + ".h\"\n"
                    import_using_origin_content = ""
                    if os.path.exists(import_using_log_path):
                        with open(import_using_log_path, "r") as input:
                            import_using_origin_content = input.read()
                    
                    if class_name in import_using_origin_content:
                        print("aleady exist, pass")
                    else:
                        with open(import_using_log_path, "a") as input:
                            input.write(import_log_str)

                    header_file_path = "already/" + class_name + ".h"
                    implamentation_file_path = "already/" + class_name + ".m"
                    copyfile(header_file_path, "using/" + class_name + ".h")
                    copyfile(implamentation_file_path, "using/" + class_name + ".m")

                    replace_line = line.replace("//////insert//", random_line)
                    file_replace_context.append(replace_line)
                else:
                    file_replace_context.append(line)
            with open(file, "w") as input:
                input.writelines(file_replace_context)
            
                


# 替换项目中的插入点
def handle_insert():
    #生成100个随机类
    generate_class_for_max(2500)
    
    #找到所有匹配的文件
    # need_replace_file_list = getfilepath("target", [".m", ".mm"])
    need_replace_file_list = get_search_files("target", [".m", ".mm"], nosearch_directorys)

    # print("search file list :" + str(need_replace_file_list))
    search_replace_insert(need_replace_file_list)
    
# 批量生成垃圾文件
def generate_class_for_max(max_num):
    for i in range(max_num):
        generate_class_file("already")

# 生成.h文件内容
def generate_header_content(class_name, init_name, method_name):
    out_str = "\n\n\n#import <Foundation/Foundation.h>\n"
    out_str += "@interface "
    out_str += class_name
    out_str += " : NSObject\n"
    out_str += "+ (instancetype)"
    out_str += init_name
    out_str += ";\n"
    out_str += "- (void)"
    out_str += method_name
    out_str += ";\n"
    out_str += "@end\n"
    return out_str

# 生成.m文件内容
def generate_implementation_content(class_name, init_name, method_name):
    out_str = "\n\n\n#import \""
    out_str += class_name
    out_str += ".h\"\n"
    out_str += "@implementation "
    out_str += class_name
    out_str += "\n"
    out_str += "+ (instancetype)"
    out_str += init_name
    out_str += ";\n"
    out_str += "{\n"
    out_str += "\t"
    out_str += class_name
    out_str += " *yyyy = [["
    out_str += class_name
    out_str += " alloc] init];\n"
    out_str += "\treturn yyyy;\n"
    out_str += "}\n"

    out_str += "- (void)"
    out_str += method_name
    out_str += "\n"
    out_str += "{\n"
    out_str += generate_instance_method_realize()
    out_str += "}\n"

    out_str += "@end\n"
    return out_str
    

# 随机算法
def generate_random_operation():
    out_str = ""
    random_operation = random.randrange(0, 30)
    if random_operation == 0:
        out_str = "\txxx = xxx + yyy;\n"
    elif random_operation == 1:
        out_str = "\txxx = xxx - yyy;\n"
    elif random_operation == 2:
        out_str = "\txxx++;\n"
    elif random_operation == 3:
        out_str = "\txxx += yyy++;\n"
    elif random_operation == 4:
        random_num = random.randrange(1, 8)
        out_str = "\txxx = %d * 2 - xxx;\n" % random_num
    elif random_operation == 5:
        out_str = "\txxx = xxx ^ 2 << 2;\n"
    elif random_operation == 6:
        out_str = "\tyyy = yyy - xxx;\n"
    elif random_operation == 7:
        out_str = "\txxx = xxx >> 4;\n"
    elif random_operation == 8:
        out_str = "\txxx = xxx & 2;\n"
    elif random_operation == 9:
        out_str = "\txxx = xxx | 0xff;\n"
    elif random_operation == 10:
        out_str = "\txxx = xxx & 1 ? xxx + 3 : xxx + 4;\n"
    elif random_operation == 11:
        out_str = "\tccc = xxx + yyy & 5 << 3;\n"
    elif random_operation == 12:
        out_str = "\tddd += ccc + xxx ^ yyy;\n"
    elif random_operation == 13:
        out_str = "\teee += ddd;\n"
    elif random_operation == 14:
        out_str = "\teee = ddd > 0 ? eee - xxx : eee + yyy;\n"
    elif random_operation == 15:
        out_str = "\tddd += xxx + yyy - ccc;\n"
    elif random_operation == 16:
        out_str = "\teee -= xxx - ccc & 2;\n"
    elif random_operation == 17:
        out_str = "\tddd = ddd << 1;\n"
    elif random_operation == 18:
        out_str = "\tccc = ccc >> 1;\n"
    elif random_operation == 19:
        out_str = "\tddd *= xxx > 1;\n"
    elif random_operation == 20:
        out_str += "\txxx -= yyy & 0xff - ccc;\n"
    else:
        out_str = "\txxx -= yyy - xxx;\n"
    return out_str


# 生成一个类文件(包括一个.h和一个.m)
def generate_class_file(save_path):
    class_name = generate_words_str("property")
    init_name = generate_words_str("func")
    method_name = generate_words_str("func")

    class_header = generate_header_content(class_name, init_name, method_name)
    class_implementation = generate_implementation_content(class_name, init_name, method_name)

    header_path = save_path + "/" + class_name + ".h"

    # print("header_class: " + class_header)
    implementation_path = save_path + "/" + class_name + ".m"
    # print("class_implementation :" + class_implementation)
    transfer_log_path = "transfer.txt"
    transfer_log_str = "[[" + class_name + " " + init_name + "] " + method_name + "];//" + class_name + "\n"
    with open(transfer_log_path, "a") as input:
        input.write(transfer_log_str)

    import_log_path = "import.txt"
    import_log_str = "#import \"" + class_name + ".h\"\n"
    with open(import_log_path, "a") as input:
        input.write(import_log_str)

    with open(header_path, "w") as input:
        input.write(class_header)
    with open(implementation_path, "w") as input:
        input.write(class_implementation)


# 随机生成实例函数实现
def generate_instance_method_realize():

    # 生成字符串数组
    out_str = "\tNSArray *xxxx = @["
    random_list_length = random.randrange(4, 10)
    red_str = ""
    for i in range(random_list_length):
        red_str += "@\""
        red_str += generate_words_str("random_str")
        red_str += "\""
        if i != random_list_length - 1:
            red_str += ", "
    out_str += red_str
    out_str += "];\n"
    # print out_str

    
    return out_str


# 随机生成字符串
def generate_random_str(input_random_type):
    random_str_length = 0
    if input_random_type == out_random_type_class:
        random_str_length = random.randrange(9, 14)
    elif input_random_type == out_random_type_method_init:
        random_str_length = random.randrange(10, 15)
    elif input_random_type == out_random_type_method_name:
        random_str_length = random.randrange(10, 18)
    elif input_random_type == out_random_type_method_realize:
        random_str_length = random.randrange(7, 30)
    
    random_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    random_target_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    
    out_str = ''
    for i in range(random_str_length):
        if 0 == i:
            #第一个字符不能是数字
            char_first = random.choice(random_char)
            out_str += char_first
        else:
            #后面的字符可以是字符串
            char_other = random.choice(random_target_str)
            out_str += char_other
    # print ("generate_random_str : " + out_str)
    return out_str

# 随机生成系统调用
def generate_implementation_search():

    out_str = ""
    random_num = random.randrange(0, 150)
    if random_num == 1:
        # 获取设备名称
        out_str += "\tNSString *iPhoneName = [[UIDevice currentDevice] name];\n"
    elif random_num == 2:
        # 获取设备系统版本号
        out_str += "\tNSString *systemVersion = [[UIDevice currentDevice] systemVersion];\n"
    elif random_num == 3:
        # 获取系统名称
        out_str += "\tNSString *systemName = [[UIDevice currentDevice] systemName];\n"
    elif random_num == 4:
        # 获取设备型号
        out_str += "\tstruct utsname systemInfo;\n"
        out_str += "\tuname(&systemInfo);\n"
        out_str += "\tNSString *device_model = [NSString stringWithCString:systemInfo.machine encoding:NSUTF8StringEncoding];\n"
    elif random_num == 5:
        # 设备上次重启的时间
        out_str += "\tNSTimeInterval time = [[NSProcessInfo processInfo] systemUptime];\n"
        out_str += "\tNSDate *lastRestartDate = [[NSDate alloc] initWithTimeIntervalSinceNow:(0 - time)];\n"
    elif random_num == 6:
        # 广告位标识符idfa
        out_str += "\tNSString *idfa = [[[ASIdentifierManager sharedManager] advertisingIdentifier] UUIDString];\n"
    elif random_num == 7:
        # idfv
        out_str += "\tNSString *uuid = [[[UIDevice currentDevice] identifierForVendor] UUIDString];\n"
    elif random_num == 8:
        # 获取设备型号
        out_str += "\tstruct utsname systemInfo;\n"
        out_str += "\tuname(&systemInfo);\n"
        out_str += "\tNSString *device_model = [NSString stringWithCString:systemInfo.machine encoding:NSUTF8StringEncoding];\n"
    elif random_num == 9:
        # 获取app版本号
        out_str += "\tNSString *appversion = [[[NSBundle mainBundle] infoDictionary] objectForKey:@\"CFBundleShortVersionString\"];\n"
    elif random_num == 10:
        # 获取电池电量
        out_str += "\tfloat BatteryLever = [[UIDevice currentDevice] batteryLevel];\n"
        out_str += "\tNSUInteger levelPercent = BatteryLever * 100;\n"
        out_str += "\tNSString *levelValue = [NSString stringWithFormat:@\"%.2f\", BatteryLever];\n"
    elif random_num == 11:
        # 获取电池状态
        out_str += "\tUIDeviceBatteryState batteryStatu = [[UIDevice currentDevice] batteryState];\n"
    elif random_num == 12:
        # 获取电池容量
        out_str += "\tNSUInteger capacity = 2800;\n"
    elif random_num == 13:
        # 获取电池电压
        out_str += "\tfloat volocity = 3.8;\n"
    elif random_num == 14:
        # 获取设备ip地址
        out_str += "\tint sockfd = socket(AF_INET, SOCK_DGRAM, 0);\n"
        out_str += "\tNSMutableArray *ips = [NSMutableArray array];\n"
        out_str += "\tint BUFFERSIZE = 4096;\n"
        out_str += "\tstruct ifconf ifc;\n"
        out_str += "\tchar buffer[BUFFERSIZE], *ptr, lastname[IFNAMSIZ], *cptr;\n"
        out_str += "\tstruct ifreq *ifr, ifrcopy;\n"
        out_str += "\tifc.ifc_len = BUFFERSIZE;\n"
        out_str += "\tifc.ifc_buf = buffer;\n"
        out_str += "\tif (ioctl(sockfd, SIOCGIFCONF, &ifc) >= 0){\n"
        out_str += "\t\tfor (ptr = buffer; ptr < buffer + ifc.ifc_len; ){\n"
        out_str += "\t\t\tifr = (struct ifreq *)ptr;\n"
        out_str += "\t\t\tint len = sizeof(struct sockaddr);\n"
        out_str += "\t\t\tif (ifr->ifr_addr.sa_len > len) {\n"
        out_str += "\t\t\t\tlen = ifr->ifr_addr.sa_len;\n"
        out_str += "\t\t\t}\n"
        out_str += "\t\t\tptr += sizeof(ifr->ifr_name) + len;\n"
        out_str += "\t\t\tif (ifr->ifr_addr.sa_family != AF_INET) continue;\n"
        out_str += "\t\t\tif ((cptr = (char *)strchr(ifr->ifr_name, ':')) != NULL) *cptr = 0;\n"
        out_str += "\t\t\tif (strncmp(lastname, ifr->ifr_name, IFNAMSIZ) == 0) continue;\n"
        out_str += "\t\t\tmemcpy(lastname, ifr->ifr_name, IFNAMSIZ);\n"
        out_str += "\t\t\tifrcopy = *ifr;\n"
        out_str += "\t\t\tioctl(sockfd, SIOCGIFFLAGS, &ifrcopy);\n"
        out_str += "\t\t\tif ((ifrcopy.ifr_flags & IFF_UP) == 0) continue;\n"
        out_str += "\t\t\tNSString *ip = [NSString  stringWithFormat:@\"%s\", inet_ntoa(((struct sockaddr_in *)&ifr->ifr_addr)->sin_addr)];\n"
        out_str += "\t\t\t[ips addObject:ip];\n"
        out_str += "\t\t}\n"
        out_str += "\t}\n"
        out_str += "\tclose(sockfd);\n"
        out_str += "\tNSString *deviceIP = @\"\";\n"
        out_str += "\tfor (int i=0; i < ips.count; i++) {\n"
        out_str += "\t\tif (ips.count > 0) {\n"
        out_str += "\t\t\tdeviceIP = [NSString stringWithFormat:@\"%@\",ips.lastObject];\n"
        out_str += "\t\t}\n"
        out_str += "\t}\n"   
    
    elif random_num == 15:
        # 获取CPU实时频率
        out_str += "\tsize_t size = sizeof(int);\n"
        out_str += "\tint result;\n"
        out_str += "\tint mib[2] = {CTL_HW, HW_CPU_FREQ};\n"
        out_str += "\tsysctl(mib, 2, &result, &size, NULL, 0);\n"
    elif random_num == 16:
        # 获取总线程频率
        out_str += "\tsize_t size = sizeof(int);\n"
        out_str += "\tint result;\n"
        out_str += "\tint mib[2] = {CTL_HW, HW_BUS_FREQ};\n"
        out_str += "\tsysctl(mib, 2, &result, &size, NULL, 0);\n"
    elif random_num == 17:
        # 获取当前设备主存
        out_str += "\tsize_t size = sizeof(int);\n"
        out_str += "\tint result;\n"
        out_str += "\tint mib[2] = {CTL_HW, HW_MEMSIZE};\n"
        out_str += "\tsysctl(mib, 2, &result, &size, NULL, 0);\n"
    elif random_num == 18:
        # 获取CPU数量
        out_str += "\tNSUInteger cpucount = [[NSProcessInfo processInfo] activeProcessorCount];\n"
    elif random_num == 19:
        # 获取单个CPU的使用百分比
        out_str += "\tprocessor_info_array_t _cpuInfo, _prevCPUInfo = nil;\n"
        out_str += "\tmach_msg_type_number_t _numCPUInfo, _numPrevCPUInfo = 0;\n"
        out_str += "\tunsigned _numCPUs;\n"
        out_str += "\tNSLock *_cpuUsageLock;\n"
        out_str += "\tint _mib[2U] = { CTL_HW, HW_NCPU };\n"
        out_str += "\tsize_t _sizeOfNumCPUs = sizeof(_numCPUs);\n"
        out_str += "\tint _status = sysctl(_mib, 2U, &_numCPUs, &_sizeOfNumCPUs, NULL, 0U);\n"
        out_str += "\tif (_status) _numCPUs = 1;\n"
        out_str += "\t_cpuUsageLock = [[NSLock alloc] init];\n"
        out_str += "\tnatural_t _numCPUsU = 0U;\n"
        out_str += "\tkern_return_t err = host_processor_info(mach_host_self(), PROCESSOR_CPU_LOAD_INFO, &_numCPUsU, &_cpuInfo, &_numCPUInfo);\n"
        out_str += "\tif (err == KERN_SUCCESS) {\n"
        out_str += "\t\t[_cpuUsageLock lock];\n"
        out_str += "\t\tNSMutableArray *cpus = [NSMutableArray new];\n"
        out_str += "\t\tfor (unsigned i = 0U; i < _numCPUs; ++i) {\n"
        out_str += "\t\t\tFloat32 _inUse, _total;\n"
        out_str += "\t\t\tif (_prevCPUInfo) {\n"
        out_str += "\t\t\t\t_inUse = (\n"
        out_str += "\t\t\t\t\t\t(_cpuInfo[(CPU_STATE_MAX * i) + CPU_STATE_USER]   - _prevCPUInfo[(CPU_STATE_MAX * i) + CPU_STATE_USER])\n"
        out_str += "\t\t\t\t\t\t+ (_cpuInfo[(CPU_STATE_MAX * i) + CPU_STATE_SYSTEM] - _prevCPUInfo[(CPU_STATE_MAX * i) + CPU_STATE_SYSTEM])\n"
        out_str += "\t\t\t\t\t\t+ (_cpuInfo[(CPU_STATE_MAX * i) + CPU_STATE_NICE]   - _prevCPUInfo[(CPU_STATE_MAX * i) + CPU_STATE_NICE])\n"
        out_str += "\t\t\t\t\t\t);\n"
        out_str += "\t\t\t\t_total = _inUse + (_cpuInfo[(CPU_STATE_MAX * i) + CPU_STATE_IDLE] - _prevCPUInfo[(CPU_STATE_MAX * i) + CPU_STATE_IDLE]);\n"
        out_str += "\t\t\t} else {\n"
        out_str += "\t\t\t\t_inUse = _cpuInfo[(CPU_STATE_MAX * i) + CPU_STATE_USER] +\n"
        out_str += "\t\t\t\t\t_cpuInfo[(CPU_STATE_MAX * i) + CPU_STATE_SYSTEM] + _cpuInfo[(CPU_STATE_MAX * i) + CPU_STATE_NICE];\n"
        out_str += "\t\t\t\t_total = _inUse + _cpuInfo[(CPU_STATE_MAX * i) + CPU_STATE_IDLE];\n"
        out_str += "\t\t\t}\n"
        out_str += "\t\t\t[cpus addObject:@(_inUse / _total)];\n"
        out_str += "\t\t}\n"
        out_str += "\t\t[_cpuUsageLock unlock];\n"
        out_str += "\t\tif (_prevCPUInfo) {\n"
        out_str += "\t\t\tsize_t prevCpuInfoSize = sizeof(integer_t) * _numPrevCPUInfo;\n"
        out_str += "\t\t\tvm_deallocate(mach_task_self(), (vm_address_t)_prevCPUInfo, prevCpuInfoSize);\n"
        out_str += "\t\t}\n"
        out_str += "\t} else {\n"
        out_str += "\t\t;\n"
        out_str += "\t}\n"

    elif random_num == 20:
        # 获取本沙盒文稿大小
        out_str += "\tNSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);\n"
        out_str += "\tNSString *folderPath = [paths firstObject];\n"
        out_str += "\tNSArray *contents = [[NSFileManager defaultManager] contentsOfDirectoryAtPath:folderPath error:nil];\n"
        out_str += "\tNSEnumerator *contentsEnumurator = [contents objectEnumerator];\n"
        out_str += "\tNSString *file;\n"
        out_str += "\tunsigned long long folderSize = 0;\n"
        out_str += "\twhile (file = [contentsEnumurator nextObject]) {\n"
        out_str += "\t\tNSDictionary *fileAttributes = [[NSFileManager defaultManager] attributesOfItemAtPath:[folderPath stringByAppendingPathComponent:file] error:nil];\n"
        out_str += "\t\tfolderSize += [[fileAttributes objectForKey:NSFileSize] intValue];\n"
        out_str += "\t}\n"
        
    elif random_num == 21:
        # 获取library目录
        out_str += "\tNSArray *paths = NSSearchPathForDirectoriesInDomains(NSLibraryDirectory, NSUserDomainMask, YES);\n"
        out_str += "\tNSString *basePath = [paths firstObject];\n"
    elif random_num == 22:
        # 获取cache目录
        out_str += "\tNSArray *paths = NSSearchPathForDirectoriesInDomains(NSCachesDirectory, NSUserDomainMask, YES);\n"
        out_str += "\tNSString *basePath = [paths firstObject];\n"
    elif random_num == 23:
        # 获取temp目录
        out_str += "\tNSString *tempPath = NSTemporaryDirectory();\n"
    elif random_num == 24:
        # 获取磁盘总空间
        out_str += "\tNSError *error = nil;\n"
        out_str += "\tNSDictionary *attrs = [[NSFileManager defaultManager] attributesOfFileSystemForPath:NSHomeDirectory() error:&error];\n"
        out_str += "\tif (error) return nil;\n"
        out_str += "\tint64_t space =  [[attrs objectForKey:NSFileSystemSize] longLongValue];\n"
        out_str += "\tif (space < 0) space = -1;\n"
        out_str += "\tNSString *totalDiskInfo = [NSString stringWithFormat:@\"== %.2f MB == %.2f GB\", space/1024/1024.0, space/1024/1024/1024.0];\n"
    elif random_num == 25:
        # 获取未使用的磁盘空间
        out_str += "\tNSError *error = nil;\n"
        out_str += "\tNSDictionary *attrs = [[NSFileManager defaultManager] attributesOfFileSystemForPath:NSHomeDirectory() error:&error];\n"
        out_str += "\tif (error) return nil;\n"
        out_str += "\tint64_t space =  [[attrs objectForKey:NSFileSystemFreeSize] longLongValue];\n"
        out_str += "\tif (space < 0) space = -1;\n"
        out_str += "\tNSString *freeDiskInfo = [NSString stringWithFormat:@\" %.2f MB == %.2f GB\", space/1024/1024.0, space/1024/1024/1024.0];\n"
    elif random_num == 26:
        # 获取总内存空间
        out_str += "\tint64_t totalMemory = [[NSProcessInfo processInfo] physicalMemory];\n"
        out_str += "\tif (totalMemory < -1) totalMemory = -1;\n"
        out_str += "\tNSString *totalMemoryInfo = [NSString stringWithFormat:@\" %.2f MB == %.2f GB\", totalMemory/1024/1024.0, totalMemory/1024/1024/1024.0];\n"
    elif random_num == 27:
        # 获取活跃的内存空间
        out_str += "\tmach_port_t host_port = mach_host_self();\n"
        out_str += "\tmach_msg_type_number_t host_size = sizeof(vm_statistics_data_t) / sizeof(integer_t);\n"
        out_str += "\tvm_size_t page_size;\n"
        out_str += "\tvm_statistics_data_t vm_stat;\n"
        out_str += "\tkern_return_t kern;\n"
        out_str += "\tkern = host_page_size(host_port, &page_size);\n"
        out_str += "\tif (kern != KERN_SUCCESS) return nil;\n"
        out_str += "\tkern = host_statistics(host_port, HOST_VM_INFO, (host_info_t)&vm_stat, &host_size);\n"
        out_str += "\tNSString *activeMemoryInfo = [NSString stringWithFormat:@\"in activety %.2f MB == %.2f GB\", vm_stat.active_count * page_size/1024/1024.0, vm_stat.active_count * page_size/1024/1024/1024.0];\n"
        out_str += "\t\n"
    elif random_num == 28:
        # 获取不活跃的内存空间
        out_str += "\tmach_port_t host_port = mach_host_self();\n"
        out_str += "\tmach_msg_type_number_t host_size = sizeof(vm_statistics_data_t) / sizeof(integer_t);\n"
        out_str += "\tvm_size_t page_size;\n"
        out_str += "\tvm_statistics_data_t vm_stat;\n"
        out_str += "\tkern_return_t kern;\n"
        out_str += "\tkern = host_page_size(host_port, &page_size);\n"
        out_str += "\tkern = host_statistics(host_port, HOST_VM_INFO, (host_info_t)&vm_stat, &host_size);\n"
        out_str += "\tNSString *inActiveMemoryInfo = [NSString stringWithFormat:@\"not activety %.2f MB == %.2f GB\", vm_stat.inactive_count * page_size/1024/1024.0, vm_stat.inactive_count * page_size/1024/1024/1024.0];\n"
    elif random_num == 29:
        # 获取空闲的内存空间
        out_str += "\tmach_port_t host_port = mach_host_self();\n"
        out_str += "\tmach_msg_type_number_t host_size = sizeof(vm_statistics_data_t) / sizeof(integer_t);\n"
        out_str += "\tvm_size_t page_size;\n"
        out_str += "\tvm_statistics_data_t vm_stat;\n"
        out_str += "\tkern_return_t kern;\n"
        out_str += "\tkern = host_page_size(host_port, &page_size);\n"
        out_str += "\tkern = host_statistics(host_port, HOST_VM_INFO, (host_info_t)&vm_stat, &host_size);\n"
        out_str += "\tNSString *freeMemoryInfo = [NSString stringWithFormat:@\" %.2f MB == %.2f GB\", vm_stat.free_count * page_size/1024/1024.0, vm_stat.free_count * page_size/1024/1024/1024.0];\n"
    elif random_num == 30:
        # 获取正在使用的内存空间
        out_str += "\tmach_port_t host_port = mach_host_self();\n"
        out_str += "\tmach_msg_type_number_t host_size = sizeof(vm_statistics_data_t) / sizeof(integer_t);\n"
        out_str += "\tvm_size_t page_size;\n"    
        out_str += "\tvm_statistics_data_t vm_stat;\n"
        out_str += "\tkern_return_t kern;\n"
        out_str += "\tkern = host_page_size(host_port, &page_size);\n"
        out_str += "\tkern = host_statistics(host_port, HOST_VM_INFO, (host_info_t)&vm_stat, &host_size);\n"
        out_str += "\tNSString *usedMemoryInfo = [NSString stringWithFormat:@\" %.2f MB == %.2f GB\", page_size * (vm_stat.active_count + vm_stat.inactive_count + vm_stat.wire_count)/1024/1024.0, page_size * (vm_stat.active_count + vm_stat.inactive_count + vm_stat.wire_count)/1024/1024/1024.0];\n"
    elif random_num == 31:
        # 获取用于存放内核的内存空间
        out_str += "\tmach_port_t host_port = mach_host_self();\n"
        out_str += "\tmach_msg_type_number_t host_size = sizeof(vm_statistics_data_t) / sizeof(integer_t);\n"
        out_str += "\tvm_size_t page_size;\n"
        out_str += "\tvm_statistics_data_t vm_stat;\n"
        out_str += "\tkern_return_t kern;\n"
        out_str += "\tkern = host_page_size(host_port, &page_size);\n"
        out_str += "\tkern = host_statistics(host_port, HOST_VM_INFO, (host_info_t)&vm_stat, &host_size);\n"
        out_str += "\tNSString *wiredMemoryInfo = [NSString stringWithFormat:@\"framework memory %.2f MB == %.2f GB\", vm_stat.wire_count * page_size/1024/1024.0, vm_stat.wire_count * page_size/1024/1024/1024.0];\n"
    elif random_num == 32:
        # 获取可释放的内存空间
        out_str += "\tmach_port_t host_port = mach_host_self();\n"
        out_str += "\tmach_msg_type_number_t host_size = sizeof(vm_statistics_data_t) / sizeof(integer_t);\n"
        out_str += "\tvm_size_t page_size;\n"
        out_str += "\tvm_statistics_data_t vm_stat;\n"
        out_str += "\tkern_return_t kern;\n"
        out_str += "\tkern = host_page_size(host_port, &page_size);\n"
        out_str += "\tkern = host_statistics(host_port, HOST_VM_INFO, (host_info_t)&vm_stat, &host_size);\n"
        out_str += "\tNSString *purgableMemoryInfo = [NSString stringWithFormat:@\"can purgable %.2f MB == %.2f GB\", vm_stat.purgeable_count * page_size/1024/1024.0, vm_stat.purgeable_count * page_size/1024/1024/1024.0];\n"
    elif random_num == 33:
        # 打印idfa
        out_str += "\tNSString *idfa = [[[ASIdentifierManager sharedManager] advertisingIdentifier] UUIDString];\n"
        out_str += "\tNSLog(@\"%@\", idfa);\n"
    else:
        # 定义随机字符串
        out_str += generate_instance_method_realize()
        
    return out_str

'''
    dic_class_a = {"class": class_name_a, 
        "init":init_name_a, 
        "search_method":method_name_a, 
        "middle":[method_middle_name_a, method_middle_name_a2], 
        "insert_classes":[class_name_c, class_name_b],
        method_middle_name_a: 
        { 
            "class":class_name_c, 
            "init":init_name_c, 
            "method":method_name_c 
        }, 
        method_middle_name_a2: 
        { 
            "class":class_name_b, 
            "init":init_name_b, 
            "method":method_middle_name_b 
        }, 
        "entrance":method_middle_name_a2
    }
'''
# 根据配置生成类文件及导入文件
def generate_class_file_by_config(class_config_dic):

    entrance_str = ""
    header_file_content = ""
    implementation_file_content = ""
    import_using_content = ""

    class_name = class_config_dic.get("class")
    init_method = class_config_dic.get("init")
    search_method = class_config_dic.get("search_method")
    middle_methods = class_config_dic.get("middle")
    insert_classes = class_config_dic.get("insert_classes")
    entrance_method = class_config_dic.get("entrance")

    header_file_content += "\n\n\n#import <Foundation/Foundation.h>\n\n"
    header_file_content += "@interface "
    header_file_content += class_name
    header_file_content += " : NSObject\n"
    header_file_content += "+ (instancetype)"
    header_file_content += init_method
    header_file_content += ";\n"

    implementation_file_content += "\n\n\n#import \""
    implementation_file_content += class_name
    implementation_file_content += ".h\"\n\n"
    
    if insert_classes:
        for insert_class in insert_classes:
            implementation_file_content += "#import \""
            implementation_file_content += insert_class
            implementation_file_content += ".h\"\n"
    
    implementation_file_content += "@implementation "
    implementation_file_content += class_name
    implementation_file_content += "\n"
    implementation_file_content += "+ (instancetype)"
    implementation_file_content += init_method
    implementation_file_content += "\n{\n\t"
    implementation_file_content += class_name
    implementation_file_content += " *yyyy = [["
    implementation_file_content += class_name
    implementation_file_content += " alloc] init];\n"
    implementation_file_content += "\treturn yyyy;\n}\n\n"

    if search_method :
        header_file_content += "- (void)"
        header_file_content += search_method
        header_file_content += ";\n"
        
        implementation_file_content += "- (void)"
        implementation_file_content += search_method
        implementation_file_content += "\n{\n"
        implementation_file_content += generate_implementation_search()
        implementation_file_content += "}\n\n"
    
    if middle_methods:
        for middle_method in middle_methods:
            header_file_content += "- (void)"
            header_file_content += middle_method
            header_file_content += ";\n"

            implementation_file_content += "- (void)"
            implementation_file_content += middle_method
            implementation_file_content += "\n{\n\t"
            
            use_class_name = (class_config_dic.get(middle_method)).get("class")
            use_class_init = (class_config_dic.get(middle_method)).get("init")
            use_class_method = (class_config_dic.get(middle_method)).get("method")

            implementation_file_content += "[["
            implementation_file_content += use_class_name
            implementation_file_content += " "
            implementation_file_content += use_class_init
            implementation_file_content += "] "
            implementation_file_content += use_class_method
            implementation_file_content += "];\n"
            
            # 中间调用类需要定义字符串
            implementation_file_content += generate_instance_method_realize()
            implementation_file_content += "}\n\n"
            
    
    header_file_content += "@end\n"
    implementation_file_content += "@end\n"
    
    if entrance_method:
        entrance_str += "[["
        entrance_str += class_name
        entrance_str += " "
        entrance_str += init_method
        entrance_str += "] "
        entrance_str += entrance_method
        entrance_str += "];\n"
        
    # pdb.set_trace()
    import_using_content += "#import \""
    import_using_content += class_name
    import_using_content += ".h\"\n"
    
    # 需要生成文件
    import_using_log_path = "import/import_using.txt"
    with open(import_using_log_path, "a") as input:
        input.write(import_using_content)
    # print("file exist %s:" % os.path.isfile(import_using_log_path))

    header_file_path = "using/" + class_name + ".h"
    implamentation_file_path = "using/" + class_name + ".m"
        
    with open(header_file_path, "w") as input:
        input.writelines(header_file_content)

    with open(implamentation_file_path, "w") as input:
        input.writelines(implementation_file_content)
    
    #返回调用入口
    return entrance_str


# 生成中间调用类3
def generate_middle_class_3_type():
    class_name_c = generate_words_str("property")
    init_name_c = generate_words_str("func")
    method_name_c = generate_words_str("func")

    class_name_b = generate_words_str("property")
    init_name_b = generate_words_str("func")
    method_middle_name_b = generate_words_str("func")

    class_name_a = generate_words_str("property")
    init_name_a = generate_words_str("func")
    method_middle_name_a = generate_words_str("func")


    dic_class_c = {"class": class_name_c, "init":init_name_c, "search_method":method_name_c}
    dic_class_b = {"class": class_name_b, "init":init_name_b, "middle":[method_middle_name_b], 
        "insert_classes":[class_name_c], 
        method_middle_name_b: 
        { 
            "class":class_name_c, 
            "init":init_name_c, 
            "method":method_name_c 
        }, 
    }
    dic_class_a = {"class": class_name_a, "init":init_name_a, 
        "middle":[method_middle_name_a],
        "insert_classes":[ class_name_b],
        method_middle_name_a: 
        { 
            "class":class_name_b, 
            "init":init_name_b, 
            "method":method_middle_name_b 
        },
        "entrance":method_middle_name_a
    }

    generate_class_file_by_config(dic_class_c)
    generate_class_file_by_config(dic_class_b)
    return generate_class_file_by_config(dic_class_a)

# 生成中间调用类5
def generate_middle_class_5_type():

    class_name_e = generate_words_str("property")
    init_name_e = generate_words_str("func")
    method_name_e = generate_words_str("func")

    class_name_d = generate_words_str("property")
    init_name_d = generate_words_str("func")
    method_middle_name_d = generate_words_str("func")

    class_name_c = generate_words_str("property")
    init_name_c = generate_words_str("func")
    method_middle_name_c = generate_words_str("func")

    class_name_b = generate_words_str("property")
    init_name_b = generate_words_str("func")
    method_middle_name_b = generate_words_str("func")

    class_name_a = generate_words_str("property")
    init_name_a = generate_words_str("func")
    method_middle_name_a = generate_words_str("func")


    dic_class_e = {"class": class_name_e, "init":init_name_e, "search_method":method_name_e}
    dic_class_d = {"class": class_name_d, "init":init_name_d, "middle":[method_middle_name_d], 
        "insert_classes":[class_name_e], 
        method_middle_name_d: 
        {
            "class":class_name_e, 
            "init":init_name_e, 
            "method":method_name_e 
        }
    }
    dic_class_c = {"class": class_name_c, "init":init_name_c, "middle":[method_middle_name_c], 
        "insert_classes":[class_name_d], 
        method_middle_name_c: 
        { 
            "class":class_name_d, 
            "init":init_name_d, 
            "method":method_middle_name_d 
        }  
    }
    dic_class_b = {"class": class_name_b, "init":init_name_b, "middle":[method_middle_name_b], 
        "insert_classes":[class_name_c], 
        method_middle_name_b: 
        { 
            "class":class_name_c, 
            "init":init_name_c, 
            "method":method_middle_name_c 
        }
    }
    dic_class_a = {"class": class_name_a, "init":init_name_a, 
        "middle":[method_middle_name_a], 
        "insert_classes":[class_name_b],
        method_middle_name_a: 
        { 
            "class":class_name_b, 
            "init":init_name_b, 
            "method":method_middle_name_b 
        }, 
        "entrance":method_middle_name_a
    }

    generate_class_file_by_config(dic_class_e)
    generate_class_file_by_config(dic_class_d)
    generate_class_file_by_config(dic_class_c)
    generate_class_file_by_config(dic_class_b)
    return generate_class_file_by_config(dic_class_a)


# 生成中间调用类4
def generate_middle_class_4_type():
    class_name_c = generate_words_str("property")
    init_name_c = generate_words_str("func")
    method_name_c = generate_words_str("func")

    class_name_a = generate_words_str("property")
    init_name_a = generate_words_str("func")
    method_middle_name_a = generate_words_str("func")

    class_name_b = generate_words_str("property")
    init_name_b = generate_words_str("func")
    method_middle_name_b = generate_words_str("func")

    method_middle_name_a2 = generate_words_str("func")

    dic_class_c = {"class": class_name_c, "init":init_name_c, "search_method":method_name_c}
    dic_class_b = {"class": class_name_b, "init":init_name_b, "middle":[method_middle_name_b], 
        "insert_classes":[class_name_a], 
        method_middle_name_b: 
        { 
            "class":class_name_a, 
            "init":init_name_a, 
            "method":method_middle_name_a 
        }   
    }
    dic_class_a = {"class": class_name_a, "init":init_name_a, 
        "middle":[method_middle_name_a, method_middle_name_a2], 
        "insert_classes":[class_name_c, class_name_b],
        method_middle_name_a: 
        { 
            "class":class_name_c, 
            "init":init_name_c, 
            "method":method_name_c 
        }, 
        method_middle_name_a2: 
        { 
            "class":class_name_b, 
            "init":init_name_b, 
            "method":method_middle_name_b 
        }, 
        "entrance":method_middle_name_a2
    }

    generate_class_file_by_config(dic_class_c)
    generate_class_file_by_config(dic_class_b)
    return generate_class_file_by_config(dic_class_a)

# 生成中间调用类6
def generate_middle_class_6_type():

    class_name_a = generate_words_str("property")
    init_name_a = generate_words_str("func")
    method_name_a = generate_words_str("func")

    class_name_d = generate_words_str("property")
    init_name_d = generate_words_str("func")
    method_middle_name_d = generate_words_str("func")

    class_name_b = generate_words_str("property")
    init_name_b = generate_words_str("func")
    method_middle_name_b = generate_words_str("func")

    class_name_c = generate_words_str("property")
    init_name_c = generate_words_str("func")
    method_middle_name_c = generate_words_str("func")

    method_middle_name_b2 = generate_words_str("func")
    method_middle_name_a2 = generate_words_str("func")

    dic_class_d = {"class": class_name_d, "init":init_name_d, 
        "middle":[method_middle_name_d], 
        "insert_classes":[class_name_a], 
        method_middle_name_d: 
        { 
            "class":class_name_a, 
            "init":init_name_a, 
            "method":method_name_a 
        } 
    }
    dic_class_c = {"class": class_name_c, "init":init_name_c, "middle":[method_middle_name_c], 
        "insert_classes":[class_name_b], 
        method_middle_name_c: 
        { 
            "class":class_name_b, 
            "init":init_name_b, 
            "method":method_middle_name_b 
        },
    }
    dic_class_b = {"class": class_name_b, "init":init_name_b, "middle":[method_middle_name_b, method_middle_name_b2],
        "insert_classes":[class_name_d, class_name_c], 
        method_middle_name_b: 
        { 
            "class":class_name_d, 
            "init":init_name_d, 
            "method":method_middle_name_d 
        },  
        method_middle_name_b2: 
        { 
            "class":class_name_c, 
            "init":init_name_c, 
            "method":method_middle_name_c 
        } 
    }
    dic_class_a = {"class": class_name_a, "init":init_name_a, 
        "middle":[method_middle_name_a2], 
        "insert_classes":[class_name_b], 
        "search_method":method_name_a, 
        method_middle_name_a2: 
        { 
            "class":class_name_b, 
            "init":init_name_b, 
            "method":method_middle_name_b 
        }, 
        "entrance":method_middle_name_a2
    }

    generate_class_file_by_config(dic_class_d)
    generate_class_file_by_config(dic_class_c)
    generate_class_file_by_config(dic_class_b)
    return generate_class_file_by_config(dic_class_a)

# 生成中间调用类7
def generate_middle_class_7_type():

    class_name_a = generate_words_str("property")
    init_name_a = generate_words_str("func")
    method_name_a = generate_words_str("func")

    class_name_c = generate_words_str("property")
    init_name_c = generate_words_str("func")
    method_middle_name_c = generate_words_str("func")

    class_name_d = generate_words_str("property")
    init_name_d = generate_words_str("func")
    method_middle_name_d = generate_words_str("func")

    class_name_b = generate_words_str("property")
    init_name_b = generate_words_str("func")
    method_middle_name_b = generate_words_str("func")

    method_middle_name_c2 = generate_words_str("func")

    method_middle_name_b2 = generate_words_str("func")
    method_middle_name_a2 = generate_words_str("func")

    dic_class_d = {"class": class_name_d, "init":init_name_d, 
        "middle":[method_middle_name_d], 
        "insert_classes":[class_name_c], 
        method_middle_name_d: 
        { 
            "class":class_name_c, 
            "init":init_name_c, 
            "method":method_middle_name_c 
        } 
    }
    dic_class_c = {"class": class_name_c, "init":init_name_c, "middle":[method_middle_name_c, method_middle_name_c2], 
        "insert_classes":[class_name_a, class_name_b], 
        method_middle_name_c: 
        { 
            "class":class_name_a, 
            "init":init_name_a, 
            "method":method_name_a 
        }, 
        method_middle_name_c2: 
        { 
            "class":class_name_b, 
            "init":init_name_b, 
            "method":method_middle_name_b 
        },
    }
    dic_class_b = {"class": class_name_b, "init":init_name_b, "middle":[method_middle_name_b, method_middle_name_b2],
        "insert_classes":[class_name_d, class_name_c], 
        method_middle_name_b:
        { 
            "class":class_name_d, 
            "init":init_name_d, 
            "method":method_middle_name_d 
        },
        method_middle_name_b2: 
        { 
            "class":class_name_c, 
            "init":init_name_c, 
            "method":method_middle_name_c 
        } 
    }
    dic_class_a = {"class": class_name_a, "init":init_name_a, 
        "middle":[method_middle_name_a2], 
        "insert_classes":[class_name_b], 
        "search_method":method_name_a, 
        method_middle_name_a2: 
        { 
            "class":class_name_b, 
            "init":init_name_b, 
            "method":method_middle_name_b 
        },
        "entrance":method_middle_name_a2
    }

    generate_class_file_by_config(dic_class_d)
    generate_class_file_by_config(dic_class_c)
    generate_class_file_by_config(dic_class_b)
    return generate_class_file_by_config(dic_class_a)
    

# 处理中间调用层
def handle_mixed_with_depth(input_depth):

    insert_str = ""
    if input_depth == mixed_type_A_B_C:
        #基本类型
        print("mixed_type_A_B_C")
        insert_str = generate_middle_class_3_type()
    elif input_depth == mixed_type_A_B_C_D_E:
        #基本类型
        print("mixed_type_A_B_C_D_E")
        insert_str = generate_middle_class_5_type()
    elif input_depth == mixed_type_A_B_A_C:
        #复杂类型
        print("mixed_type_A_B_A_C")
        insert_str = generate_middle_class_4_type()
    elif input_depth == mixed_type_A_B_C_B_D_A:
        #复杂类型
        print("mixed_type_A_B_C_B_D_A")
        insert_str = generate_middle_class_6_type()
    elif input_depth == mixed_type_A_B_C_B_D_C_A:
        #复杂类型
        print("mixed_type_A_B_C_B_D_C_A")
        insert_str = generate_middle_class_7_type()
    else:
        print("--未知深度类型--error!!")
    return insert_str    

# 处理生成中间调用层
def handle_insert_mixed():

    # need_replace_file_list = getfilepath("target", [".m", ".mm"])
    need_replace_file_list = get_search_files("target", [".m", ".mm"], nosearch_directorys)

    for file in need_replace_file_list:

        file_context = []
        with open(file, "r+") as input:
            file_context = input.readlines()
        if len(file_context) > 0:
            file_replace_context = []
            for line in file_context:
                if "//////insert//" in line:
                    # 随机深度值3~7
                    mixed_depth = random.randrange(3, 8)
                    # 生成一个基本类
                    need_replace_str = handle_mixed_with_depth(mixed_depth)
                    replace_line = line.replace("//////insert//", need_replace_str)
                    file_replace_context.append(replace_line)
                else:
                    file_replace_context.append(line)
            with open(file, "w") as input:
                input.writelines(file_replace_context)



# # 生成随机混淆类
# def generate_random_files():

#     # 随机生成30~40个类
#     random_class_num = random.randrange(32, 52)
#     # random_class_num = 3
#     for class_index in range(random_class_num):
#         class_name = generate_words_str("property")

#         # print("class_name :" + class_name)
#         # random_shared = global_shared_instance[random.randrange(0, len(global_shared_instance))]
#         random_shared = generate_words_str("func")

#         #随机生成0~10个属性
#         property_list = []
#         random_property_count = random.randrange(0, 15)
#         for property_index in range(random_property_count):
#             property_name = generate_words_str("property")
#             property_list.append(property_name)

#         #随机生成10~20个数组字符串方法
#         method_list = []
#         method_type_list = []
#         random_method_count = random.randrange(7, 25)
#         for method_index in range(random_method_count):
#             method_name = generate_words_str("func")

#             # random_index = random.randrange(0, 100)

#             # 指定类型
#             random_index = implamentation_type_0722
#             # method_type = 0
#             # if random_index <= 48:
#             method_type = random_index
#             # else:
#             #     method_type = len(method_return_type) - 1

#             method_list.append(method_name)
#             method_type_list.append(method_type)
        
#         #生成指定类的.h文件内容
#         header_str = header_of_file(class_name, random_shared, property_list, method_list, method_type_list)

#         #生成指定类的.m文件内容
#         implamentation_str = implamentation_of_file(class_name, random_shared, property_list, method_list, method_type_list)

#         #生成对应类的对应method的调用方法
#         transfer_str = transfer_for_class(class_name, random_shared, method_list, method_type_list)

#         #生成对应类的导入import信息
#         import_str = import_for_class(class_name)

#         #将上述的东西写进文件
#         header_path = "already/" + class_name + ".h"
#         implamentation_path = "already/" + class_name + ".m"
#         transfer_path = "alltransfer.txt"
#         import_path = "allimport.txt"

#         with open(header_path, "w") as input:
#             input.write(header_str)
        
#         with open(implamentation_path, "w") as input:
#             input.write(implamentation_str)
        
#         with open(transfer_path, "a") as input:
#             input.write(transfer_str)
        
#         with open(import_path, "a") as input:
#             input.write(import_str)


# 生成指定类的对应方法的调用
def transfer_for_class(class_name, shared_instance, method_list, method_type_list):
    out_str = ""
    if method_list:
        for index, method_name in enumerate(method_list):
            method_type = method_type_list[index]
            if method_type == implamentation_type_string_array:
                random_str = "@\"" + generate_words_str("random_str") + "\""
                out_str += "[[" + class_name + " " + shared_instance + "]" + " " + method_name + ":" + random_str + "];" + "//" + class_name + "\n"
            else:
                out_str += "[[" + class_name + " " + shared_instance + "]" + " " + method_name + "];" + "//" + class_name + "\n"
    return out_str

# 生成指定类的导入信息
def import_for_class(class_name):
    out_str = ""
    out_str += "#import \"" + class_name + ".h\"\n"
    return out_str


# 生成指定类的.h文件
def header_of_file(class_name, shared_instance, property_list, method_list, method_type_list):
    out_str = ""
    out_str += "\n\n\n"

    #导入头文件
    out_str += "#import <Foundation/Foundation.h>\n"
    out_str += "#import <UIKit/UIKit.h>"
    out_str += "\n"
    
    random_class_index = random.randrange(0, len(global_system_class_list))
    random_class_name = global_system_class_list[random_class_index]
    random_class_name = "NSObject"
    out_str += "@interface " + class_name + " : " + random_class_name + "\n"
    
    out_str += "+ (instancetype)" + shared_instance + ";\n"
    if property_list:
        for property_name in property_list:
            property_str = implamentation_property(property_name)
            out_str += property_str
    
    if method_list:
        for index, method_obj in enumerate(method_list):
            method_str = method_obj.get_method_prototype()
            method_str += ";\n"
            out_str += method_str
    out_str += "\n@end\n"
    return out_str


# 生成指定类的.m文件
def implamentation_of_file(class_name, shared_instance, property_list, method_list, method_type_list, class_obj_list):
    out_str = ""
    out_str += "\n\n\n"

    #导入头文件
    out_str += "#import \"" + class_name + ".h\"\n"
    out_str += "\n"
    out_str += "@implementation " + class_name + "\n"
    
    if property_list:
        for property_name in property_list:
            out_str += "@synthesize " + property_name + " = _" + property_name + ";\n"
    out_str += "\n"

    #sharedinstance方法位置
    out_str += "+ (instancetype)" + shared_instance + "\n{\n"
    out_str += implamentation_of_sharedinstance(class_name)
    out_str += "}\n\n"
     
    #method_list方法位置
    if method_list:
        for index, method_obj in enumerate(method_list):
            method_implamentation = implamentation_method_with_type(method_obj, implamentation_type_mutablestring_data_tNSMutableData, property_list, class_obj_list)
            out_str += method_implamentation
            
    out_str += "\n@end\n"
    return out_str
    

# 生成属性名的实现
def implamentation_property(property_name):
    out_str = ""
    out_str += "@property ("
    random_type = random.randrange(0, 100)
    random_type = 0
    property_type = ""
    if random_type % 2:
        property_type = global_property_normal_type[random.randrange(0, len(global_property_normal_type))]
        property_type = "NSString"
        out_str += "nonatomic) "
        out_str += property_type
        out_str += " "
    else:
        property_type = global_property_point_type[random.randrange(0, len(global_property_point_type))]
        property_type = "NSString"
        out_str += "retain, nonatomic) "
        out_str += property_type + " *"

    out_str += property_name
    out_str += ";\n"
    return out_str

# 随机生成实例方法的实现
def implamentation_of_sharedinstance(class_name):
    out_str = ""
    var_handle = generate_random_str(out_random_type_class)
    var_once = generate_random_str(out_random_type_class)
    out_str += "\tstatic " + class_name + " *" + var_handle +" = nil;\n"
    out_str += "\tstatic dispatch_once_t " + var_once + ";\n"
    
    out_str += "\tdispatch_once(&" + var_once + ", ^{\n"
    out_str += "\t\tif(!" + var_handle + ")\n"
    out_str += "\t\t{\n"
    out_str += "\t\t\t" + var_handle + " = [[" + class_name +" alloc] init];\n"
    out_str += "\t\t}\n"
    out_str += "\t});\n"
    
    out_str += "\treturn " + var_handle + ";\n"
    return out_str

# 随机获取一个参数名
def get_random_arg(method_obj):
    '''
    随机获取一个参数名
    '''
    out_str = ""
    if method_obj.arg_list == []:
        out_str = "-1"
    else:
        out_str = method_obj.arg_list[random.randrange(0, len(method_obj.arg_list))]
    return out_str

# 随机获取一个属性值的调用
def get_random_property(class_list):
    class_obj = class_list[random.randrange(0, len(class_list))]
    property_list = class_obj.get_property_list()
    while property_list == []:
        class_obj = class_list[random.randrange(0, len(class_list))]
        property_list = class_obj.get_property_list()
    out_str = "["
    out_str += class_obj.get_class_name()
    out_str += " " + class_obj.get_shared_method() + "]"
    out_str += "." + property_list[random.randrange(0, len(property_list))]
    return out_str




# 生成对应方法的实现
def implamentation_method_with_type(method_obj, method_type, current_property_list, class_obj_list):
    out_str = ""
    out_str += method_obj.get_method_prototype()
    out_str += "\n"
    
    out_str += "{\n"
    if method_type == implamentation_type_get_device_name:
        # 获取设备名称
        out_str += "\t//获取设备名称\n"
        out_str += "\tNSString *iPhoneName = [[UIDevice currentDevice] name];\n"
        out_str += "\t return iPhoneName;\n"
        
    elif method_type == implamentation_type_get_system_version:
        # 获取设备系统版本号
        out_str += "\t//获取设备系统版本号\n"
        out_str += "\tNSString *systemVersion = [[UIDevice currentDevice] systemVersion];\n"
        out_str += "\treturn systemVersion;\n"
    elif method_type == implamentation_type_get_system_name:
        # 获取系统名称
        out_str += "\t//获取系统名称\n"
        out_str += "\tNSString *systemName = [[UIDevice currentDevice] systemName];\n"
        out_str += "\treturn systemName;\n"
    elif method_type == implamentation_type_get_device_model:
        # 获取设备型号
        out_str += "\t//获取设备型号\n"
        out_str += "\tstruct utsname systemInfo;\n"
        out_str += "\tuname(&systemInfo);\n"
        out_str += "\tNSString *device_model = [NSString stringWithCString:systemInfo.machine encoding:NSUTF8StringEncoding];\n"
        out_str += "\treturn device_model;\n"
    elif method_type == implamentation_type_get_reboot_time:
        # 设备上次重启的时间
        out_str += "\t//设备上次重启的时间\n"
        out_str += "\tNSTimeInterval time = [[NSProcessInfo processInfo] systemUptime];\n"
        out_str += "\tNSDate *lastRestartDate = [[NSDate alloc] initWithTimeIntervalSinceNow:(0 - time)];\n"
        out_str += "\treturn lastRestartDate;\n"
    elif method_type == implamentation_type_get_idfa:
        # 广告位标识符idfa
        out_str += "\t//广告位标识符idfa\n"
        out_str += "\tNSString *idfa = [[[ASIdentifierManager sharedManager] advertisingIdentifier] UUIDString];\n"
        out_str += "\treturn idfa;\n"
    elif method_type == implamentation_type_get_idfv:
        # idfv
        out_str += "\t//idfv\n"
        out_str += "\tNSString *idfv = [[[UIDevice currentDevice] identifierForVendor] UUIDString];\n"
        out_str += "\treturn idfv;\n"
    elif method_type == implamentation_type_get_app_version:
        # 获取app版本号
        out_str += "\t//获取app版本号\n"
        out_str += "\tNSString *appversion = [[[NSBundle mainBundle] infoDictionary] objectForKey:@\"CFBundleShortVersionString\"];\n"
        out_str += "\treturn appversion;\n"
    elif method_type == implamentation_type_get_battery_electricity:
        # 获取电池电量
        out_str += "\t//获取电池电量\n"
        out_str += "\tfloat BatteryLever = [[UIDevice currentDevice] batteryLevel];\n"
        out_str += "\tNSUInteger levelPercent = BatteryLever * 100;\n"
        out_str += "\tNSString *levelValue = [NSString stringWithFormat:@\"%.2f\", BatteryLever];\n"
        out_str += "\treturn levelValue;\n"
    elif method_type == implamentation_type_get_battery_status:
        # 获取电池状态
        out_str += "\t//获取电池状态\n"
        out_str += "\tUIDeviceBatteryState batteryStatu = [[UIDevice currentDevice] batteryState];\n"
        out_str += "\treturn batteryStatu;\n"
    elif method_type == implamentation_type_get_battery_capacity:
        # 获取电池容量
        out_str += "\t//获取电池容量\n"
        out_str += "\tNSUInteger capacity = 2800;\n"
        out_str += "\treturn capacity;\n"
    elif method_type == implamentation_type_get_battery_voltage:
        # 获取电池电压
        out_str += "\t//获取电池电压\n"
        out_str += "\tfloat volocity = 3.8;\n"
        out_str += "\treturn volocity;\n"
    elif method_type == implamentation_type_get_ip:
        # 获取设备ip地址
        out_str += "\t//获取设备ip地址\n"
        out_str += "\tint sockfd = socket(AF_INET, SOCK_DGRAM, 0);\n"
        out_str += "\tNSMutableArray *ips = [NSMutableArray array];\n"
        out_str += "\tint BUFFERSIZE = 4096;\n"
        out_str += "\tstruct ifconf ifc;\n"
        out_str += "\tchar buffer[BUFFERSIZE], *ptr, lastname[IFNAMSIZ], *cptr;\n"
        out_str += "\tstruct ifreq *ifr, ifrcopy;\n"
        out_str += "\tifc.ifc_len = BUFFERSIZE;\n"
        out_str += "\tifc.ifc_buf = buffer;\n"
        out_str += "\tif (ioctl(sockfd, SIOCGIFCONF, &ifc) >= 0){\n"
        out_str += "\t\tfor (ptr = buffer; ptr < buffer + ifc.ifc_len; ){\n"
        out_str += "\t\t\tifr = (struct ifreq *)ptr;\n"
        out_str += "\t\t\tint len = sizeof(struct sockaddr);\n"
        out_str += "\t\t\tif (ifr->ifr_addr.sa_len > len) {\n"
        out_str += "\t\t\t\tlen = ifr->ifr_addr.sa_len;\n"
        out_str += "\t\t\t}\n"
        out_str += "\t\t\tptr += sizeof(ifr->ifr_name) + len;\n"
        out_str += "\t\t\tif (ifr->ifr_addr.sa_family != AF_INET) continue;\n"
        out_str += "\t\t\tif ((cptr = (char *)strchr(ifr->ifr_name, ':')) != NULL) *cptr = 0;\n"
        out_str += "\t\t\tif (strncmp(lastname, ifr->ifr_name, IFNAMSIZ) == 0) continue;\n"
        out_str += "\t\t\tmemcpy(lastname, ifr->ifr_name, IFNAMSIZ);\n"
        out_str += "\t\t\tifrcopy = *ifr;\n"
        out_str += "\t\t\tioctl(sockfd, SIOCGIFFLAGS, &ifrcopy);\n"
        out_str += "\t\t\tif ((ifrcopy.ifr_flags & IFF_UP) == 0) continue;\n"
        out_str += "\t\t\tNSString *ip = [NSString  stringWithFormat:@\"%s\", inet_ntoa(((struct sockaddr_in *)&ifr->ifr_addr)->sin_addr)];\n"
        out_str += "\t\t\t[ips addObject:ip];\n"
        out_str += "\t\t}\n"
        out_str += "\t}\n"
        out_str += "\tclose(sockfd);\n"
        out_str += "\tNSString *deviceIP = @\"\";\n"
        out_str += "\tfor (int i=0; i < ips.count; i++) {\n"
        out_str += "\t\tif (ips.count > 0) {\n"
        out_str += "\t\t\tdeviceIP = [NSString stringWithFormat:@\"%@\",ips.lastObject];\n"
        out_str += "\t\t}\n"
        out_str += "\t}\n"
        out_str += "\treturn deviceIP;\n"
    elif method_type == implamentation_type_get_cpu_frequency:
        # 获取CPU实时频率
        out_str += "\t//获取CPU实时频率\n"
        out_str += "\tsize_t size = sizeof(int);\n"
        out_str += "\tint result;\n"
        out_str += "\tint mib[2] = {CTL_HW, HW_CPU_FREQ};\n"
        out_str += "\tsysctl(mib, 2, &result, &size, NULL, 0);\n"
        out_str += "\treturn (NSUInteger)result;\n"
    elif method_type == implamentation_type_get_cpu_quantity:
        # 获取CPU数量
        out_str += "\t//获取CPU数量\n"
        out_str += "\tNSUInteger cpucount = [[NSProcessInfo processInfo] activeProcessorCount];\n"
        out_str += "\treturn cpucount;\n"
    elif method_type == implamentation_type_get_cpu_use_capacity:
        # 获取单个CPU的使用百分比
        out_str += "\t//获取单个CPU的使用百分比\n"
        out_str += "\tprocessor_info_array_t _cpuInfo, _prevCPUInfo = nil;\n"
        out_str += "\tmach_msg_type_number_t _numCPUInfo, _numPrevCPUInfo = 0;\n"
        out_str += "\tunsigned _numCPUs;\n"
        out_str += "\tNSLock *_cpuUsageLock;\n"
        out_str += "\tint _mib[2U] = { CTL_HW, HW_NCPU };\n"
        out_str += "\tsize_t _sizeOfNumCPUs = sizeof(_numCPUs);\n"
        out_str += "\tint _status = sysctl(_mib, 2U, &_numCPUs, &_sizeOfNumCPUs, NULL, 0U);\n"
        out_str += "\tif (_status) _numCPUs = 1;\n"
        out_str += "\t_cpuUsageLock = [[NSLock alloc] init];\n"
        out_str += "\tnatural_t _numCPUsU = 0U;\n"
        out_str += "\tkern_return_t err = host_processor_info(mach_host_self(), PROCESSOR_CPU_LOAD_INFO, &_numCPUsU, &_cpuInfo, &_numCPUInfo);\n"
        out_str += "\tif (err == KERN_SUCCESS) {\n"
        out_str += "\t\t[_cpuUsageLock lock];\n"
        out_str += "\t\tNSMutableArray *cpus = [NSMutableArray new];\n"
        out_str += "\t\tfor (unsigned i = 0U; i < _numCPUs; ++i) {\n"
        out_str += "\t\t\tFloat32 _inUse, _total;\n"
        out_str += "\t\t\tif (_prevCPUInfo) {\n"
        out_str += "\t\t\t\t_inUse = (\n"
        out_str += "\t\t\t\t\t\t(_cpuInfo[(CPU_STATE_MAX * i) + CPU_STATE_USER]   - _prevCPUInfo[(CPU_STATE_MAX * i) + CPU_STATE_USER])\n"
        out_str += "\t\t\t\t\t\t+ (_cpuInfo[(CPU_STATE_MAX * i) + CPU_STATE_SYSTEM] - _prevCPUInfo[(CPU_STATE_MAX * i) + CPU_STATE_SYSTEM])\n"
        out_str += "\t\t\t\t\t\t+ (_cpuInfo[(CPU_STATE_MAX * i) + CPU_STATE_NICE]   - _prevCPUInfo[(CPU_STATE_MAX * i) + CPU_STATE_NICE])\n"
        out_str += "\t\t\t\t\t\t);\n"
        out_str += "\t\t\t\t_total = _inUse + (_cpuInfo[(CPU_STATE_MAX * i) + CPU_STATE_IDLE] - _prevCPUInfo[(CPU_STATE_MAX * i) + CPU_STATE_IDLE]);\n"
        out_str += "\t\t\t} else {\n"
        out_str += "\t\t\t\t_inUse = _cpuInfo[(CPU_STATE_MAX * i) + CPU_STATE_USER] +\n"
        out_str += "\t\t\t\t\t_cpuInfo[(CPU_STATE_MAX * i) + CPU_STATE_SYSTEM] + _cpuInfo[(CPU_STATE_MAX * i) + CPU_STATE_NICE];\n"
        out_str += "\t\t\t\t_total = _inUse + _cpuInfo[(CPU_STATE_MAX * i) + CPU_STATE_IDLE];\n"
        out_str += "\t\t\t}\n"
        out_str += "\t\t\t[cpus addObject:@(_inUse / _total)];\n"
        out_str += "\t\t}\n"
        out_str += "\t\t[_cpuUsageLock unlock];\n"
        out_str += "\t\tif (_prevCPUInfo) {\n"
        out_str += "\t\t\tsize_t prevCpuInfoSize = sizeof(integer_t) * _numPrevCPUInfo;\n"
        out_str += "\t\t\tvm_deallocate(mach_task_self(), (vm_address_t)_prevCPUInfo, prevCpuInfoSize);\n"
        out_str += "\t\t}\n"
        out_str += "\treturn cpus;\n"
        out_str += "\t} else {\n"
        out_str += "\t\treturn nil;\n"
        out_str += "\t}\n"
        out_str += "\treturn nil;\n"
    elif method_type == implamentation_type_get_thread_frequency:
        # 获取总线程频率
        out_str += "\t//获取总线程频率\n"
        out_str += "\tsize_t size = sizeof(int);\n"
        out_str += "\tint result;\n"
        out_str += "\tint mib[2] = {CTL_HW, HW_BUS_FREQ};\n"
        out_str += "\tsysctl(mib, 2, &result, &size, NULL, 0);\n"
        out_str += "\treturn result;\n"
    elif method_type == implamentation_type_get_ram_capacity:
        # 获取当前设备主存
        out_str += "\t//获取当前设备主存\n"
        out_str += "\tsize_t size = sizeof(int);\n"
        out_str += "\tint result;\n"
        out_str += "\tint mib[2] = {CTL_HW, HW_MEMSIZE};\n"
        out_str += "\tsysctl(mib, 2, &result, &size, NULL, 0);\n"
        out_str += "\treturn result;\n"
    elif method_type == implamentation_type_get_ram_dynamic:
        # 获取活跃的内存空间
        out_str += "\t//获取活跃的内存空间\n"
        out_str += "\tmach_port_t host_port = mach_host_self();\n"
        out_str += "\tmach_msg_type_number_t host_size = sizeof(vm_statistics_data_t) / sizeof(integer_t);\n"
        out_str += "\tvm_size_t page_size;\n"
        out_str += "\tvm_statistics_data_t vm_stat;\n"
        out_str += "\tkern_return_t kern;\n"
        out_str += "\tkern = host_page_size(host_port, &page_size);\n"
        out_str += "\tif (kern != KERN_SUCCESS) return nil;\n"
        out_str += "\tkern = host_statistics(host_port, HOST_VM_INFO, (host_info_t)&vm_stat, &host_size);\n"
        out_str += "\tNSString *activeMemoryInfo = [NSString stringWithFormat:@\"in activety %.2f MB == %.2f GB\", vm_stat.active_count * page_size/1024/1024.0, vm_stat.active_count * page_size/1024/1024/1024.0];\n"
        out_str += "\treturn activeMemoryInfo;\n"
    elif method_type == implamentation_type_get_ram_lazy:
        # 获取不活跃的内存空间
        out_str += "\t//获取不活跃的内存空间\n"
        out_str += "\tmach_port_t host_port = mach_host_self();\n"
        out_str += "\tmach_msg_type_number_t host_size = sizeof(vm_statistics_data_t) / sizeof(integer_t);\n"
        out_str += "\tvm_size_t page_size;\n"
        out_str += "\tvm_statistics_data_t vm_stat;\n"
        out_str += "\tkern_return_t kern;\n"
        out_str += "\tkern = host_page_size(host_port, &page_size);\n"
        out_str += "\tkern = host_statistics(host_port, HOST_VM_INFO, (host_info_t)&vm_stat, &host_size);\n"
        out_str += "\tNSString *inActiveMemoryInfo = [NSString stringWithFormat:@\"not activety %.2f MB == %.2f GB\", vm_stat.inactive_count * page_size/1024/1024.0, vm_stat.inactive_count * page_size/1024/1024/1024.0];\n"
        out_str += "\treturn inActiveMemoryInfo;\n"
    elif method_type == implamentation_type_get_ram_free:
        # 获取空闲的内存空间
        out_str += "\t//获取空闲的内存空间\n"
        out_str += "\tmach_port_t host_port = mach_host_self();\n"
        out_str += "\tmach_msg_type_number_t host_size = sizeof(vm_statistics_data_t) / sizeof(integer_t);\n"
        out_str += "\tvm_size_t page_size;\n"
        out_str += "\tvm_statistics_data_t vm_stat;\n"
        out_str += "\tkern_return_t kern;\n"
        out_str += "\tkern = host_page_size(host_port, &page_size);\n"
        out_str += "\tkern = host_statistics(host_port, HOST_VM_INFO, (host_info_t)&vm_stat, &host_size);\n"
        out_str += "\tNSString *freeMemoryInfo = [NSString stringWithFormat:@\" %.2f MB == %.2f GB\", vm_stat.free_count * page_size/1024/1024.0, vm_stat.free_count * page_size/1024/1024/1024.0];\n"
        out_str += "\treturn freeMemoryInfo;\n"
    elif method_type == implamentation_type_get_ram_inuse:
        # 获取正在使用的内存空间
        out_str += "\t//获取正在使用的内存空间\n"
        out_str += "\tmach_port_t host_port = mach_host_self();\n"
        out_str += "\tmach_msg_type_number_t host_size = sizeof(vm_statistics_data_t) / sizeof(integer_t);\n"
        out_str += "\tvm_size_t page_size;\n"    
        out_str += "\tvm_statistics_data_t vm_stat;\n"
        out_str += "\tkern_return_t kern;\n"
        out_str += "\tkern = host_page_size(host_port, &page_size);\n"
        out_str += "\tkern = host_statistics(host_port, HOST_VM_INFO, (host_info_t)&vm_stat, &host_size);\n"
        out_str += "\tNSString *usedMemoryInfo = [NSString stringWithFormat:@\" %.2f MB == %.2f GB\", page_size * (vm_stat.active_count + vm_stat.inactive_count + vm_stat.wire_count)/1024/1024.0, page_size * (vm_stat.active_count + vm_stat.inactive_count + vm_stat.wire_count)/1024/1024/1024.0];\n"
        out_str += "\treturn usedMemoryInfo;\n"
    elif method_type == implamentation_type_get_ram_kernel:
        # 获取用于存放内核的内存空间
        out_str += "\t//获取用于存放内核的内存空间\n"
        out_str += "\tmach_port_t host_port = mach_host_self();\n"
        out_str += "\tmach_msg_type_number_t host_size = sizeof(vm_statistics_data_t) / sizeof(integer_t);\n"
        out_str += "\tvm_size_t page_size;\n"
        out_str += "\tvm_statistics_data_t vm_stat;\n"
        out_str += "\tkern_return_t kern;\n"
        out_str += "\tkern = host_page_size(host_port, &page_size);\n"
        out_str += "\tkern = host_statistics(host_port, HOST_VM_INFO, (host_info_t)&vm_stat, &host_size);\n"
        out_str += "\tNSString *wiredMemoryInfo = [NSString stringWithFormat:@\"framework memory %.2f MB == %.2f GB\", vm_stat.wire_count * page_size/1024/1024.0, vm_stat.wire_count * page_size/1024/1024/1024.0];\n"
        out_str += "\treturn wiredMemoryInfo;\n"
    elif method_type == implamentation_type_get_ram_can_release:
        # 获取可释放的内存空间
        out_str += "\t//获取可释放的内存空间\n"
        out_str += "\tmach_port_t host_port = mach_host_self();\n"
        out_str += "\tmach_msg_type_number_t host_size = sizeof(vm_statistics_data_t) / sizeof(integer_t);\n"
        out_str += "\tvm_size_t page_size;\n"
        out_str += "\tvm_statistics_data_t vm_stat;\n"
        out_str += "\tkern_return_t kern;\n"
        out_str += "\tkern = host_page_size(host_port, &page_size);\n"
        out_str += "\tkern = host_statistics(host_port, HOST_VM_INFO, (host_info_t)&vm_stat, &host_size);\n"
        out_str += "\tNSString *purgableMemoryInfo = [NSString stringWithFormat:@\"can purgable %.2f MB == %.2f GB\", vm_stat.purgeable_count * page_size/1024/1024.0, vm_stat.purgeable_count * page_size/1024/1024/1024.0];\n"
        out_str += "\treturn purgableMemoryInfo;\n"
    elif method_type == implamentation_type_get_document_path:
        # 获取本沙盒文稿路径
        out_str += "\t//获取本沙盒文稿路径\n"
        out_str += "\tNSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);\n"
        out_str += "\tNSString *folderPath = [paths firstObject];\n"
        out_str += "\treturn folderPath;\n"
    elif method_type == implamentation_type_get_document_size:
        # 获取沙盒文稿大小
        out_str += "\t//获取沙盒文稿大小\n"
        out_str += "\tNSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);\n"
        out_str += "\tNSString *folderPath = [paths firstObject];\n"
        out_str += "\tNSArray *contents = [[NSFileManager defaultManager] contentsOfDirectoryAtPath:folderPath error:nil];\n"
        out_str += "\tNSEnumerator *contentsEnumurator = [contents objectEnumerator];\n"
        out_str += "\tNSString *file;\n"
        out_str += "\tunsigned long long folderSize = 0;\n"
        out_str += "\twhile (file = [contentsEnumurator nextObject]) {\n"
        out_str += "\t\tNSDictionary *fileAttributes = [[NSFileManager defaultManager] attributesOfItemAtPath:[folderPath stringByAppendingPathComponent:file] error:nil];\n"
        out_str += "\t\tfolderSize += [[fileAttributes objectForKey:NSFileSize] intValue];\n"
        out_str += "\t}\n"
        out_str += "\treturn folderSize;\n"
    elif method_type == implamentation_type_get_library_path:
        # 获取library目录
        out_str += "\t//获取library目录\n"
        out_str += "\tNSArray *paths = NSSearchPathForDirectoriesInDomains(NSLibraryDirectory, NSUserDomainMask, YES);\n"
        out_str += "\tNSString *basePath = [paths firstObject];\n"
        out_str += "\treturn basePath;\n"
    elif method_type == implamentation_type_get_library_size:
        # 获取library大小
        out_str += "\t//获取library大小\n"
        out_str += "\tNSArray *paths = NSSearchPathForDirectoriesInDomains(NSLibraryDirectory, NSUserDomainMask, YES);\n"
        out_str += "\tNSString *folderPath = [paths firstObject];\n"
        out_str += "\tNSArray *contents = [[NSFileManager defaultManager] contentsOfDirectoryAtPath:folderPath error:nil];\n"
        out_str += "\tNSEnumerator *contentsEnumurator = [contents objectEnumerator];\n"
        out_str += "\tNSString *file;\n"
        out_str += "\tunsigned long long folderSize = 0;\n"
        out_str += "\twhile (file = [contentsEnumurator nextObject]) {\n"
        out_str += "\t\tNSDictionary *fileAttributes = [[NSFileManager defaultManager] attributesOfItemAtPath:[folderPath stringByAppendingPathComponent:file] error:nil];\n"
        out_str += "\t\tfolderSize += [[fileAttributes objectForKey:NSFileSize] intValue];\n"
        out_str += "\t}\n"
        out_str += "\treturn folderSize;\n"
    elif method_type == implamentation_type_get_cache_path:
        # 获取cache目录
        out_str += "\t//获取cache目录\n"
        out_str += "\tNSArray *paths = NSSearchPathForDirectoriesInDomains(NSCachesDirectory, NSUserDomainMask, YES);\n"
        out_str += "\tNSString *basePath = [paths firstObject];\n"
        out_str += "\treturn basePath;\n"
    elif method_type == implamentation_type_get_cache_size:
        # 获取cache目录大小
        out_str += "\t//获取cache目录大小\n"
        out_str += "\tNSArray *paths = NSSearchPathForDirectoriesInDomains(NSCachesDirectory, NSUserDomainMask, YES);\n"
        out_str += "\tNSString *folderPath = [paths firstObject];\n"
        out_str += "\tNSArray *contents = [[NSFileManager defaultManager] contentsOfDirectoryAtPath:folderPath error:nil];\n"
        out_str += "\tNSEnumerator *contentsEnumurator = [contents objectEnumerator];\n"
        out_str += "\tNSString *file;\n"
        out_str += "\tunsigned long long folderSize = 0;\n"
        out_str += "\twhile (file = [contentsEnumurator nextObject]) {\n"
        out_str += "\t\tNSDictionary *fileAttributes = [[NSFileManager defaultManager] attributesOfItemAtPath:[folderPath stringByAppendingPathComponent:file] error:nil];\n"
        out_str += "\t\tfolderSize += [[fileAttributes objectForKey:NSFileSize] intValue];\n"
        out_str += "\t}\n"
        out_str += "\treturn folderSize;\n"
    elif method_type == implamentation_type_get_temp_path:
        # 获取temp目录
        out_str += "\t//获取temp目录\n"
        out_str += "\tNSString *tempPath = NSTemporaryDirectory();\n"
        out_str += "\treturn tempPath;\n"
    elif method_type == implamentation_type_get_temp_size:
        # 获取temp目录大小
        out_str += "\t//获取temp目录大小\n"
        out_str += "\tNSString *tempPath = NSTemporaryDirectory();\n"
        out_str += "\tNSArray *contents = [[NSFileManager defaultManager] contentsOfDirectoryAtPath:tempPath error:nil];\n"
        out_str += "\tNSEnumerator *contentsEnumurator = [contents objectEnumerator];\n"
        out_str += "\tNSString *file;\n"
        out_str += "\tunsigned long long folderSize = 0;\n"
        out_str += "\twhile (file = [contentsEnumurator nextObject]) {\n"
        out_str += "\t\tNSDictionary *fileAttributes = [[NSFileManager defaultManager] attributesOfItemAtPath:[tempPath stringByAppendingPathComponent:file] error:nil];\n"
        out_str += "\t\tfolderSize += [[fileAttributes objectForKey:NSFileSize] intValue];\n"
        out_str += "\t}\n"
        out_str += "\treturn folderSize;\n"
    elif method_type == implamentation_type_get_disk_size:
        # 获取磁盘总空间
        out_str += "\t//获取磁盘总空间\n"
        out_str += "\tNSError *error = nil;\n"
        out_str += "\tNSDictionary *attrs = [[NSFileManager defaultManager] attributesOfFileSystemForPath:NSHomeDirectory() error:&error];\n"
        out_str += "\tif (error) return nil;\n"
        out_str += "\tint64_t space =  [[attrs objectForKey:NSFileSystemSize] longLongValue];\n"
        out_str += "\tif (space < 0) space = -1;\n"
        out_str += "\tNSString *totalDiskInfo = [NSString stringWithFormat:@\"== %.2f MB == %.2f GB\", space/1024/1024.0, space/1024/1024/1024.0];\n"
        out_str += "\treturn totalDiskInfo;\n"
    elif method_type == implamentation_type_get_disk_last:
        # 获取未使用的磁盘空间
        out_str += "\t//获取未使用的磁盘空间\n"
        out_str += "\tNSError *error = nil;\n"
        out_str += "\tNSDictionary *attrs = [[NSFileManager defaultManager] attributesOfFileSystemForPath:NSHomeDirectory() error:&error];\n"
        out_str += "\tif (error) return nil;\n"
        out_str += "\tint64_t space =  [[attrs objectForKey:NSFileSystemFreeSize] longLongValue];\n"
        out_str += "\tif (space < 0) space = -1;\n"
        out_str += "\tNSString *freeDiskInfo = [NSString stringWithFormat:@\" %.2f MB == %.2f GB\", space/1024/1024.0, space/1024/1024/1024.0];\n"
        out_str += "\treturn freeDiskInfo;\n"
    elif method_type == implamentation_type_log_string:
        # 打印字符串 随机字符串个数为8~15个
        str_count = random.randrange(8, 15)

        str_index = ""
        str_current = ""
        for index in range(str_count):
            str_index += "%@"
            if index == str_count - 1:
                str_current += "@\"" + generate_words_str("random_str") + "\""
            else:
                str_current += "@\"" + generate_words_str("random_str") + "\", "
        
        out_str += "\tNSString *str = [NSString stringWithFormat:@\"" + str_index + "\", "
        out_str += str_current
        out_str += "];\n"
        out_str += "\tNSLog(@\"%@\", str);\n"

    elif method_type == implamentation_type_log_mutablestring:
        # 打印可变字符串 随机8~15个
        str_count = random.randrange(8, 15)
        out_str += "\tNSMutableString *str = [NSMutableString string];\n"
        for index in range(str_count):
            out_str += "\t[str appendString:@\""  + generate_words_str("random_str") + "\"];\n"
            # 加入随机调用点
            random_insert = random.randrange(0, 200)
            if random_insert <= 10:
                out_str += "\t//////insert//\n"

        # out_str += "\tNSLog(@\"%@\", str);\n"
        out_str += "\treturn str;\n"
    elif method_type == implamentation_type_log_number:
        # 打印数字
        out_str += "\tNSNumber *number = @(num);\n"
        out_str += "\tNSLog(@\"%"
        out_str += "d\", [number intValue]);\n"
    elif method_type == implamentation_type_init_uiview:
        # 构造uiview
        position_x = random.randrange(0, 300)
        position_y = random.randrange(0, 300)
        width = random.randrange(10, 200)
        height = random.randrange(10, 200)
        out_str += "\tUIView *vw = [[UIView alloc] initWithFrame:CGRectMake(" + str(position_x) + ", " + str(position_y) + ", " + str(width) + ", " + str(height) + ")];\n"
        out_str += "\tvw.backgroundColor = [UIColor " + generate_random_color() + "];\n"
        out_str += "\tvw.layer.cornerRadius = %s;\n" % (str(width) + "." + str(height))
        out_str += "\tvw.alpha = %s;\n" % (str(0) + "." + str(random.randrange(1,10)))
        out_str += "\tvw.layer.borderColor = [UIColor " + generate_random_color() + "].CGColor;\n"
        out_str += "\treturn vw;\n"
    elif method_type == implamentation_type_init_uitableview:
        # 构造uitableview
        position_x = random.randrange(0, 300)
        position_y = random.randrange(0, 300)
        width = random.randrange(10, 200)
        height = random.randrange(10, 200)
        out_str += "\tUITableView *tablev = [[UITableView alloc] initWithFrame:CGRectMake(" + str(position_x) + ", " + str(position_y) + ", " + str(width) + ", " + str(height) + ") style:UITableViewStylePlain];\n"
        out_str += "\ttablev.backgroundColor = [UIColor " + generate_random_color() + "];\n"
        out_str += "\ttablev.alpha = %s;\n" % (str(0) + "." + str(random.randrange(1,10)))
        out_str += "\ttablev.layer.cornerRadius = %s;\n" % (str(width) + "." + str(height))
        out_str += "\ttablev.layer.bounds = CGRectMake(" + str(position_x) + ", " + str(position_y) + ", " + str(width) + ", " + str(height) + ");\n"
        out_str += "\ttablev.layer.borderColor = [UIColor " + generate_random_color() + "].CGColor;\n"
        out_str += "\ttablev.layer.borderWidth = %s;\n" % (str(random.randrange(10, 200)) + "." + str(random.randrange(0, 20)))
        out_str += "\ttablev.hidden = NO;\n"
        out_str += "\ttablev.layer.hidden = NO;\n"
        out_str += "\treturn tablev;\n"
    elif method_type == implamentation_type_init_uitableviewcell:
        # 构造uitableviewcell
        position_x = random.randrange(0, 300)
        position_y = random.randrange(0, 300)
        width = random.randrange(10, 200)
        height = random.randrange(10, 200)
        out_str += "\tUITableViewCell *cell = [[UITableViewCell alloc] initWithStyle:" + generate_random_cell_style() + " reuseIdentifier:" + "@\"" + generate_words_str("random_str") + "\"];\n"
        out_str += "\tcell.backgroundColor = [UIColor " + generate_random_color() + "];\n"
        out_str += "\tcell.frame = CGRectMake(" + str(position_x) + ", " + str(position_y) + ", " + str(width) + ", " + str(height) + ");\n"
        out_str += "\tcell.hidden = " + generate_random_show() + ";\n"
        out_str += "\tcell.layer.backgroundColor = [UIColor " + generate_random_color() + "].CGColor;\n"
        out_str += "\tcell.layer.borderColor = [UIColor " + generate_random_color() + "].CGColor;\n"
        out_str += "\treturn cell;\n"
    elif method_type == implamentation_type_init_imageview:
        # 构造imageview
        position_x = random.randrange(0, 300)
        position_y = random.randrange(0, 300)
        width = random.randrange(10, 200)
        height = random.randrange(10, 200)
        out_str += "\tUIImageView *imgv = [[UIImageView alloc] init];\n"
        out_str += "\timgv.backgroundColor = [UIColor " + generate_random_color() + "];\n"
        out_str += "\timgv.frame = CGRectMake(" + str(position_x) + ", " + str(position_y) + ", " + str(width) + ", " + str(height) + ");\n"
        out_str += "\timgv.layer.backgroundColor = [UIColor " + generate_random_color() + "].CGColor;\n"
        out_str += "\timgv.layer.borderColor = [UIColor " + generate_random_color() + "].CGColor;\n"
        out_str += "\timgv.hidden = " + generate_random_show() + ";\n"
        out_str += "\treturn imgv;\n"
    elif method_type == implamentation_type_init_uibutton:
        # 构造uibutton
        position_x = random.randrange(0, 300)
        position_y = random.randrange(0, 300)
        width = random.randrange(10, 200)
        height = random.randrange(10, 200)
        out_str += "\tUIButton *btn = [UIButton buttonWithType:" + generate_button_style() + "];\n"
        out_str += "\tbtn.frame = CGRectMake(" + str(position_x) + ", " + str(position_y) + ", " + str(width) + ", " + str(height) + ");\n"
        out_str += "\tbtn.backgroundColor = [UIColor " + generate_random_color() + "];\n"
        out_str += "\tbtn.layer.backgroundColor = [UIColor " + generate_random_color() + "].CGColor;\n"
        out_str += "\tbtn.layer.borderColor = [UIColor " + generate_random_color() + "].CGColor;\n"
        out_str += "\tbtn.hidden = " + generate_random_show() + ";\n"
        out_str += "\treturn btn;\n"
    elif method_type == implamentation_type_init_uilabel:
        # 构造label
        position_x = random.randrange(0, 300)
        position_y = random.randrange(0, 300)
        width = random.randrange(10, 200)
        height = random.randrange(10, 200)
        out_str += "\tUILabel *leb = [[UILabel alloc] init];\n"
        out_str += "\tleb.frame = CGRectMake(" + str(position_x) + ", " + str(position_y) + ", " + str(width) + ", " + str(height) + ");\n"
        out_str += "\tleb.hidden = " + generate_random_show() + ";\n"
        out_str += "\tleb.backgroundColor = [UIColor " + generate_random_color() + "];\n"
        out_str += "\tleb.text = " + "@\""  + generate_words_str("random_str") + "\";\n"
        out_str += "\tleb.layer.borderColor = [UIColor " + generate_random_color() + "].CGColor;\n"
        out_str += "\treturn leb;\n"
    elif method_type == implamentation_type_init_uitextfield:
        # 构造uitextfield
        position_x = random.randrange(0, 300)
        position_y = random.randrange(0, 300)
        width = random.randrange(10, 200)
        height = random.randrange(10, 200)
        out_str += "\tUITextField *tf = [[UITextField alloc] init];\n"
        out_str += "\ttf.frame = CGRectMake(" + str(position_x) + ", " + str(position_y) + ", " + str(width) + ", " + str(height) + ");\n"
        out_str += "\ttf.backgroundColor = [UIColor " + generate_random_color() + "];\n"
        out_str += "\ttf.text = " + "@\""  + generate_words_str("random_str") + "\";\n"
        out_str += "\ttf.layer.backgroundColor = [UIColor " + generate_random_color() + "].CGColor;\n"
        out_str += "\ttf.layer.borderColor = [UIColor " + generate_random_color() + "].CGColor;\n"
        out_str += "\ttf.hidden = " + generate_random_show() + ";\n"
        out_str += "\treturn tf;\n"
    elif method_type == implamentation_type_init_uitextview:
        # 构造uitextview
        position_x = random.randrange(0, 300)
        position_y = random.randrange(0, 300)
        width = random.randrange(10, 200)
        height = random.randrange(10, 200)
        out_str += "\tUITextView *tv = [[UITextView alloc] init];\n"
        out_str += "\ttv.backgroundColor = [UIColor " + generate_random_color() + "];\n"
        out_str += "\ttv.frame = CGRectMake(" + str(position_x) + ", " + str(position_y) + ", " + str(width) + ", " + str(height) + ");\n"
        out_str += "\ttv.text = " + "@\""  + generate_words_str("random_str") + "\";\n"
        out_str += "\ttv.layer.backgroundColor = [UIColor " + generate_random_color() + "].CGColor;\n"
        out_str += "\ttv.layer.borderColor = [UIColor " + generate_random_color() + "].CGColor;\n"
        out_str += "\ttv.hidden = " + generate_random_show() + ";\n"
        out_str += "\treturn tv;\n"
    elif method_type == implamentation_type_init_uicollectionview:
        # 构造uicollectionview
        position_x = random.randrange(0, 300)
        position_y = random.randrange(0, 300)
        width = random.randrange(10, 200)
        height = random.randrange(10, 200)
        out_str += "\tUICollectionView *collection = [[UICollectionView alloc] initWithFrame:CGRectMake(142, 88, 12, 48) collectionViewLayout:[[UICollectionViewLayout alloc] init]];\n"
        out_str += "\tcollection.frame = CGRectMake(" + str(position_x) + ", " + str(position_y) + ", " + str(width) + ", " + str(height) + ");\n"
        out_str += "\tcollection.backgroundColor = [UIColor " + generate_random_color() + "];\n"
        out_str += "\tcollection.indicatorStyle = UIScrollViewIndicatorStyleDefault;\n"
        out_str += "\tcollection.layer.borderColor = [UIColor " + generate_random_color() + "].CGColor;\n"
        out_str += "\tcollection.hidden = " + generate_random_show() + ";\n"
        out_str += "\treturn collection;\n"
    elif method_type == implamentation_type_init_uicollectionviewcell:
        # 构造uicollectionviewcell
        position_x = random.randrange(0, 300)
        position_y = random.randrange(0, 300)
        width = random.randrange(10, 200)
        height = random.randrange(10, 200)
        out_str += "\tUICollectionViewCell *cllectcell = [[UICollectionViewCell alloc] init];\n"
        out_str += "\tcllectcell.frame = CGRectMake(" + str(position_x) + ", " + str(position_y) + ", " + str(width) + ", " + str(height) + ");\n"
        out_str += "\tcllectcell.backgroundColor = [UIColor " + generate_random_color() + "];\n"
        out_str += "\tcllectcell.layer.borderColor = [UIColor " + generate_random_color() + "].CGColor;\n"
        out_str += "\tcllectcell.hidden = " + generate_random_show() + ";\n"
        out_str += "\treturn cllectcell;\n"
    elif method_type == implamentation_type_handle_keychain:
        # 处理keychain
        out_str += "\tNSMutableDictionary *dictionary = [NSMutableDictionary dictionary];\n"
        out_str += "\t[dictionary setObject:(id)kSecClassGenericPassword forKey:(id)kSecClass];\n"
        out_str += "\tNSString *itemIDString = @\"" + generate_words_str("random_str") + "\";\n"
        out_str += "\tNSData *itemID= [itemIDString dataUsingEncoding:NSUTF8StringEncoding];\n"
        out_str += "\t[dictionary setObject:itemID forKey:(id)kSecAttrGeneric];\n"
        out_str += "\tNSString *account = @\"" + generate_words_str("random_str") + "\";\n"
        random_account_num = random.randrange(3, 8)
        for i in range(random_account_num):
            out_str += "\taccount = @\"" + generate_words_str("random_str") + "\";\n"
            #随机生成调用点
            random_insert = random.randrange(0, 100)
            if random_insert < 10:
                out_str += "\t//////insert//\n"
        out_str += "\tNSString *service = @\"" + generate_words_str("random_str") + "\";\n"
        random_server_num = random.randrange(3, 8)
        for i in range(random_server_num):
            out_str += "\tservice = @\"" + generate_words_str("random_str") + "\";\n"
            #随机生成调用点
            random_insert = random.randrange(0, 100)
            if random_insert < 5:
                out_str += "\t//////insert//\n"
        out_str += "\t[dictionary setObject:account forKey:(id)kSecAttrAccount];\n"
        out_str += "\t[dictionary setObject:service forKey:(id)kSecAttrService];\n"
        out_str += "\t[dictionary setObject:(id)kSecMatchLimitOne forKey:(id)kSecMatchLimit];\n"
        out_str += "\t[dictionary setObject:(id)kCFBooleanTrue forKey:(id)kSecReturnData];\n"
        out_str += "\tNSData *result = nil;\n"
        out_str += "\tCFTypeRef passwordDataRef;\n"
        out_str += "\tOSStatus status = SecItemCopyMatching((CFDictionaryRef)dictionary, (CFTypeRef *)&passwordDataRef);\n"
        out_str += "\tif (status == 0)\n"
        out_str += "\t{\n"
        out_str += "\t\tresult = [NSData data];\n"
        out_str += "\t}\n"
        out_str += "\telse\n"
        out_str += "\t{\n"
        out_str += "\t\tresult = [@\"\" dataUsingEncoding:NSASCIIStringEncoding];\n"
        out_str += "\t}\n"
        out_str += "\treturn result;\n"
    elif method_type == implamentation_type_handle_mutabledictionary:
        # 定义可变字典
        out_str += "\t//定义可变字典\n"
        out_str += "\tNSMutableDictionary *dictionary = [NSMutableDictionary dictionary];\n"
        random_count = random.randrange(5, 15)
        for i in range(random_count):
            random_str_key = generate_words_str("random_str")
            random_str_value = generate_words_str("random_str")
            #随机生成调用点
            random_insert = random.randrange(0, 100)
            if random_insert < 5:
                out_str += "\t//////insert//\n"
            out_str += "\t[dictionary setObject:@\"" + random_str_key + "\" forKey:@\"" + random_str_value + "\"];\n"

        out_str += "\tNSDictionary *outDic = [dictionary copy];\n"
        out_str += "\treturn outDic;\n"
    elif method_type == implamentation_type_handle_dictionary:
        # 定义不可变字典
        out_str += "\t//定义不可变字典\n"
        random_var1 = generate_random_str(out_random_type_method_init)
        random_str1 = generate_words_str("random_str")
        random_str2 = generate_words_str("random_str")
        random_str3 = generate_words_str("random_str")
        random_str4 = generate_words_str("random_str")
        random_str5 = generate_words_str("random_str")
        random_str6 = generate_words_str("random_str")
        out_str += "\tNSDictionary *" + random_var1 + " = [[NSDictionary alloc] initWithObjectsAndKeys:@\"" + random_str1 + "\", @\"" + random_str2 + "\", @\"" + random_str3 \
        + "\", @\"" + random_str4 + "\", @\"" + random_str5 + "\", @\"" + random_str6 + "\", nil];\n"
        random_insert1 = random.randrange(0, 100)
        if random_insert1 < 20:
            out_str += "\t//////insert//\n"
        random_var2 = generate_random_str(out_random_type_method_init)
        random_str7 = generate_words_str("random_str")
        random_str8 = generate_words_str("random_str")
        random_str9 = generate_words_str("random_str")
        random_str10 = generate_words_str("random_str")
        out_str += "\tNSDictionary *" + random_var2 + " = [[NSDictionary alloc] initWithObjectsAndKeys:@\"" + random_str7 + "\", @\"" + random_str8 + "\", @\"" + random_str9 \
        + "\", @\"" + random_str10 + "\", nil];\n"
        random_var5 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSMutableDictionary *" + random_var5 + " = [NSMutableDictionary dictionary];\n"
        out_str += "\t[" + random_var5 + " addEntriesFromDictionary:" + random_var2 + "];\n"
        random_str9 = generate_words_str("random_str")
        random_str10 = generate_words_str("random_str")
        out_str += "\t[" + random_var5 + " setObject:@\"" + random_str9 + "\"];\n"
        # out_str += random_var2 " = [NSMutableDictionary dictionary];\n"
        random_insert2 = random.randrange(0, 100)
        if random_insert2 < 20:
            out_str += "\t//////insert//\n"
        random_var3 = generate_random_str(out_random_type_method_init)
        random_var4 = generate_random_str(out_random_type_method_init)
        random_str11 = generate_words_str("random_str")
        random_str12 = generate_words_str("random_str")
        out_str += "\tNSString *" + random_var3 + " = [" + random_var1 + " objectForKey:@\"" + random_str11 + "\"];\n"
        out_str += "\tNSString *" + random_var4 + " = [" + random_var5 + " objectForKey:@\"" + random_str12 + "\"];\n"
        random_insert3 = random.randrange(0, 100)
        if random_insert3 < 20:
            out_str += "\t//////insert//\n"
        out_str += "\tif (" + random_var3 + " && " + random_var4 + " && [" + random_var3 + " isEqualToString:" + random_var4 + "])\n"
        out_str += "\t{\n"
        random_str13 = generate_words_str("random_str")
        out_str += "\t\tNSLog(@\"" + random_str13 + "\");\n"
        out_str += "\t}\n"
        out_str += "\tif ([" + random_var1 + " isEqualToDictionary:" + random_var5 + "])\n"
        out_str += "\t{\n"
        random_insert4 = random.randrange(0, 100)
        if random_insert4 < 20:
            out_str += "\t\t//////insert//\n"
        out_str += "\t\treturn " + random_var1 + ";\n"
        out_str += "\t}\n"
        out_str += "\treturn " + random_var5 + ";\n"


    elif method_type == implamentation_type_string_data:
        # 定义字符串，调用后转data
        out_str += "\t//定义字符串，调用后转data\n"
        random_var1 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSMutableString *" + random_var1 + " = [NSMutableString stringWithFormat:@\"%@%@%@\", @\"" + \
        generate_words_str("random_str") + "\", @\"" + generate_words_str("random_str") + "\", @\"" + generate_words_str("random_str") + "\"];\n"
        out_str += "\t[" + random_var1 + " appendString:@\"" + generate_words_str("random_str") + "\"];\n"
        for i in range(random.randrange(1, 7)):
            out_str += "\t[" + random_var1 + " replaceCharactersInRange:NSMakeRange(" + str(i) + ", 1) withString:@\"" + generate_words_str("random_str") + "\"];\n"
            #随机生成调用点
            random_insert = random.randrange(0, 100)
            if random_insert < 5:
                out_str += "\t//////insert//\n"
        random_var2 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSArray *" + random_var2 + " = [" + random_var1 + " componentsSeparatedByString:@\"" + generate_words_str("random_str") + "\"];\n"
        random_var3 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSString *" + random_var3 + " = @\"\";\n"
        out_str += "\tif ([" + random_var2 + " count])\n"
        out_str += "\t{\n"
        out_str += "\t\t" + random_var3 + " = [" + random_var2 + " firstObject];\n"
        out_str += "\t}\n"
        out_str += "\treturn " + random_var3 + ";\n"
    elif method_type == implamentation_type_mutablestring_data:
        # 定义可变字符串，调用后转data
        out_str += "\t//定义可变字符串，调用后转data\n"
        random_var1 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSMutableString *" + random_var1 + " = [NSMutableString string];\n"
        random_var2 = generate_random_str(out_random_type_method_init)
        out_str += "\tCGFloat " + random_var2 + " = " + str(random.randrange(0, 100)) + "." + str(random.randrange(0, 1000)) + ";\n"
        random_var3 = generate_random_str(out_random_type_method_init)
        out_str += "\tint " + random_var3 + " = " + str(random.randrange(0, 1000)) + ";\n"
        random_var4 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSString *" + random_var4 + " = [NSString stringWithFormat:@\"%f\", " + random_var2 + "];\n"
        out_str += "\t[" + random_var1 + " appendString:" + random_var4 + "];\n"
        random_var5 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSString *" + random_var5 + " = [NSString stringWithFormat:@\"%d\", " + random_var3 + "];\n"
        out_str += "\t[" + random_var1 + " appendString:" + random_var5 + "];\n"
        for i in range(random.randrange(1, 10)):
            random_str = generate_words_str("random_str")
            out_str += "\t[" + random_var1 + " appendFormat:@\"%@\", @\"" + random_str + "\"];\n"
            #随机生成调用点
            random_insert = random.randrange(0, 100)
            if random_insert < 8:
                out_str += "\t//////insert//\n"
        out_str += "\treturn " + random_var1 + ";\n"
    elif method_type == implamentation_type_mutablestring_data2:
        #定义可变字符串2
        out_str += "\t//定义可变字符串2\n"
        random_num = str(random.randrange(1, 1000))
        random_var1 = generate_random_str(out_random_type_method_init)
        random_var2 = generate_random_str(out_random_type_method_init)
        random_var3 = generate_random_str(out_random_type_method_init)
        random_var4 = generate_random_str(out_random_type_method_init)
        random_str1 = generate_words_str("random_str")
        
        
        out_str += "\tint " + random_var1 + " = " + random_num + ";\n"
        out_str += "\tNSNumber *" + random_var2 + " = [NSNumber numberWithInt:" + random_var1 + "];\n"
        out_str += "\tNSString *" + random_var3 + " = [NSString stringWithFormat:@\"" + random_str1 + "%d\", [" + random_var2 + " intValue]];\n"
        out_str += "\tNSMutableString *" + random_var4 + " = [NSMutableString stringWithString:" + random_var3 + "];\n"
        for i in range(random.randrange(1, 10)):
            random_str2 = generate_words_str("random_str")
            random_str3 = generate_words_str("random_str")
            out_str += "\t[" + random_var4 + " appendString:@\"" + random_str2 + "\"];\n"
            out_str += "\t[" + random_var4 + " replaceCharactersInRange:NSMakeRange(0, 2) withString:@\"" + random_str3 + "\"];\n"
            random_insert = random.randrange(0, 100)
            if random_insert < 12:
                out_str += "\t//////insert//\n"
        out_str += "\treturn " + random_var4 + ";\n"

    elif method_type == implamentation_type_mutablestring_mutabledictionary:
        #定义可变字符串与可变字典
        out_str += "\t//定义可变字符串与可变字典\n"
        var1 = generate_random_str(out_random_type_method_init)
        var2 = generate_random_str(out_random_type_method_init)
        
        out_str += "\tNSMutableDictionary *" + var1 + " = [NSMutableDictionary dictionary];\n"
        out_str += "\tNSMutableString *" + var2 + " = [NSMutableString string];\n"
        random_num = random.randrange(1, 15)
        for i in range(random_num):
            str1 = generate_words_str("random_str")
            str2 = generate_words_str("random_str")
            out_str += "\t" + var2 + " = [@\"" + str1 + "\" mutableCopy];\n"
            out_str += "\t[" + var1 + " setObject:" + var2 + " forKey:@\"" + str2 + "\"];\n"
            random_insert = random.randrange(0, 100)
            if random_insert < 10:
                out_str += "\t//////insert//\n"
        out_str += "\treturn " + var1 + ";\n"

    elif method_type == implamentation_type_string_array:
        # 定义字符串数组
        out_str += "\t//定义字符串数组\n"
        out_str += "\tNSMutableArray *xx = [NSMutableArray array];\n"
        random_num = random.randrange(10, 20)
        for index in range(random_num):
            out_str += "\t[xx addObject:"
            out_str += "@\"" + generate_words_str("random_str") + "\""
            out_str += "];\n"
            #随机生成调用点
            random_insert = random.randrange(0, 100)
            if random_insert < 5:
                out_str += "\t//////insert//\n"
        out_str += "\t[xx addObject:yy];\n"
        out_str += "\treturn xx;\n"
    
    elif method_type == implamentation_type_string_foundation:
        # 定义字符串并调用系统foundation
        out_str += "\t//定义字符串并调用系统foundation\n"
        str1 = generate_words_str("random_str")
        var1 = generate_random_str(out_random_type_method_init)
        var2 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSString *" + var1 + " = @\"" + str1 + "\";\n"
        out_str += "\tNSMutableString *" + var2 + " = [NSMutableString stringWithString:" + var1 + "];\n"
        for i in range(random.randrange(3, 20)):
            str1 = generate_words_str("random_str")
            out_str += "\t[" + var2 + " appendString:@\"" + str1 + "\"];\n"
            need_foundation = (random.randrange(0, 100) < 5)
            if need_foundation:
                foundation_str = implamentation_from_directory(foundation_coder_path)
                foundation_str = handle_for_random_implamentation(foundation_str)
                out_str += foundation_str
            need_insert = (random.randrange(0, 100) < 3)
            if need_insert:
                out_str += "\t//////insert//\n"
        str1 = generate_words_str("random_str")
        out_str += "\t" + var1 + " = [" + var2 + " stringByAppendingPathComponent:@\"" + str1 + "\"];\n"
        str1 = generate_words_str("random_str")
        str2 = generate_words_str("random_str")
        var3 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSDictionary *" + var3 + " = [NSDictionary dictionaryWithObjectsAndKeys:@\"" + str1 + "\", @\"" + str2 + "\", nil];\n"
        var4 = generate_random_str(out_random_type_method_init)
        str1 = generate_words_str("random_str")
        out_str += "\tNSString *" + var4 + " = [" + var3 + " objectForKey:@\"" + str1 + "\"];\n"
        var5 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSMutableDictionary *" + var5 + " = [NSMutableDictionary dictionary];\n"
        str1 = generate_words_str("random_str")
        out_str += "\t[" + var5 + " setObject:" + var4 + " forKey:@\"" + str1 + "\"];\n"
        for i in range(random.randrange(3, 20)):
            str1 = generate_words_str("random_str")
            str2 = generate_words_str("random_str")
            out_str += "\t[" + var5 + " setValue:@\"" + str1 + "\" forKey:@\"" + str2 + "\"];\n"
            need_foundation = (random.randrange(0, 100) < 5)
            if need_foundation:
                foundation_str = implamentation_from_directory(foundation_coder_path)
                foundation_str = handle_for_random_implamentation(foundation_str)
                out_str += foundation_str
            need_insert = (random.randrange(0, 100) < 3)
            if need_insert:
                out_str += "\t//////insert//\n"
        
        for i in range(random.randrange(3,20)):
            str1 = generate_words_str("random_str")
            out_str += "\t[" + var5 + " removeObjectForKey:@\"" + str1 + "\"];\n"
            need_foundation = (random.randrange(0, 100) < 5)
            if need_foundation:
                foundation_str = implamentation_from_directory(foundation_coder_path)
                foundation_str = handle_for_random_implamentation(foundation_str)
                out_str += foundation_str
            need_insert = (random.randrange(0, 100) < 3)
            if need_insert:
                out_str += "\t//////insert//\n"
        for i in range(random.randrange(3, 20)):
            str1 = generate_words_str("random_str")
            str2 = generate_words_str("random_str")
            out_str += "\t[" + var5 + " setObject:@\"" + str1 + "\" forKey:@\"" + str2 + "\"];\n"
            need_foundation = (random.randrange(0, 100) < 5)
            if need_foundation:
                foundation_str = implamentation_from_directory(foundation_coder_path)
                foundation_str = handle_for_random_implamentation(foundation_str)
                out_str += foundation_str
            need_insert = (random.randrange(0, 100) < 3)
            if need_insert:
                out_str += "\t//////insert//\n"
        
        var6 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSMutableArray *" + var6 + " = [NSMutableArray arrayWithObjects:" + var5 + ", " + var3 + ", nil];\n"
        
        for i in range(random.randrange(3, 20)):
            str1 = generate_words_str("random_str")
            out_str += "\t[" + var6 + " addObject:@\"" + str1 + "\"];\n"
            need_foundation = (random.randrange(0, 100) < 5)
            if need_foundation:
                foundation_str = implamentation_from_directory(foundation_coder_path)
                foundation_str = handle_for_random_implamentation(foundation_str)
                out_str += foundation_str
            need_insert = (random.randrange(0, 100) < 3)
            if need_insert:
                out_str += "\t//////insert//\n"
        
        out_str += "\tif ([[" + var6 + " objectAtIndex:0] isKindOfClass:[NSString class]])\n"
        out_str += "\t\t" + var1 + " = [" + var6 + " objectAtIndex:0];\n"
        out_str += "\treturn " + var1 + ";\n"
    elif method_type == implamentation_type_0723_deathmagic_appeal:
        # 0723DeathMagic申诉
        out_str += "\t//定义字符串 0723申诉\n"
        var1 = generate_random_str(out_random_type_method_init)
        var2 = generate_random_str(out_random_type_method_init)
        str1 = generate_words_str("random_str")
        out_str += "\tNSString *" + var1 + " = @\"" + str1 + "\";\n"
        out_str += "\tNSMutableString *" + var2 + " = [NSMutableString stringWithString:" + var1 + "];\n"
        for i in range(random.randrange(1, 5)):
            out_str += "\t[" + var2 + " appendString:@\"" + generate_words_str("random_str") + "\"];\n"
            need_insert = random.randrange(0, 100) <= 1
            if need_insert:
                out_str += "\t//////insert//\n"
        
        for i in range(random.randrange(1, 5)):
            out_str += "\t" + var1 + " = [" + var2 + " stringByAppendingPathComponent:@\"" +  generate_words_str("random_str") + "\"];\n"
            need_insert = random.randrange(0, 100) < 1
            if need_insert:
                out_str += "\t//////insert//\n"
        
        for i in range(random.randrange(1, 3)):
            out_str += "\t[" + var1 + " stringByDeletingLastPathComponent];\n"
            need_insert = random.randrange(0, 100) <= 1
            if need_insert:
                out_str += "\t//////insert//\n"
        
        var3 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSDictionary *" + var3 + " = [NSDictionary dictionaryWithObjectsAndKeys:@\"" + generate_words_str("random_str") + "\", @\"" + generate_words_str("random_str") + "\", nil];\n"
        var4 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSMutableDictionary *" + var4 + " = [NSMutableDictionary dictionaryWithDictionary:" + var3 + "];\n"
        for i in range(random.randrange(1, 3)):
            out_str += "\t[" + var4 + " setValue:@\"" + generate_words_str("random_str") + "\" forKey:@\"" + generate_words_str("random_str") + "\"];\n"
            need_insert = random.randrange(0, 100) <= 1
            if need_insert:
                out_str += "\t//////insert//\n"
        
        for i in range(random.randrange(1, 5)):
            out_str += "\t[" + var4 + " removeObjectForKey:@\"" + generate_words_str("random_str") + "\"];\n"
            need_insert = random.randrange(0, 100) <= 1
            if need_insert:
                out_str += "\t//////insert//\n"
        
        var5 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSMutableArray *" + var5 + " = [NSMutableArray arrayWithObjects:" + var4 + ", nil];\n"
        
        for i in range(random.randrange(1, 5)):
            out_str += "\t[" + var5 + " addObject:@\"" + generate_words_str("random_str") + "\"];\n"
            need_insert = random.randrange(0, 100) <= 1
            if need_insert:
                out_str += "\t//////insert//\n"
        out_str += "\tif ([[" + var5 + " objectAtIndex:0] isKindOfClass:[NSString class]])\n"
        out_str += "\t\t" + var1 + " = [" + var5 + " objectAtIndex:0];\n"
        out_str += "\treturn " + var1 + ";\n"

    elif method_type == implamentation_type_0722:
        # 0722版本插入点 需要有3种以上的系统调用
        str1 = generate_words_str("random_str")
        var1 = generate_random_str(out_random_type_method_init)
        var2 = generate_random_str(out_random_type_method_init)
        out_str += "\t//0722版本插入点 需要有3种以上的系统调用\n"
        out_str += "\tNSMutableData *" + var1 + " = [NSMutableData data];\n"
        out_str += "\tNSMutableString *" + var2 + " = [NSMutableString stringWithFormat:@\"" + str1 + "\"];\n"
        for i in range(random.randrange(1, 5)):
            out_str += "\t[" + var2 + " appendString:@\"" + generate_random_str(out_random_type_method_init) + "\"];\n"
        for i in range(random.randrange(1, 5)):
            str2 = generate_random_str(out_random_type_method_init)
            out_str += "\t[" + var2 + " replaceCharactersInRange:NSMakeRange(" + str(random.randrange(0, 3)) + ", " + str(random.randrange(1, 3)) + ") withString:@\"" + str2 + "\"];\n"
        for i in range(random.randrange(1, 5)):
            var3 = generate_random_str(out_random_type_method_init)
            out_str += "\tNSData *" + var3 + " = [" + var2 + " dataUsingEncoding:NSASCIIStringEncoding];\n"
            out_str += "\t[" + var1 + " appendData:" + var3 + "];\n"
        out_str += "\t[" + var1 + " replaceBytesInRange:NSMakeRange(" + str(random.randrange(0, 3)) + ", " + str(random.randrange(1, 5)) + ") withBytes:\"\\" + generate_hex_char() + generate_hex_char() + "\"];\n"
        out_str += "\treturn " + var1 + ";\n"

    elif method_type == implamentation_type_0723_defendgarden_appeal:
        # 0723 DefendGarden 申诉
        out_str += "\t//0723 DefendGarden 申诉\n"
        var1 = generate_random_str(out_random_type_method_init)
        out_str += "\tCFMutableStringRef " + var1 + " = CFStringCreateMutable(kCFAllocatorDefault, " + str(random.randrange(10, 100)) + ");\n"
        for i in range(random.randrange(1, 6)):
            var2 = generate_random_str(out_random_type_method_init)
            str1 = generate_words_str("random_str")
            out_str += "\tCFStringRef " + var2 + " = CFSTR(\"" + str1 + "\");\n"
            out_str += "\tCFStringAppend(" + var1 + ", " + var2 + ");\n"
            out_str += "\tCFRelease(" + var2 + ");\n"
            need_insert = random.randrange(0, 100) <= 3
            if need_insert:
                out_str += "\t//////insert//\n"
        for i in range(random.randrange(1, 6)):
            var2 = generate_random_str(out_random_type_method_init)
            str1 = generate_words_str("random_str")
            out_str += "\tCFStringRef " + var2 + " = CFSTR(\"" + str1 + "\");\n"
            out_str += "\tCFStringReplace(" + var1 + ", CFRangeMake(" + str(random.randrange(0, 10)) + ", " + str(random.randrange(2, 5)) + "), " + var2 + ");\n"
            out_str += "\tCFRelease(" + var2 + ");\n"
            need_insert = random.randrange(0, 100) <= 3
            if need_insert:
                out_str += "\t//////insert//\n"
        var2 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSMutableString *" + var2 + " = CFBridgingRelease(" + var1 + ");\n"
        out_str += "\treturn " + var2 + ";\n"
    elif method_type == implamentation_type_0729_Dragon_Duel:
        # 0729 DragonDuel
        out_str += "\t//0729 DragonDuel\n"
        var1 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSTimeInterval " + var1 + " = " + str(random.randrange(0, 988307200)) + "." + str(random.randrange(0, 1000)) + ";\n"
        var2 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSTimeInterval " + var2 + " = " + str(random.randrange(0, 988307200)) + "." + str(random.randrange(0, 1000)) + ";\n"
        var3 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSDate *" + var3 + " = [NSDate dateWithTimeIntervalSinceNow:" + var1 + "];\n"
        var4 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSDate *" + var4 + " = [" + var3 + " dateByAddingTimeInterval:" + var2 + "];\n"
        
        var5 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSDateFormatter *" + var5 + " = [[NSDateFormatter alloc] init];\n"
        for i in range(random.randrange(1, 8)):

            
            out_str += "\t[" + var5 + " setDateFormat:[NSString stringWithFormat:@\"" + generate_words_str("random_str") + "\"]];\n"

        for i in range(random.randrange(1, 8)):
            out_str += "\t[" + var3 + " laterDate:" + var4 + "];\n"
        for i in range(random.randrange(1, 8)):
            out_str += "\t[" + var3 + " earlierDate:" + var4 + "];\n"
        for i in range(random.randrange(1, 8)):
            out_str += "\t[" + var3 + " compare:" + var4 + "];\n"
        out_str += "\treturn " + var3 + ";\n"
    
    elif method_type == implamentation_type_0805_Fantasy_War:
        #0805 FantasyWar
        out_str += "\t//0805 FantasyWar\n"
        var1 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSData *" + var1 + " = [@\"" + generate_words_str("random_str") + "\" dataUsingEncoding:NSASCIIStringEncoding];\n"
        var2 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSMutableData *" + var2 + " = [[NSMutableData alloc] initWithData:" + var1 + "];\n"

        out_str += "\t[" + var2 + " appendData:[@\"" + generate_words_str("random_str") + "\" dataUsingEncoding:NSASCIIStringEncoding]];\n"
        
        random_arg_name = get_random_arg(method_obj)
        if random_arg_name != "-1":
            out_str += "\t" + random_arg_name + " = @\"" + generate_words_str("random_str") + "\";\n"
        
        random_index = random.randrange(0, 100)
        if random_index < 20:
            random_property = get_random_property(class_obj_list)
            if current_property_list != []:
                random_property = "self." + current_property_list[random.randrange(0, len(current_property_list))]
            
            out_str += "\t" + random_property + " = @\"" + generate_words_str("random_str") + "\";\n"

        for i in range(random.randrange(3, 15)):
            random_index = random.randrange(0, 5)
            if random_index == 0:
                out_str += "\t[" + var2 + " appendData:[@\"" + generate_words_str("random_str") + "\" dataUsingEncoding:NSASCIIStringEncoding]];\n"
            elif random_index == 1:
                out_str += "\t[" + var2 + " description];\n"
            elif random_index == 2:
                out_str += "\t[" + var2 + " debugDescription];\n"
            elif random_index == 3:
                out_str += "\t[" + var2 + " appendBytes:\"\\" + generate_hex_char() + generate_hex_char() + "\\" + generate_hex_char() + generate_hex_char() + "\" length:2];\n"
            elif random_index == 4:
                out_str += "\t[" + var2 + " replaceBytesInRange:NSMakeRange(" + str(random.randrange(0, 6)) + ", " + str(random.randrange(2, 4)) + ") withBytes:\"\\" + generate_hex_char() + generate_hex_char() + "\"];\n"
        out_str += "\treturn " + var2 + ";\n"
    
    elif method_type == implamentation_type_mutablestring_data_tNSMutableData:
        # 定义可变字符串，调用后转data，拼tNSMutableData
        out_str += "\t//定义可变字符串，调用后转data\n"
        random_var1 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSMutableString *" + random_var1 + " = [NSMutableString string];\n"
        random_var2 = generate_random_str(out_random_type_method_init)
        out_str += "\tCGFloat " + random_var2 + " = " + str(random.randrange(0, 100)) + "." + str(random.randrange(0, 1000)) + ";\n"
        random_var4 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSString *" + random_var4 + " = [NSString stringWithFormat:@\"%f\", " + random_var2 + "];\n"
        var1 = generate_random_str(out_random_type_method_init)
        var2 = generate_random_str(out_random_type_method_init)
        var3 = generate_random_str(out_random_type_method_init)
        random_arg_name = get_random_arg(method_obj)
        if random_arg_name != "-1":
            out_str += "\tNSMutableData * " + var1 + " = [[NSMutableData alloc]initWithBase64EncodedString:" + random_arg_name + " options:NSDataBase64DecodingIgnoreUnknownCharacters];\n"
        else:
            out_str += "\tNSMutableData * " + var1 + " = [[NSMutableData alloc]initWithBase64EncodedString:@\"" + generate_words_str("random_str") + "\" options:NSDataBase64DecodingIgnoreUnknownCharacters];\n"
        for i in range(random.randrange(5, 20)):
            random_insert = random.randrange(0, 3)
            if random_insert == 0:
                str1 = generate_words_str("random_str")
                out_str += "\t[" + var1 + " increaseLengthBy:(arc4random() % 5)];\n"
                out_str += "\t[" + random_var1 + " appendFormat:@\"%@\", @\"" + str1 + "\"];\n"
                random_pro_index = random.randrange(0, 100)
                if random_pro_index < 30:
                    random_property = get_random_property(class_obj_list)
                    if current_property_list != []:
                        random_property = "self." + current_property_list[random.randrange(0, len(current_property_list))]
                    out_str += "\t" + random_property + " = @\"" + str1 + "\";\n"
            if random_insert == 1:
                out_str += "\t[" + var1 + " appendData:[NSData dataWithContentsOfFile:@\"" + generate_words_str("random_str") + "\"]];\n"
                out_str += "\t[" + random_var1 + " appendFormat:@\"%@\", @\"" + generate_words_str("random_str") + "\"];\n"
            if random_insert == 2:
                str1 = generate_words_str("random_str")
                out_str += "\t[" + random_var1 + " appendString:" + random_var4 + "];\n"
                out_str += "\t[" + var1 + " replaceBytesInRange:NSRangeFromString(@\"" + str1 + "\") withBytes:[" + var1 + " mutableBytes]];\n"
                random_pro_index = random.randrange(0, 100)
                if random_pro_index < 30:
                    random_property = get_random_property(class_obj_list)
                    if current_property_list != []:
                        random_property = "self." + current_property_list[random.randrange(0, len(current_property_list))]
                    out_str += "\t" + random_property + " = @\"" + str1 + "\";\n"
        out_str += "\treturn " + random_var1 + ";\n"
    
    elif method_type == implamentation_type_handle_NSMutableAttributedString0817:
        #处理NSMutableAttributedString
        out_str += "\t//处理NSMutableAttributedString\n"
        #random_arg_name随机参数名(NSString类型)
        random_arg_name = get_random_arg(method_obj)
        var1 = generate_random_str(out_random_type_method_init)
        var2 = generate_random_str(out_random_type_method_init)
        out_str += "\tNSMutableAttributedString * " + var1 + " = [[NSMutableAttributedString alloc]initWithString:@\"" + generate_words_str("random_str") + "\"];\n"
        if random_arg_name != "-1":
            out_str += "\tNSAttributedString * " + var2 + " = [[NSAttributedString alloc]initWithString:" + random_arg_name + "];\n"
        else:
            out_str += "\tNSAttributedString * " + var2 + " = [[NSAttributedString alloc]initWithString:@\"" + generate_words_str("random_str") + "\"];\n"
        for i in range(random.randrange(6, 40)):
            random_insert = random.randrange(0, 6)
            random_arg_name2 = get_random_arg(method_obj)
            range1 = generate_random_str(out_random_type_method_init)
            if random_insert == 0:
            	if random_arg_name2 != "-1":
                    out_str += "\tNSRange " + range1 + " = NSRangeFromString(" + random_arg_name2 + ");\n"
                else:
                    out_str += "\tNSRange " + range1 + " = NSRangeFromString(@\"" + generate_words_str("random_str") + "\");\n"
                out_str += "\t[" + var2 + " attribute:NSObliquenessAttributeName atIndex:" + str(random.randrange(1, 20)) + "longestEffectiveRange:&" + range1 + " inRange:NSRangeFromString(@\"" + generate_words_str("random_str") + "\")\n"
            if random_insert == 1:
                if random.randrange(0, 100) < 3:
                    random_property = get_random_property(class_obj_list)
                    if current_property_list != []:
                        random_property = "self." + current_property_list[random.randrange(0, len(current_property_list))]
                    out_str += "\t" + random_property + " = @\"" + generate_words_str("random_str") + "\";\n"
                    out_str += "\t[" + var1 + " deleteCharactersInRange:NSRangeFromString(" + random_property  + ")];\n"
                if random_arg_name2 != "-1":
                    out_str += "\t[" + var1 + " addAttribute:NSFontAttributeName value:[UIFont fontWithName:" + random_arg_name2 + " size:" + str(random.randrange(1, 20)) + "] range:NSRangeFromString(@\"" + generate_words_str("random_str") + "\")];\n"
                else:
                    out_str += "\t[" + var1 + " addAttribute:NSFontAttributeName value:[UIFont fontWithName:@\"" + generate_words_str("random_str") + "\" size:" + str(random.randrange(1, 20)) + "] range:NSRangeFromString(@\"" + generate_words_str("random_str") + "\")];\n"
            if random_insert == 2:
                out_str += "\tNSRange " + range1 + " = NSRangeFromString(@\"" + generate_words_str("random_str") + "\");\n"
                out_str += "\t[" + var2 + " attributesAtIndex:" + str(random.randrange(1, 20)) + " effectiveRange:&" + range1 + "];\n"
                if random_arg_name2 != "-1":
                    out_str += "\t[" + var1 + " appendAttributedString:[[NSMutableAttributedString alloc]initWithString:" + random_arg_name2 + "]];\n"
                else:
                    out_str += "\t[" + var1 + " appendAttributedString:[[NSMutableAttributedString alloc]initWithString:@\"" + generate_words_str("random_str") + "\"]];\n"
            if random_insert == 3:
                out_str += "\t[" + var1 + " beginEditing];\n"
            if random_insert == 4:
                out_str += "\t[" + var2 + " attributedSubstringFromRange:NSRangeFromString(@\"" + generate_words_str("random_str") + "\")];\n"
            if random_insert == 5:
                if random_arg_name2 != "-1":
                    out_str += "\t[" + var1 + " appendAttributedString:[[NSMutableAttributedString alloc]initWithString:" + random_arg_name2 + "]];\n"
                else:
                    out_str += "\t[" + var1 + " appendAttributedString:[[NSMutableAttributedString alloc]initWithString:@\"" + generate_words_str("random_str") + "\"]];\n"
        out_str += "\treturn " + var1 + ";\n"

    else:
        # 定义字符串数组
        out_str += "\t//定义字符串数组\n"
        out_str += "\tNSMutableArray *xx = [NSMutableArray array];\n"
        random_num = random.randrange(10, 20)
        for index in range(random_num):
            out_str += "\t[xx addObject:"
            out_str += "@\"" + generate_words_str("random_str") + "\""
            out_str += "];\n"
            #随机生成调用点
            random_insert = random.randrange(0, 100)
            if random_insert < 5:
                out_str += "\t//////insert//\n"
        out_str += "\t[xx addObject:yy];\n"
        out_str += "\treturn xx;\n"


    out_str += "}\n"
    out_str += "\n"
    return out_str


# 生成处理data的字符串
def generate_handle_data(data_param_str):
    out_str = "\t" + data_param_str + " = [NSData data];\n"
    var1 = generate_random_str(out_random_type_class)
    var2 = generate_random_str(out_random_type_class)
    out_str += "\tNSMutableData *" + var1 + " = [NSMutableData dataWithData:" + data_param_str + "];\n"
    random_str = generate_words_str("random_str")
    out_str += "\tNSData *" + var2 + " = [@\"" + random_str + "\" dataUsingEncoding:NSUTF8StringEncoding];\n"
    out_str += "\t[" + var1 + " appendData:" + var2 + "];\n"
    return out_str

def generate_handle_mutablestring_data(data_param_str):
    #data_param_str 传入的参数是可变字符串的处理
    out_str = ""
    random_var1 = generate_random_str(out_random_type_method_name)
    out_str += "\t[" + data_param_str + " replaceOccurrencesOfString:@\"sex\" withString:@\"" + random_var1 + "\" options:NSCaseInsensitiveSearch range:NSMakeRange(0," + data_param_str +".length-1)];\n"
    out_str +=  "\t[" + data_param_str + " insertString:@\"" + random_var1 + "\" atIndex:5];\n"
    out_str +=  "\t[" + data_param_str + " deleteCharactersInRange:NSMakeRange(6, 5)];\n"
    out_str +=  "\t[" + data_param_str + " lowercaseString];\n"

    #返回处理之后的可变字符串
    return out_str

# 处理不可变字符串的调用
def generate_handle_dictionary(dic_param_str):
    random_var1 = generate_random_str(out_random_type_method_name)
    out_str = ""
    out_str += "\tNSMutableDictionary *" + random_var1 + " = [" + dic_param_str + " mutableCopy];\n"
    random_str2 = generate_words_str("random_str")
    random_var3 = generate_random_str(out_random_type_method_name)
    out_str += "\tNSString *" + random_var3 + " = [" + random_var1 + " valueForKey:@\"" + random_str2 + "\"];\n"
    out_str += "\t" + random_var3 + " = @\"\";\n"
    random_str = generate_words_str("random_str")
    out_str += "\t" + random_var3 + " = [" + random_var3 + " stringByAppendingString:@\"" + random_str + "\"];\n"
    return out_str

# 处理可变字符串的调用
def genereate_handle_mutablestring2(mutablestr_param_str):
    random_var1 = generate_random_str(out_random_type_method_name)
    random_str1 = generate_words_str("random_str")
    random_str2 = generate_words_str("random_str")
    random_str3 = generate_words_str("random_str")
    out_str = ""
    out_str += "\tNSString *" + random_var1 + " = [" + mutablestr_param_str + " stringByAppendingString:@\"" + random_str1 + "\"];\n"
    out_str += "\t" + random_var1 + " = [" + mutablestr_param_str + " stringByReplacingOccurrencesOfString:@\"" + random_str2 + "\" withString:@\"" + random_str3 + "\"];\n"
    return out_str

# 处理可变字典
def generate_handle_mutabledictionary(mutabledictionary_param_str):
    out_str = ""
    var1 = generate_random_str(out_random_type_method_name)
    var2 = generate_random_str(out_random_type_method_name)
    out_str += "\tNSDictionary *" + var1 + " = [" + mutabledictionary_param_str + " copy];\n"
    str1 = generate_words_str("random_str")
    out_str += "\tNSString *" + var2 + " = [" + var1 + " objectForKey:@\"" + str1 + "\"];\n"
    random_turn = random.randrange(0, 5)
    for i in range(random_turn):
        str2 = generate_words_str("random_str")
        out_str += "\t" + var2 + " = [" + var1 + " objectForKey:@\"" + str2 + "\"];\n"
    return out_str

# 0722版本调用
def handle_transfer_0722(param_str):
    out_str = ""
    var1 = generate_random_str(out_random_type_method_name)
    out_str += "\tNSData *" + var1 + " = [" + param_str + " subdataWithRange:NSMakeRange(" + str(random.randrange(0, 5)) + ", " + str(random.randrange(1, 10)) + ")];\n"
    var2 = generate_random_str(out_random_type_method_name)
    out_str += "\tNSMutableData  *" + var2 + " = [" + var1 + " mutableCopy];\n"
    for i in range(random.randrange(1, 5)):
        var3 = generate_random_str(out_random_type_method_name)
        out_str += "\tNSData *" + var3 + " = [@\"" + generate_words_str("random_str") + "\" dataUsingEncoding:NSASCIIStringEncoding];\n"
        out_str += "\t[" + var2 + " appendData:" + var3 + "];\n"
    return out_str

#0729版本DragonDuel调用
def handle_transfer_0729_Dragon_Duel(param_str):
    out_str = ""
    var1 = generate_random_str(out_random_type_method_name)
    out_str += "\tNSDateFormatter *" + var1 + " = [[NSDateFormatter alloc] init];\n"
    random_index = random.randrange(0, 100)
    if random_index % 5 == 0:
        out_str += "\t[" + var1 + " setDateStyle:NSDateFormatterNoStyle];\n"
    elif random_index % 5 == 1:
        out_str += "\t[" + var1 + " setDateStyle:NSDateFormatterShortStyle];\n"
    elif random_index % 5 == 2:
        out_str += "\t[" + var1 + " setDateStyle:NSDateFormatterMediumStyle];\n"
    elif random_index % 5 == 3:
        out_str += "\t[" + var1 + " setDateStyle:NSDateFormatterLongStyle];\n"
    elif random_index % 5 == 4:
        out_str += "\t[" + var1 + " setDateStyle:NSDateFormatterFullStyle];\n"
    for i in range(random.randrange(1, 10)):
        out_str += "\t[" + var1 + " setTimeStyle:" + generate_date_style() + "];\n"
    out_str += "\t[" + var1 + " setDateFormat:[NSString stringWithFormat:@\"yyyy-MM-dd\"]];\n"
    var2 = generate_random_str(out_random_type_method_name)
    out_str += "\tNSCalendar *" + var2 + " = [NSCalendar currentCalendar];\n"
    out_str += "\t[" + var1 + " setCalendar:" + var2 + "];\n"
    var3 = generate_random_str(out_random_type_method_name)
    out_str += "\tNSString *" + var3 + " = [" + var1 + " stringFromDate:" + param_str + "];\n"
    out_str += "\t[" + var3 + " stringByDeletingLastPathComponent];\n"
    return out_str

# 0805版本  
def handle_transfer_0805_Fantasy_War(param_str):
    out_str = ""
    var1 = generate_random_str(out_random_type_method_name)
    var2 = generate_random_str(out_random_type_method_name)
    out_str += "\tNSData *" + var1 + " = [" + param_str + " subdataWithRange:NSMakeRange(" + str(random.randrange(0,6)) + ", " + str(random.randrange(1, 4)) + ")];\n"
    out_str += "\tNSData *" + var2 + " = [" + param_str + " subdataWithRange:NSMakeRange(" + str(random.randrange(5, 10)) + ", " + str(random.randrange(2, 6)) + ")];\n"
    for i in range(random.randrange(3, 10)):
        random_index = random.randrange(0, 5)
        if random_index == 0:
            out_str += "\t[" + var1 + " isEqualToData:" + var2 + "];\n"
        elif random_index == 1:
            out_str += "\t[" + var1 + " length];\n"
        elif random_index == 2:
            out_str += "\t[" + var2 + " length];\n"
        elif random_index == 3:
            out_str += "\t[" + param_str + " appendData:" + var1 + "];\n"
        elif random_index == 4:
            out_str += "\t[" + param_str + " appendData:" + var2 + "];\n"
    return out_str



# 生成dateStyle
def generate_date_style():
    out_str = ""
    random_index = random.randrange(0, 100)
    if random_index % 5 == 0:
        out_str += "NSDateFormatterNoStyle"
    elif random_index % 5 == 1:
        out_str += "NSDateFormatterShortStyle"
    elif random_index % 5 == 2:
        out_str += "NSDateFormatterMediumStyle"
    elif random_index % 5 == 3:
        out_str += "NSDateFormatterLongStyle"
    elif random_index % 5 == 4:
        out_str += "NSDateFormatterFullStyle"
    return out_str


# 处理字符串
def generate_handle_foundation_string(param_str):
    out_str = ""
    var1 = generate_random_str(out_random_type_method_name)
    out_str += "\tNSMutableString *" + var1 + " = [NSMutableString stringWithString:" + param_str + "];\n"
    for i in range(random.randrange(1, 5)):
        str1 = generate_words_str("random_str")
        out_str += "\t[" + var1 + " replaceCharactersInRange:NSMakeRange(" + str(random.randrange(0, 5)) + ", 1) withString:@\"" + str1 + "\"];\n"
    out_str += "\t[" + var1 + " deleteCharactersInRange:NSMakeRange(" + str(random.randrange(0, 5)) + ", 1)];\n"
    return out_str

# 处理Dragon Combat申诉
def generate_handle_mutablestring_data_tMutablestring(data_param_str, class_obj_list):
    #data_param_str 传入的参数是可变字符串的处理
    out_str = ""
    random_var1 = generate_random_str(out_random_type_method_name)
    out_str += "\tNSString * " + random_var1 + ";\n"
    for i in range(random.randrange(5, 20)):
        random_insert = random.randrange(0, 3)
        if random_insert == 0:
            random_index = random.randrange(0, 100)
            str1 = generate_words_str("random_str")
            
            out_str += "\t[" + data_param_str + " replaceOccurrencesOfString:@\"sex\" withString:@\"" + generate_random_str(out_random_type_method_name) + "\" options:NSCaseInsensitiveSearch range:NSMakeRange(0," + data_param_str +".length-1)];\n"
            out_str += "\t" + random_var1 + " = [" + data_param_str + " stringByAppendingString:@\"" + str1 + "\"];\n"
            if random_index < 10:
                property_str = get_random_property(class_obj_list)
                out_str += "\t" + property_str + " = @\"" + str1 + "\";\n"
        if random_insert == 1:
            out_str +=  "\t[" + data_param_str + " insertString:@\"" + generate_random_str(out_random_type_method_name) + "\" atIndex:5];\n"
            out_str += "\t" + random_var1 + " = [" + data_param_str + " stringByReplacingOccurrencesOfString:@\"" + generate_words_str("random_str") + "\" withString:@\"" + generate_words_str("random_str") + "\"];\n"
        if random_insert == 2:
            out_str +=  "\t[" + data_param_str + " lowercaseString];\n"
            out_str += "\t" + random_var1 + " = [" + data_param_str + " stringByAppendingString:@\"" + generate_words_str("random_str")+ "\"];\n"
    #返回处理之后的可变字符串
    return out_str

# 处理0723DefendGarden申诉调用
def handle_transfer_defend_Garden():
    out_str = ""
    var1 = generate_random_str(out_random_type_class)
    out_str += "\tNSMutableString *" + var1 + " = [NSMutableString string];\n"
    str1 = generate_words_str("random_str")
    out_str += "\t[" + var1 + " appendString:@\"" + str1 + "\"];\n"
    random_depth = random.randrange(1, 3)
    for i in range(random_depth):
        random_index = random.randrange(0, 5)
        if random_index == 0:
            out_str += "\t[" + var1 + " stringByRemovingPercentEncoding];\n"
        elif random_index == 1:
            out_str += "\t[" + var1 + " appendFormat:@\"%@\", @\"" + generate_words_str("random_str") + "\"];\n"
        elif random_index == 2:
            out_str += "\t[" + var1 + " appendString:@\"" + generate_words_str("random_str") + "\"];\n"
        elif random_index == 3:
            out_str += "\t[" + var1 + " replaceCharactersInRange:NSMakeRange(" + str(random.randrange(0, 3)) + ", " + str(random.randrange(0, 2)) + ") withString:@\"" + generate_words_str("random_str") + "\"];\n"
        elif random_index == 4:
            var2 = generate_random_str(out_random_type_class)
            out_str += "\tNSString *" + var2 + " = [" + var1 + " stringByAppendingString:@\"" + generate_words_str("random_str") + "\"];\n"
            out_str += "\t" + var2 + " = [" + var2 + " stringByDeletingLastPathComponent];\n"

    return out_str

# 02.27新插入点
def generate_handle_0303_NSLayoutConstraint_NSLayoutManager():
    #data_param_str 传入的参数是可变字符串的处理
    out_str = ""
    random_var1 = generate_random_str(out_random_type_method_name)
    random_var2 = generate_random_str(out_random_type_method_name)
    # random_var3 = generate_random_str(out_random_type_method_name)
    out_str += "\tNSLayoutConstraint * " + random_var1 + " = [[NSLayoutConstraint alloc]init];\n"
    # out_str += "\tNSMutableIndexSet * " + random_var1 + " = [[NSMutableIndexSet alloc]init];\n"
    out_str += "\tNSLayoutManager * " + random_var2 + " = [[NSLayoutManager alloc]init];\n"
    # out_str += "\t[" + random_var2 + " setMinimum:@([" + random_var1 + " doubleValue] - 100.100)];\n"
    # out_str += "\tCGFloat " + random_var3 + " = " + str(random.randrange(0, 30)) + ";\n"
    myList = []
    for i in range(random.randrange(5, 10)):
        random_insert = random.randrange(1, 9)
        if random_insert == 1 and 1 not in myList:
            myList.append(1)
            out_str += "\t[" + random_var1 + " setActive:[" + random_var2 + " allowsNonContiguousLayout]];\n"
        if random_insert == 2 and 2 not in myList:
            myList.append(2)
            out_str += "\t[" + random_var1 + " setIdentifier:@\"" + generate_words_str("random_str") + "\"];\n"
        if random_insert == 3 and 3 not in myList:
            myList.append(3)
            out_str += "\t[" + random_var1 + " setConstant:" + str(random.randrange(0, 10)) + "];\n"
        if random_insert == 4 and 4 not in myList:
            myList.append(4)
            out_str += "\t[" + random_var1 + " firstAttribute];\n"
        if random_insert == 5 and 5 not in myList:
            myList.append(5)
            out_str += "\t[" + random_var2 + " ensureLayoutForCharacterRange:NSRangeFromString([" + random_var1 + " identifier])];\n"
        if random_insert == 6 and 6 not in myList:
            myList.append(6)
            out_str += "\t[" + random_var2 + " getFirstUnlaidCharacterIndex:nil glyphIndex:nil];\n"
        if random_insert == 7 and 7 not in myList:
            myList.append(7)
            out_str += "\t[" + random_var2 + " invalidateLayoutForCharacterRange:NSRangeFromString([" + random_var1 + " identifier]) actualCharacterRange:nil];\n"
        if random_insert == 8 and 8 not in myList:
            myList.append(8)
            out_str += "\t[" + random_var2 + " setUsesFontLeading:[" + random_var1 + " isActive]];\n"
#返回处理之后的可变字符串
    return out_str


# 生成定义字符串，调用后转data调用
def generate_handle_string_data(data_param_str):
    out_str = ""
    random_var1 = generate_random_str(out_random_type_method_name)
    out_str += "\tNSData *" + random_var1 + " = [" + data_param_str + " dataUsingEncoding:NSASCIIStringEncoding];\n"
    random_var2 = generate_random_str(out_random_type_method_name)
    out_str += "\tNSMutableData *" + random_var2 + " = [" + random_var1 + " mutableCopy];\n"
    out_str += "\t[" + random_var2 + " appendBytes:\"" + generate_words_str("random_str") + "\" length:4];\n"
    out_str += "\t[" + random_var2 + " replaceBytesInRange:NSMakeRange(0, 1) withBytes:\"" + generate_words_str("random_str") + "\"];\n"
    return out_str
    


# 生成处理字典的调用
def generate_handle_dic(dic_param_str):
    out_str = ""
    random_var0 = generate_random_str(out_random_type_class)
    out_str += "\tNSData *" + random_var0 + " = [NSJSONSerialization dataWithJSONObject:" + dic_param_str + " options:NSJSONWritingPrettyPrinted error:nil];\n"
    random_var = generate_random_str(out_random_type_class)
    random_index = random.randrange(6, 21)
    out_str += "\tNSData *" + random_var + " = [" + random_var0 + " subdataWithRange:NSMakeRange(0, %d)];\n" % random_index
    out_str += "\t" + random_var + " = [" + random_var0 + " copy];\n"
    
    random_sqlite = random.randrange(0, 101)
    if random_sqlite == 1:
        out_str += "\tNSString *documentpath = [NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES) firstObject];\n"
        out_str += "\tNSString *path = [NSString stringWithFormat:@\"%@/matchB.db\",documentpath];\n"
        out_str += "\tsqlite3 *database;\n"
        out_str += "\tint databaseResult = sqlite3_open([path UTF8String], &database);\n"
        out_str += "\tif (databaseResult != SQLITE_OK)\n"
        out_str += "\t{\n"
        random_str = generate_words_str("random_str")
        out_str += "\t\tNSLog(@\"" + random_str + ",%d\", databaseResult);\n"
        out_str += "\t}\n"
        out_str += "\tchar *error;\n"
        random_str1 = generate_words_str("random_str")
        out_str += "\tconst char *createSQL = \"" + random_str1 +"\";\n"
        out_str += "\tint tableResult = sqlite3_exec(database, createSQL, NULL, NULL, &error);\n"
        out_str += "\tif (tableResult != SQLITE_OK)\n"
        out_str += "\t{\n"
        random_str2 = generate_words_str("random_str")
        out_str += "\t\tNSLog(@\"" + random_str2 +":%s\",error);\n"
        out_str += "\t}\n"
        out_str += "\tsqlite3_stmt *stmt;\n"
        random_str3 = generate_words_str("random_str")

        out_str += "\tconst char *insertSQL = \"" + random_str3 + "\";\n"
        out_str += "\tint insertResult = sqlite3_prepare_v2(database, insertSQL, -1, &stmt, nil);\n"
        out_str += "\tif (insertResult != SQLITE_OK)\n"
        out_str += "\t{\n"
        random_str4 = generate_words_str("random_str")
        out_str += "\t\tNSLog(@\""+ random_str4 + ",%d\",insertResult);\n"
        out_str += "\t}\n"
        out_str += "\telse\n"
        out_str += "\t{\n"
        out_str += "\t\tsqlite3_step(stmt);\n"
        out_str += "\t}\n"
    
    return out_str

# 生成处理可变字符串
def generate_handle_mutablestr(mutablestr_param):
    need_replace_str = ""
    random_target_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    random_index_1 = random.randrange(0, len(random_target_str))
    random_index_2 = random.randrange(0, len(random_target_str))
    random_index_3 = random.randrange(0, len(random_target_str))
    random_index_4 = random.randrange(0, len(random_target_str))
    random_str = generate_words_str("random_str")
    need_replace_str += "\t[" + mutablestr_param + " replaceCharactersInRange:NSMakeRange(0, 1) withString:@\"" + random_target_str[random_index_1] + "\"];\n"
    need_replace_str += "\t[" + mutablestr_param + " replaceCharactersInRange:NSMakeRange(1, 1) withString:@\"" + random_target_str[random_index_2] + "\"];\n"
    need_replace_str += "\t[" + mutablestr_param + " appendString:" + "@\"" + random_str + "\"];\n"
    need_replace_str += "\t[" + mutablestr_param + " stringByReplacingOccurrencesOfString:@\"" + random_target_str[random_index_3] + "\" withString:@\"" + random_target_str[random_index_4] + "\"];\n"
    return need_replace_str

# 随机生成oc颜色字符串
def generate_random_color():
    random_index = random.randrange(0, 16)
    if random_index == 0:
        return "blackColor"
    elif random_index == 1:
        return "darkGrayColor"
    elif random_index == 2:
        return "lightGrayColor"
    elif random_index == 3:
        return "whiteColor"
    elif random_index == 4:
        return "grayColor"
    elif random_index == 5:
        return "redColor"
    elif random_index == 6:
        return "greenColor"
    elif random_index == 7:
        return "blueColor"
    elif random_index == 8:
        return "cyanColor"
    elif random_index == 9:
        return "yellowColor"
    elif random_index == 10:
        return "magentaColor"
    elif random_index == 11:
        return "orangeColor"
    elif random_index == 12:
        return "purpleColor"
    elif random_index == 13:
        return "brownColor"
    elif random_index == 14:
        return "clearColor"
    else:
        return "blackColor"

# 随机生成button的style
def generate_button_style():
    random_index = random.randrange(0, 200)
    if random_index % 6 == 0:
        return "UIButtonTypeCustom"
    elif random_index % 6 == 1:
        return "UIButtonTypeSystem"
    elif random_index % 6 == 2:
        return "UIButtonTypeDetailDisclosure"
    elif random_index % 6 == 3:
        return "UIButtonTypeInfoLight"
    elif random_index % 6 == 4:
        return "UIButtonTypeInfoDark"
    elif random_index % 6 == 5:
        return "UIButtonTypeContactAdd"
    else:
        return "UIButtonTypeCustom"


# 随机显示隐藏
def generate_random_show():
    random_index = random.randrange(0, 20)
    if random_index % 2  == 0:
        return "NO"
    else:
        return "YES"

# 随机生成cell的风格
def generate_random_cell_style():
    random_index = random.randrange(0, 200)
    if random_index % 4 == 0:
        return "UITableViewCellStyleDefault"
    elif random_index % 4 == 1:
        return "UITableViewCellStyleValue1"
    elif random_index % 4 == 2:
        return "UITableViewCellStyleValue2"
    elif random_index % 4 == 3:
        return "UITableViewCellStyleSubtitle"
    else:
        return "UITableViewCellStyleDefault"

# 随机选取一个实现
def implamentation_from_directory(directory_name):
    '''
    随机选取一个实现
    param:
    directory_name:文件夹名称
    '''
    out_str = ""
    target_implamentation_list = []
    if directory_name == foundation_coder_path:
        target_implamentation_list = foundation_implamentation_list
    elif directory_name == model_coder_path:
        target_implamentation_list = model_implamentation_list
    random_index = random.randrange(0, len(target_implamentation_list))
    file_path = target_implamentation_list[random_index]
    with open(file_path, "r") as input:
        out_str = input.read()
    return out_str

# 处理随机实现
def handle_for_random_implamentation(random_str):
    '''
    随机处理随机实现
    param:
    random_str:实现内容 type:string
    '''
    out_str = random_str
    str1 = generate_words_str("random_str")
    str2 = generate_words_str("random_str")
    str3 = generate_words_str("random_str")
    str4 = generate_words_str("random_str")
    str5 = generate_words_str("random_str")
    var1 = generate_random_str(out_random_type_method_init)
    var2 = generate_random_str(out_random_type_method_init)
    var3 = generate_random_str(out_random_type_method_init)
    var4 = generate_random_str(out_random_type_method_init)
    var5 = generate_random_str(out_random_type_method_init)
    out_str = out_str.replace("var1", var1).replace("var2", var2).replace("var3", var3).replace("var4", var4).replace("var5", var5)
    out_str = out_str.replace("str1", str1).replace("str2", str2).replace("str3", str3).replace("str4", str4).replace("str5", str5)
    return out_str


# 随机生成数组的实现
def implamentation_of_mutablearray():
    out_str = ""
    out_str += "\tNSMutableArray *xx = [NSMutableArray array];\n"
    random_num = random.randrange(10, 20)
    for index in range(random_num):
        out_str += "\t[xx addObject:"
        out_str += "@\"" + generate_words_str("random_str") + "\""
        out_str += "];\n"
        #随机生成调用点
        random_insert = random.randrange(0, 100)
        if random_insert < 5:
            out_str += "\t//////insert//\n"
    
    out_str += "\treturn xx;\n"
    return out_str


# 搜索所有的C函数及实现
def initial_C_funcs_from_file(implamentation_file_list):
    return ""


# 搜索所有的函数及实现
def initial_class_from_file(implamentation_file_list):
    
    class_obj_list = []
    for file in implamentation_file_list:
        file_content = ""
        with open(file, "r") as input:
            file_content = input.read()

        filename = os.path.splitext(file)[0]
        #去掉文件的后缀
        nosuffix_file_name = os.path.basename(filename)
        #文件名即类名
        method_list = oc_func_rule3.findall(file_content)

        generate_method_list = []
        generate_implamentation_list = []
        for method_str in method_list:
            
            print("method_str :" + method_str)
            current_implamentation = findimplamentation(method_str, file_content)
            # print("implamentation:" + current_implamentation)
            return_value = methodtransfer.returnvalue_from_method(method_str)
            method_type = methodtransfer.methodtype_from_method(method_str)
            transfer = methodtransfer.transfer_from_method(method_str)
            print("transfer:" + transfer)
            # if method_str.startswith("initW"):
            #     continue
            # if "instancetype" in return_value:
            #     continue

            # print("transfer :" + transfer)
            parampair_list = methodtransfer.parampair_from_method(method_str)

            method_obj = methodtransfer.MethodPrototype(transfer, method_type, return_value, parampair_list)
            # print("method_obj :" + method_obj.output_prototype())
            implamentation_obj = methodtransfer.MethodImplamentation(method_obj, current_implamentation)
            generate_method_list.append(method_obj)
            generate_implamentation_list.append(implamentation_obj)
        class_obj = methodtransfer.ClassObject(nosuffix_file_name, "", [], generate_method_list, generate_implamentation_list)
        class_obj_list.append(class_obj)
    return class_obj_list

# 生成头文件记录
def generate_import_record(class_list):
    out_str = ""
    for class_obj in class_list:
        class_name = class_obj.class_name
        out_str += "#import \"" + class_name + ".h\"\n"
    return out_str

# 处理项目重构
def handle_reconstruction():
    '''
    处理项目重构
    '''
    global global_param_name
    global_param_name = generate_words_str("property")
    print("param_name:" + global_param_name)

    implamentation_file_list = get_search_files("target", [".m", ".mm"], nosearch_directorys)
    our_class_list = initial_class_from_file(implamentation_file_list)

    # 生成类列表
    generate_class_list = generate_classlist(10)

    #记录头文件信息
    our_import = generate_import_record(our_class_list)
    generete_import = generate_import_record(generate_class_list)
    record_file_path = "import/import.txt"
    with open(record_file_path, "w") as input:
        input.write(our_import+generete_import)

    #开始处理函数实现
    move_implamentation(our_class_list, generate_class_list, 5)

    #写文件
    for class_obj in generate_class_list:
        path = "ganerate/"
        header_file_path = path + class_obj.class_name + ".h"
        implamentation_file_path = path + class_obj.class_name + ".m"

        with open(header_file_path, "w") as input:
            input.write(class_obj.output_class_header())

        with open(implamentation_file_path, "w") as input:
            input.write(class_obj.output_class_implamentation())

    #更新原来文件的实现
    for index, file in enumerate(implamentation_file_list):
        file_content = ""
        with open(file, "r") as input:
            file_content = input.read()
        # pdb.set_trace()
        # filename = os.path.splitext(file)[0]
        #去掉文件的后缀
        # nosuffix_file_name = os.path.basename(filename)
        #文件名即类名
        method_list = oc_func_rule3.findall(file_content)
        our_class_obj = our_class_list[index]

        for j, method_str in enumerate(method_list):
            origin_implamentation_str = findimplamentation(method_str, file_content)
            handle_method_str = method_str.replace(" ", "")
            implamentation_obj = our_class_obj.implamentation_list[j]
            current_method_str = implamentation_obj.method_prototype.output_prototype()
            current_method_str = current_method_str.replace(" ", "")
            if handle_method_str in current_method_str:
                new_implamentation_str = implamentation_obj.implamentation
                file_content = file_content.replace(origin_implamentation_str, new_implamentation_str)
        with open(file, "w") as input:
            input.write(file_content)
        
    
    
    # for class_obj in our_class_list:
    #     #写文件
    #     path = "ganerate_origin/"
    #     header_file_path = path + class_obj.class_name + ".h"
    #     implamentation_file_path = path + class_obj.class_name + ".m"

    #     with open(header_file_path, "w") as input:
    #         input.write(class_obj.output_class_header())

    #     with open(implamentation_file_path, "w") as input:
    #         input.write(class_obj.output_class_implamentation())


# 从目标函数名与参数列表生成对应的函数名
def methodname_from_method(parampair_list):
    # pdb.set_trace()
    # 设置有语义
    method_name = generate_words_str("func")
    # 设置无语义
    # method_name = generate_random_str(out_random_type_method_name)
    out_str = ""
    out_str += method_name
    for parampair_obj in parampair_list:
        # 无语义
        # param_name = generate_random_str(out_random_type_class)
        # 有语义
        param_name = generate_words_str("property")

        # out_str += parampair_obj.param_name + ":"
        
        out_str += param_name + ":"
    return out_str   

# 将旧类的实现转换到新类
def move_implamentation(old_class_list, new_class_list, max_depth):

    for class_obj in old_class_list:
        class_name = class_obj.class_name
        for implamentation_obj in class_obj.implamentation_list:
            implamentation_str = implamentation_obj.implamentation
            prototype_obj = implamentation_obj.method_prototype


            # 过滤掉初始化函数
            if prototype_obj.transfer_name.startswith("initW") or "instancetype" in prototype_obj.return_type:
                continue
            
            # 实现中带super的也过滤掉
            if "super" in implamentation_str and "super viewDidLoad" not in implamentation_str:
                continue

            # #过滤掉setter方法和getter方法
            # if "_" in implamentation_str:
            #     continue
            
            # 设置一个添加比例 35%添加
            random_precent = random.randrange(0, 100)
            if random_precent < 65:
                continue


            #随机取出一个新类
            random_class_obj = new_class_list[random.randrange(0, len(new_class_list))]
            #将旧的实现copy到新的随机类里面
            # param_name = "oldClassName"
            param_name = global_param_name
            parampair_obj = methodtransfer.ParamPair(param_name, class_name + " *")
            new_transfer = methodname_from_method(copy.copy(prototype_obj.parampair_list)) + param_name + ":"
            new_parampair_list = copy.copy(prototype_obj.parampair_list)
            # 需要更新参数列表
            new_parampair_list.append(parampair_obj)
            new_prototype_obj = methodtransfer.MethodPrototype(new_transfer, "+", prototype_obj.return_type, new_parampair_list)
            implamentation_str = implamentation_str.replace("self", global_param_name)
            new_implamentation_obj = methodtransfer.MethodImplamentation(new_prototype_obj, implamentation_str)

            random_class_obj.addprototype(new_prototype_obj)
            random_class_obj.addimplamentation(new_implamentation_obj)
            
            # max_depth = 3
            random_depth = random.randrange(2, max_depth)
            # random_depth = 2
            
            #处理中间调用层
            handle_middle_transfer(new_class_list, class_name, implamentation_obj, random_class_obj.class_name, new_implamentation_obj, random_depth)

# 生成函数调用
def generate_transfer(transfer_str, param_list):
    # pdb.set_trace()
    # print("transfer_str " + transfer_str)
    out_str = ""
    char_list = methodtransfer.count_str(":", transfer_str)
    if len(char_list):

        pieces_list = []
        prefix_str = ""
        for index, index_value in enumerate(char_list):
            if index == 0:
                prefix_str = transfer_str[0:index_value + 1]
            else:
                prefix_str = transfer_str[char_list[index-1]+1:index_value + 1]
            pieces_list.append(prefix_str)
        for index, piece in enumerate(pieces_list):
            if index > len(param_list) - 1:
                out_str += piece + "self "
            else:
                out_str += piece + param_list[index].param_name + " "
        # print("out_str " + out_str)
    else:
        out_str = transfer_str
    return out_str


# 中间调用层为原有实现添加判断分支
def add_branch_for_middle_implamentation(origin_implamentation):

    print("添加分支:origin_imp:" + origin_implamentation)
    #为原来的实现添加上判断分支
    
    # 50%的概率会加上分支
    random_number = random.randrange(0, 100)
    if random_number < 50:
        return origin_implamentation

    # 主线分支是恒成立的条件，剩下的分支是不会被运行的，这里不能弄错!!!!

    # 去掉首尾
    if (origin_implamentation.startswith("{\n")):
        origin_implamentation = origin_implamentation[2:]
    if (origin_implamentation.endswith("}\n")):
        origin_implamentation = origin_implamentation[:-2]

    print("remove head and tail:" + origin_implamentation)

    out_implamentation = ""
    # 需要加上判断条件及分支
    random_number = random.randrange(1, 14)
    # pdb.set_trace()
    if random_number == 1:
        # 判断系统版本号
        out_implamentation += "\tNSString *systemVersion = [[UIDevice currentDevice] systemVersion];\n"
        out_implamentation += "\tif ([systemVersion floatValue] > 7.0)\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t" + origin_implamentation
        out_implamentation += "\t}\n"
        out_implamentation += "\telse\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t\t//////insert//\n"
        out_implamentation += "\t}\n"
    elif (random_number == 2):
        # 判断系统名称
        out_implamentation += "\tNSString *systemName = [[UIDevice currentDevice] systemName];\n"
        out_implamentation += "\tif ([systemName isEqualToString:@\"" + generate_words_str("random_str") + "\"])\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t\t//////insert//\n"
        out_implamentation += "\t}\n"
        out_implamentation += "\telse\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t" + origin_implamentation
        out_implamentation += "\t}\n"
    elif (random_number == 3):
        # 判断设备model
        out_implamentation += "\tif ([[[UIDevice currentDevice] model] isEqualToString:@\"" + generate_words_str("random_str") + "\"])\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t\t//////insert//\n"
        out_implamentation += "\t}\n"
        out_implamentation += "\telse\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t" + origin_implamentation
        out_implamentation += "\t}\n"
    elif (random_number == 4):
        # idfv
        out_implamentation += "\tNSString *idfv = [[[UIDevice currentDevice] identifierForVendor] UUIDString];\n"
        out_implamentation += "\tif (idfv != nil && [idfv isEqualToString:@\"" + generate_words_str("random_str") + "\"])\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t\t//////insert//\n"
        out_implamentation += "\t}\n"
        out_implamentation += "\telse\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t" + origin_implamentation
        out_implamentation += "\t}\n"
    elif (random_number == 5):
        # 获取当前时间
        out_implamentation += "\tNSDate *currentDate = [NSDate dateWithTimeIntervalSinceNow:0];\n"
        out_implamentation += "NSTimeInterval time = [currentDate timeIntervalSince1970];\n"
        random_index = random.randrange(1, 10000)
        out_implamentation += "\tif (time > " + str(random_index) + ")\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t" + origin_implamentation
        out_implamentation += "\t}\n"
        out_implamentation += "\telse\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t\t//////insert//\n"
        out_implamentation += "\t}\n"
    elif (random_number == 6):
        # 字符串
        out_implamentation += "\tNSString *testStr = @\"" + generate_words_str("random_str") + "\";\n"
        out_implamentation += "\tif ([testStr containsString:@\"" + generate_words_str("random_str") + "\"])\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t\t//////insert//\n"
        out_implamentation += "\t}\n"
        out_implamentation += "\telse\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t" + origin_implamentation
        out_implamentation += "\t}\n"
    elif (random_number == 7):
        # number
        random_index = random.randrange(1, 1000)
        out_implamentation += "\tNSNumber *lastNum = @(" + str(random_index) + ");\n"
        out_implamentation += "\tif ([lastNum floatValue] > 0)\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t" + origin_implamentation
        out_implamentation += "\t}\n"
        out_implamentation += "\telse\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t\t//////insert//\n"
        out_implamentation += "\t}\n"
    elif (random_number == 8):
        # 数组
        out_implamentation += "\tNSArray *fromArr = @[@\"" + generate_words_str("random_str") + "\", @\"" + generate_words_str("random_str") + "\", @\"" + generate_words_str("random_str") + "\"];\n"
        out_implamentation += "\tif ([fromArr containsObject:@\"" + generate_words_str("random_str") + "\"])\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t\t//////insert//\n"
        out_implamentation += "\t}\n"
        out_implamentation += "\telse\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t" + origin_implamentation
        out_implamentation += "\t}\n"
    elif (random_number == 9):
        # userDefault
        out_implamentation += "\tNSString *userDefaultsStr = [[NSUserDefaults standardUserDefaults] objectForKey:@\"" + generate_words_str("random_str") + "\"];\n"
        out_implamentation += "\tif (userDefaultsStr)\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t\t//////insert//\n"
        out_implamentation += "\t}\n"
        out_implamentation += "\telse\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t" + origin_implamentation
        out_implamentation += "\t}\n"
    elif (random_number == 10):
        # Pasteboard
        out_implamentation += "\tNSString *pastboardStr = [UIPasteboard generalPasteboard].string;\n"
        out_implamentation += "\tif (pastboardStr && [pastboardStr hasPrefix:@\"" + generate_words_str("random_str") + "\"])\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t\t//////insert//\n"
        out_implamentation += "\t}\n"
        out_implamentation += "\telse\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t" + origin_implamentation
        out_implamentation += "\t}\n"
    elif (random_number == 11):
        # 字典
        out_implamentation += "\tNSDictionary *dicStr = @{@\"" + generate_words_str("random_str") + "\":@\"" + generate_words_str("random_str") + "\", @\"" + generate_words_str("random_str") + "\":@\"" + generate_words_str("random_str") + "\"};\n"
        out_implamentation += "\tNSString *dicValue = [dicStr objectForKey:@\"" + generate_words_str("random_str") + "\"];\t"
        out_implamentation += "\tif (dicValue && [dicValue hasSuffix:@\"" + generate_words_str("random_str") + "\"])\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t\t//////insert//\n"
        out_implamentation += "\t}\n"
        out_implamentation += "\telse\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t" + origin_implamentation
        out_implamentation += "\t}\n"
    elif (random_number == 12):
        # rootWindow
        out_implamentation += "\tUIWindow *rootWindow = [[UIApplication sharedApplication].delegate window];\n"
        out_implamentation += "\tif (rootWindow.alpha == 0)\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t\t//////insert//\n"
        out_implamentation += "\t}\n"
        out_implamentation += "\telse\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t" + origin_implamentation
        out_implamentation += "\t}\n"
    elif (random_number == 13):
        # rootView
        out_implamentation += "\tUIView *rootV = [[UIApplication sharedApplication].delegate window].rootViewController.view;\n"
        out_implamentation += "\tif (rootV.hidden)\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t\t//////insert//\n"
        out_implamentation += "\t}\n"
        out_implamentation += "\telse\n"
        out_implamentation += "\t{\n"
        out_implamentation += "\t" + origin_implamentation
        out_implamentation += "\t}\n"

    print("out_implamentation1:" + out_implamentation)
    # 需要重新添加上首尾
    out_implamentation = "{\n" + out_implamentation + "\n}"
    
    print("out_implamentation2:" + out_implamentation)
    return out_implamentation

# 处理中间调用层
def handle_middle_transfer(new_class_list, first_class_name, first_implamentation_obj, last_class_name, last_implamentation_obj, random_depth):
    '''
    new_class_list:生成的类list
    first_class_name:旧的类名
    first_implamentation_obj:旧的实现对象
    last_class_name:新的类名
    last_implamentation_obj:新的实现对象
    random_depth:随机深度
    '''
    # print("first_transfer:" + first_implamentation_obj.method_prototype.transfer_name)
    # print("last_transfer:" + last_implamentation_obj.method_prototype.transfer_name)

    pre_class_name = first_class_name
    pre_implamentation_obj = first_implamentation_obj
    # print(random_depth)
    for i in range(random_depth):

        old_update_implamentation = "{\n"
        if random.randrange(0, 100) < 20:
            old_update_implamentation += "\t//////insert//\n"
        
        new_update_implamentation = "{\n"
        if random.randrange(0, 100) < 20:
            new_update_implamentation += "\t//////insert//\n"
        
        # pdb.set_trace()
        if i == 0:
            #上一个类就是 first_implamentation_obj
            #随机取出一个新类
            old_class_name = first_class_name
            random_class_obj = new_class_list[random.randrange(0, len(new_class_list))]
            # print("random_class_obj_class_name:" + random_class_obj.class_name)
            new_class_name = random_class_obj.class_name
        
            new_parampair_list = copy.copy(first_implamentation_obj.method_prototype.parampair_list)
            #参数列表需要更新
            # param_name = "oldClassName"
            param_name = global_param_name
            parampair_obj = methodtransfer.ParamPair(param_name, old_class_name + " *")
            new_parampair_list.append(parampair_obj)
            
            new_transfer = methodname_from_method(new_parampair_list)
            generate_prototype_obj = methodtransfer.MethodPrototype(new_transfer, "+", first_implamentation_obj.method_prototype.return_type, new_parampair_list)
            generate_implamentation_obj = methodtransfer.MethodImplamentation(generate_prototype_obj,  "{\n\n}")
            
            # 根据返回类型判断是否需要return
            old_return_value = first_implamentation_obj.method_prototype.return_type
            if "void" in old_return_value:
                old_update_implamentation += "\t[" + new_class_name + " " + generate_transfer(generate_prototype_obj.transfer_name, copy.copy(first_implamentation_obj.method_prototype.parampair_list)) + "];\n"
            else:
                old_update_implamentation += "\treturn [" + new_class_name + " " + generate_transfer(generate_prototype_obj.transfer_name, copy.copy(first_implamentation_obj.method_prototype.parampair_list)) + "];\n"
            old_update_implamentation += "}\n"


            # # 需要为中间调用层添加分支
            # old_update_implamentation = add_branch_for_middle_implamentation(old_update_implamentation)


            #需要更新上一个的实现
            first_implamentation_obj.update_implamentation(old_update_implamentation)
            
            # print("first_implamentation_obj:" + first_implamentation_obj.output_implamentation())

            random_class_obj.addprototype(generate_prototype_obj)
            random_class_obj.addimplamentation(generate_implamentation_obj)
            # print("0current depth:" + str(random_depth))
            # print("0current method:" + generate_implamentation_obj.method_prototype.transfer_name)
            # print("0current implamentation:" + generate_implamentation_obj.output_implamentation())
            # print("0pre method:" + pre_implamentation_obj.method_prototype.transfer_name)
            # print("0pre implamentation:" + pre_implamentation_obj.output_implamentation())
            
            #更新旧的对象
            pre_implamentation_obj = generate_implamentation_obj
            pre_class_name = random_class_obj.class_name
        elif i == random_depth - 1:
            #最后一个 上一个类就是 pre_implamentation_obj
            # 本轮不需要随机类 需要更新上一轮的实现
            #需要更新上一个的实现
            old_return_value = pre_implamentation_obj.method_prototype.return_type
            if "void" in old_return_value:
                old_update_implamentation += "\t[" + last_class_name + " " + generate_transfer(last_implamentation_obj.method_prototype.transfer_name, copy.copy(pre_implamentation_obj.method_prototype.parampair_list)) + "];\n"
            else:
                old_update_implamentation += "\treturn [" + last_class_name + " " + generate_transfer(last_implamentation_obj.method_prototype.transfer_name, copy.copy(pre_implamentation_obj.method_prototype.parampair_list)) + "];\n"
            old_update_implamentation += "}\n"

            # 需要为中间调用层添加分支
            # old_update_implamentation = add_branch_for_middle_implamentation(old_update_implamentation)

            pre_implamentation_obj.update_implamentation(old_update_implamentation)
            # print("random_depth - 1:" + pre_implamentation_obj.output_implamentation())

            # print("current method not generate")
            # print("current implamentation not generate")
            # print("pre method:" + pre_implamentation_obj.method_prototype.transfer_name)
            # print("pre implamentation:" + pre_implamentation_obj.output_implamentation())

            #更新旧的对象
            pre_implamentation_obj = last_implamentation_obj
            pre_class_name = last_class_name
        else:
            #上一个类就是 pre_implamentation_obj
            #随机取出一个新类
            old_class_name = pre_class_name
            random_class_obj = new_class_list[random.randrange(0, len(new_class_list))]
            # print("random_class_obj_class_name:" + random_class_obj.class_name)
            new_class_name = random_class_obj.class_name
        
            #不需要生成新的参数列表
            new_parampair_list = copy.copy(pre_implamentation_obj.method_prototype.parampair_list)

            new_transfer = methodname_from_method(pre_implamentation_obj.method_prototype.parampair_list)
            generate_prototype_obj = methodtransfer.MethodPrototype(new_transfer, "+", pre_implamentation_obj.method_prototype.return_type, new_parampair_list)
            generate_implamentation_obj = methodtransfer.MethodImplamentation(generate_prototype_obj,  "{\n\n}")
            
            #需要更新上一个的实现
            old_return_value = pre_implamentation_obj.method_prototype.return_type
            if "void" in old_return_value:
                old_update_implamentation += "\t[" + new_class_name + " " + generate_transfer(generate_prototype_obj.transfer_name, copy.copy(pre_implamentation_obj.method_prototype.parampair_list)) + "];\n"
            else:
                old_update_implamentation += "\treturn [" + new_class_name + " " + generate_transfer(generate_prototype_obj.transfer_name, copy.copy(pre_implamentation_obj.method_prototype.parampair_list)) + "];\n"
            old_update_implamentation += "}\n"

            # 需要为中间调用层添加分支
            # old_update_implamentation = add_branch_for_middle_implamentation(old_update_implamentation)

            pre_implamentation_obj.update_implamentation(old_update_implamentation)

            # print("pre_implamentation_obj:" + pre_implamentation_obj.output_implamentation())
            
            random_class_obj.addprototype(generate_prototype_obj)
            random_class_obj.addimplamentation(generate_implamentation_obj)

            # print("-1current method:" + generate_implamentation_obj.method_prototype.transfer_name)
            # print("-1current implamentation:" + generate_implamentation_obj.output_implamentation())
            # print("-1pre method:" + pre_implamentation_obj.method_prototype.transfer_name)
            # print("-1pre implamentation:" + pre_implamentation_obj.output_implamentation())

            #更新旧的对象
            pre_implamentation_obj = generate_implamentation_obj
            pre_class_name = random_class_obj.class_name


# 随机生成类对象
def generate_classlist(count):
    class_list = []
    for i in range(count):
        prefix_str = class_prefix_str
        class_name = generate_words_str("property")
        # class_name = prefix_str + generate_random_str(out_random_type_class)
        class_obj = methodtransfer.ClassObject(class_name, "NSObject", [], [], [])
        class_list.append(class_obj)
    return class_list

# 生成一条新的调用
def generate_fourth_transfer(class_obj_list):
    '''
    第四版生成调用
    规则：90%的概率重新生成，10%的概率从库里拿旧的，如果没拿到旧的，就重新生成
    '''
    random_index = random.randrange(0, 100)
    class_obj = class_obj_list[random.randrange(0, len(class_obj_list))]
    method_name = ""
    if random_index <= 90:
        # 生成新的
        method_name = generate_words_str("func")
        class_obj.add_method(copy.copy(method_name))
    else:
        # 取旧的
        method_list = class_obj.get_method_list()
        if method_list == []:
            # 取不到旧的就直接取新的
            method_name = generate_words_str("func")
            class_obj.add_method(copy.copy(method_name))
        else:
            # 取旧的
            method_name = copy.copy(method_list[random.randrange(0, len(method_list))])
    
    transfer_name = "\t[[" + copy.copy(class_obj.get_class_name()) + " " + copy.copy(class_obj.get_shared_method()) + "] " + method_name + "];//" + copy.copy(class_obj.get_class_name())
    return transfer_name


# 生成一条新的调用
def generate_fifth_transfer(class_obj, target_probability, class_obj_list):
    '''
    第五版生成调用
    规则：90%的概率重新生成，10%的概率从库里拿旧的，如果没拿到旧的，就重新生成
    与第四版区别：增加了参数列表，需要兼容有多个参数的情况
    0817版修改
    增加了target_probability参数:是支持概率可变
    class_obj_list:插入点类列表
    '''
    return_type = method_return_type[implamentation_type_mutablestring_data_tNSMutableData]
    random_index = random.randrange(0, 100)
    method_obj = inserthandler.MethodObject("", return_type, [])
    if random_index <= target_probability:
        # 生成新的
        method_name = generate_words_str("func")
        # 随机生成0~9个参数
        arg_count = random.randrange(0, 10)
        arg_list = []
        for i in range(arg_count):
            arg_name = generate_words_str("property")
            arg_list.append(arg_name)
        method_obj = inserthandler.MethodObject(method_name, return_type, arg_list)
        class_obj.add_method(method_obj)
    else:
        # 取旧的
        method_list = class_obj.get_method_list()
        if method_list == []:
            # 取不到旧的就直接取新的
            # 生成新的
            method_name = generate_words_str("func")
            # 随机生成0~9个参数
            arg_count = random.randrange(0, 10)
            arg_list = []
            for i in range(arg_count):
                arg_name = generate_words_str("property")
                arg_list.append(arg_name)
            method_obj = inserthandler.MethodObject(method_name, return_type, arg_list)
            class_obj.add_method(method_obj)
        else:
            # 取旧的
            method_obj = copy.copy(method_list[random.randrange(0, len(method_list))])
    # transfer_name = "\t[[" + copy.copy(class_obj.get_class_name()) + " " + copy.copy(class_obj.get_shared_method()) + "] " + method_obj.mainbody
    transfer_name = "\t[" + copy.copy(class_obj.get_static_var()) + " " + method_obj.mainbody
    out_str = ""
    if len(method_obj.arg_list) > 0:
        for index, arg_name in enumerate(method_obj.arg_list):
            random_property_index = random.randrange(0, 100)

            real_var_name = ""
            if random_property_index < 50:
                # 需要随机属性
                random_property = get_random_property(class_obj_list)
                out_str += "\t" + random_property + " = @\"" + generate_words_str("random_str") + "\";\n"
                real_var_name = random_property
            else:
                real_var_name = "@\"" + generate_words_str("random_str") + "\""
            transfer_name += arg_name + ":"
            transfer_name += real_var_name
            
            if index != len(method_obj.arg_list) - 1:
                transfer_name += " "
    transfer_name += "];//" + copy.copy(class_obj.get_class_name())
    out_dic = {}
    out_dic["0"] = out_str
    out_dic["1"] = transfer_name
    # out_str += transfer_name
    
    return out_dic



# 写插入点的实现文件
def generate_insert_file(class_obj_list, target_directory_name):
    for class_obj in class_obj_list:

        class_name = copy.copy(class_obj.get_class_name())
        shared_name = copy.copy(class_obj.get_shared_method())
        property_list = copy.copy(class_obj.get_property_list())
        method_list = copy.copy(class_obj.get_method_list())

        method_type_list = []
        for i in range(len(method_list)):
            # 指定类型
            method_type = implamentation_type_mutablestring_data_tNSMutableData
            method_type_list.append(method_type)

        #生成指定类的.h文件内容
        header_str = header_of_file(class_name, shared_name, property_list, method_list, method_type_list)

        #生成指定类的.m文件内容
        implamentation_str = implamentation_of_file(class_name, shared_name, property_list, method_list, method_type_list, class_obj_list)

        #生成对应类的导入import信息
        import_str = import_for_class(class_name)

        #将上述的东西写进文件
        header_path = target_directory_name + class_name + ".h"
        implamentation_path = target_directory_name + class_name + ".m"
        # transfer_path = "alltransfer.txt"
        import_path = "allimport.txt"

        with open(header_path, "w") as input:
            input.write(header_str)
        
        with open(implamentation_path, "w") as input:
            input.write(implamentation_str)
        
        # with open(transfer_path, "a") as input:
        #     input.write(transfer_str)
        
        with open(import_path, "a") as input:
            input.write(import_str)


# 生成extern声明的全局变量
def generate_static_definition(class_obj_list):
    definition = ""
    giveValue = ""
    for index, class_obj in enumerate(class_obj_list):
        static_var = class_obj.get_static_var()
        class_name = class_obj.get_class_name()

        definition += class_name + " *" + static_var + ";\n"
        giveValue += static_var + " = [" + class_name + " " + class_obj.get_shared_method() + "];\n"
    definition_path = "static_definition.txt"
    giveValue_path = "static_giveValue.txt"

    with open(definition_path, "w") as input:
        input.write(definition)
    
    with open(giveValue_path, "w") as input:
        input.write(giveValue)


# 0823 生成uitableView和uitextfield的调用
def get_ui_0823_transfer(transfer_str, param_list):
    out_str = ""
    char_list = methodtransfer.count_str(":", transfer_str)
    if len(char_list):

        pieces_list = []
        prefix_str = ""
        for index, index_value in enumerate(char_list):
            if index == 0:
                prefix_str = transfer_str[0:index_value + 1]
            else:
                prefix_str = transfer_str[char_list[index-1]+1:index_value + 1]
            pieces_list.append(prefix_str)
        for index, piece in enumerate(pieces_list):
            if index == len(pieces_list) - 1:
                out_str += piece + param_list[index]
            else:
                out_str += piece + param_list[index] + " "
        # print("out_str " + out_str)
    else:
        out_str = transfer_str
    return out_str


# 0823版生成调用语句
def generate_0823_transfer(insert_class_list):
    '''
    insert_class_list:被插入的类列表
    '''
    random_insert_obj = insert_class_list[random.randrange(0, len(insert_class_list))]
    prototype_list = random_insert_obj.method_prototype_list
    
    prototype_obj = prototype_list[random.randrange(0, len(prototype_list))]
    return_type = prototype_obj.return_type
    transfer_name = prototype_obj.transfer_name

    out_str = "\t"
    # if "NSString" in return_type:
    #     #需要用到返回值
    #     random_var = generate_random_str(out_random_type_class)
    #     first_var = "@\"" + generate_words_str("random_str") + "\""
    #     param_list = [first_var]
    #     cf_str = "[" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
    #     out_str += cf_str

    # elif "UITableView" in return_type:
    #     #第一个参数是frame
    #     first_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
    #     second_var = "[UIColor " + generate_random_color() + "]"
    #     param_list = [first_var, second_var]
    #     tableview_str = "[" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
    #     out_str += tableview_str
        
    # elif "UITextField" in return_type:
    #     #第一个参数是frame
    #     first_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
    #     second_var = "[UIColor " + generate_random_color() + "]"
    #     param_list = [first_var, second_var]
    #     textfield_str = "[" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
    #     out_str += textfield_str
    # if "fdjgfjlfsdahiuwnei3834jhkfcxdsjoffsdjl" in transfer_name:
    #     #UICollectionView 有三个参数
    #     first_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
    #     second_var = "@\"" + generate_random_str(out_random_type_method_realize) + "\""
    #     third_var = "[UIColor " + generate_random_color() + "]"
    #     param_list = [first_var, second_var, third_var]
    #     collectionview_str = "[" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
    #     out_str += collectionview_str
    # elif "cellfdjkgfjijkel32duidsfjk8kefjsk" in transfer_name:
    #     #UICollectionViewCell
    #     first_var = "[UIColor " + generate_random_color() + "]"
    #     second_var = ""
    #     random_second = random.randrange(0, 100) % 2
    #     if random_second == 0:
    #         second_var = "YES"
    #     else:
    #         second_var = "NO"
    #     param_list = [first_var, second_var]
    #     collectionviewcell_str = "[" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
    #     out_str += collectionviewcell_str
    # elif "fjdkgrjkgfdykerijofp" in transfer_name:
    #     # NSString
    #     first_var = "@\"" + generate_random_str(out_random_type_method_realize) + "\""
    #     param_list = [first_var]
    #     random_var = generate_random_str(out_random_type_class)
    #     nsstring_str = "NSString * " + random_var + " = [" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
    #     out_str += nsstring_str
    #     out_str += "\tneed_handle_replace = " + random_var + ";"
    # elif "epqrhjfgdhksdfhjkruhfdjf" in transfer_name:
    #     # UILabel
    #     first_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
    #     second_var = "@\"" + generate_random_str(out_random_type_method_realize) + "\""
    #     param_list = [first_var, second_var]
    #     uilabel_str = "[" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
    #     out_str += uilabel_str
    # if "textFieldbingbong" in transfer_name:
    #     random_var = generate_random_str(out_random_type_class)
    #     first_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
    #     second_var = "@\"" + generate_random_str(out_random_type_method_realize) + "\""
    #     param_list = [first_var, second_var]
    #     UITextField_str = "UITextField *" + random_var + " = [" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
    #     out_str += UITextField_str
    #     out_str += "\t[Drstcxopvhropqbui shrjgkhuodfjo].jfdkgfjkl = " + random_var + ";\n"
    # elif "tableViewaeovdaiwilo" in transfer_name:
    #     random_var = generate_random_str(out_random_type_class)
    #     first_var = "@\"" + generate_random_str(out_random_type_method_realize) + "\""
    #     second_var = str(random.randrange(0, 100))
    #     param_list = [first_var, second_var]
    #     UITableView_str = "UITableView *" + random_var + " = [" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
    #     out_str += UITableView_str
    #     out_str += "\t[Drstcxopvhropqbui shrjgkhuodfjo].dfjkgjk = " + random_var + ";\n"
    # elif "imageimagefley" in transfer_name:
    #     random_var = generate_random_str(out_random_type_class)
    #     first_var = "@\"" + generate_random_str(out_random_type_method_realize) + "\""
    #     second_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
    #     param_list = [first_var, second_var]
    #     UITableView_str = "UIImage *" + random_var + " = [" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
    #     out_str += UITableView_str
    #     out_str += "\t[Drstcxopvhropqbui shrjgkhuodfjo].prkelj = " + random_var + ";\n"
    # elif "imageViewWuViewWu" in transfer_name:
    #     random_var = generate_random_str(out_random_type_class)
    #     first_var = "[UIImage imageNamed:@\"" + generate_random_str(out_random_type_method_realize) + "\"]"
    #     second_var = "@\"" + generate_random_str(out_random_type_method_realize) + "\""
    #     param_list = [first_var, second_var]
    #     UITableView_str = "UIImageView *" + random_var + " = [" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
    #     out_str += UITableView_str
    #     out_str += "\t[Drstcxopvhropqbui shrjgkhuodfjo].jvfkodgjf = " + random_var + ";\n"
    # elif "tableViewCelloavbiwe" in transfer_name:
    #     random_var = generate_random_str(out_random_type_class)
    #     first_var = "@\"" + generate_random_str(out_random_type_method_realize) + "\""
    #     param_list = [first_var]
    #     UITableView_str = "UITableViewCell *" + random_var + " = [" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
    #     out_str += UITableView_str
    #     out_str += "\t[Drstcxopvhropqbui shrjgkhuodfjo].fjklfg = " + random_var + ";\n"
    # elif "CFDataReflyvioaweruio" in transfer_name:
    #     first_var = str(random.randrange(0, 100))
    #     second_var = str(random.randrange(0, 100))
    #     random_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    #     random_index = random.randrange(0, len(random_char) - 1)
    #     third_var = "'" + random_char[random_index:random_index+1] + "'"
    #     fourth_var = "CFRangeMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 10)) + ")"
    #     param_list = [first_var, second_var, third_var, fourth_var]
    #     UITableView_str = "[" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
    #     out_str += UITableView_str
    
    if "jokfdtoolgjfiobarjkogfdsf" in transfer_name:
        #UIToolbar
        first_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        second_var = "@\"" + generate_random_str(out_random_type_method_realize) + "\""
        param_list = [first_var, second_var]
        random_var = generate_random_str(out_random_type_class)
        UITableView_str = "UIToolbar *" + random_var + " = [" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str

        # 后续处理
        for i in range(random.randrange(1, 3)):
            random_index = random.randrange(0, 4)
            if random_index == 0:
                out_str += "\t[" + random_var + " barTintColor];\n"
            elif random_index == 1:
                out_str += "\t[" + random_var + " barStyle];\n"
            elif random_index == 2:
                out_str += "\t[" + random_var + " tintColor];\n"
    elif "jdsiojgfogfjocell" in transfer_name:
        #UICollectionViewCell
        first_var = ""
        randomfdsf = random.randrange(0, 100) % 2
        if randomfdsf == 0:
            first_var = "YES"
        else:
            first_var = "NO"
        
        param_list = [first_var]
        random_var = generate_random_str(out_random_type_class)
        UITableView_str = "UICollectionViewCell *" + random_var + " = [" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
        # 后续处理
        for i in range(random.randrange(1, 4)):
            random_index = random.randrange(0, 4)
            if random_index == 0:
                out_str += "\t[" + random_var + " contentView];\n"
            elif random_index == 1:
                out_str += "\t[" + random_var + " isHighlighted];\n"
            elif random_index == 2:
                out_str += "\t[" + random_var + " isSelected];\n"
    elif "fdjofgjojojodjlhihewi" in transfer_name:
        #UITabBarController
        first_var = ""
        randomdfsfds = random.randrange(0, 50)
        first_var = str(randomdfsfds)
        
        param_list = [first_var]
        random_var = generate_random_str(out_random_type_class)
        UITableView_str = "UITabBarController *" + random_var + " = [" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
        # 后续处理
        for i in range(random.randrange(1, 3)):
            random_index = random.randrange(0, 4)
            if random_index == 0:
                out_str += "\t[" + random_var + " selectedIndex];\n"
            elif random_index == 1:
                out_str += "\t[" + random_var + " selectedViewController];\n"
            elif random_index == 2:
                out_str += "\t[" + random_var + " tabBar];\n"
    
    elif "joihiuofgjooiopehjfdhguihduisnkuzk" in transfer_name:
        #UITabBarItem
        first_var = "@\"" + generate_random_str(out_random_type_method_realize) + "\""
        second_var = "@\"" + generate_random_str(out_random_type_method_realize) + "\""
        third_var = "@\"" + generate_random_str(out_random_type_method_realize) + "\""
        
        param_list = [first_var, second_var, third_var]
        random_var = generate_random_str(out_random_type_class)
        UITableView_str = "UITabBarItem *" + random_var + " = [" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
        # 后续处理
        for i in range(random.randrange(1, 3)):
            random_index = random.randrange(0, 4)
            if random_index == 0:
                out_str += "\t[" + random_var + " selectedImage];\n"
            elif random_index == 1:
                out_str += "\t[" + random_var + " titlePositionAdjustment];\n"
            elif random_index == 2:
                out_str += "\t[" + random_var + " isEnabled];\n"
    
    elif "jdlgjodkfiojodifjoig" in transfer_name:
        #UIScrollView
        
        param_list = []
        random_var = generate_random_str(out_random_type_class)
        UITableView_str = "UIScrollView *" + random_var + " = [" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
        # 后续处理
        for i in range(random.randrange(1, 3)):
            random_index = random.randrange(0, 4)
            if random_index == 0:
                out_str += "\t[" + random_var + " canCancelContentTouches];\n"
            elif random_index == 1:
                out_str += "\t[" + random_var + " contentOffset];\n"
            elif random_index == 2:
                out_str += "\t[" + random_var + " isScrollEnabled];\n"
    elif "jdlgjodkfiojodifjoig" in transfer_name:
        #UIProgressView
        first_var = "@\"" + generate_random_str(out_random_type_method_realize) + "\""
        param_list = [first_var]
        random_var = generate_random_str(out_random_type_class)
        UITableView_str = "UIProgressView *" + random_var + " = [" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
        # 后续处理
        for i in range(random.randrange(1, 3)):
            random_index = random.randrange(0, 2)
            if random_index == 0:
                out_str += "\t[" + random_var + " progressImage];\n"
            elif random_index == 1:
                out_str += "\t[" + random_var + " observedProgress];\n"
    elif "jfodjojdsojoidjfo" in transfer_name:
        #UILabel
        first_var = ""
        random11 = random.randrange(0, 100) % 2
        if random11 == 0:
            first_var = "YES"
        else:
            first_var = "NO"

        second_var = "[UIColor " + generate_random_color() + "]"
        param_list = [first_var, second_var]
        random_var = generate_random_str(out_random_type_class)
        UITableView_str = "UILabel *" + random_var + " = [" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
        # 后续处理
        for i in range(random.randrange(1, 3)):
            random_index = random.randrange(0, 4)
            if random_index == 0:
                out_str += "\t[" + random_var + " font];\n"
            elif random_index == 1:
                out_str += "\t[" + random_var + " adjustsFontSizeToFitWidth];\n"
            elif random_index == 2:
                out_str += "\t[" + random_var + " attributedText];\n"
            elif random_index == 3:
                out_str += "\t[" + random_var + " isEnabled];\n"
    elif "fdjiogjfojojdojojfdjlgjfdljo" in transfer_name:
        #UIBarButtonItem
        param_list = []
        random_var = generate_random_str(out_random_type_class)
        UITableView_str = "UIBarButtonItem *" + random_var + " = [" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
        # 后续处理
        for i in range(random.randrange(1, 3)):
            random_index = random.randrange(0, 3)
            if random_index == 0:
                out_str += "\t[" + random_var + " buttonGroup];\n"
            elif random_index == 1:
                out_str += "\t[" + random_var + " customView];\n"
            elif random_index == 2:
                out_str += "\t[" + random_var + " width];\n"
            
    elif "fjojgojodfjlkgdjorkjelrmlgldfdd" in transfer_name:
        #UINavigationController
        first_var = "YES"
        if random.randrange(0, 100) % 2 == 0:
            first_var = "NO"
        param_list = [first_var]
        random_var = generate_random_str(out_random_type_class)
        UITableView_str = "UINavigationController *" + random_var + " = [" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
        # 后续处理
        for i in range(random.randrange(1, 3)):
            random_index = random.randrange(0, 4)
            if random_index == 0:
                out_str += "\t[" + random_var + " hidesBarsOnSwipe];\n"
            elif random_index == 1:
                out_str += "\t[" + random_var + " hidesBarsOnTap];\n"
            elif random_index == 2:
                out_str += "\t[" + random_var + " barHideOnTapGestureRecognizer];\n"
            elif random_index == 3:
                out_str += "\t[" + random_var + " topViewController];\n"
    
    elif "jdiogjiofjasdjojresokjfdo" in transfer_name:
        #UIButton
        first_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        second_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        param_list = [first_var, second_var]
        random_var = generate_random_str(out_random_type_class)
        UITableView_str = "UIButton *" + random_var + " = [" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
        # 后续处理
        for i in range(random.randrange(1, 3)):
            random_index = random.randrange(0, 3)
            if random_index == 0:
                out_str += "\t[" + random_var + " buttonType];\n"
            elif random_index == 1:
                out_str += "\t[" + random_var + " adjustsImageWhenDisabled];\n"
            elif random_index == 2:
                out_str += "\t[" + random_var + " currentImage];\n"
    elif "jopfjkdoigofdjdlidfdsgf" in transfer_name:
        #UISwitch
        # first_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        # second_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        param_list = []
        random_var = generate_random_str(out_random_type_class)
        UITableView_str = "UISwitch *" + random_var + " = [" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
        # 后续处理
        for i in range(random.randrange(1, 3)):
            random_index = random.randrange(0, 2)
            if random_index == 0:
                out_str += "\t[" + random_var + " tintColor];\n"
            elif random_index == 1:
                out_str += "\t[" + random_var + " offImage];\n"
    elif "dfjiofgojosajkofgwoiuejf" in transfer_name:
        #UITouch
        # first_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        # second_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        param_list = []
        random_var = generate_random_str(out_random_type_class)
        UITableView_str = "UITouch *" + random_var + " = [" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
        # 后续处理
        for i in range(random.randrange(1, 3)):
            random_index = random.randrange(0, 2)
            if random_index == 0:
                out_str += "\t[" + random_var + " phase];\n"
            elif random_index == 1:
                out_str += "\t[" + random_var + " window];\n"
    elif "udofisjowjeioujefgudogjfiojsoijfiojdso" in transfer_name:
        #UISlider
        first_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        # second_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        param_list = [first_var]
        random_var = generate_random_str(out_random_type_class)
        UITableView_str = "UISlider *" + random_var + " = [" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
        # 后续处理
        for i in range(random.randrange(1, 3)):
            random_index = random.randrange(0, 3)
            if random_index == 0:
                out_str += "\t[" + random_var + " isContinuous];\n"
            elif random_index == 1:
                out_str += "\t[" + random_var + " currentThumbImage];\n"
            elif random_index == 2:
                out_str += "\t[" + random_var + " maximumValue];\n"
    
    elif "djiojfgojljljgrtgj9ii" in transfer_name:
        #UIPress
        # first_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        # second_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        param_list = []
        random_var = generate_random_str(out_random_type_class)
        UITableView_str = "UIPress *" + random_var + " = [" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
        # 后续处理
        for i in range(random.randrange(1, 3)):
            random_index = random.randrange(0, 3)
            if random_index == 0:
                out_str += "\t[" + random_var + " phase];\n"
            elif random_index == 1:
                out_str += "\t[" + random_var + " gestureRecognizers];\n"
            elif random_index == 2:
                out_str += "\t[" + random_var + " responder];\n"
    elif "jiofdjgiofjiojdfiojdkjor" in transfer_name:
        #CFSet
        # first_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        # second_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        param_list = []
        # random_var = generate_random_str(out_random_type_class)
        UITableView_str = "[" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
    
    elif "jdifojgiojdoijoiojdso" in transfer_name:
        #CFData
        # first_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        # second_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        param_list = []
        # random_var = generate_random_str(out_random_type_class)
        UITableView_str = "[" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
    elif "fudiofjmgrdfjgiojero2jofdi" in transfer_name:
        #CFData
        # first_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        # second_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        param_list = []
        # random_var = generate_random_str(out_random_type_class)
        UITableView_str = "[" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
    elif "djiojrofjgoiduihioajudih23dfds" in transfer_name:
        #CFData
        # first_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        # second_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        param_list = []
        # random_var = generate_random_str(out_random_type_class)
        UITableView_str = "[" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
    elif "dfjiodjhi2rfiodsjfioudjo" in transfer_name:
        #CFData
        # first_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        # second_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        param_list = []
        # random_var = generate_random_str(out_random_type_class)
        UITableView_str = "[" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
    elif "djioij23fhgiujioujf" in transfer_name:
        #CFData
        # first_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        # second_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        param_list = []
        # random_var = generate_random_str(out_random_type_class)
        UITableView_str = "[" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
    elif "djfo32jfidogjdfiojofd" in transfer_name:
        #CFData
        first_var = "@\"" + generate_random_str(out_random_type_method_realize) + "\""
        # second_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        param_list = [first_var]
        # random_var = generate_random_str(out_random_type_class)
        UITableView_str = "[" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
    elif "jo23jdfojsijio95fgdgiod" in transfer_name:
        #CFData
        # first_var = "@\"" + generate_random_str(out_random_type_method_realize) + "\""
        # second_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        param_list = []
        # random_var = generate_random_str(out_random_type_class)
        UITableView_str = "[" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
    elif "fdfd2fjigo7gtkjgdiol" in transfer_name:
        #CFData
        # first_var = "@\"" + generate_random_str(out_random_type_method_realize) + "\""
        # second_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        param_list = []
        # random_var = generate_random_str(out_random_type_class)
        UITableView_str = "[" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
    elif "fdji9fgjjgifodhiojdo" in transfer_name:
        #CFData
        # first_var = "@\"" + generate_random_str(out_random_type_method_realize) + "\""
        # second_var = "CGRectMake(" + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ", " + str(random.randrange(0, 100)) + ")"
        param_list = []
        # random_var = generate_random_str(out_random_type_class)
        UITableView_str = "[" + random_insert_obj.class_name + " " + get_ui_0823_transfer(transfer_name, param_list) + "];\n"
        out_str += UITableView_str
        


    return out_str


# 0823版替换插入点
def replace_insert_0823(target_file_list, insert_class_list):
    '''
    0823版替换插入点，只需要替换调用，没有后续处理
        target_file_list:目标文件列表
        insert_class_list:插入点类列表
    '''
    for file in target_file_list:
        file_context = []
        with open(file, "r+") as input:
            file_context = input.readlines()
        if len(file_context) > 0:
            file_replace_context = []
            for line in file_context:
                if "//////insert//" in line:
                    need_replace_str = ""
                    # 生成替换语句
                    need_replace_str = generate_0823_transfer(insert_class_list)
                    replace_line = line.replace("//////insert//", need_replace_str)
                    file_replace_context.append(replace_line)
                else:
                    file_replace_context.append(line)
            with open(file, "w") as input:
                input.writelines(file_replace_context)

# 替换目标文件中的插入点标记
def replace_insert(target_file_list, insert_class_list, target_probability):
    '''
    param:
        target_file_list:目标文件列表
        insert_class_list:被选用的插入类文件列表
        target_probability:插入点函数生成规则中的百分比(0~100),比例越大，生成新的实现的概率越大，使用旧的实现的概率越小，反之则反
    '''
    for file in target_file_list:

        file_context = []
        with open(file, "r+") as input:
            file_context = input.readlines()
        if len(file_context) > 0:
            file_replace_context = []
            for line in file_context:
                if "//////insert//" in line:
                    need_replace_str = ""
                    # 50%的概率取调用插入函数，50%的概率不调用函数直接初始化
                    random_num = random.randrange(0, 50)
                    random_var = generate_random_str(out_random_type_class)
                    if random_num > 50:
                        # 50%的概率取调用插入函数
                        #随机取一个调用，插入
                        class_obj = insert_class_list[random.randrange(0, len(insert_class_list))]
                        prefix_str = "\textern " + class_obj.get_class_name() + " *" + class_obj.get_static_var() + ";\n"
                        # transfer_str = generate_fifth_transfer(class_obj, target_probability, insert_class_list)
                        transfer_dic = generate_fifth_transfer(class_obj, target_probability, insert_class_list)
                        need_replace_str = prefix_str + transfer_dic["0"] + "NSMutableAttributedString *" + random_var + " = " + transfer_dic["1"] + "\n"
                    else:
                        # 50%的概率不调用函数直接初始化
                        need_replace_str = "\tNSMutableString *" + random_var + " = [NSMutableString stringWithString:@\"" + generate_words_str("random_str") + "\"];\n"
                    
                    # need_replace_str += generate_handle_string_data(random_var)
                    need_replace_str += generate_handle_mutablestring_data_tMutablestring(random_var, insert_class_list)

                    replace_line = line.replace("//////insert//", need_replace_str)
                    file_replace_context.append(replace_line)
                else:
                    file_replace_context.append(line)
            with open(file, "w") as input:
                input.writelines(file_replace_context)

# 处理NSMutableAttributedString0817调用
def generate_handle_NSMutableAttributedString0817(param_str, class_obj_list):
    out_str = ""
    for i in range(random.randrange(6, 30)):
        random_insert = random.randrange(0, 5)
        range1 = generate_random_str(out_random_type_method_init)
        if random_insert == 0:
            if random.randrange(0, 100) < 5:
                random_property = get_random_property(class_obj_list)
                out_str += "\t" + random_property + " = @\"" + generate_words_str("random_str") + "\";\n"
                out_str += "\t[" + param_str + " deleteCharactersInRange:NSRangeFromString(" + random_property  + ")];\n"
            out_str += "\tNSRange " + range1 + " = NSRangeFromString(@\"" + generate_words_str("random_str") + "\");\n"
            out_str += "\t[" + param_str + " endEditing];\n"
        if random_insert == 1:
            out_str += "\t[" + param_str + " isKindOfClass:[NSMutableAttributedString class]];\n"
        if random_insert == 2:
            out_str += "\t[" + param_str + " isMemberOfClass:[NSMutableAttributedString class]];\n"
        if random_insert == 3:
            out_str += "\t[" + param_str + " isEqual:@\"" + generate_words_str("random_str") + "\"];\n"
        if random_insert == 4:
            out_str += "\t[" + param_str + " isEqualToAttributedString:[[NSAttributedString alloc]initWithString:@\"" + generate_words_str("random_str") + "\"]];\n"
    return out_str

# 查找插入点实现函数中的insert标记并替换
def find_insert_and_replace_second(class_obj_list):
    need_replace_file_list = get_search_files("already", [".m", ".mm"], nosearch_directorys)
    #替换插入点标记
    replace_insert(need_replace_file_list, class_obj_list, -1)


# 查找所有的insert标记
def find_insert_and_replace(class_obj_list):

    # static_instance_list = get_static_list(class_obj_list)
    # 生成extern声明的全局变量
    # generate_static_definition(class_obj_list)

    need_replace_file_list = get_search_files("target", [".m", ".mm"], nosearch_directorys)
    #替换插入点标记
    replace_insert(need_replace_file_list, class_obj_list, 90)

    # 替换完成之后需要写插入点的实现文件
    generate_insert_file(class_obj_list, "already/")

# 第四版插入点
def handle_replace_fourth_insert():
    print("第四版替换插入点")

    #生成随机的30~50个类的list
    insert_class_list = []
    random_class_length = random.randrange(30, 50)
    for i in range(random_class_length):
        class_name = generate_words_str("property")
        random_shared = generate_words_str("func")

        #随机生成0~10个属性
        property_list = []
        random_property_count = random.randrange(0, 15)
        for property_index in range(random_property_count):
            property_name = generate_words_str("property")
            property_list.append(property_name)

        static_var = generate_random_str(out_random_type_class)
        class_obj = inserthandler.ClassObject(class_name, property_list, static_var, random_shared, [])
        insert_class_list.append(class_obj)

    #查找所有的insert标记
    find_insert_and_replace(insert_class_list)

    # # 查找并替换插入点实现函数中的标记，使支持插入函数嵌套
    find_insert_and_replace_second(insert_class_list)


# 工具添加混淆类第三版
def handle_replace_insert():
    print("第三版替换插入点")

    # 生成随机类
    # generate_random_files()

    need_replace_file_list = get_search_files("target", [".m", ".mm"], nosearch_directorys)
    # 替换
    # transfer_content = []
    # with open("alltransfer.txt", "r") as input:
    #     transfer_content = input.readlines()
    
    # transfer_length = len(transfer_content)
    # print("transfer_length :" + str(transfer_length))

    for file in need_replace_file_list:

        file_context = []
        with open(file, "r+") as input:
            file_context = input.readlines()
        if len(file_context) > 0:
            file_replace_context = []
            for line in file_context:
                if "//////insert//" in line:
                    #随机取一个调用，插入
                    # transfer_str = transfer_content[random.randrange(0, transfer_length)].replace("\n", "")
                    need_replace_str = ""
                    # need_replace_str = "NSMutableString *" + random_var + " = " + transfer_str + "\n"
                    # need_replace_str += generate_handle_string_data(random_var)
                    # need_replace_str += handle_transfer_defend_Garden()
                    need_replace_str = generate_handle_0303_NSLayoutConstraint_NSLayoutManager()

                    replace_line = line.replace("//////insert//", need_replace_str)
                    file_replace_context.append(replace_line)
                else:
                    file_replace_context.append(line)
            with open(file, "w") as input:
                input.writelines(file_replace_context)


# 查找函数的实现
def findimplamentation(target_method, filter_str):
    out_str = ""
    if len(filter_str) <= 0:
        print("filter str is null,please check")
        return out_str
    if len(target_method) <= 0:
        print("target_method is null , please check")
        return out_str
    
    if target_method not in filter_str:
        return out_str

    sub_str = filter_str.split(target_method)[1]
    stack = 0
    first_char = 1
    for item_char in sub_str:
        
        out_str += item_char
        if item_char != "{" and item_char != "}":
            continue
        elif item_char == "{":
            stack += 1
            first_char = 0
            continue
        elif item_char == "}":
            stack -= 1
        if first_char == 0 and stack == 0:
            break
    return out_str
        


def showhelp():
    print("请输入3个参数, 第一个参数是当前脚本名称，第二个参数是导出路径，第三个参数是导出数量")

# # 处理参数
# def handleargv():
# 	# print("当前输入参数为:" + str(sys.argv))

# 	if len(sys.argv) == 1:
# 		# 打印命令
# 		showhelp()
# 	elif len(sys.argv) == 2:
# 		if int(sys.argv[1]) == 1:
# 			occlass_confuse()
# 		elif int(sys.argv[1]) == 2:
#             print("参数个数不足")
#         elif int(sys.argv[1]) == :
#             pass

# 1030版本 处理包含CGRectMake的UI微调
def handle_CGRectMake_1030(target_str):
    # 如果一行中有两个CGRectMake默认处理第一个，第二个不处理
    matches = []
    for match_item in oc_CGRectMake_rule.finditer(target_str):
        matches.append(match_item)
    if len(matches) <= 0:
        return target_str
    match = matches[0]
    s = match.start()
    e = match.end()
    result = target_str[s:e]
    print("CGRectMake:%s" % result)
    prefix = target_str[0:s]
    suffix = target_str[e:]

    out_str = prefix
    first_param = oc_CGRectMake_param1_rule.findall(target_str)[0]
    second_param = oc_CGRectMake_param2_rule.findall(target_str)[0]
    third_param = oc_CGRectMake_param3_rule.findall(target_str)[0]
    fourth_param = oc_CGRectMake_param4_rule.findall(target_str)[0]

    first_param += "+ " + str(random.uniform(-0.1, 0.1))
    second_param += "+ " + str(random.uniform(-0.1, 0.1))
    third_param += "+ " + str(random.uniform(-0.1, 0.1))
    fourth_param += "+ " + str(random.uniform(-0.1, 0.1))

    middle_str = "CGRectMake(" + first_param + ", " + second_param + ", " + third_param + ", " + fourth_param + ")"
    out_str += middle_str

    out_str += suffix
    print("CGRectMake out:%s" % out_str)

    return out_str

# 1030版本 处理包含CGSizeMake的UI微调
def handle_CGSizeMake_1030(target_str):
    # 如果一行中有两个CGSizeMake默认处理第一个，第二个不处理
    matches = []
    for match_item in oc_CGSizeMake_rule.finditer(target_str):
        matches.append(match_item)
    if len(matches) <= 0:
        return target_str
    match = matches[0]
    s = match.start()
    e = match.end()
    result = target_str[s:e]
    print("CGSizeMake:%s" % result)
    prefix = target_str[0:s]
    suffix = target_str[e:]

    out_str = prefix
    first_param = oc_CGSizeMake_param1_rule.findall(target_str)[0]
    second_param = oc_CGSizeMake_param2_rule.findall(target_str)[0]

    first_param += "+ " + str(random.uniform(-0.1, 0.1))
    second_param += "+ " + str(random.uniform(-0.1, 0.1))

    middle_str = "CGSizeMake(" + first_param + ", " + second_param + ")"
    out_str += middle_str

    out_str += suffix
    print("CGSizeMake out:%s" % out_str)

    return out_str

# 1030版本 处理包含CGPointMake的UI微调
def handle_CGPointMake_1030(target_str):
    # 如果一行中有两个CGSizeMake默认处理第一个，第二个不处理
    matches = []
    for match_item in oc_CGPointMake_rule.finditer(target_str):
        matches.append(match_item)
    if len(matches) <= 0:
        return target_str
    match = matches[0]
    s = match.start()
    e = match.end()
    result = target_str[s:e]
    print("CGPointMake:%s" % result)
    prefix = target_str[0:s]
    suffix = target_str[e:]

    out_str = prefix
    first_param = oc_CGPointMake_param1_rule.findall(target_str)[0]
    second_param = oc_CGPointMake_param2_rule.findall(target_str)[0]

    first_param += "+ " + str(random.uniform(-0.1, 0.1))
    second_param += "+ " + str(random.uniform(-0.1, 0.1))

    middle_str = "CGPointMake(" + first_param + ", " + second_param + ")"
    out_str += middle_str

    out_str += suffix
    print("CGPointMake out:%s" % out_str)

    return out_str

# 1030版本 处理包含UIColor colorWithRed的UI微调
def handle_UIColor_colorWithRed_1030(target_str):
    
    # 如果一行中有两个CGRectMake默认处理第一个，第二个不处理
    matches = []
    for match_item in oc_UIColor_colorWithRed_rule.finditer(target_str):
        matches.append(match_item)
    if len(matches) <= 0:
        return target_str
    match = matches[0]
    s = match.start()
    e = match.end()
    result = target_str[s:e]
    print("UIColor_col:%s" % result)
    prefix = target_str[0:s]
    suffix = target_str[e:]

    out_str = prefix
    first_param = oc_UIColor_colorWithRed_param1_rule.findall(target_str)[0]
    second_param = oc_UIColor_colorWithRed_param2_rule.findall(target_str)[0]
    third_param = oc_UIColor_colorWithRed_param3_rule.findall(target_str)[0]
    fourth_param = oc_UIColor_colorWithRed_param4_rule.findall(target_str)[0]

    first_param += "+ " + str(random.uniform(-0.1, 0.1))
    second_param += "+ " + str(random.uniform(-0.1, 0.1))
    third_param += "+ " + str(random.uniform(-0.1, 0.1))
    fourth_param += "+ " + str(random.uniform(-0.001, 0.001))

    middle_str = "[UIColor colorWithRed:" + first_param + " green:" + second_param + " blue:" + third_param + " alpha:" + fourth_param + "]"
    out_str += middle_str

    out_str += suffix
    print("UIColor_col out:%s" % out_str)

    return out_str

# 1030版本 判断当前行是否包含CGRectMake字段
def contains_CGRectMake_1030(target_str):
    contains = False
    if "CGRectMake" in target_str:
        contains = True
    return contains

# 1030版本 判断当前行是否包含CGSizeMake字段
def contains_CGSizeMake_1030(target_str):
    contains = False
    if "CGSizeMake" in target_str:
        contains = True
    return contains

# 1030版本 判断当前行是否包含CGPointMake字段
def contains_CGPointMake_1030(target_str):
    contains = False
    if "CGPointMake" in target_str:
        contains = True
    return contains

# 1008版本 判断实现是否包含addSubview:字段
def contains_addSubview_1008(target_str):
    contains = False
    if " addSubview:" in target_str:
        contains = True
    return contains

# 1008版本 判断实现是否包含UIColor colorWithRed字段
def contains_UIColor_colorWithRed_1030(target_str):
    contains = False
    if "UIColor colorWithRed:" in target_str:
        contains = True
    return contains


# 判断字符串中是否包含0905版插入点对应的处理字符类型
def contains_0905_insert_type(target_str):
    contains = False
    for insert_type in global_0905insert_type_handle_list:
        if insert_type in target_str:
            contains = True
            return contains
    return contains

# 判断字符串中包含0905版插入点的哪一个插入点
def insert_0905_type_from_str(target_str):
    out_str = ""
    for insert_type in global_0905insert_type_handle_list:
        if insert_type in target_str:
            out_str = insert_type
    return out_str

# 获取插入点类型中的变量类型
def get_var_type(insert_0905_type):
    var_type = ""
    if insert_0905_type == global_0905insert_type_longlong:
        var_type = "longlong"
    elif insert_0905_type == global_0905insert_type_NSString:
        var_type = "NSString*"
    elif insert_0905_type == global_0905insert_type_double:
        var_type = "double"
    elif insert_0905_type == global_0905insert_type_NSArray:
        var_type = "NSArray*"
    return var_type

# 1008版本 获取对应行的目标UI变量
def get_1008_target_ui(target_line):
    var_name = ""
    target_line = target_line.strip().replace(" ", "")
    addSubview_index = target_line.find("addSubview:")
    if addSubview_index == -1:
        # 未找到匹配项
        return var_name
    # 已找到匹配项
    var_name = oc_find_target_ui_varname_rule.findall(target_line)[0]

    return var_name


# 获取对应行的变量名
def get_0905_varname(target_line, insert_0905_type):
    var_name = ""
    var_type = get_var_type(insert_0905_type)

    target_line = target_line.strip().replace(" ", "")
    target_var_index = len(var_type)
    equal_symble_index = 0
    for index, char_str in enumerate(target_line):
        if char_str == "=":
            equal_symble_index = index
            break
    var_name = target_line[target_var_index:equal_symble_index]
    return var_name

# 获取0912版本对应插入类型的还原类
def get_insert_0912_reduction_class_obj(use_insert_class_list, insert_0905_type):
    class_name = ""
    if insert_0905_type == global_0905insert_type_longlong:
        class_name = "Tjkdsjfl0912djkReductionLo"
    elif insert_0905_type == global_0905insert_type_NSString:
        class_name = "Tdjfk0912jgfkReductionSt"
    elif insert_0905_type == global_0905insert_type_double:
        class_name = "Tdjfko0912FDjReductionDob"
    elif insert_0905_type == global_0905insert_type_NSArray:
        class_name = "Tdjfkf0912jkdfReductionAr"
    for insert_class_obj in use_insert_class_list:
        if insert_class_obj.class_name == class_name:
            return insert_class_obj
    return None

# 获取0926版本对应插入类型的处理类
def get_insert_0926_prototype(use_insert_class_list, insert_0905_type, insert_function_type):

    # 返回字典包含两个字段，一个是类名，一个是函数原型
    out_dic = {}
    insert_type = 0
    #80%的比例调用功能性函数的插入点，20%的比例调用正常函数，如果功能性函数找不到，就默认走正常函数
    random_num = random.randrange(0, 100)
    if random_num > 20:
        insert_type = global_0926insert_type_data
    else:
        insert_type = global_0926insert_type_feature
    
    # class_name = ""
    if insert_type == global_0926insert_type_data:
        #如果是要数据处理类的插入点函数
        class_name = "DDMNouldeMadBVdsm"
    else:
        if insert_0905_type == global_0905insert_type_NSArray:
            class_name = "DDMNouldeMadBVdsm"
        elif insert_0905_type == global_0905insert_type_NSString:
            class_name = "DDMNouldeMadBVdsm"
        elif insert_0905_type == global_0905insert_type_double:
            class_name = "DDMNouldeMadBVdsm"
        elif insert_0905_type == global_0905insert_type_longlong:
            class_name = "DDMNouldeMadBVdsm"
        else:
            class_name = "DDMNouldeMadBVdsm"
    
    # insert_class_obj = None

    for class_obj in use_insert_class_list:
        if class_obj.class_name == class_name:
            insert_class_obj = class_obj
    
    insert_prototype_list = insert_class_obj.prototype_list
    for prototype_obj in insert_prototype_list:
        
        if insert_function_type == global_0926insert_function_type_handle:
            # 处理
            if insert_0905_type == global_0905insert_type_NSArray:
                if "" in prototype_obj.transfer_name or "" in prototype_obj.transfer_name:
                    out_dic["class_name"] = ""
                    out_dic["prototype"] = prototype_obj
                    return out_dic
            elif insert_0905_type == global_0905insert_type_NSString:
                if "" in prototype_obj.transfer_name or "" in prototype_obj.transfer_name:
                    out_dic["class_name"] = ""
                    out_dic["prototype"] = prototype_obj
                    return out_dic
            elif insert_0905_type == global_0905insert_type_double:
                if "" in prototype_obj.transfer_name or "" in prototype_obj.transfer_name:
                    out_dic["class_name"] = ""
                    out_dic["prototype"] = prototype_obj
                    return out_dic
            elif insert_0905_type == global_0905insert_type_longlong:
                if "" in prototype_obj.transfer_name or "" in prototype_obj.transfer_name:
                    out_dic["class_name"] = ""
                    out_dic["prototype"] = prototype_obj
                    return out_dic
        else:
            # 还原
            if insert_0905_type == global_0905insert_type_NSArray:
                if "" in prototype_obj.transfer_name or "" in prototype_obj.transfer_name:
                    out_dic["class_name"] = ""
                    out_dic["prototype"] = prototype_obj
                    return out_dic
            elif insert_0905_type == global_0905insert_type_NSString:
                if "" in prototype_obj.transfer_name or "" in prototype_obj.transfer_name:
                    out_dic["class_name"] = ""
                    out_dic["prototype"] = prototype_obj
                    return out_dic
            elif insert_0905_type == global_0905insert_type_double:
                if "" in prototype_obj.transfer_name or "" in prototype_obj.transfer_name:
                    out_dic["class_name"] = ""
                    out_dic["prototype"] = prototype_obj
                    return out_dic
            elif insert_0905_type == global_0905insert_type_longlong:
                if "" in prototype_obj.transfer_name or "" in prototype_obj.transfer_name:
                    out_dic["class_name"] = ""
                    out_dic["prototype"] = prototype_obj
                    return out_dic
    
    return None




# 获取0924版本对应插入类型的处理类
def get_insert_0924_handle_class_obj(use_insert_class_list, insert_0905_type):
    class_name = ""
    if insert_0905_type == global_0905insert_type_NSArray:
        class_name = ""
    elif insert_0905_type == global_0905insert_type_NSString:
        class_name = ""
    elif insert_0905_type == global_0905insert_type_longlong:
        class_name = ""
    else:
        class_name = ""
    for insert_class_obj in use_insert_class_list:
        if class_name in insert_class_obj.class_name:
            return insert_class_obj

# 获取0919版本对应插入类型的处理类
def get_insert_0919_handle_class_obj(use_insert_class_list, insert_0905_type):
    class_name = "NowehniovMendnvion"
    for insert_class_obj in use_insert_class_list:
        if class_name in insert_class_obj.class_name:
            return insert_class_obj
    return None


# 获取0912版本对应插入类型的处理类
def get_insert_0912_handle_class_obj(use_insert_class_list, insert_0905_type):
    class_name = ""
    if insert_0905_type == global_0905insert_type_double:
        class_name = "NowehniovMendnvionTYs5ugt"

    elif insert_0905_type == global_0905insert_type_longlong:
        class_name = "NowehniovMendnvionYsg4dfu"

    elif insert_0905_type == global_0905insert_type_NSString:
        class_name = "NowehniovMendnvionKshdgh2jwe"    

    elif insert_0905_type == global_0905insert_type_NSArray:
        class_name = "NowehniovMendnvionKstd6hstd"

    for insert_class_obj in use_insert_class_list:
        if insert_class_obj.class_name == class_name:
            return insert_class_obj
    return None



# 获取0905版本对应插入类型的类
def get_insert_0905_class_obj(use_insert_class_list, insert_0905_type):
    class_name = ""
    if insert_0905_type == global_0905insert_type_double:
        class_name = "NowehniovMendnvionTixzvnpwe"

    elif insert_0905_type == global_0905insert_type_longlong:
        class_name = "NowehniovMendnvionFixnvmwpek"

    elif insert_0905_type == global_0905insert_type_NSString:
        class_name = "NowehniovMendnvionNwohgnpwet"

    elif insert_0905_type == global_0905insert_type_NSArray:
        class_name = "NowehniovMendnvionDiwoehgnpie"

    for insert_class_obj in use_insert_class_list:
        if insert_class_obj.class_name == class_name:
            return insert_class_obj
    return None

# 根据参数类型构造参数字符串
def generate_0905_param_str(param_type):
    out_str = ""
    if "NSString *" in param_type:
        out_str = "@\"" + generate_words_str("random_str") + "\""
    elif "CGRect" in param_type:
        out_str = "CGRectMake(" + str(random.randrange(115, 235)) + ", " + str(random.randrange(0, 200)) + ", " + str(random.randrange(0, 50)) + ", " + str(random.randrange(0, 60)) + ")"
    elif "CGPoint" in param_type:
        out_str = "CGPointMake(" + str(random.randrange(0, 50)) + ", " + str(random.randrange(0, 60)) + ")"
    elif "CGSize" in param_type:
        out_str = "CGSizeMake(" + str(random.randrange(0, 15)) + ", " + str(random.randrange(2, 15)) + ")"        
    elif "int" in param_type or "NSInteger" in param_type:
        out_str = str(random.randrange(0, 25))
    elif "NSUInteger" in param_type or "unsigned long" in param_type:
        out_str = str(random.randrange(0, 20))
    elif "UIColor *" in param_type:
        out_str = "[UIColor " + generate_random_color() + "]"
    elif "UIFont *" in param_type:
        random_index = random.randrange(0,100)%3
        if random_index == 0:
            out_str = "[UIFont systemFontOfSize:" + str(random.randrange(12, 20)) + "]"                    
        elif random_index == 1:
            out_str = "[UIFont boldSystemFontOfSize:" + str(random.randrange(12, 20)) + "]"        
        elif random_index == 2:
            out_str = "[UIFont italicSystemFontOfSize:" + str(random.randrange(12, 20)) + "]"        
        else:
            out_str = "[UIFont systemFontOfSize:" + str(random.randrange(12, 20)) + "]"        
    elif "NSURL *" in param_type:
        out_str = "[NSURL URLWithString:@\"" + generate_words_str("random_str") + "\"]"
    elif "BOOL" in param_type:
        bool_str = "NO"
        if random.randrange(0, 100) % 2 == 0:
            bool_str = "YES"
        out_str = bool_str
    elif "CGFloat" in param_type:
        out_str = "0.00" + str(random.randrange(0, 100))
    elif "float" in param_type:
        out_str = "0.00" + str(random.randrange(0, 100))
    elif "double" in param_type:
        out_str = "0.00" + str(random.randrange(0, 100))
    elif "NSArray *" in param_type:
        random_depth = random.randrange(1, 6)
        out_str = "@["
        for i in range(random_depth):
            out_str += generate_0905_param_str("NSString *")
            if i != random_depth - 1:
                out_str += ", "
        out_str += "]"

    return out_str

# 根据函数返回值类型添加不同的后续处理
def handle_transfer_0912_letter(return_type, target_var_name):
    out_str = ""
    if "NSArray *" == return_type:
        random_num = random.randrange(0, 5)
        if random_num == 0:
            out_str += "\t[" + target_var_name + " count];\n"
        elif random_num == 1:
            out_str += "\t[" + target_var_name + " description];\n"
        elif random_num == 2:
            out_str += "\t[" + target_var_name + " firstObject];\n"
        elif random_num == 3:
            out_str += "\t[" + target_var_name + " lastObject];\n"
        elif random_num == 4:
            out_str += "\t[" + target_var_name + " objectEnumerator];\n"
    elif "NSString *" == return_type:
        random_num = random.randrange(0, 5)
        if random_num == 0:
            out_str += "\t[" + target_var_name + " length];\n"
        elif random_num == 1:
            out_str += "\t[" + target_var_name + " doubleValue];\n"
        elif random_num == 2:
            out_str += "\t[" + target_var_name + " uppercaseString];\n"
        elif random_num == 3:
            out_str += "\t[" + target_var_name + " intValue];\n"
        elif random_num == 4:
            out_str += "\t[" + target_var_name + " longLongValue];\n"
    elif "double" == return_type:
        pass
    elif "long long" == return_type:
        pass
    return out_str

# 处理1008版本ui函数调用
def handle_1008_uifunctions_transfer(prototype_obj, class_name):
    out_str = "["
    #处理
    out_str += class_name + " "
    transfer_str = prototype_obj.transfer_name
    # 获取参数个数
    char_list = methodtransfer.count_str(":", transfer_str)
    if len(char_list):
        #切片
        pieces_list = []
        prefix_str = ""
        param_list = prototype_obj.parampair_list
        for index, index_value in enumerate(char_list):
            if index == 0:
                prefix_str = transfer_str[0:index_value + 1]
            else:
                prefix_str = transfer_str[char_list[index-1]+1:index_value + 1]
            pieces_list.append(prefix_str)
        for index, piece in enumerate(pieces_list):
            if index == len(pieces_list) - 1:
                out_str += piece + generate_0905_param_str(param_list[index].param_type)
            else:
                out_str += piece + generate_0905_param_str(param_list[index].param_type) + " "
        # print("out_str " + out_str)
    else:
        out_str += transfer_str

    out_str += "];//in1008_handle_ui\n"
    return out_str


# 0304版处理还原 根据函数原型组装成C函数调用
def handle_transfer_c_0304(prototype_obj, first_var_name, class_name):
    '''
    0304版本组装函数调用，至少有一个参数，第一个参数是关联参数 C函数调用
    '''
    # out_str = "["
    out_str = ""
    
    #处理
    # out_str += class_name + " "
    transfer_str = prototype_obj.transfer_name

    #0305添加
    out_str += transfer_str.replace(":", "") + "("

    # 获取参数个数
    char_list = methodtransfer.count_str(":", transfer_str)
    if len(char_list):
        #切片
        pieces_list = []
        prefix_str = ""
        param_list = prototype_obj.parampair_list
        for index, index_value in enumerate(char_list):
            if index == 0:
                prefix_str = transfer_str[0:index_value + 1]
            else:
                prefix_str = transfer_str[char_list[index-1]+1:index_value + 1]
            pieces_list.append(prefix_str)
        for index, piece in enumerate(pieces_list):
            if index == 0:
                first_param_type = param_list[index].param_type
                first_var_str = ""
                if first_param_type == "double":
                    first_var_str = first_var_name
                if first_param_type == "double *":
                    first_var_str = "&" + first_var_name
                elif first_param_type == "NSArray **":
                    first_var_str = "&" + first_var_name
                elif first_param_type == "NSArray *":
                    first_var_str = first_var_name
                elif first_param_type == "long long *":
                    first_var_str = "&" + first_var_name
                elif first_param_type == "long long":
                    first_var_str = first_var_name
                elif first_param_type == "NSString **":
                    first_var_str = "&" + first_var_name
                elif first_param_type == "NSString *":
                    first_var_str = first_var_name
                elif first_param_type == "char *":
                    first_var_str = first_var_name
                elif first_param_type == "NSDate *":
                    first_var_str = first_var_name
                elif first_param_type == "NSData *":
                    first_var_str = first_var_name
                elif first_param_type == "NSMutableDictionary *":
                    first_var_str = first_var_name
                # elif first_param_type == "float":
                #     first_var_str = first_var_name

                else:
                    first_var_str = first_var_name
                
                #第一个参数需要用first_var_name
                # out_str += piece + first_var_str + " "

                out_str += first_var_str 

            elif index == len(pieces_list) - 1:
                # out_str += piece + generate_0905_param_str(param_list[index].param_type)
                out_str += ", " + generate_0905_param_str(param_list[index].param_type)
            else:
                # out_str += piece + generate_0905_param_str(param_list[index].param_type) + " "
                out_str += ", " + generate_0905_param_str(param_list[index].param_type)
        # print("out_str " + out_str)
    else:
        out_str += transfer_str

    # out_str += "];//in0912_handle\n"
    out_str += ");//in0304_inline_handle\n"

    return out_str


# 根据函数原型组装成函数调用处理
def handle_transfer_0912(prototype_obj, first_var_name, class_name):
    '''
    0912版本组装函数调用，至少有一个参数，第一个参数是关联参数
    '''
    out_str = "["
    
    #处理
    # out_str += class_name + " "
    transfer_str = prototype_obj.transfer_name

    #0305添加
    # out_str += transfer_str.replace(":", "") + "("

    # 获取参数个数
    char_list = methodtransfer.count_str(":", transfer_str)
    if len(char_list):
        #切片
        pieces_list = []
        prefix_str = ""
        param_list = prototype_obj.parampair_list
        for index, index_value in enumerate(char_list):
            if index == 0:
                prefix_str = transfer_str[0:index_value + 1]
            else:
                prefix_str = transfer_str[char_list[index-1]+1:index_value + 1]
            pieces_list.append(prefix_str)
        for index, piece in enumerate(pieces_list):
            if index == 0:
                first_param_type = param_list[index].param_type
                first_var_str = ""
                if first_param_type == "double":
                    first_var_str = first_var_name
                if first_param_type == "double *":
                    first_var_str = "&" + first_var_name
                elif first_param_type == "NSArray **":
                    first_var_str = "&" + first_var_name
                elif first_param_type == "NSArray *":
                    first_var_str = first_var_name
                elif first_param_type == "long long *":
                    first_var_str = "&" + first_var_name
                elif first_param_type == "long long":
                    first_var_str = first_var_name
                elif first_param_type == "NSString **":
                    first_var_str = "&" + first_var_name
                elif first_param_type == "NSString *":
                    first_var_str = first_var_name
                elif first_param_type == "char *":
                    first_var_str = first_var_name
                elif first_param_type == "NSDate *":
                    first_var_str = first_var_name
                elif first_param_type == "NSData *":
                    first_var_str = first_var_name
                elif first_param_type == "NSMutableDictionary *":
                    first_var_str = first_var_name
                # elif first_param_type == "float":
                #     first_var_str = first_var_name

                else:
                    first_var_str = first_var_name
                
                #第一个参数需要用first_var_name
                out_str += piece + first_var_str + " "

                # out_str += first_var_str 

            elif index == len(pieces_list) - 1:
                out_str += piece + generate_0905_param_str(param_list[index].param_type)
                # out_str += ", " + generate_0905_param_str(param_list[index].param_type)
            else:
                out_str += piece + generate_0905_param_str(param_list[index].param_type) + " "
                # out_str += ", " + generate_0905_param_str(param_list[index].param_type)
        # print("out_str " + out_str)
    else:
        out_str += transfer_str

    out_str += "];//in0912_handle\n"
    # out_str += ");//in0912_handle\n"

    return out_str

# 根据函数原型组装成函数调用
def handle_transfer_0905(prototype_obj, first_var_name, class_name):
    '''
    0905版本组装函数调用，至少有一个参数
    '''
    out_str = "["
    
    #处理
    out_str += class_name + " "
    transfer_str = prototype_obj.transfer_name
    # 获取参数个数
    char_list = methodtransfer.count_str(":", transfer_str)
    if len(char_list):
        #切片
        pieces_list = []
        prefix_str = ""
        param_list = prototype_obj.parampair_list
        for index, index_value in enumerate(char_list):
            if index == 0:
                prefix_str = transfer_str[0:index_value + 1]
            else:
                prefix_str = transfer_str[char_list[index-1]+1:index_value + 1]
            pieces_list.append(prefix_str)
        for index, piece in enumerate(pieces_list):
            if index == 0:
                #第一个参数需要用first_var_name
                out_str += piece + "&" + first_var_name + " "
            elif index == len(pieces_list) - 1:
                out_str += piece + generate_0905_param_str(param_list[index].param_type)
            else:
                out_str += piece + generate_0905_param_str(param_list[index].param_type) + " "
        # print("out_str " + out_str)
    else:
        out_str += transfer_str

    out_str += "];//in0905_handle\n"
    return out_str


# 处理0905版本插入点函数调用的后续处理
def handle_transfer_0905_letter(return_type, var_name):
    '''
    处理0905版本插入点的函数调用的后续处理
    param:
        return_type:函数调用的返回值类型，不可能是void类型
        var_name:用来接收函数返回的变量名
    '''
    out_str = ""
    # 每一个包都需要根据返回值类型定制处理
    # 0905BattleTale处理
    if return_type == "NSArray *":
        # random_var = generate_random_str(out_random_type_class)
        # out_str += "\tNSArray *" + random_var + ";"
        for i in range(random.randrange(1, 3)):
            random_ion = random.randrange(0, 2)
            if random_ion == 0:
                out_str += "\t[" + var_name + " count];\n"
            elif random_ion == 1:
                out_str += "\t[" + var_name + " isEqualToArray:@[]];\n"
    elif return_type == "AVPlayerItem *":
        for i in range(random.randrange(1, 3)):
            random_ion = random.randrange(0, 3)
            if random_ion == 0:
                out_str += "\t[" + var_name + " audioMix];\n"
            elif random_ion == 1:
                out_str += "\t[" + var_name + " canPlayReverse];\n"
            elif random_ion == 2:
                out_str += "\t[" + var_name + " isPlaybackBufferFull];\n"
    elif return_type == "AVPlayer *":
        for i in range(random.randrange(1, 3)):
            random_ion = random.randrange(0, 2)
            if random_ion == 0:
                out_str += "\t[" + var_name + " status];\n"
            elif random_ion == 1:
                out_str += "\t[" + var_name + " currentItem];\n"
    elif return_type == "GLKViewController *":
        for i in range(random.randrange(1, 3)):
            random_ion = random.randrange(0, 2)
            if random_ion == 0:
                out_str += "\t[" + var_name + " isPaused];\n"
            elif random_ion == 1:
                out_str += "\t[" + var_name + " resumeOnDidBecomeActive];\n"
    elif return_type == "GLKMesh *":
        for i in range(random.randrange(1, 3)):
            random_ion = random.randrange(0, 2)
            if random_ion == 0:
                out_str += "\t[" + var_name + " submeshes];\n"
            elif random_ion == 1:
                out_str += "\t[" + var_name + " name];\n"
    elif return_type == "GLKTextureInfo *":
        for i in range(random.randrange(1, 3)):
            random_ion = random.randrange(0, 2)
            if random_ion == 0:
                out_str += "\t[" + var_name + " depth];\n"
            elif random_ion == 1:
                out_str += "\t[" + var_name + " target];\n"
    elif return_type == "AVCaptureVideoPreviewLayer *":
        out_str += "\t[" + var_name + " setVideoGravity:AVLayerVideoGravityResizeAspectFill];\n"
    elif return_type == "CABasicAnimation *":
        for i in range(random.randrange(1, 3)):
            random_ion = random.randrange(0, 2)
            if random_ion == 0:
                out_str += "\t[" + var_name + " byValue];\n"
            elif random_ion == 1:
                out_str += "\t[" + var_name + " fromValue];\n"
    elif return_type == "GCGamepad *":
        for i in range(random.randrange(1, 3)):
            random_ion = random.randrange(0, 2)
            if random_ion == 0:
                out_str += "\t[" + var_name + " leftShoulder];\n"
            elif random_ion == 1:
                out_str += "\t[" + var_name + " rightShoulder];\n"
    elif return_type == "GKScore *":
        for i in range(random.randrange(1, 3)):
            random_ion = random.randrange(0, 2)
            if random_ion == 0:
                out_str += "\t[" + var_name + " player];\n"
            elif random_ion == 1:
                out_str += "\t[" + var_name + " leaderboardIdentifier];\n"
    elif return_type == "UIAlertController *":
        for i in range(random.randrange(1, 3)):
            random_ion = random.randrange(0, 2)
            if random_ion == 0:
                out_str += "\t[" + var_name + " actions];\n"
            elif random_ion == 1:
                out_str += "\t[" + var_name + " title];\n"
    elif return_type == "UIAlertAction *":
        for i in range(random.randrange(1, 3)):
            random_ion = random.randrange(0, 2)
            if random_ion == 0:
                out_str += "\t[" + var_name + " style];\n"
            elif random_ion == 1:
                out_str += "\t[" + var_name + " title];\n"
    elif return_type == "UIDevice *":
        for i in range(random.randrange(1, 3)):
            random_ion = random.randrange(0, 2)
            if random_ion == 0:
                out_str += "\t[" + var_name + " batteryLevel];\n"
            elif random_ion == 1:
                out_str += "\t[" + var_name + " batteryState];\n"
    elif return_type == "UIActivityIndicatorView *":
        for i in range(random.randrange(1, 3)):
            random_ion = random.randrange(0, 2)
            if random_ion == 0:
                out_str += "\t[" + var_name + " color];\n"
            elif random_ion == 1:
                out_str += "\t[" + var_name + " backgroundColor];\n"
    elif return_type == "UIBezierPath *":
        for i in range(random.randrange(1, 3)):
            random_ion = random.randrange(0, 2)
            if random_ion == 0:
                out_str += "\t[" + var_name + " addClip];\n"
            elif random_ion == 1:
                out_str += "\t[" + var_name + " bounds];\n"
    elif return_type == "UIVisualEffectView *":
        for i in range(random.randrange(1, 3)):
            random_ion = random.randrange(0, 2)
            if random_ion == 0:
                out_str += "\t[" + var_name + " contentView];\n"
            elif random_ion == 1:
                out_str += "\t[" + var_name + " frame];\n"
    elif return_type == "GCMotion *":
        for i in range(random.randrange(1, 3)):
            random_ion = random.randrange(0, 2)
            if random_ion == 0:
                out_str += "\t[" + var_name + " controller];\n"
            elif random_ion == 1:
                out_str += "\t[" + var_name + " userAcceleration];\n"
    elif return_type == "UIColor *":
        for i in range(random.randrange(1, 3)):
            random_ion = random.randrange(0, 2)
            if random_ion == 0:
                out_str += "\t[" + var_name + " CGColor];\n"
            elif random_ion == 1:
                out_str += "\t[" + var_name + " set];\n"
    elif return_type == "UIFont *":
        for i in range(random.randrange(1, 3)):
            random_ion = random.randrange(0, 2)
            if random_ion == 0:
                out_str += "\t[" + var_name + " fontName];\n"
            elif random_ion == 1:
                out_str += "\t[" + var_name + " xHeight];\n"
    

    return out_str

def reduction_0919_prototype_from_type(prototype_list, insert_0919_type):
    method_transfer_name = ""
    if insert_0919_type == global_0905insert_type_double:
        method_transfer_name = "NowehniovMendnvionTixzvnpwe"
    elif insert_0919_type == global_0905insert_type_longlong:
        method_transfer_name = "NowehniovMendnvionFixnvmwpek"
    elif insert_0919_type == global_0905insert_type_NSString:
        method_transfer_name = "NowehniovMendnvionNwohgnpwet"
    elif insert_0919_type == global_0905insert_type_NSArray:
        method_transfer_name = "NowehniovMendnvionDiwoehgnpie"
    for prototype_obj in prototype_list:
        if method_transfer_name in prototype_obj.transfer_name:
            return prototype_obj
    return None

# 获取0924版本插入点原型
def handle_0924_prototype_from_type(prototype_list, insert_0919_type):
    min_use_count = 10
    # 拿到最小调用次数
    for prototype_obj in prototype_list:
        cur_use_count = prototype_obj.get_use_count()
        if cur_use_count < min_use_count:
            min_use_count = cur_use_count
    
    # 只要符合最小被用次数，就可以返回当前函数原型
    for prototype_obj in prototype_list:
        if prototype_obj.get_use_count() == min_use_count:
            # 更新使用次数
            prototype_obj.add_count()
            return prototype_obj
    return None

# 获取0919版本插入点原型
def handle_0919_prototype_from_type(prototype_list, insert_0919_type):
    method_transfer_name = ""
    if insert_0919_type == global_0905insert_type_double:
        method_transfer_name = "NowehniovMendnvionTYs5ugt"
    elif insert_0919_type == global_0905insert_type_longlong:
        method_transfer_name = "NowehniovMendnvionYsg4dfu"
    elif insert_0919_type == global_0905insert_type_NSString:
        method_transfer_name = "NowehniovMendnvionKshdgh2jwe"
    elif insert_0919_type == global_0905insert_type_NSArray:
        method_transfer_name = "NowehniovMendnvionKstd6hstd"
    for prototype_obj in prototype_list:
        if method_transfer_name in prototype_obj.transfer_name:
            return prototype_obj
    return None


# 生成0926版被替换函数
def generate_0926_transfer(use_insert_class_list, insert_0919_type, target_var_name):
    print("insert class list:" + str(use_insert_class_list))

    #处理
    handle_out_dic = get_insert_0926_prototype(use_insert_class_list, insert_0919_type, global_0926insert_function_type_handle)
    handle_class_name = handle_out_dic["class_name"]
    prototype_0926_obj = handle_out_dic["prototype"]
    out_str = "\n\t"
    random_var = generate_random_str(out_random_type_class)
    out_str += prototype_0926_obj.return_type + " " + random_var + " = "
    out_str += handle_transfer_0912(prototype_0926_obj, target_var_name, handle_class_name)
    #加上值还原
    #获取还原的类
    reduction_out_dic = get_insert_0926_prototype(use_insert_class_list, insert_0919_type, global_0926insert_function_type_reduction)
    reduction_class_name = reduction_out_dic["class_name"]
    reduction_prototype_obj = reduction_out_dic["prototype"]
    #拼接还原的调用
    out_str += "\t" + target_var_name + " = "
    out_str += handle_transfer_0912(reduction_prototype_obj, random_var, reduction_class_name)

    return out_str


# 生成0924版被替换函数
def generate_0924_transfer(use_insert_class_list, insert_0919_type, target_var_name):
    print("insert class list:" + str(use_insert_class_list))
    insert_class_obj = get_insert_0924_handle_class_obj(use_insert_class_list, insert_0919_type)
    prototype_list = insert_class_obj.method_prototype_list
    prototype_obj = handle_0924_prototype_from_type(prototype_list, insert_0919_type)

    out_str = "\n\t"
    # random_var = generate_random_str(out_random_type_class)
    # out_str += prototype_obj.return_type + " " + random_var + " = "
    # out_str += handle_transfer_0905(prototype_obj, target_var_name, insert_class_obj.class_name)
    out_str += handle_transfer_0912(prototype_obj, target_var_name, insert_class_obj.class_name)
    #加上值还原
    #获取还原的类
    # insert_reduction_class_obj = get_insert_0919_handle_class_obj(use_insert_class_list, insert_0919_type)
    # reduction_prototype_list = insert_reduction_class_obj.method_prototype_list
    # reduction_prototype_obj = reduction_0919_prototype_from_type(reduction_prototype_list, insert_0919_type)
    # #拼接还原的调用
    # out_str += "\t" + target_var_name + " = "
    # out_str += handle_transfer_0912(reduction_prototype_obj, random_var, insert_reduction_class_obj.class_name)

    return out_str

# 生成0304版C函数替换
def generaate_0304_C_transfer(use_insert_class_list, insert_0919_type, target_var_name):
    print("insert class list:" + str(use_insert_class_list))
    insert_class_obj = get_insert_0919_handle_class_obj(use_insert_class_list, insert_0919_type)
    prototype_list = insert_class_obj.method_prototype_list
    prototype_obj = handle_0919_prototype_from_type(prototype_list, insert_0919_type)

    out_str = "\n\t"
    random_var = generate_random_str(out_random_type_class)
    out_str += prototype_obj.return_type + " " + random_var + " = "

    # out_str += handle_transfer_0912(prototype_obj, target_var_name, insert_class_obj.class_name)
    out_str += handle_transfer_c_0304(prototype_obj, target_var_name, insert_class_obj.class_name)

    #加上值还原
    #获取还原的类
    insert_reduction_class_obj = get_insert_0919_handle_class_obj(use_insert_class_list, insert_0919_type)
    reduction_prototype_list = insert_reduction_class_obj.method_prototype_list
    reduction_prototype_obj = reduction_0919_prototype_from_type(reduction_prototype_list, insert_0919_type)
    #拼接还原的调用
    out_str += "\t" + target_var_name + " = "
    # out_str += handle_transfer_0912(reduction_prototype_obj, random_var, insert_reduction_class_obj.class_name)
    out_str += handle_transfer_c_0304(reduction_prototype_obj, random_var, insert_reduction_class_obj.class_name)

    return out_str


# 生成0919版被替换函数
def generate_0919_transfer(use_insert_class_list, insert_0919_type, target_var_name):
    print("insert class list:" + str(use_insert_class_list))
    insert_class_obj = get_insert_0919_handle_class_obj(use_insert_class_list, insert_0919_type)
    prototype_list = insert_class_obj.method_prototype_list
    prototype_obj = handle_0919_prototype_from_type(prototype_list, insert_0919_type)

    out_str = "\n\t"
    random_var = generate_random_str(out_random_type_class)
    out_str += prototype_obj.return_type + " " + random_var + " = "
    # out_str += handle_transfer_0905(prototype_obj, target_var_name, insert_class_obj.class_name)
    out_str += handle_transfer_0912(prototype_obj, target_var_name, insert_class_obj.class_name)
    #加上值还原
    #获取还原的类
    insert_reduction_class_obj = get_insert_0919_handle_class_obj(use_insert_class_list, insert_0919_type)
    reduction_prototype_list = insert_reduction_class_obj.method_prototype_list
    reduction_prototype_obj = reduction_0919_prototype_from_type(reduction_prototype_list, insert_0919_type)
    #拼接还原的调用
    out_str += "\t" + target_var_name + " = "
    out_str += handle_transfer_0912(reduction_prototype_obj, random_var, insert_reduction_class_obj.class_name)

    return out_str

# 生成0912版被替换函数、
def generate_0912_transfer(use_insert_class_list, insert_0912_type, target_var_name):
    '''
    生成0912版插入点，按照过的版本做，一定有返回值，但是函数是一个进行修改参数值，后一个是还原参数值
    param:
        use_insert_class_list:被用到类列表
        insert_0912_type:当前的替换类型
        target_var_name:目标变量名
    '''
    print("generate_0912_transfer")
    # insert_class_obj = get_insert_0905_class_obj(use_insert_class_list, insert_0912_type)
    insert_class_obj = get_insert_0912_handle_class_obj(use_insert_class_list, insert_0912_type)

    prototype_list = insert_class_obj.method_prototype_list
    prototype_obj = prototype_list[random.randrange(0, len(prototype_list))]
    
    out_str = "\n\t"
    random_var = generate_random_str(out_random_type_class)
    out_str += prototype_obj.return_type + " " + random_var + " = "
    # out_str += handle_transfer_0905(prototype_obj, target_var_name, insert_class_obj.class_name)
    out_str += handle_transfer_0912(prototype_obj, target_var_name, insert_class_obj.class_name)
    #加上值还原
    #获取还原的类
    insert_reduction_class_obj = get_insert_0912_reduction_class_obj(use_insert_class_list, insert_0912_type)
    reduction_prototype_list = insert_reduction_class_obj.method_prototype_list
    reduction_prototype_obj = reduction_prototype_list[random.randrange(0, len(reduction_prototype_list))]
    #拼接还原的调用
    out_str += "\t" + target_var_name + " = "
    out_str += handle_transfer_0912(reduction_prototype_obj, random_var, insert_reduction_class_obj.class_name)

    #如果需要后续处理的就打开
    out_str += "\t" + handle_transfer_0912_letter(reduction_prototype_obj.return_type, target_var_name)
    
    return out_str



# 生成0905版被替换函数
def generate_0905_transfer(use_insert_class_list, insert_0905_type, target_var_name):
    '''
    生成0905版插入点
    param:
        use_insert_class_list:被用到类列表
        insert_0905_type:当前的替换类型
        target_var_name:目标变量名
    '''
    print("generate_0905_transfer")
    insert_class_obj = get_insert_0905_class_obj(use_insert_class_list, insert_0905_type)
    prototype_list = insert_class_obj.method_prototype_list
    prototype_obj = prototype_list[random.randrange(0, len(prototype_list))]
    need_handle_letter = False
    if "void" == prototype_obj.return_type:
        #无后续处理
        need_handle_letter = False
    else:
        #需要有后续处理
        need_handle_letter = True
    out_str = "\n\t"
    if need_handle_letter:
        random_var = generate_random_str(out_random_type_class)
        out_str = prototype_obj.return_type + " " + random_var + " = "
        out_str += handle_transfer_0905(prototype_obj, target_var_name, insert_class_obj.class_name)
        #加上后续处理
        out_str += handle_transfer_0905_letter(prototype_obj.return_type, random_var)
    else:
        #无后续处理
        out_str = handle_transfer_0905(prototype_obj, target_var_name, insert_class_obj.class_name)
    
    return out_str

# 处理0926版插入点
def replace_insert_0926(need_replace_file_list, use_insert_class_list):
    for file in need_replace_file_list:
        file_context = []
        with open(file, "r+") as input:
            file_context = input.readlines()
        if len(file_context) > 0:
            file_replace_context = []
            for line in file_context:
                if contains_0905_insert_type(line):
                    insert_0912_type = insert_0905_type_from_str(line)
                    print("line:" + line)
                    print("insert_type:" + insert_0912_type)
                    need_replace_str = insert_0912_type
                    # 找到对应的变量名
                    var_name = get_0905_varname(line, insert_0912_type)
                    if var_name == "":
                        file_replace_context.append(line)
                        continue
                    # 生成替换语句
                    need_replace_str = generate_0926_transfer(use_insert_class_list, insert_0912_type, var_name)
                    replace_line = line.replace(insert_0912_type, need_replace_str)
                    file_replace_context.append(replace_line)
                else:
                    file_replace_context.append(line)
            with open(file, "w") as input:
                input.writelines(file_replace_context)


# 处理0924版插入点
def replace_insert_0924(need_replace_file_list, use_insert_class_list):
    for file in need_replace_file_list:
        file_context = []
        with open(file, "r+") as input:
            file_context = input.readlines()
        if len(file_context) > 0:
            file_replace_context = []
            for line in file_context:
                if contains_0905_insert_type(line):
                    insert_0912_type = insert_0905_type_from_str(line)
                    print("line:" + line)
                    print("insert_type:" + insert_0912_type)
                    need_replace_str = insert_0912_type
                    # 找到对应的变量名
                    var_name = get_0905_varname(line, insert_0912_type)
                    if var_name == "":
                        file_replace_context.append(line)
                        continue
                    # 生成替换语句
                    need_replace_str = generate_0924_transfer(use_insert_class_list, insert_0912_type, var_name)
                    replace_line = line.replace(insert_0912_type, need_replace_str)
                    file_replace_context.append(replace_line)
                else:
                    file_replace_context.append(line)
            with open(file, "w") as input:
                input.writelines(file_replace_context)


# 给处理还原添加上inline
def replace_and_add_inline_0304(need_replace_file_list, use_insert_class_list):

    for file in need_replace_file_list:
        file_context = []
        with open(file, "r+") as input:
            file_context = input.readlines()
        if len(file_context) > 0:
            file_replace_context = []
            for line in file_context:
                if contains_0905_insert_type(line):
                    insert_0912_type = insert_0905_type_from_str(line)
                    print("line:" + line)
                    print("insert_type:" + insert_0912_type)
                    need_replace_str = insert_0912_type
                    # 找到对应的变量名
                    var_name = get_0905_varname(line, insert_0912_type)
                    if var_name == "":
                        file_replace_context.append(line)
                        continue
                    # 生成替换语句
                    # need_replace_str = generate_0919_transfer(use_insert_class_list, insert_0912_type, var_name)

                    need_replace_str = generaate_0304_C_transfer(use_insert_class_list, insert_0912_type, var_name)

                    replace_line = line.replace(insert_0912_type, need_replace_str)
                    file_replace_context.append(replace_line)
                else:
                    file_replace_context.append(line)

            file_content_str = "".join(file_replace_context)
            # 需要查找本文件是否有函数调用，如果有，需要在文件头部添加inline函数的声明与调用
            contains_transfer_list = file_content_contain_inline_transfer(use_insert_class_list, file_content_str)

            # 根据已经存在的函数实现，生成新的函数原型及实现
            inline_C_0304_implamentation_str = inline_inuse_C_funcs(use_insert_class_list, contains_transfer_list)

            # 将生成的函数实现加到文件的头部
            file_content_str = inline_C_0304_implamentation_str + file_content_str

            #需要对用到的inline函数进行重命名
            replace_str = replace_transfer_str(contains_transfer_list, file_content_str)
            file_content_str = replace_str


            with open(file, "w") as input:
                input.write(file_content_str)

# 0314版 对用到inline函数进行重命名
def replace_transfer_str(contains_transfer_list, target_content_str):
    out_replaced_str = target_content_str
    for transfer_str in contains_transfer_list:
        renamed_str = generate_words_str("func")
        out_replaced_str = out_replaced_str.replace(transfer_str, renamed_str)
    return out_replaced_str


# 0314版 根据已经存在的调用，生成函数原型及实现
def inline_inuse_C_funcs(use_insert_class_list, contains_transfer_list):
    out_implamentation_str = ""
    for c_method_transfer in contains_transfer_list:
        for insert_class_obj in use_insert_class_list:
            for implementation_obj in insert_class_obj.implamentation_list:
                method_obj = implementation_obj.method_prototype
                if c_method_transfer in method_obj.transfer_name.replace(":", ""):
                    # 找到当前函数调用，组装成对应的函数声明及函数实现

                    # 拿到参数值
                    param_str = "("
                    for index, param_obj in enumerate(method_obj.parampair_list):
                        param_str += param_obj.param_type + " " + param_obj.param_name
                        if index != (len(method_obj.parampair_list) - 1):
                            param_str += ", "
                    param_str += ")"

                    prototype_str = "static inline " + method_obj.return_type + " " + c_method_transfer + param_str + ";\n"
                    prototype_str += "static inline " + method_obj.return_type + " " + c_method_transfer + param_str
                    prototype_str += implementation_obj.implamentation

                    out_implamentation_str += prototype_str + "\n\n"
    return out_implamentation_str


# 0314添加 查找目标内容是否包含inline函数调用
def file_content_contain_inline_transfer(use_insert_class_list, target_content_str):

    containd_transfer_list = []
    for insert_class_obj in use_insert_class_list:
        for method_obj in insert_class_obj.method_prototype_list:
            transfer_str = method_obj.transfer_name
            transfer_str = transfer_str.replace(":", "")
            if transfer_str in target_content_str:
                # 搜索到了目标字符串
                containd_transfer_list.append(transfer_str)
    return containd_transfer_list




# 处理0919版插入点替换
def replace_insert_0919(need_replace_file_list, use_insert_class_list):
    for file in need_replace_file_list:
        file_context = []
        with open(file, "r+") as input:
            file_context = input.readlines()
        if len(file_context) > 0:
            file_replace_context = []
            for line in file_context:
                if contains_0905_insert_type(line):
                    insert_0912_type = insert_0905_type_from_str(line)
                    print("line:" + line)
                    print("insert_type:" + insert_0912_type)
                    need_replace_str = insert_0912_type
                    # 找到对应的变量名
                    var_name = get_0905_varname(line, insert_0912_type)
                    if var_name == "":
                        file_replace_context.append(line)
                        continue
                    # 生成替换语句
                    need_replace_str = generate_0919_transfer(use_insert_class_list, insert_0912_type, var_name)
                    replace_line = line.replace(insert_0912_type, need_replace_str)
                    file_replace_context.append(replace_line)
                else:
                    file_replace_context.append(line)
            with open(file, "w") as input:
                input.writelines(file_replace_context)

# 处理0912版插入点替换
def replace_insert_0912(need_replace_file_list, use_insert_class_list):
    for file in need_replace_file_list:
        file_context = []
        with open(file, "r+") as input:
            file_context = input.readlines()
        if len(file_context) > 0:
            file_replace_context = []
            for line in file_context:
                if contains_0905_insert_type(line):
                    insert_0912_type = insert_0905_type_from_str(line)
                    print("line:" + line)
                    print("insert_type:" + insert_0912_type)
                    need_replace_str = insert_0912_type
                    # 找到对应的变量名
                    var_name = get_0905_varname(line, insert_0912_type)
                    # 生成替换语句
                    need_replace_str = generate_0912_transfer(use_insert_class_list, insert_0912_type, var_name)
                    replace_line = line.replace(insert_0912_type, need_replace_str)
                    file_replace_context.append(replace_line)
                else:
                    file_replace_context.append(line)
            with open(file, "w") as input:
                input.writelines(file_replace_context)


# 处理0905版插入点替换
def replace_insert_0905(need_replace_file_list, use_insert_class_list):
    '''
    '''
    for file in need_replace_file_list:
        file_context = []
        with open(file, "r+") as input:
            file_context = input.readlines()
        if len(file_context) > 0:
            file_replace_context = []
            for line in file_context:
                if contains_0905_insert_type(line):
                    insert_0905_type = insert_0905_type_from_str(line)
                    print("line:" + line)
                    print("insert_type:" + insert_0905_type)
                    need_replace_str = insert_0905_type
                    # 找到对应的变量名
                    var_name = get_0905_varname(line, insert_0905_type)
                    # 生成替换语句
                    need_replace_str = generate_0905_transfer(use_insert_class_list, insert_0905_type, var_name)
                    replace_line = line.replace(insert_0905_type, need_replace_str)
                    file_replace_context.append(replace_line)
                else:
                    file_replace_context.append(line)
            with open(file, "w") as input:
                input.writelines(file_replace_context)


# 0905版插入点
def handle_replace_0905_insert():
    '''
    0905版插入点的主要目的是增加插入点与上下文的关联
    第一版确定为longlong、NSString 、double、NSarray四种类型
    替换原则：将特定标记对应的类型替换成对应的函数，第一个函数参数是指定的对应变量的引用，后续参数是随机参数
    '''
    print("使用0905版插入点")
    # 扫描插入库函数
    header_file_list = get_search_files("already", [".h"], nosearch_directorys)
    insert_class_list = initial_class_from_file(header_file_list)

    need_replace_file_list = get_search_files("target", [".m", ".mm"], nosearch_directorys)

    # 0905版处理插入点替换
    replace_insert_0905(need_replace_file_list, insert_class_list)

# 0912版插入点
def handle_replace_0912_insert():
    # 扫描插入库函数
    header_file_list = get_search_files("already", [".h"], nosearch_directorys)
    insert_class_list = initial_class_from_file(header_file_list)

    need_replace_file_list = get_search_files("target", [".m", ".mm"], nosearch_directorys)

    # 0905版处理插入点替换
    replace_insert_0912(need_replace_file_list, insert_class_list)

# 0926版本插入点
def handle_replace_0926_insert():
    # 扫描插入库函数
    header_file_list = get_search_files("already", [".h"], nosearch_directorys)
    insert_class_list = initial_class_from_file(header_file_list)

    need_replace_file_list = get_search_files("target", [".m", ".mm"], nosearch_directorys)

    replace_insert_0926(need_replace_file_list, insert_class_list)


#0924版本插入点
def handle_replace_0924_insert():
    # 扫描插入库函数
    header_file_list = get_search_files("already", [".h"], nosearch_directorys)
    insert_class_list = initial_class_from_file(header_file_list)

    need_replace_file_list = get_search_files("target", [".m", ".mm"], nosearch_directorys)

    replace_insert_0924(need_replace_file_list, insert_class_list)

# 0314新增处理还原函数的inline替换
def handle_replace_inline():
    #扫描插入库函数
    implamentation_file_list = get_search_files("already", [".m"], nosearch_directorys)
    print("implamentation file list :" + str(implamentation_file_list))

    # file_creator_obj = ins_objcreatorfactor.ObjCreatorFactor(ins_objcreatorfactor.obj_creator_type_0919).creator()
    # insert_class_list = file_creator_obj.generate_object()
    insert_class_list = initial_class_from_file(implamentation_file_list)

    # 2020-0305新增扫描C函数
    # insert_class_list = initial_C_funcs_from_file(header_file_list)

    need_replace_file_list = get_search_files("target", [".m", ".mm"], nosearch_directorys)

    # replace_insert_0919(need_replace_file_list, insert_class_list)

    replace_and_add_inline_0304(need_replace_file_list, insert_class_list)

    # insert_class_list = initial_class_from_file(header_file_list)

# 0919版本插入点
def handle_replace_0919_insert():
    # 扫描插入库函数
    header_file_list = get_search_files("already", [".h"], nosearch_directorys)

    # file_creator_obj = ins_objcreatorfactor.ObjCreatorFactor(ins_objcreatorfactor.obj_creator_type_0919).creator()
    # insert_class_list = file_creator_obj.generate_object()
    insert_class_list = initial_class_from_file(header_file_list)

    # 2020-0305新增扫描C函数
    # insert_class_list = initial_C_funcs_from_file(header_file_list)

    need_replace_file_list = get_search_files("target", [".m", ".mm"], nosearch_directorys)

    replace_insert_0919(need_replace_file_list, insert_class_list)

    # insert_class_list = initial_class_from_file(header_file_list)

# 0823版插入点
def handle_replace_0823():
    '''
    0823版插入点的主要原则是降低插入点功能函数的重复次数，加大某一个插入点函数的调用次数
    第一版确定为UITableView、UITextField、CFStringRef三种功能函数被随机调用
    插入点替换原则：
        随机库里的一条函数，生成对应的调用，然后替换掉insert标记
    '''
    # 扫描插入库的函数
    header_file_list = get_search_files("already", [".h"], nosearch_directorys)
    insert_class_list = initial_class_from_file(header_file_list)

    need_replace_file_list = get_search_files("target", [".m", ".mm"], nosearch_directorys)

    # 0823版处理插入点替换
    replace_insert_0823(need_replace_file_list, insert_class_list)


# 0905版本判断一行代码中是否有标准格式的变量定义
def line_has_0905_standard_symble(target_line):
    contains_standard = False
    #去掉target_line中的前后空格
    target_line = target_line.strip()
    if target_line.startswith("long long "):
        contains_standard = True
    elif target_line.startswith("NSString *"):
        contains_standard = True
    elif target_line.startswith("double "):
        contains_standard = True
    elif target_line.startswith("NSArray *"):
        contains_standard = True


    return contains_standard

# 找出0905版本标准格式插入点标记的格式
def standard_insert_type_0905_from_line(target_line):
    '''
    0905版本标准格式的插入点标记一行有且只有一个
    '''
    current_insert_type = ""
    #去掉target_line中的前后空格
    target_line = target_line.strip()
    if target_line.startswith("long long "):
        current_insert_type = global_0905insert_type_longlong
    elif target_line.startswith("NSString *"):
        current_insert_type = global_0905insert_type_NSString
    elif target_line.startswith("double "):
        current_insert_type = global_0905insert_type_double
    elif target_line.startswith("NSArray *"):
        current_insert_type = global_0905insert_type_NSArray

    return current_insert_type

def add_0905_standard_symble(target_line, insert_type):
    # print("添加0905版标准格式插入点标记")
    # 去掉末尾的换行符
    target_line = target_line.replace("\n", "")
    new_line_str = target_line + insert_type + "\n"
    return new_line_str


# 0905判断目标行是否包含double类型值
def line_0905_has_double_value(target_line):
    result = double_insert_0905_rule.findall(target_line)
    # print("double result: " + str(result))
    if result != []:
        return True
    return False

# 0905版判断目标行是否包含longlong类型值    
def line_0905_has_longlong_value(target_line):
    result = longlong_insert_0905_rule.findall(target_line)
    if result != []:
        return True
    return False

#0905版判断目标行是否包含NSString类型值
def line_0905_has_NSString_value(target_line):
    result = NSString_insert_0905_rule.findall(target_line)
    if result != []:
        return True
    return False

#0905版判断目标行是否包含NSArray类型值
def line_0905_has_NSArray_value(target_line):
    result = NSArray_insert_0905_rule.findall(target_line)
    if result != []:
        return True
    return False

# 0905版本判断一行代码中是否有非标准格式的变量定义
def line_has_0905_non_standard_symble(target_line):
    contains_non_standard = False
    if line_0905_has_NSString_value(target_line):
        contains_non_standard = True
    elif line_0905_has_NSArray_value(target_line):
        contains_non_standard = True
    elif line_0905_has_double_value(target_line):
        contains_non_standard = True
    elif line_0905_has_longlong_value(target_line):
        contains_non_standard = True

    return contains_non_standard

# 0905版本获取一行代码中的非标准格式的变量
def non_standard_insert_type_0905_from_line(target_line):
    '''
    获取一行代码中的非标准格式变量，有可能有多个
    '''
    # insert_type_list = []
    insert_type_dic = dict()

    if line_0905_has_NSArray_value(target_line):
        insert_type = global_0905insert_type_NSArray
        matches = (NSArray_insert_0905_rule.finditer(target_line))
        match_list = []
        for match in matches:
            match_list.append(match)
        match = match_list[0]
        insert_type_dic["insert_type"] = insert_type
        insert_type_dic["location"] = match
    elif line_0905_has_NSString_value(target_line):
        insert_type = global_0905insert_type_NSString
        matches = (NSString_insert_0905_rule.finditer(target_line))
        match_list = []
        for match in matches:
            match_list.append(match)
        match = match_list[0]
        # print("find str :" + target_line[match.start():match.end()])
        insert_type_dic["insert_type"] = insert_type
        insert_type_dic["location"] = match
    elif line_0905_has_double_value(target_line):
        insert_type = global_0905insert_type_double
        matches = (double_insert_0905_rule.finditer(target_line))
        match_list = []
        for match in matches:
            match_list.append(match)
        match = match_list[0]
        insert_type_dic["insert_type"] = insert_type
        insert_type_dic["location"] = match
    elif line_0905_has_longlong_value(target_line):
        insert_type = global_0905insert_type_longlong
        matches = (longlong_insert_0905_rule.finditer(target_line))
        match_list = []
        for match in matches:
            match_list.append(match)
        match = match_list[0]
        insert_type_dic["insert_type"] = insert_type
        insert_type_dic["location"] = match

    return insert_type_dic

# 为一行代码添加对应的插入点标记
def add_0905_non_standard_symble(target_line, insert_info_dic):
    '''
    param:
        target_line:目标行
        insert_info_dic:已找到的第一个符合规则的参数信息，包含insert_type和location
    '''
    # print("为一行代码添加对应的插入点标记")
    new_line_str = ""
    insert_type = insert_info_dic["insert_type"]
    start_index = insert_info_dic["location"].start()
    # print("line:" + target_line)
    if (insert_type == global_0905insert_type_double or insert_type == global_0905insert_type_longlong) and target_line[start_index-1:start_index] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-/":
        return target_line
    end_index = insert_info_dic["location"].end()
    if target_line[end_index:end_index+1] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-/":
        return target_line
    target_value = target_line[start_index:end_index]
    type_str = ""
    
    if insert_type == global_0905insert_type_double:
        type_str = "double "
    elif insert_type == global_0905insert_type_longlong:
        type_str = "long long "
    elif insert_type == global_0905insert_type_NSString:
        type_str = "NSString *"
    else:
        type_str = "NSArray *"
    
    var_name = generate_random_str(out_random_type_class)
    new_line_str += "\t" + type_str + var_name + " = " + target_value + ";" + insert_type + "\n"
    replaced_line = target_line[0:start_index] + var_name + target_line[end_index:]
    new_line_str += replaced_line

    return new_line_str

# 查找oc函数的实现占用的行数
def find_oc_func(file_content_list, start_index):
    method_line = file_content_list[start_index]
    method_str = oc_func_rule3.findall(method_line)[0]
    max_line_index = 0
    max_line_str = ""
    while True:
        max_line_str = ""
        for i in range(max_line_index):
            cur_str = file_content_list[i+start_index]
            max_line_str += cur_str
        
        if len(max_line_str) > 0:
            implamentation_str = findimplamentation(method_str, max_line_str)
            if implamentation_str.endswith("\n}"):
                #找到了最大行
                break
        max_line_index += 1
    return max_line_index

    

# 1108版添加插入点标记
def add_1108_insert_symbol(target_file_list):
    for file in target_file_list:
        file_content = []
        with open(file, "r") as input:
            file_content = input.readlines()
        
        file_out_str = ""
        current_line_index = 0
        #找到oc函数
        while current_line_index < len(file_content):
            # func_index = 0
            cur_line = file_content[current_line_index]
            results = oc_func_rule3.findall(cur_line)
            if len(results) <= 0:
                file_out_str += cur_line
                current_line_index += 1
                
            else:
                #找到了一个函数，需要找到它的实现
                func_lines = find_oc_func(file_content, current_line_index)
                print("lines:" + str(func_lines))
                origin_imp_str = ""
                for i in range(func_lines):
                    cur_str = file_content[current_line_index + i]
                    origin_imp_str += cur_str
                print("origin:" + origin_imp_str)
                current_line_index += func_lines
                contains_symbol = contains_0905_insert_type(origin_imp_str)
                if contains_symbol:
                    #已经包含处理还原插入点标记，pass
                    file_out_str += origin_imp_str
                else:
                    #未找到标记，需要添加标记
                    handle_str = handle_insert_symbol_1108(origin_imp_str)
                    print("now:" + handle_str)
                    file_out_str += handle_str
                # break
        with open(file, "w") as input:
            input.write(file_out_str)
            
            
                        
                        


# 1108 对未添加标记的函数添加处理还原标记
def handle_insert_symbol_1108(target_no_symbol_str):
    # 添加上一个标记就可以了，随机生成出一个标记
    insert_str = ""
    random_num = random.randrange(0, 4)
    insert_type = ""
    r_var_name = generate_random_str(out_random_type_class)
    if random_num == 0:
        insert_type = global_0905insert_type_double
        insert_str = "\n\tdouble " + r_var_name + " = " + generate_0905_param_str("double") + ";" + insert_type + "\n"
        insert_str += "\tNSLog(@\"%f\", " + r_var_name + ");\n"
    elif random_num == 1:
        insert_type = global_0905insert_type_longlong
        insert_str = "\n\tlong long " + r_var_name + " = " + generate_0905_param_str("NSUInteger") + ";" + insert_type + "\n"
        insert_str += "\tNSLog(@\"%lld\", " + r_var_name + ");\n"
    elif random_num == 2:
        insert_type = global_0905insert_type_NSArray
        insert_str = "\n\tNSArray *" + r_var_name + " = " + generate_0905_param_str("NSArray *") + ";" + insert_type + "\n"
        insert_str += "\tNSLog(@\"%@\", " + r_var_name + ");\n"
    else:
        insert_type = global_0905insert_type_NSString
        insert_str = "\n\tNSString *" + r_var_name + " = " + generate_0905_param_str("NSString *") + ";" + insert_type + "\n"
        insert_str += "\tNSLog(@\"%@\", " + r_var_name + ");\n"
    
    first_end_index = target_no_symbol_str.find(";")

    if first_end_index < 0:
        #未找到“;”,需要重新找{
        first_end_index = target_no_symbol_str.find("{")
    if first_end_index < 0:
        return target_no_symbol_str
    prefix_str = target_no_symbol_str[0:first_end_index+1]
    suffix_str = target_no_symbol_str[first_end_index+1:]
    out_str = prefix_str + insert_str + suffix_str
    return out_str




# 0905版添加插入点标记
def add_0905_insert_symble(target_file_list):
    # 
    for file in target_file_list:
        file_content = []
        with open(file, "r") as input:
            file_content = input.readlines()
        
        file_replace_content = []
        #一行一行遍历
        for line in file_content:
            if "//in0905put_" in line:
                file_replace_content.append(line)
                continue
            if line.strip().startswith("//"):
                file_replace_content.append(line)
                continue
            if line_has_0905_standard_symble(line):
                # print("standard line:" + line)
                #如果一行中有标准格式的变量定义 
                #double jdposkfgo =  20.f;
                insert_type = standard_insert_type_0905_from_line(line)
                new_line = add_0905_standard_symble(line, insert_type)
                file_replace_content.append(new_line)
            elif line_has_0905_non_standard_symble(line):
                # print("non line:" + line)
                #如果一行中有符合非标准格式的变量定义
                #colorBallCell.redRange = 1.f;
                
                random_num = random.randrange(0, 100)
                if random_num < 40:
                    # 40%的概率是会添加
                    insert_type_list = non_standard_insert_type_0905_from_line(line)
                    new_line = add_0905_non_standard_symble(line, insert_type_list)
                    file_replace_content.append(new_line)
                else:
                    file_replace_content.append(line)
            else:
                # 没有符合条件的变量
                file_replace_content.append(line)
        # 写文件        
        with open(file, "w") as input:
            input.writelines(file_replace_content)


# 1108版对未添加处理还原插入点标记的函数添加处理还原标记
def handle_add_insert_symble_1108():
    print("1108版对未添加插入点标记的函数添加标记")
    need_replace_file_list = get_search_files("target", [".m", ".mm"], nosearch_directorys)
    # 1108版本添加插入点标记
    add_1108_insert_symbol(need_replace_file_list)

# 0905版添加插入点标记
def handle_add_insert_symble_0905():
    print("0905版添加insert标记")
    need_replace_file_list = get_search_files("target", [".m", ".mm"], nosearch_directorys)

    # 0905版添加插入点标记
    add_0905_insert_symble(need_replace_file_list)


# 返回ui的一个随机类
def get_1008_ui_functions_classobj(use_ui_class_list):
    class_name = ""
    for class_obj in use_ui_class_list:
        if class_name in class_obj.class_name:
            return class_obj
    return None

# 1030版脚本微调UI的位置、大小
def adjustUI_1030(need_replace_file_list):
    for file in need_replace_file_list:
        file_context = []
        with open(file, "r+") as input:
            file_context = input.readlines()
        if len(file_context) > 0:
            file_replace_context = []
            for line in file_context:
                if contains_CGRectMake_1030(line):
                    # 当前行包含CGRectMake
                    replace_str = handle_CGRectMake_1030(line)
                elif contains_CGSizeMake_1030(line):
                    replace_str = handle_CGSizeMake_1030(line)
                elif contains_CGPointMake_1030(line):
                    replace_str = handle_CGPointMake_1030(line)
                elif contains_UIColor_colorWithRed_1030(line):
                    replace_str = handle_UIColor_colorWithRed_1030(line)
                else:
                    replace_str = line
                file_replace_context.append(replace_str)
        with open(file, "w") as input:
            input.writelines(file_replace_context)


# 1026脚本添加透明色UI
def add_transparentUI_1026(need_replace_file_list):
    for file in need_replace_file_list:
        file_context = []
        with open(file, "r+") as input:
            file_context = input.readlines()
        if len(file_context) > 0:
            file_replace_context = []
            for line in file_context:
                if contains_addSubview_1008(line):
                    # 获取到目标视图
                    target_ui = get_1008_target_ui(line)

                    if target_ui == "":
                        #未找到目标ui
                        file_replace_context.append(line)
                        continue
                    #生成对应的UI实现
                    out_ui_dic = generate_1026_ui()
                    replace_line = ""
                    replace_line += out_ui_dic["ui_impra"]
                    replace_line += "\t[" + target_ui + " addSubview:" + out_ui_dic["ui_name"] + "];\n"
                    replace_line += line
                    file_replace_context.append(replace_line)
                else:
                    file_replace_context.append(line)

            with open(file, "w") as input:
                input.writelines(file_replace_context)



# 1026版本生成透明色ui
def generate_1026_ui():
    out_dic = {}
    ui_var_name = generate_random_str(out_random_type_class)
    out_dic["ui_name"] = ui_var_name
    random_max_type = random.randrange(0, 10)
    ui_implamentation_str = ""
    if random_max_type == 0:
        #UIDatePicker
        ui_implamentation_str += "\tUIDatePicker * " + ui_var_name + " = [[UIDatePicker alloc]init];\n"
        ui_implamentation_str += "\t[" + ui_var_name + " setFrame:" + generate_0905_param_str("CGRect") + "];\n"
        ui_implamentation_str += "\t[" + ui_var_name + " setDate:[NSDate dateWithTimeIntervalSinceNow:" + random.randrange(0, 1000) + "] animated:YES];\n"
        random_num1 = random.randrange(0, 10)
        if random_num1 < 5:
            ui_implamentation_str += "\t[" + ui_var_name + " setCalendar:[NSCalendar currentCalendar]];\n"
        ui_implamentation_str += "\t[" + ui_var_name + " setCountDownDuration:" + generate_0905_param_str("NSUInteger") + "];\n"
        random_num2 = random.randrange(0, 10)
        if random_num2 < 5:
            ui_implamentation_str += "\t[" + ui_var_name + " setEnabled:" + generate_0905_param_str("BOOL") + "];\n"
        ui_implamentation_str += "\t[" + ui_var_name + " setBackgroundColor:[UIColor clearColor]];\n"
    elif random_max_type == 1:
        #UIImageView
        ui_implamentation_str += "\tUIImageView * " + ui_var_name + " = [[UIImageView alloc]initWithFrame:" + generate_0905_param_str("CGRect") + "];\n"
        ui_implamentation_str += "\t" + ui_var_name + ".backgroundColor = [UIColor clearColor];\n"
        ui_implamentation_str += "\tlong long llZEQuBrX1Ue = " + generate_0905_param_str("NSUInteger") + ";\n"
        ui_implamentation_str += "\t[" + ui_var_name + " setAnimationDuration:llZEQuBrX1Ue];\n"
        random_num1 = random.randrange(0, 10)
        if random_num1 < 3:
            ui_implamentation_str += "\t" + ui_var_name + ".image = [UIImage imageNamed:" + generate_0905_param_str("NSString *") + "];\n"
        ui_implamentation_str += "\t" + ui_var_name + ".contentMode = UIViewContentModeScaleToFill;\n"
        random_num2 = random.randrange(0, 10)
        if random_num2 < 6:
            ui_implamentation_str += "\t[" + ui_var_name + " setHighlighted:" + generate_0905_param_str("BOOL") + "];\n"
        ui_implamentation_str += "\t" + ui_var_name + ".layer.borderWidth = " + generate_0905_param_str("double") + ";\n"
        random_num3 = random.randrange(0, 10)
        if random_num3 < 2:
            ui_implamentation_str += "\t" + ui_var_name + ".layer.borderColor = [UIColor clearColor].CGColor;\n"
        ui_implamentation_str += "\t" + ui_var_name + ".clipsToBounds = YES;\n"
    elif random_max_type == 2:
        #UINavigationBar
        ui_implamentation_str += "\tUINavigationBar *" + ui_var_name + " = [[UINavigationBar alloc] initWithFrame:" + generate_0905_param_str("CGRect") + "];\n"
        ui_implamentation_str += "\t" + ui_var_name + ".barStyle = UIBarStyleBlack;\n"
        random_num1 = random.randrange(0, 10)
        if random_num1 < 3:
            ui_implamentation_str += "\t[" + ui_var_name + " setBackgroundImage:[UIImage imageNamed:" + generate_0905_param_str("NSString *") + "] forBarMetrics:UIBarMetricsCompact];\n"
        ui_implamentation_str += "\t[" + ui_var_name + " setBackgroundColor:[UIColor clearColor]];\n"
        ui_implamentation_str += "\t" + ui_var_name + ".tintColor = [UIColor clearColor];\n"
    elif random_max_type == 3:
        #UIControl
        ui_implamentation_str += "\tUIControl *" + ui_var_name + " = [[UIControl alloc] init];\n"
        ui_implamentation_str += "\t" + ui_var_name + ".selected = " + generate_0905_param_str("BOOL") + ";\n"
        ui_implamentation_str += "\t" + ui_var_name + ".backgroundColor = [UIColor clearColor];\n"
        random_num2 = random.randrange(0, 10)
        if random_num2 < 3:
            ui_implamentation_str += "\t[" + ui_var_name + " cancelTrackingWithEvent:[[UIEvent alloc]init]];\n"
        ui_implamentation_str += "\t" + ui_var_name + ".enabled = " + generate_0905_param_str("BOOL") + ";\n"
        ui_implamentation_str += "\tdouble Q0L4hF9vbV = " + generate_0905_param_str("double") + ";\n"
        ui_implamentation_str += "\t" + ui_var_name + ".alpha = Q0L4hF9vbV;\n"
        random_num1 = random.randrange(0, 10)
        if random_num1 < 3:
            ui_implamentation_str += "\t" + ui_var_name + ".highlighted = " + generate_0905_param_str("BOOL") + ";\n"
    elif random_max_type == 4:
        #UIInputView
        ui_implamentation_str += "\tUIInputView *" + ui_var_name + " = [[UIInputView alloc]initWithFrame:CGRectZero inputViewStyle:UIInputViewStyleDefault];\n"
        random_num1 = random.randrange(0, 10)
        if random_num1 < 3:
            ui_implamentation_str += "\t[" + ui_var_name + " setFrame:" + generate_0905_param_str("CGRect") + "];\n"
        ui_implamentation_str += "\t[" + ui_var_name + " setTintColor:[UIColor clearColor]];\n"
        ui_implamentation_str += "\t[" + ui_var_name + " setBackgroundColor:[UIColor clearColor]];\n"
        ui_implamentation_str += "\t[" + ui_var_name + " setAllowsSelfSizing:" + generate_0905_param_str("BOOL") + "];\n"
    elif random_max_type == 5:
        #UIScrollView
        ui_implamentation_str += "\tUIScrollView * " + ui_var_name + " = [[UIScrollView alloc] initWithFrame:" + generate_0905_param_str("CGRect") + "];\n"
        ui_implamentation_str += "\tUIImageView * view = [[UIImageView alloc] initWithImage:[UIImage imageNamed:" + generate_0905_param_str("NSString *") + "]];\n"
        ui_implamentation_str += "\t[view setBackgroundColor:[UIColor clearColor]];\n"
        random_num1 = random.randrange(0, 10)
        if random_num1 < 3:
            ui_implamentation_str += "\t[view setAnimationDuration:1];\n"
        ui_implamentation_str += "\t[view setHighlighted:" + generate_0905_param_str("BOOL") + "];\n"
        ui_implamentation_str += "\tlong long EXKlds7c65M = " + generate_0905_param_str("NSInteger") + ";\n"
        ui_implamentation_str += "\t" + ui_var_name + ".contentSize = CGSizeMake(EXKlds7c65M, " + generate_0905_param_str("NSInteger") + ");\n"
        ui_implamentation_str += "\t" + ui_var_name + ".showsHorizontalScrollIndicator = " + generate_0905_param_str("BOOL") + ";\n"
        random_num2 = random.randrange(0, 10)
        if random_num2 < 3:
            ui_implamentation_str += "\t" + ui_var_name + ".showsVerticalScrollIndicator = " + generate_0905_param_str("BOOL") + ";\n"
        ui_implamentation_str += "\t[" + ui_var_name + " setBackgroundColor:[UIColor clearColor]];\n"
        ui_implamentation_str += "\t" + ui_var_name + ".bounces = " + generate_0905_param_str("BOOL") + ";\n"
        ui_implamentation_str += "\t" + ui_var_name + ".pagingEnabled = " + generate_0905_param_str("BOOL") + ";\n"
    elif random_max_type == 6:
        #UITextView
        ui_implamentation_str += "\tUITextView *" + ui_var_name + " = [[UITextView alloc] initWithFrame:" + generate_0905_param_str("CGRect") + "];\n"
        ui_implamentation_str += "\t" + ui_var_name + ".backgroundColor = [UIColor clearColor];\n"
        ui_implamentation_str += "\t" + "long long KnooxrUmlJRa = " + generate_0905_param_str("NSInteger") + ";\n"
        ui_implamentation_str += "\t" + ui_var_name + ".font = [UIFont boldSystemFontOfSize:KnooxrUmlJRa];\n"
        random_num1 = random.randrange(0, 10)
        if random_num1 < 3:
            ui_implamentation_str += "\t" + ui_var_name + ".text = " + generate_0905_param_str("NSString *") + ";\n"
        ui_implamentation_str += "\t" + ui_var_name + ".textAlignment = NSTextAlignmentLeft;\n"
        ui_implamentation_str += "\t" + ui_var_name + ".textColor = [UIColor clearColor];\n"
        random_num2 = random.randrange(0, 10)
        if random_num2 < 3:
            ui_implamentation_str += "\t" + ui_var_name + ".editable = " + generate_0905_param_str("BOOL") + ";\n"
        ui_implamentation_str += "\t" + ui_var_name + ".userInteractionEnabled = " + generate_0905_param_str("BOOL") + ";\n"
        ui_implamentation_str += "\t" + ui_var_name + ".scrollEnabled = " + generate_0905_param_str("BOOL") + ";\n"
    elif random_max_type == 7:
        #UIView
        ui_implamentation_str += "\tUIView *" + ui_var_name + " = [[UIView alloc] initWithFrame:" + generate_0905_param_str("CGRect") + "];\n"
        ui_implamentation_str += "\t" + ui_var_name + ".backgroundColor = [UIColor clearColor];\n"
        random_num1 = random.randrange(0, 10)
        if random_num1 < 3:
            ui_implamentation_str += "\t" + ui_var_name + ".layer.cornerRadius = " + generate_0905_param_str("double") + ";\n"
        ui_implamentation_str += "\t" + ui_var_name + ".layer.borderColor = [UIColor lightGrayColor].CGColor;\n"
        ui_implamentation_str += "\t" + ui_var_name + ".layer.borderWidth = " + generate_0905_param_str("double") + ";\n"


    out_dic["ui_impra"] = ui_implamentation_str

    return out_dic

# 1008自动替换并删除
def replace_1008_functions(need_replace_file_list, use_ui_class_list):

    # 初始化一个移除类
    random_class_name = class_prefix_str + generate_random_str(out_random_type_class)
    generate_class_obj = methodtransfer.ClassObject(random_class_name, "NSObject", [], [], [])

    first_generate_ui = 0
    remove_prototype_transfername = generate_words_str("func")
    for file in need_replace_file_list:
        file_context = []
        with open(file, "r+") as input:
            file_context = input.readlines()
        if len(file_context) > 0:
            file_replace_context = []
            for line in file_context:
                if contains_addSubview_1008(line):
                    
                    # 获取到目标视图
                    target_ui = get_1008_target_ui(line)

                    if target_ui == "":
                        #未找到目标ui
                        file_replace_context.append(line)
                        continue
                    random_indexg = random.randrange(0, 100)
                    if random_indexg > 5:
                        file_replace_context.append(line)
                        continue

                    # 随机拿到一条调用原型
                    uifunctions_class_obj = get_1008_ui_functions_classobj(use_ui_class_list)
                    prototype_obj_list = uifunctions_class_obj.method_prototype_list
                    prototype_obj = prototype_obj_list[random.randrange(0, len(prototype_obj_list))]

                    return_type = prototype_obj.return_type
                    random_var = generate_random_str(out_random_type_class)

                    uifunctions_class_obj1 = get_1008_ui_functions_classobj(use_ui_class_list)
                    prototype_obj_list1 = uifunctions_class_obj1.method_prototype_list
                    prototype_obj1 = prototype_obj_list1[random.randrange(0, len(prototype_obj_list))]

                    return_type1 = prototype_obj1.return_type
                    random_var1 = generate_random_str(out_random_type_class)

                    # 生成替换语句
                    replace_line = ""
                    replace_line += "\t" + return_type + " " + random_var + " = "
                    replace_line += handle_1008_uifunctions_transfer(prototype_obj, uifunctions_class_obj.class_name)
                    replace_line += "\t[" + target_ui + " addSubview:" + random_var + "];\n"

                    # 生成替换语句
                    replace_line += "\t" + return_type1 + " " + random_var1 + " = "
                    replace_line += handle_1008_uifunctions_transfer(prototype_obj1, uifunctions_class_obj1.class_name)
                    replace_line += "\t[" + target_ui + " addSubview:" + random_var1 + "];\n" 

                    replace_line += line

                    # 生成移除函数并添加移除代码的调用
                    remove_prototype_type = "+"
                    remove_prototype_returntype = "void"
                    param_name = generate_random_str(out_random_type_class)
                    param_pair_obj = methodtransfer.ParamPair(param_name, "UIView *")
                    remove_prototype_obj = methodtransfer.MethodPrototype(remove_prototype_transfername + ":", remove_prototype_type, remove_prototype_returntype, [param_pair_obj])
                
                    remove_implamentation_str = "{\n"
                    remove_implamentation_str += "\t[" + param_name + " removeFromSuperview];\n"
                    remove_implamentation_str += "}\n"
                    remove_implamentation_obj = methodtransfer.MethodImplamentation(remove_prototype_obj, remove_implamentation_str)
                    if first_generate_ui == 0:
                        # 更新generate_class_obj
                        generate_class_obj.addprototype(remove_prototype_obj)
                        generate_class_obj.addimplamentation(remove_implamentation_obj)
                        first_generate_ui = 1
                    
                    replace_line += "\t" + handle_transfer_0912(remove_prototype_obj, random_var, random_class_name)
                    replace_line += "\t" + handle_transfer_0912(remove_prototype_obj, random_var1, random_class_name)
                    
                    file_replace_context.append(replace_line)
                else:
                    file_replace_context.append(line)
            with open(file, "w") as input:
                input.writelines(file_replace_context)
    
    # 写UI的移除实现文件
    removal_file_path = "uiremove/" + random_class_name
    with open(removal_file_path + ".h", "w") as input:
            input.write(generate_class_obj.output_class_header())

    with open(removal_file_path + ".m", "w") as input:
        input.write(generate_class_obj.output_class_implamentation())

# 1008自动添加UI的功能性代码
def handle_replace_function_1008():
    # 扫描插入库函数
    header_file_list = get_search_files("uicode", [".h"], nosearch_directorys)

    insert_class_list = initial_class_from_file(header_file_list)

    need_replace_file_list = get_search_files("target", [".m", ".mm"], nosearch_directorys)

    replace_1008_functions(need_replace_file_list, insert_class_list)

# 1026透明色UI的自动添加
def handle_transparentUI_replace_1026():
    # 扫描插入库函数
    need_replace_file_list = get_search_files("target", [".m", ".mm"], nosearch_directorys)
    add_transparentUI_1026(need_replace_file_list)

# 1030微调UI坐标大小
def handle_adjustUI_frame_1030():
    need_replace_file_list = get_search_files("target", [".m", ".mm"], nosearch_directorys)
    adjustUI_1030(need_replace_file_list)

# 1104版本 自动生成ui
def get_add_ui_1104():
    #随机生成ui
    ui_type = ""
    ui_imp = ""
    ui_dic = {}
    random_num = random.randrange(0, 5)
    if random_num == 0:
        #UILabel
        label_type = "UILabel"
        ui_type = label_type
        ui_name = generate_random_str(out_random_type_class)
        ui_imp += "\t" + label_type + " *" + ui_name + " = [[UILabel alloc] initWithFrame:" + generate_0905_param_str("CGRect") + "];\n"
        random_index = random.randrange(2, 6)
        for i in random_index:
            random_param = random.randrange(0, 6)
            if random_param == 0:
                ui_imp += "\t" + ui_name + ".backgroundColor = " + generate_0905_param_str("UIColor *") + ";\n"
            elif random_param == 1:
                ui_imp += "\t" + ui_name + ".text = " + generate_0905_param_str("NSString *") + ";\n"
            elif random_param == 2:
                ui_imp += "\t" + ui_name + ".textAlignment = NSTextAlignmentLeft;\n"
            elif random_param == 3:
                ui_imp += "\t" + ui_name + ".font = [UIFont systemFontOfSize:" + generate_0905_param_str("CGFloat") + "];\n"
            elif random_param == 4:
                ui_imp += "\t" + ui_name + ".textColor = " + generate_0905_param_str("UIColor *") + ";\n"
            elif random_param == 5:
                ui_imp += "\t" + ui_name + ".numberOfLines = " + generate_0905_param_str("NSInteger") + ";\n"
            else:
                pass
        ui_imp += "\t[self.view addSubview:" + ui_name + "];\n"
        ui_dic["e_imp"] = ui_imp
        ui_dic["e_ui_type"] = ui_type
    elif random_num == 1:
        #UITextField
        pass


    return ui_dic

# 1104版本 在viewDidDisappear/viewWillDisappear添加ui
def generate_add_ui_1104():
    # 随机添加2~5个ui
    add_ui_dic = {}
    ui_type_list = []
    ui_imp_str = ""
    #随机深度为2~5
    depth = random.randrange(2, 6)
    for i in depth:
        ui_dic = get_add_ui_1104()
        ui_imp_str += ui_dic["e_imp"]
        e_ui_type = ui_dic["e_ui_type"]
        ui_type_list.append(e_ui_type)

    return add_ui_dic

# 1104版本 在viewDidAppear/viewWillAppear删除ui
def generate_remove_ui_1104(remove_tag):
    return ""

# 1104版本 对viewDidDisappear/viewWillDisappear添加ui
def handle_add_ui_1104(need_handle_file_list):

    for file in need_handle_file_list:
        file_content = []
        file_rplc_content = []
        with open(file, "r+") as input:
            file_content = input.readlines()
        ui_property_list = []
        global global_remove_tag
        global_remove_tag = 0
        for line in file_content:
            # file_rplc_content.append(line)
            if global_need_add_ui in line:
                # 需要添加ui
                add_ui_dic = generate_add_ui_1104()
                replace_str = add_ui_dic["ui_imp"]
                ui_list = add_ui_dic["ui_list"]
                ui_property_list.extend(ui_list)
                file_rplc_content.append(replace_str)
            elif global_need_did_remove_ui in line:
                # 需要移除ui
                remove_str = generate_remove_ui_1104(0)
                file_rplc_content.append(remove_str)
            elif global_need_will_remove_ui in line:
                # 需要移除ui
                remove_str = generate_remove_ui_1104(0)
            else:
                file_rplc_content.append(line)



# 对viewDidDisappear/viewWillDisappear添加ui
def handle_add_ui_for_viewDidDisappear_1104():
    need_handle_file_list = get_search_files("target", [".m", ".mm"], nosearch_directorys)
    # 1104版本添加ui
    handle_add_ui_1104(need_handle_file_list)
    # 1104版本添加ui属性
    handle_add_property_1104(need_handle_file_list)


def main():
    print ("处理插入点代码或者添加中间调用层")
    # handleargv()

    # 第一版
    # handle_insert()

    # 第二版
    # handle_insert_mixed()

    # 第三版插入点---1028复用
    # handle_replace_insert()

    # 第四版插入点
    # handle_replace_fourth_insert()

    # 0823版本插入点
    # handle_replace_0823()

    # 0905版本插入点自动添加插入点标记
    # handle_add_insert_symble_0905()

    # 1108版本对未添加标记的函数添加标记
    # handle_add_insert_symble_1108()

    # 0905版本插入点替换
    # handle_replace_0905_insert()

    # 0912版本插入点替换
    # handle_replace_0912_insert()

    # 0919版本插入点替换 --- 插入点的类只有一个 插入函数共8个，针对double、longlong、NSString、NSArray四种类型做的处理还原
    # handle_replace_0919_insert()

    # 0314增加的处理还原inline替换
    handle_replace_inline()

    # 0924版本插入点替换
    # handle_replace_0924_insert()

    # 0926版本插入点
    # handle_replace_0926_insert()

    # 重构代码(中间调用层)
    # handle_reconstruction()

    # 处理UI功能性代码的自动添加
    # handle_replace_function_1008()

    # 处理透明色UI的自动添加
    # handle_transparentUI_replace_1026()

    # 微调ui的坐标、大小
    # handle_adjustUI_frame_1030()

    # 对viewDidDisappear/viewWillDisappear等函数添加ui
    # handle_add_ui_for_viewDidDisappear_1104()

    # 测试
    # test()


def test():
    '''
    测试函数
    '''
    # modifier_list = ["nonatomic", "strong", "readonly"]
    # property_obj = methodtransfer.PropertyObject(modifier_list, "fiesjfogids", "NSString *")
    # # print(property_obj.output_property())

    # param_obj = methodtransfer.ParamPair("xx", "NSString *")
    # # param_obj.log_param()

    # param_list = [param_obj]
    # method_obj = methodtransfer.MethodPrototype("viewDidLoad", "+", "NSString *", 1, param_list)
    # # print(method_obj.output_prototype())

    # method_implamentation_str = "{\n"
    # method_implamentation_str += "\tNSLog(\"11\");\n"
    # method_implamentation_str += "}"
    # implamentation_obj = methodtransfer.MethodImplamentation(method_obj, method_implamentation_str)
    # # print(implamentation_obj.output_implamentation())

    # class_name = "YYfijdoaKfgdst"
    # class_obj = methodtransfer.ClassObject(class_name, "NSObject", [property_obj], [method_obj], [implamentation_obj])
    # # print(class_obj.output_class_header())
    # print(class_obj.output_class_implamentation())
    # test_str = "-(int)hello;\n"
    # test_str += "+ (void) viewDidAppear"
    # test_str += " {\n"
    # test_str += "\tprint(1);\n"
    # test_str += "}\n"
    # test_str += "+ (NSString *)viewDidLoad:(NSString *)xx\n"
    # test_str += "{\n"
    # test_str += "\tNSLog(\"11\");\n"
    # test_str += "\tif(1)\n"
    # test_str += "\t{\n"
    # test_str += "\t\tNSLog(\"2\");\n"
    # test_str += "\t}\n"
    # test_str += "}\n"

    # test_str = "- (CGPoint)ConvertDir:(CGPoint)p {"
    # print(test_str)
    # result = oc_func_rule3.findall(test_str)
    # print("result:%s" % str(result))

    # implamentation_str = findimplamentation("+ (NSString *)viewDidLoad:(NSString *)xx", test_str)
    # print("implamentation_str :" + implamentation_str)

    # test_str = "- (void)webView:(WKWebView *)webView didStartProvisionalNavigation:(null_unspecified WKNavigation *)navigation"
    # print(methodtransfer_from_method(test_str))

    # class_list = initial_class_from_file()
    # for class_obj in class_list:
    #     print(class_obj.output_class_implamentation())

    # test_str = "- (void)webView:(id)webView decidePolicyForNavigationAction:(id)navigationAction decisionHandler:(void (^)(int))decisionHandler"
    # parampair_list = methodtransfer.parampair_from_method(test_str)
    # for parampair_obj in parampair_list:
    #     print("name :" + parampair_obj.param_name)
    #     print("type :" + parampair_obj.param_type)
    # handle_reconstruction()

    out_str = generate_words_str("random_str")
    print("random:%s" % out_str)




if __name__ == "__main__":
	main()