import unittest
from herbie import Herbie
import pandas as pd
import xarray as xr

class placeHolderTest(unittest.TestCase):

    def test1(self):
        H = Herbie(
        f"2024-06-10 00:00",
        model="rtma",
        product="anl",
        )

        H.download(verbose=True)

        ds = H.xarray("TMP:2 m")

        self.assertEqual(ds['t2m'].data[495][480], 293.0)
