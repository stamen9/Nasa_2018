import shutil
import urllib.request

def main():
    urllib.request.urlretrieve('ftp://sidads.colorado.edu/pub/DATASETS/AGDC/dixon_nsidc_0318/10m_temps_NSIDC_Dixon.xls',"file.xls")

if __name__ == "__main__":
    main()