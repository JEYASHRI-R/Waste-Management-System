from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pandas as pd
import os
import csv
import calendar
from datetime import datetime
date = datetime.today().strftime('%Y-%m-%d')
time = datetime.today().strftime('%H:%M:%S')
