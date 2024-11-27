from django.test import TestCase

import os


from dotenv import load_dotenv

load_dotenv()
PASSWORD = os.getenv('PASSWORD')

print(PASSWORD)
