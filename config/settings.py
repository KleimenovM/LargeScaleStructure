### settings file which specifies directories

from pathlib import Path

# root project directory (ExtremeBlazars_FermiLAT)
ROOT_DIR: Path = Path(__file__).resolve().parent.parent

DATA_DIR: Path = ROOT_DIR / 'galcats'

FIG_DIR: Path = ROOT_DIR / 'figures'

OVD_DIR: Path = ROOT_DIR / 'overdensity'
