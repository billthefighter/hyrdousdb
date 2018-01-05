import json
import numpy as np
import pandas as pd
import re
import io
import os

writer = pd.ExcelWriter(u'C:/Users/lucasw/Documents/machinining_library_manager/' + 'backups/backup_{}.xlsx'.format(pd.datetime.today().strftime('%y%m%d-%H%M%S')))