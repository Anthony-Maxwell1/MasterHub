from PIL import ImageFilter

ROTATE_DEFAULT = 0
ZOOM_DEFAULT = 0
FLIP_OPTIONS = ['None', 'X', 'Y', 'Both']
BLUR_DEFAULT = 0
BLUR_TYPE_DEFAULT = 'GaussianBlur'
CONTRAST_DEFAULT = 0
BLUR_OPTIONS_LIST = ['GaussianBlur', 'BoxBlur']
BLUR_OPTIONS = {'GaussianBlur': ImageFilter.GaussianBlur, 'BoxBlur': ImageFilter.BoxBlur}
EFFECT_OPTIONS = ['None', 'Emboss', 'Find edges', 'Contour', 'Edge enhance']
BRIGHTNESS_DEFAULT = 1
VIBRANCE_DEFAULT = 1
GRAYSCALE_DEFAULT = False
INVERT_DEFAULT = False

BACKGROUND_COLOR = '#000000' 
WHITE = '#FFF'
GRAY = 'grey'
BLUE = '#1f6aa5'
DARK_GRAY = '#4a4a4a'
CLOSE_RED =  '#8a0606'
SLIDER_BG = '#64686b'
DROPDOWN_MAIN_COLOR = '#444'
DROPDOWN_HOVER_COLOR = '#333'
DROPDOWN_MENU_COLOR = '#666'