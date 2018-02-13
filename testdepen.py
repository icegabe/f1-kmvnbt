# Required Dependencies
import setuptools
import NumPy >= 1.9.0
import python-dateutil >= 1.5
import pytz # Needed for time zone support

# Highly Recommended Dependencies
import numexpr >= 2.4.6 #for accelerating certain numerical operations. numexpr uses multiple cores as well as smart chunking and caching to achieve large speedups
import bottleneck >= 1.0.0 #for accelerating certain types of nan evaluations. bottleneck uses specialized cython routines to achieve large speedups

# Optional Dependencies
import SciPy >= 0.14.0 #miscellaneous statistical functions
    #xarray: pandas like handling for > 2 dims, needed for converting Panels to xarray objects. Version 0.7.0 or higher is recommended.
    #PyTables: necessary for HDF5-based storage. Version 3.0.0 or higher required, Version 3.2.1 or higher highly recommended.
    #Feather Format: necessary for feather-based storage, version 0.3.1 or higher.
    #SQLAlchemy >= 0.8.1 #for SQL database support. Besides SQLAlchemy, you also need a database specific driver. You can find an overview of supported drivers for each SQL dialect in the SQLAlchemy docs.
    #    pymysql: for MySQL.
    #    SQLite: for SQLite, this is included in Python’s standard library by default.
import matplotlib >=1.4.3 #for plotting
    #For Excel I/O:
    #    xlrd/xlwt: Excel reading (xlrd) and writing (xlwt)
    #    openpyxl: openpyxl version 1.6.1 or higher (but lower than 2.0.0), or version 2.2 or higher, for writing .xlsx files (xlrd >= 0.9.0)
import Jinja2 #Template engine for conditional HTML formatting.
    #s3fs: necessary for Amazon S3 access (s3fs >= 0.0.7).
    #blosc: for msgpack compression using blosc
    #One of PyQt4, PySide, pygtk, xsel, or xclip: necessary to use read_clipboard(). Most package managers on Linux distributions will have xclip and/or xsel immediately available for installation.
import pandas-gbq #for Google BigQuery I/O.
import BeautifulSoup4, html5lib, lxml
