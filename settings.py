from os import environ

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'bart_only',
        'display_name': "BART Only",
        'num_demo_participants': 1,
        'app_sequence': ['bart'],
    },
    {
        'name': 'bret_only',
        'display_name': "BRET Only",
        'num_demo_participants': 1,
        'app_sequence': ['bret'],
    },
    {
        'name': 'bart_bret',
        'display_name': "BART + BRET",
        'num_demo_participants': 1,
        'app_sequence': ['bart', 'bret'],
    },
]

LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = []

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
<h2>Risk Task Experiments</h2>
<p>BART (Balloon Analogue Risk Task) and BRET (Bomb Risk Elicitation Task)</p>
"""

SECRET_KEY = 'risk_tasks_secret_key_change_me'

INSTALLED_APPS = ['otree']
