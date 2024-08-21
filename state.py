'''
프로그램 내 변수 형상관리
'''
import json


is_stop_requested = False  # Stream 대답 중, 대답 중지
is_screenshot_area_selecting = False  # 현재 스크린샷 범위 설정 중

g_language = 'en'  # 언어 : ["日本語", "English", "한국어"] to ['ja', 'en', 'ko']

def get_is_stop_requested():
    global is_stop_requested
    return is_stop_requested

def set_is_stop_requested(value=True):
    global is_stop_requested
    is_stop_requested = value

def get_is_screenshot_area_selecting():
    global is_screenshot_area_selecting
    return is_screenshot_area_selecting

def set_is_screenshot_area_selecting(value=True):
    global is_screenshot_area_selecting
    is_screenshot_area_selecting = value

# setting의 UI 언어
def get_g_language():
    global g_language
    g_language = 'en'  # ["日本語", "English", "한국어"]
    try:
        with open('config/setting.json', 'r', encoding='utf-8') as file:
            settings = json.load(file)
            if 'setting_language' in settings:
                if settings['setting_language'] == '한국어':
                    g_language = 'ko'
                elif settings['setting_language'] == '日本語':
                    g_language = 'ja'
    except:
        pass
    return g_language
    